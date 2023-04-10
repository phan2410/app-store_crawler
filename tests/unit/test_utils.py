import pytest

from app.utils import normalize_text, clean_text, rand_float, get_delay_ms, get_delay_s, is_app_url, is_company_url, \
    get_developer_name_from_company_url, get_first_longest_common_substring, calc_likelihood, get_best_matching_text


def test_normalize_text():
    test_str = 'This is a space:\xa0'
    expected_str = 'This is a space: '
    assert normalize_text(test_str) == expected_str


def test_clean_text():
    test_str = '\n A text\xa0to test \n'
    expected_str = 'A text to test'
    assert clean_text(test_str) == expected_str


@pytest.mark.parametrize("low, high, reso, expects", (
    (4.3, 7.5, 2, (4.3, 7.5)),
    (1.0, 4.0, 4, (1.0, 2.0, 3.0, 4.0)),
    (2.5, 3.5, 3, (2.5, 3.0, 3.5)),
))
def test_rand_float(low, high, reso, expects):
    res = rand_float(low=low, high=high, resolution=reso)
    assert res in expects, f'{res} not in {expects}'


def test_get_delay_ms():
    min_val = 200
    max_val = 700
    result_1 = get_delay_ms(min_val=min_val, max_val=max_val)
    result_2 = get_delay_ms(min_val=min_val, max_val=max_val)
    result_3 = get_delay_ms(min_val=min_val, max_val=max_val)

    assert not result_1 == result_2 == result_3
    assert all(min_val <= r <= max_val for r in (result_1, result_2, result_3))


def test_get_delay_s():
    min_val = 0.4
    max_val = 5
    result_1 = get_delay_s(min_val=min_val, max_val=max_val)
    result_2 = get_delay_s(min_val=min_val, max_val=max_val)
    result_3 = get_delay_s(min_val=min_val, max_val=max_val)

    assert not result_1 == result_2 == result_3
    assert all(min_val <= r <= max_val for r in (result_1, result_2, result_3))


@pytest.mark.parametrize(('url', 'expected'), (
    ('https://apps.apple.com/app/netflix/id363590051', True),
    ('https://apps.apple.com/vn/developer/sony-corporation/id1315534741', False),
    ('https://apps.apple.com/vn/app/sony-b%E1%BA%A3o-h%C3%A0nh-%C4%91i%E1%BB%87n-t%E1%BB%AD/id1193542964', True),
    ('https://apps.apple.com/us/developer/netflix-inc/id363590054', False),
))
def test_is_app_url(url: str, expected: bool):
    assert is_app_url(url) == expected


@pytest.mark.parametrize(('url', 'expected'), (
    ('https://apps.apple.com/app/netflix/id363590051', False),
    ('https://apps.apple.com/vn/developer/sony-corporation/id1315534741', True),
    ('https://apps.apple.com/vn/app/sony-b%E1%BA%A3o-h%C3%A0nh-%C4%91i%E1%BB%87n-t%E1%BB%AD/id1193542964', False),
    ('https://apps.apple.com/us/developer/netflix-inc/id363590054?mt=1', True),
))
def test_is_company_url(url: str, expected: bool):
    assert is_company_url(url) == expected


@pytest.mark.parametrize(('url', 'expected'), (
    ('https://apps.apple.com/vn/developer/sony-corporation/id1315534741', 'sony-corporation'),
    ('https://apps.apple.com/us/developer/netflix-inc/id363590054?xyz=3', 'netflix-inc'),
    ('https://apps.apple.com/app/netflix/id363590051', None),
))
def test_get_developer_name_from_company_url(url: str, expected: str | None):
    assert get_developer_name_from_company_url(url) == expected


@pytest.mark.parametrize(('str1', 'str2', 'expected'), (
    ('sony-corporation', 'sony', 'sony'),
    ('netflix', 'netflix-inc', 'netflix'),
    ('helloae', 'helishelloaethehelloaeqq', 'helloae'),
))
def test_get_first_longest_common_substring(str1: str, str2: str, expected: str):
    assert get_first_longest_common_substring(str1, str2) == expected


@pytest.mark.parametrize(('str1', 'str2', 'expected'), (
    ('netflix', 'netflix', 1.0),
    ('abc', 'eabc', 0.75),
))
def test_calc_likelihood(str1: str, str2: str, expected: float):
    assert calc_likelihood(str1, str2) == expected


@pytest.mark.parametrize(('hint_text', 'texts', 'expected'), (
    ('netflix', ['netflix-inc', 'apple-netflix', 'am-netflix-co'], 'netflix-inc'),
    ('sony', ['sony-vietnam', 'sony'], 'sony'),
))
def test_get_best_matching_text(hint_text: str, texts: list[str], expected: str):
    assert get_best_matching_text(hint_text, texts) == expected
