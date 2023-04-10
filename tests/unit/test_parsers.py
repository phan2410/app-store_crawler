import pytest
from bs4 import PageElement, BeautifulSoup

from app.parsers import get_text


@pytest.mark.parametrize(('ele', 'selector', 'expected'), (
    (
        BeautifulSoup('<div>contained\xa0text\n</div>', 'html.parser'),
        '',
        'contained text'
    ),
    (
        BeautifulSoup('<div>parent text 1 <p> text of interest\n </p> parent text 2<br/></div>', 'html.parser'),
        'p',
        'text of interest'
    )
))
def test_get_text(ele: PageElement, selector: str, expected: str):
    result = get_text(ele=ele, selector=selector)

    assert result == expected
