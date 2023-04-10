import argparse
import json

from app.crawlers import crawl_company_apps


def main(args=None):
    parser = argparse.ArgumentParser(description='craw all apps info from the company.')
    parser.add_argument('-v', '--verbose', help='print out data during progress', action='store_true')
    parser.add_argument('-b', '--browser', help='show browser if possible', action='store_true', default=False)
    parser.add_argument('-s', '--slow_mo', type=float, help='slow down by an amount of milliseconds', default=None)
    parser.add_argument('-n', '--company_name', type=str, help='specify company name', required=True)
    parser = parser.parse_args(args)

    data = crawl_company_apps(company_name=parser.company_name, **dict(
        print=parser.verbose,
        headless=not parser.browser,
        slow_mo=parser.slow_mo
    ))

    print(f"=> Result:\n{json.dumps(data, indent=4)}")


if __name__ == '__main__':
    main()


