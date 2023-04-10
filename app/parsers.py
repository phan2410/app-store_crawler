from typing import Dict, Any, List

from bs4 import PageElement, BeautifulSoup

from app.utils import clean_text


def get_text(ele: PageElement, selector: str = None) -> str:
    target_ele = ele
    if selector and hasattr(target_ele, 'select_one'):
        target_ele = target_ele.select_one(selector)
    return clean_text(target_ele.text) if target_ele else ''


class AppInfoParser:
    def __init__(self, html: str):
        self.soup = BeautifulSoup(html, features='html.parser')

    def parse_url(self) -> str:
        url_ele = self.soup.select_one(selector='meta[property="og:url"]')
        return url_ele.get('content') if url_ele else ''

    def parse_id(self) -> str:
        id_ele = self.soup.select_one(selector='meta[name="apple:content_id"]')
        return id_ele.get('content', '') if id_ele else ''

    def parse_name(self) -> str:
        name_ele = self.soup.select_one(selector='h1.product-header__title.app-header__title')
        return get_text(name_ele).split('\n')[0]

    def parse_compatibilities(self) -> List[str]:
        compat_ele_list = self.soup.select(selector='dt:-soup-contains("Compatibility") + dd > dl > dt')
        return list(map(get_text, compat_ele_list))

    def parse_languages(self) -> List[str]:
        language_ele = self.soup.select_one(selector='dt:-soup-contains("Languages") + dd')
        full_str = get_text(language_ele)
        return list(map(clean_text, full_str.split(sep=',')))

    def parse(self) -> dict:
        return dict(
            app_name=self.parse_name(),
            app_id=f"id{self.parse_id()}",
            app_url=self.parse_url(),
            app_targets=self.parse_compatibilities()
        )
