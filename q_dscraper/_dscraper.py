"""
指定されるURLのページソースを取得
"""
import datetime as dt
import json
import os
import time
from urllib import request, parse
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
from selenium import webdriver
from fake_useragent import UserAgent

from ._logger import getLogger


# ログ設定
logfilename = os.path.splitext(os.path.basename(__file__))[0] + '.log'
logger = getLogger(os.path.basename(__file__), saveName=logfilename)

# 日本標準時タイムゾーン定義
TZ_JST = dt.timezone(dt.timedelta(hours=+9))

# 遅延ロード開始位置オフセット
PAGE_LOAD_OFFSET = 300


class DyScrape:
    """ 静的/動的ページスクレイプ用クラス
        遅延ロードページ対応
    """
    def __init__(self, endpoint: str, params: dict = None, method: str = 'GET'):
        self.__endpoint = endpoint
        self.__params = params
        self.__method = method
        self.__domlist = None
        self.__datetime = None
        self.__useragent = UserAgent()

    # 静的ページの走査
    def fetch(self, selector: str = None, dselector: str = None) -> None:
        logger.info('FETCH: STARTED')

        # リクエストヘッダ設定（疑似ユーザーエージェント）
        headers = {
            'User-Agent': self.__useragent.random
        }
        # リクエストパラメータ設定
        if self.__params is not None:
            self.__params = json.dumps(self.__params).encode()

        req = request.Request(self.__endpoint, data=self.__params, headers=headers, method=self.__method)

        self.__datetime = dt.datetime.now(TZ_JST)
        logger.info(f'Endpoint: {self.__endpoint}')
        logger.info(f'Parameters: {self.__params}')

        try:
            with request.urlopen(req) as res:
                soup = BeautifulSoup(res, 'html.parser')

                if selector is None:
                    # セレクタ指定がない場合は対象ページすべてのDOMを設定
                    logger.info('Selector: None')
                    self.__domlist = [soup.prettify()]
                else:
                    logger.info(f'Selector: {selector}')
                    self.__domlist = soup.select(selector)

                    # セレクタで指定したDOMがなく、遅延ロード対象のセレクタが指定されている場合は動的ページの走査を行う
                    if self.__domlist == [] and dselector is not None:
                        self.dynamic_fetch(selector, dselector)
        except HTTPError as e:
            logger.error(e)
        except URLError as e:
            logger.error(e)

        logger.info('FETCH: SUCCESSED')

    # 動的ページの走査
    def dynamic_fetch(self, selector: str = None, dselector: str = None) -> None:
        logger.info(f'Dynamic Selector: {dselector}')

        # ユーザーエージェント取得
        useragent = UserAgent().random

        # ブラウザをheadlessモード（バックグラウンドで動くモード）で立ち上げる
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument(f'user-agent="{useragent}"')

        # ブラウザを起動する
        driver = webdriver.Chrome('chromedriver', options=options)

        uri = self.__endpoint + f'?{parse.urlencode(json.loads(self.__params))}' if self.__params is not None else ''

        driver.get(uri)
        html = driver.page_source.encode('utf-8')

        if dselector is not None:
            while True:

                js = f'window.scrollTo(0, document.querySelector("{dselector}").scrollHeight + {PAGE_LOAD_OFFSET})'
                driver.execute_script(js)
                logger.info('Lazy Loading...')
                time.sleep(1)
                html_after_scroll = driver.page_source.encode('utf-8')
                if html != html_after_scroll:
                    html = html_after_scroll
                else:
                    break

        soup = BeautifulSoup(html, 'html.parser')

        if selector is None:
            self.__domlist = [soup.find()]
        else:
            self.__domlist = soup.select(selector)

    @property
    def domlist(self):
        """
        dom getter
        """
        return self.__domlist

    @property
    def datetime(self):
        """
        datetime getter
        """
        return self.__datetime
