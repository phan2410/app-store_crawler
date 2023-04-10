# App Store Crawler

1. [Run Locally](#run-locally)
2. [Run in Container](#run-in-container)
3. [Technical Decisions](#technical-decisions)
4. [Known Issues/Limitations](#known-issueslimitations)
5. [Potential Enhancements](#potential-enhancements)

## Run Locally

### Prerequisites
* python >= 3.10
* poetry

### Preparation

```shell
git clone https://github.com/phan2410/app-store_crawler
cd app-store_crawler
poetry install
source $(poetry env info --path)/bin/activate
playwright install
playwright install-deps
export PYTHONPATH=$(pwd)
```

### Running

```shell
python app/main.py -h
```

```text
(app-store-crawler-py3.11) anphan@Ans-MacBook-Pro app-store_crawler % python app/main.py -h
usage: main.py [-h] [-v] [-b] [-s SLOW_MO] -n COMPANY_NAME

craw all apps info from the company.

options:
  -h, --help            show this help message and exit
  -v, --verbose         print out data during progress
  -b, --browser         show browser if possible
  -s SLOW_MO, --slow_mo SLOW_MO
                        slow down by an amount of milliseconds
  -n COMPANY_NAME, --company_name COMPANY_NAME
                        specify company name
```

For example, if we want to craw all apps from `netflix`, we can run:

```shell
python app/main.py -v -n netflix
```

```text
(app-store-crawler-py3.11) anphan@Ans-MacBook-Pro app-store_crawler % python app/main.py -bv -n netflix
=> Found companies
{
    "netflix-inc": "https://apps.apple.com/vn/developer/netflix-inc/id363590054",
    "iqiyi-international-singapore-pte-ltd": "https://apps.apple.com/vn/developer/iqiyi-international-singapore-pte-ltd/id1512375522",
    "pixel-web-design": "https://apps.apple.com/vn/developer/pixel-web-design/id1482651454",
    "digital-tools-ltd": "https://apps.apple.com/vn/developer/digital-tools-ltd/id852921471",
    "google-llc": "https://apps.apple.com/vn/developer/google-llc/id281956209",
    "apple": "https://apps.apple.com/vn/developer/apple/id284417353?mt=12",
    "vlad-khodiachiy": "https://apps.apple.com/vn/developer/vlad-khodiachiy/id1269553810"
}
=> Best match name: netflix-inc | https://apps.apple.com/vn/developer/netflix-inc/id363590054
=> App urls to be crawled
[
    "https://apps.apple.com/vn/app/raji-an-ancient-epic/id1616746285",
    "https://apps.apple.com/vn/app/terra-nil/id1643974911",
    "https://apps.apple.com/vn/app/highwater/id1634668889",
...
...
...
=> Result:
[
    {
        "app_name": "Raji: An Ancient Epic",
        "app_id": "id1616746285",
        "app_url": "https://apps.apple.com/vn/app/raji-an-ancient-epic/id1616746285",
        "app_targets": [
            "iPhone",
            "iPad"
        ]
    },
    {
        "app_name": "Terra Nil",
        "app_id": "id1643974911",
        "app_url": "https://apps.apple.com/vn/app/terra-nil/id1643974911",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Highwater",
        "app_id": "id1634668889",
        "app_url": "https://apps.apple.com/vn/app/highwater/id1634668889",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Dust & Neon",
        "app_id": "id1622720173",
        "app_url": "https://apps.apple.com/vn/app/dust-neon/id1622720173",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Tomb Raider Reloaded NETFLIX",
        "app_id": "id6444630059",
        "app_url": "https://apps.apple.com/vn/app/tomb-raider-reloaded-netflix/id6444630059",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Valiant Hearts: Coming Home",
        "app_id": "id1639590978",
        "app_url": "https://apps.apple.com/vn/app/valiant-hearts-coming-home/id1639590978",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Narcos: Cartel Wars Unlimited",
        "app_id": "id1631388889",
        "app_url": "https://apps.apple.com/vn/app/narcos-cartel-wars-unlimited/id1631388889",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "TMNT: Shredder's Revenge",
        "app_id": "id6443475072",
        "app_url": "https://apps.apple.com/vn/app/tmnt-shredders-revenge/id6443475072",
        "app_targets": [
            "iPhone",
            "iPad"
        ]
    },
    {
        "app_name": "Puzzle Gods",
        "app_id": "id1639986474",
        "app_url": "https://apps.apple.com/vn/app/puzzle-gods/id1639986474",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Kentucky Route Zero",
        "app_id": "id1608096851",
        "app_url": "https://apps.apple.com/vn/app/kentucky-route-zero/id1608096851",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Twelve Minutes",
        "app_id": "id1608097361",
        "app_url": "https://apps.apple.com/vn/app/twelve-minutes/id1608097361",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Classic Solitaire NETFLIX",
        "app_id": "id6443474985",
        "app_url": "https://apps.apple.com/vn/app/classic-solitaire-netflix/id6443474985",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Scriptic Netflix Edition",
        "app_id": "id6443474850",
        "app_url": "https://apps.apple.com/vn/app/scriptic-netflix-edition/id6443474850",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Too Hot to Handle NETFLIX",
        "app_id": "id1633494204",
        "app_url": "https://apps.apple.com/vn/app/too-hot-to-handle-netflix/id1633494204",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Cats & Soup Netflix Edition",
        "app_id": "id1633703782",
        "app_url": "https://apps.apple.com/vn/app/cats-soup-netflix-edition/id1633703782",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "HELLO KITTY HAPPINESS PARADE",
        "app_id": "id1615428932",
        "app_url": "https://apps.apple.com/vn/app/hello-kitty-happiness-parade/id1615428932",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Reigns: Three Kingdoms",
        "app_id": "id1636948693",
        "app_url": "https://apps.apple.com/vn/app/reigns-three-kingdoms/id1636948693",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "IMMORTALITY",
        "app_id": "id1603724053",
        "app_url": "https://apps.apple.com/vn/app/immortality/id1603724053",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Country Friends",
        "app_id": "id1633708360",
        "app_url": "https://apps.apple.com/vn/app/country-friends/id1633708360",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Stranger Things: Puzzle Tales",
        "app_id": "id1633705525",
        "app_url": "https://apps.apple.com/vn/app/stranger-things-puzzle-tales/id1633705525",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "NETFLIX Flutter Butterflies",
        "app_id": "id1636547336",
        "app_url": "https://apps.apple.com/vn/app/netflix-flutter-butterflies/id1636547336",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Skies of Chaos",
        "app_id": "id1612698180",
        "app_url": "https://apps.apple.com/vn/app/skies-of-chaos/id1612698180",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Spiritfarer: Netflix Edition",
        "app_id": "id1610577424",
        "app_url": "https://apps.apple.com/vn/app/spiritfarer-netflix-edition/id1610577424",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Desta: The Memories Between",
        "app_id": "id1599584290",
        "app_url": "https://apps.apple.com/vn/app/desta-the-memories-between/id1599584290",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Nailed It! Baking Bash",
        "app_id": "id1597203429",
        "app_url": "https://apps.apple.com/vn/app/nailed-it-baking-bash/id1597203429",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "SpongeBob: Get Cooking",
        "app_id": "id1633284064",
        "app_url": "https://apps.apple.com/vn/app/spongebob-get-cooking/id1633284064",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "OXENFREE: Netflix Edition",
        "app_id": "id1613438096",
        "app_url": "https://apps.apple.com/vn/app/oxenfree-netflix-edition/id1613438096",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Rival Pirates",
        "app_id": "id1597203106",
        "app_url": "https://apps.apple.com/vn/app/rival-pirates/id1597203106",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Wild Things Animal Adventures",
        "app_id": "id1615431398",
        "app_url": "https://apps.apple.com/vn/app/wild-things-animal-adventures/id1615431398",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Lucky Luna",
        "app_id": "id1609150630",
        "app_url": "https://apps.apple.com/vn/app/lucky-luna/id1609150630",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Heads Up! Netflix Edition",
        "app_id": "id1618819167",
        "app_url": "https://apps.apple.com/vn/app/heads-up-netflix-edition/id1618819167",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Mahjong Solitaire NETFLIX",
        "app_id": "id1616966568",
        "app_url": "https://apps.apple.com/vn/app/mahjong-solitaire-netflix/id1616966568",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Before Your Eyes",
        "app_id": "id1614500347",
        "app_url": "https://apps.apple.com/vn/app/before-your-eyes/id1614500347",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Into the Breach",
        "app_id": "id1616542180",
        "app_url": "https://apps.apple.com/vn/app/into-the-breach/id1616542180",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "NETFLIX Poinpy",
        "app_id": "id1615093407",
        "app_url": "https://apps.apple.com/vn/app/netflix-poinpy/id1615093407",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "NETFLIX Exploding Kittens",
        "app_id": "id1606221795",
        "app_url": "https://apps.apple.com/vn/app/netflix-exploding-kittens/id1606221795",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Dragon Up!",
        "app_id": "id1605049471",
        "app_url": "https://apps.apple.com/vn/app/dragon-up/id1605049471",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "NETFLIX Moonlighter",
        "app_id": "id1612148433",
        "app_url": "https://apps.apple.com/vn/app/netflix-moonlighter/id1612148433",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Townsmen \u2013 A Kingdom Rebuilt",
        "app_id": "id1606798199",
        "app_url": "https://apps.apple.com/vn/app/townsmen-a-kingdom-rebuilt/id1606798199",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Relic Hunters: Rebels",
        "app_id": "id1605236950",
        "app_url": "https://apps.apple.com/vn/app/relic-hunters-rebels/id1605236950",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Into the Dead 2: Unleashed",
        "app_id": "id1607178247",
        "app_url": "https://apps.apple.com/vn/app/into-the-dead-2-unleashed/id1607178247",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Shatter Remastered",
        "app_id": "id1605234654",
        "app_url": "https://apps.apple.com/vn/app/shatter-remastered/id1605234654",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "This is a True Story",
        "app_id": "id1598949458",
        "app_url": "https://apps.apple.com/vn/app/this-is-a-true-story/id1598949458",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Dungeon Dwarves",
        "app_id": "id1594689765",
        "app_url": "https://apps.apple.com/vn/app/dungeon-dwarves/id1594689765",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Hextech Mayhem Netflix Edition",
        "app_id": "id1589160731",
        "app_url": "https://apps.apple.com/vn/app/hextech-mayhem-netflix-edition/id1589160731",
        "app_targets": [
            "iPhone",
            "iPad"
        ]
    },
    {
        "app_name": "Arcanium: Rise of Akhan",
        "app_id": "id1589157123",
        "app_url": "https://apps.apple.com/vn/app/arcanium-rise-of-akhan/id1589157123",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Krispee Street",
        "app_id": "id1597202855",
        "app_url": "https://apps.apple.com/vn/app/krispee-street/id1597202855",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Dominoes Cafe\u0301",
        "app_id": "id1589123450",
        "app_url": "https://apps.apple.com/vn/app/dominoes-caf%C3%A9/id1589123450",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Knittens: Match 3 Puzzle",
        "app_id": "id1588956383",
        "app_url": "https://apps.apple.com/vn/app/knittens-match-3-puzzle/id1588956383",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Wonderputt Forever",
        "app_id": "id1589157030",
        "app_url": "https://apps.apple.com/vn/app/wonderputt-forever/id1589157030",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Asphalt Xtreme",
        "app_id": "id1590574622",
        "app_url": "https://apps.apple.com/vn/app/asphalt-xtreme/id1590574622",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Card Blast!",
        "app_id": "id1586360462",
        "app_url": "https://apps.apple.com/vn/app/card-blast/id1586360462",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "NETFLIX Bowling Ballers",
        "app_id": "id1589157317",
        "app_url": "https://apps.apple.com/vn/app/netflix-bowling-ballers/id1589157317",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Shooting Hoops",
        "app_id": "id1585735348",
        "app_url": "https://apps.apple.com/vn/app/shooting-hoops/id1585735348",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Stranger Things: 1984",
        "app_id": "id1574739824",
        "app_url": "https://apps.apple.com/vn/app/stranger-things-1984/id1574739824",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Stranger Things 3 The Game",
        "app_id": "id1574824199",
        "app_url": "https://apps.apple.com/vn/app/stranger-things-3-the-game/id1574824199",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Teeter Up: Remastered",
        "app_id": "id1585735663",
        "app_url": "https://apps.apple.com/vn/app/teeter-up-remastered/id1585735663",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "FAST Speed Test",
        "app_id": "id1133348139",
        "app_url": "https://apps.apple.com/vn/app/fast-speed-test/id1133348139",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch"
        ]
    },
    {
        "app_name": "Netflix",
        "app_id": "id363590051",
        "app_url": "https://apps.apple.com/vn/app/netflix/id363590051",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch",
            "Apple TV"
        ]
    },
    {
        "app_name": "Netflix",
        "app_id": "id363590051",
        "app_url": "https://apps.apple.com/vn/app/netflix/id363590051",
        "app_targets": [
            "iPhone",
            "iPad",
            "iPod touch",
            "Apple TV"
        ]
    }
]
```

### Testing

```shell
pytest --cov
```

```text
(app-store-crawler-py3.11) anphan@Ans-MacBook-Pro app-store_crawler % pytest --cov
===================================================================== test session starts =====================================================================
platform darwin -- Python 3.11.2, pytest-7.3.0, pluggy-1.0.0
rootdir: /Users/anphan/Dropbox/git/app-store_crawler
plugins: cov-4.0.0
collected 39 items                                                                                                                                            

tests/unit/test_appinfoparser.py ............                                                                                                           [ 30%]
tests/unit/test_parsers.py ..                                                                                                                           [ 35%]
tests/unit/test_utils.py .........................                                                                                                      [100%]

---------- coverage: platform darwin, python 3.11.2-final-0 ----------
Name                                 Stmts   Miss  Cover
--------------------------------------------------------
app/__init__.py                          0      0   100%
app/parsers.py                          29      0   100%
app/utils.py                            57      0   100%
tests/__init__.py                        0      0   100%
tests/data/__init__.py                   0      0   100%
tests/data/snapshots/__init__.py         1      0   100%
tests/data/snapshots/base.py             2      0   100%
tests/integration/__init__.py            0      0   100%
tests/integration/test_crawlers.py       0      0   100%
tests/unit/__init__.py                   0      0   100%
tests/unit/test_appinfoparser.py        32      0   100%
tests/unit/test_parsers.py               7      0   100%
tests/unit/test_utils.py                48      0   100%
--------------------------------------------------------
TOTAL                                  176      0   100%


===================================================================== 39 passed in 0.74s ======================================================================
```

## Run In Container

### Prerequisites

* docker

### Preparation

* build docker image

```shell
docker build -t crawler .
```

### Running

Similar to the local version, we can run:

```shell
docker run -it --rm crawler \
bash -c 'export PYTHONPATH=$(pwd) && poetry run python app/main.py --help'
```

```text

```

For example,

```shell
docker run -it --rm crawler \
bash -c 'export PYTHONPATH=$(pwd) && poetry run python app/main.py -v -n netflix'
```

```text

```


### Testing

```shell
docker run -it --rm crawler bash -c 'export PYTHONPATH=$(pwd) && poetry run pytest --cov'
```

```text

```

## Technical decisions

* I use headless browser because there is several javascript and expandable purposes for future tasks
* I choose Playwright over Selenium because:
  * Playwright is built specifically for modern web development, 
    and it has better support for modern web frameworks like React and Angular.
  * Playwright is built from the ground up to be lightweight and fast, 
    and it has better performance than Selenium in many scenarios.
  * Playwright has better support for headless testing 
    and provides more control over the headless browser environment.
  * Playwright has better support for integrated testing.

## Known issues/limitations:

There are still issues/limitations to be taken care of:
* Company name matching: Currently, I just take the most similar name from the search list, to decide the company from a given name. 
  If it is in real life, we need to clarify with customer, so that the result is more accurate
* Region/Language issue: some apps only exist for some regions/languages, so do company
* Bot detection: currently crawling too much might get banned, need to imitate human being behaviors at finer granularity
* Crawling speed: currently only a single page is up at a time, need to improve later

## Potential enhancements:

Still, there is a lot to consider, so I haven't yet implement integration tests. But I do manually test myself,
you can check [here](https://youtu.be/SeMjE_R_2AE).

If I have more time/resources, I can do:
* Stealth mode: make use of context settings such as user-agent, proxy, ..., in order to bypass fingerprint check
* IP rotation: to overcome region/language issue, and access more resource to crawl
* Async/parallel worker: with the use of IP rotation, number of concurrent/parallel worker can be used to maximize speed
* Regional worker specialization: we can spin up several headless browser servers, each has its own proxy list with respects
  to a specific region, doing this way, we can have a main app running to coordinate crawling from these regional workers. 
  Making the modules become loose-coupling, and thereby easier to maintain and develop.


