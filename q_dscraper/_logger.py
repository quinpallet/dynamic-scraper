import datetime as dt
import logging


def getLogger(name, level=logging.DEBUG, saveName='logger.log'):
    """
    Loggerを作成する。
    name：Loggerの名前（string)
    level:Loggingのレベル(int)
    saveName：Loggerの保存先（string)
    """
    # ロガーの定義
    logger = logging.getLogger(name)
    logger.setLevel(level)
    # フォーマットの定義
    formatter = logging.Formatter(
        '%(asctime)s %(name)-14s %(levelname)-10s %(message)s')
    formatter.converter = lambda *args: dt.datetime.now(
        dt.timezone(dt.timedelta(hours=9))).timetuple()
    # ファイル書き込み用
    fh = logging.FileHandler(saveName)
    fh.setFormatter(formatter)
    # コンソール出力用
    # sh = logging.StreamHandler()
    # sh.setFormatter(formatter)
    # それぞれロガーに追加
    logger.addHandler(fh)
    # logger.addHandler(sh)

    return logger
