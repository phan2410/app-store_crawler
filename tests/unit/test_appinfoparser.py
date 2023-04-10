from os.path import join as join_path

import pytest

from app.parsers import AppInfoParser
from tests.data.snapshots import PARENT_DIR as SNAPSHOT_DIR


@pytest.fixture(scope="module", params=((
    ("app_id363590051.html", dict(
        url="https://apps.apple.com/us/app/netflix/id363590051",
        id="363590051",
        name="Netflix",
        languages=["English", "Arabic", "Croatian", "Czech", "Danish", "Dutch", "Filipino",
                         "Finnish", "French", "German", "Greek", "Hebrew", "Hindi", "Hungarian",
                         "Indonesian", "Italian", "Japanese", "Korean", "Malay", "Norwegian Bokmål",
                         "Polish", "Portuguese", "Romanian", "Russian", "Simplified Chinese", "Spanish",
                         "Swedish", "Thai", "Traditional Chinese", "Turkish", "Ukrainian", "Vietnamese"],
        compatibilities=["iPhone", "iPad", "iPod touch", "Apple TV"],
    )),
    ("app_id1193542964.html", dict(
        url="https://apps.apple.com/vn/app/sony-b%E1%BA%A3o-h%C3%A0nh-%C4%91i%E1%BB%87n-t%E1%BB%AD/id1193542964",
        id="1193542964",
        name="Sony Ba\u0309o ha\u0300nh \u0111ie\u0323\u0302n tu\u031b\u0309",
        languages=["English"],
        compatibilities=["iPhone", "iPad", "iPod touch", "Mac"],
    )),
)))
def dataset(request):
    snapshot_file, expected_data = request.param
    with open(join_path(SNAPSHOT_DIR, snapshot_file), 'r') as f:
        html = f.read()

    return AppInfoParser(html=html), expected_data


def test_parse_url(dataset):
    parser, expected = dataset
    assert parser.parse_url() == expected['url']


def test_parse_id(dataset):
    parser, expected = dataset
    assert parser.parse_id() == expected['id']


def test_parse_name(dataset):
    parser, expected = dataset
    assert parser.parse_name() == expected['name']


def test_parse_languages(dataset):
    parser, expected = dataset
    assert parser.parse_languages() == expected['languages']


def test_parse_compatibilities(dataset):
    parser, expected = dataset
    assert parser.parse_compatibilities() == expected['compatibilities']


def test_parse(dataset):
    parser, expected = dataset
    result = parser.parse()

    assert result['app_name'] == expected['name']
    assert result['app_id'] == f"id{expected['id']}"
    assert result['app_url'] == expected['url']
    assert result['app_targets'] == expected['compatibilities']
