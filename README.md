# dynamic-scraper

Dynamic scraper package for Python

## Requirements

- [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Selenium](https://www.selenium.dev/documentation/en/)
- [ChromeDriver](http://chromedriver.chromium.org/getting-started)
- [fake-useragent](https://github.com/hellysmile/fake-useragent)

## Prerequisites

- Python >= 3.9
- beautifulsoup4 >= 4.9.3
- (bs4 >= 0.0.1)
- fake-useragent >= 0.1.11
- selenium >= 3.141.0
- fake-useragent >= 0.1.11

## Usage

```sh
$ pip install git+https://github.com/quinpallet/dynamic-scraper
```

``` python
from q_dscraper import DyScrape

scrape = DyScrape('https://yahoo.co.jp')
scrape.fetch(selector='#tabpanelTopics1 > div > div > ul > li > article > a > div > div > h1 > span')

print(scrape.domlist)
print([dom.text for dom in scrape.domlist])
```

> OUTPUT:
>
> [<span class="fQMqQTGJTbIMxjQwZA2zk _3tGRl6x9iIWRiFTkKl3kcR">時短要請甘かった 首相が反省</span>, <span class="fQMqQTGJTbIMxjQwZA2zk _3tGRl6x9iIWRiFTkKl3kcR">PCR結果待つ間 2人自宅で死亡</span>, <span class="fQMqQTGJTbIMxjQwZA2zk _3tGRl6x9iIWRiFTkKl3kcR">家に感染中傷ビラ 偏見やめて</span>, <span class="fQMqQTGJTbIMxjQwZA2zk _3tGRl6x9iIWRiFTkKl3kcR">旭川医大に職員 驚きあきれる</span>, <span class="fQMqQTGJTbIMxjQwZA2zk _3tGRl6x9iIWRiFTkKl3kcR">トランプ氏 フロリダに事務所</span>, <span class="fQMqQTGJTbIMxjQwZA2zk _3tGRl6x9iIWRiFTkKl3kcR">給食に異物週3回 保護者怒り</span>, <span class="fQMqQTGJTbIMxjQwZA2zk _3tGRl6x9iIWRiFTkKl3kcR">ヒルマイルド 商標巡り声明</span>, <span class="fQMqQTGJTbIMxjQwZA2zk _3tGRl6x9iIWRiFTkKl3kcR">歌手・BENI 第1子男児を出産</span>]
> ['時短要請甘かった 首相が反省', 'PCR結果待つ間 2人自宅で死亡', '家に感染中傷ビラ 偏見やめて', '旭川医大に職員 驚きあきれる', 'トランプ氏 フロリダに事務所', '給食に異物週3回 保護者怒り', 'ヒルマイルド 商標巡り声明', '歌手・BENI 第1子男児を出産']


## License

&copy; 2021 [Ken Kurosaki](https://github.com/quinpallet).<br>
This project is [MIT](https://github.com/quinpallet/dynamic-scraper/blob/master/LICENSE) licensed.