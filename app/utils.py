import re
import unicodedata
from random import randint
import platform

SYSTEM = platform.system()
IS_MAC = SYSTEM.lower() == 'darwin'

company_url_re = re.compile(
    r'^https://apps.apple.com/(\w{2}/)?developer/([\w\-%]+)/id\d+(\?([\w\-]+=[\w\-]+&?)*)?$',
    flags=re.IGNORECASE)

app_url_re = re.compile(
    r'^https://apps.apple.com/(\w{2}/)?app/[\w\-%]+/id\d+(\?([\w\-]+=[\w\-]+&?)*)?$',
    flags=re.IGNORECASE)


def normalize_text(text: str): return unicodedata.normalize('NFKD', text)


def clean_text(text: str): return normalize_text(text.strip())


def rand_float(low: float, high: float, resolution: int = 2) -> float:
    assert low < high, 'invalid inputs'
    delta = (high - low) / (resolution - 1)
    return low + randint(0, resolution-1) * delta


def get_delay_ms(min_val: int = 70, max_val: int = 500, resolution: int = 7) -> int:
    return round(rand_float(low=min_val, high=max_val, resolution=resolution))


def get_delay_s(min_val: float = 0.3, max_val: float = 2, resolution: int = 8) -> float:
    return rand_float(low=min_val, high=max_val, resolution=resolution)


def is_app_url(url: str) -> bool:
    return app_url_re.fullmatch(url) is not None


def is_company_url(url: str) -> bool:
    return company_url_re.fullmatch(url) is not None


def get_developer_name_from_company_url(url: str) -> str | None:
    match_obj = company_url_re.fullmatch(url)
    if match_obj:
        return match_obj.group(2)


def get_first_longest_common_substring(str1: str, str2: str) -> str:
    m = len(str1)
    n = len(str2)
    counter = [[0]*(n+1) for x in range(m+1)]
    longest = 0
    lcs_set = set()
    for i in range(m):
        for j in range(n):
            if str1[i] == str2[j]:
                c = counter[i][j] + 1
                counter[i+1][j+1] = c
                if c > longest:
                    lcs_set = set()
                    longest = c
                    lcs_set.add(str1[i - c + 1:i + 1])
                elif c == longest:
                    lcs_set.add(str1[i - c + 1:i + 1])

    return ''.join(lcs_set)


def calc_likelihood(str1: str, str2: str) -> float:
    common = get_first_longest_common_substring(str1, str2)
    return len(common)/max(len(str1), len(str2))


def get_best_matching_text(hint_text: str, texts: list[str]) -> str | None:
    ans = None
    best_point = 0
    for text in texts:
        point = calc_likelihood(hint_text, text)
        if point > best_point:
            ans = text
            best_point = point

    if ans is not None:
        return ans
