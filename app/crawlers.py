import json
import time
from functools import lru_cache
from random import randint
from typing import Dict, Tuple, Any, Union

from bs4 import PageElement
from playwright.sync_api import Page, sync_playwright, Browser, BrowserContext, Locator

from app.parsers import AppInfoParser
from app.utils import get_delay_ms, get_delay_s, is_app_url, get_developer_name_from_company_url, calc_likelihood, \
    is_company_url, get_best_matching_text, IS_MAC


def _is_end_of_page(page: Page) -> Tuple[bool, Any]:
    page_height = page.evaluate('document.body.scrollHeight')
    scroll_position = page.evaluate('window.scrollY')
    return scroll_position >= page_height, scroll_position


def discover_page(page: Page):
    last_pos = 0
    while True:
        page.mouse.wheel(delta_x=0, delta_y=randint(300, 900))
        time.sleep(get_delay_s(max_val=1))
        is_end, pos = _is_end_of_page(page)
        if is_end or last_pos == pos:
            break
        last_pos = pos


def collect_app_html(page: Page, app_url: str) -> str:
    assert is_app_url(app_url)

    page.bring_to_front()
    page.goto(app_url)
    page.wait_for_selector(selector="#ember3", state="visible")

    discover_page(page)

    # discovery info_list
    info_list = page.locator(selector=".information-list.information-list--app")
    info_list.scroll_into_view_if_needed()

    # expand languages if necessary
    language_dd_ele = info_list.locator("div", has_text="Languages").locator("dd")
    btn_ele = language_dd_ele.locator("button", has_text="more")
    if btn_ele.count() > 0:
        btn_ele.click(delay=get_delay_ms())
        btn_ele.wait_for(state="hidden")

    return page.content()


def craw_app_info(page: Page, app_url: str) -> dict:
    html = collect_app_html(page=page, app_url=app_url)
    parser = AppInfoParser(html=html)
    return parser.parse()


def collect_company_urls(ctx: BrowserContext, company_name: str) -> dict[str:str]:
    page = ctx.new_page()
    page.goto('https://apps.apple.com')

    # accept regional redirection
    continue_btn = page.wait_for_selector(selector="#ac-ls-continue", state="visible")
    continue_btn.click(delay=get_delay_ms())

    # page discovery behavior
    page.mouse.wheel(delta_x=0, delta_y=randint(100, 500))

    # search company_name
    search_button = page.locator(selector="#globalnav-menubutton-link-search")
    search_button.scroll_into_view_if_needed()
    search_box = page.get_by_placeholder("Search apple.com")

    while search_box.is_hidden():
        search_button.hover()
        search_button.click(delay=get_delay_ms())
        time.sleep(get_delay_s())

    search_box.click(delay=get_delay_ms())
    search_box.type(text=company_name, delay=get_delay_ms(min_val=100, max_val=300))
    search_box.press(key="Enter", delay=300)

    # iterate through result pages, and get company urls
    company_data = {}
    visited_links = []
    while True:
        page.wait_for_load_state(state="networkidle")

        discover_page(page)

        # iterate each line
        search_result = page.locator(selector="#exploreCurated").first
        if search_result.count() < 1:
            break
        for link_ele in search_result.get_by_role(role="listitem").locator("a.rf-serp-productname-link").all():
            link = link_ele.get_attribute('href')
            if link in visited_links:
                continue
            visited_links.append(link)
            if is_app_url(link):
                link_ele.scroll_into_view_if_needed()

                # go to the item page
                with ctx.expect_page() as item_page_info:
                    link_ele.hover()
                    key = "Meta" if IS_MAC else "Control"
                    page.keyboard.down(key=key)
                    link_ele.click(delay=get_delay_ms())
                    page.keyboard.up(key=key)
                    time.sleep(get_delay_s(min_val=0.7, max_val=2, resolution=9))

                item_page = item_page_info.value
                item_page.bring_to_front()
                company_ele = item_page.locator(selector='h2.product-header__identity.app-header__identity')\
                    .locator("a")
                company_ele.wait_for(state="attached")
                company_url = company_ele.get_attribute('href')
                company_data[get_developer_name_from_company_url(company_url)] = company_url
                item_page.close()

        next_btn = page.locator(selector="#explore nav.rc-pagination div.rc-pagination-arrow > button", has_text="Next")
        if next_btn.count() > 0:
            next_btn.click(delay=get_delay_ms())
            continue

        break

    page.close()
    return company_data


def collect_app_urls(ctx: BrowserContext, company_url: str) -> list[str]:
    assert is_company_url(company_url)

    def check_and_save_link(link_ele_list_: list[Locator]) -> list[str]:
        ans = []
        for link_ele_ in link_ele_list_:
            link_ = link_ele_.get_attribute('href')
            if is_app_url(link_):
                ans.append(link_)
        return ans

    page = ctx.new_page()
    page.goto(company_url, wait_until="load")

    discover_page(page)

    app_urls = []

    device_sections = page.locator(selector='section.section.section--bordered').all()
    for section in device_sections:
        section.scroll_into_view_if_needed()

        see_all_btn = section.locator('div.section__nav > a', has_text='See All')
        if see_all_btn.count() > 0:
            # go to the see-all page
            with ctx.expect_page() as detail_page_info:
                see_all_btn.hover()
                key = "Meta" if IS_MAC else "Control"
                page.keyboard.down(key=key)
                see_all_btn.click(delay=get_delay_ms())
                page.keyboard.up(key=key)
                time.sleep(get_delay_s(min_val=0.7, max_val=2, resolution=9))

            detail_page = detail_page_info.value
            detail_page.bring_to_front()
            discover_page(detail_page)

            link_ele_list = detail_page.locator(selector='div.l-row[role="feed"] > a').all()
            app_urls += check_and_save_link(link_ele_list)

            detail_page.close()
        else:
            link_ele_list = section.locator('div.l-row.l-row--peek > a').all()
            app_urls += check_and_save_link(link_ele_list)

    page.close()
    return app_urls


def crawl_company_apps(company_name: str, **kwargs) -> dict[str:Union[str, list]]:
    log = ...
    if kwargs.get('print'):
        log = print

    company_name = company_name.lower()
    data = []
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=kwargs.get('headless', False),
            slow_mo=kwargs.get('slow_mo', None)
        )
        context = browser.new_context()
        page = context.new_page()

        company_data = collect_company_urls(ctx=context, company_name=company_name)
        if not company_data:
            log(f'=> Not found any company with keyword {company_name}')
            return data
        log(f'=> Found companies\n{json.dumps(company_data, indent=4)}')

        actual_company_name = get_best_matching_text(hint_text=company_name, texts=company_data.keys())
        company_url = company_data[actual_company_name]
        log(f'=> Best match name: {actual_company_name} | {company_url}')

        app_urls = collect_app_urls(ctx=context, company_url=company_url)
        log(f'=> App urls to be crawled\n{json.dumps(app_urls, indent=4)}')
        for app_url in app_urls:
            app_data = craw_app_info(page=page, app_url=app_url)
            log(f'=> Craw URL {app_url}\n{json.dumps(app_data, indent=4)}')

            data.append(app_data)

        if kwargs.get('headless') and kwargs.get('delay_close_s'):
            page.wait_for_timeout(kwargs['delay_close_s'])
        browser.close()

    return data
