from q_dscraper import DyScrape


def main():
    scrape = DyScrape('https://yahoo.co.jp')
    scrape.fetch(selector='#tabpanelTopics1 > div > div > ul > li > article > a > div > div > h1 > span')

    print(scrape.domlist)
    print([dom.text for dom in scrape.domlist])


if __name__ == '__main__':
    main()
