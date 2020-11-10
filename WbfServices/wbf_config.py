
from WbfServices import open_yaml
import os
import logging
import time

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_name = 'stg'
sex = 0
symbol = 'zhfusdt'
symbols = [
    'oxeusdt','xdcusdt','scusdt','wbiusdt','vscusdt','xdusdt','atomusdt','ptocusdt','vrdusdt','btcvusdt',
    'myusdt','cs3usdt','ggausdt','btrusdt','atcusdt','cs2usdt','ttmusdt','acdusdt','vipusdt','ljbusdt',
    'ggbusdt','ystusdt','ccmusdt','dscusdt','aplusdt','xrpusdt','aacusdt','oneusdt','swcusdt','diausdt',
    'wbbusdt','bchusdt','ltcusdt','etcusdt','ethusdt','batusdt','eosusdt','vcceth','ttmeth','ldseth',
    'eoseth','dscbtc','timebtc','ltcbtc','ethbtc','zrxbtc','eosbtc','batbtc','dgdbtc','mywt','btcvdusd',
    'usdtdusd','ilcusdt','btcwt','www22usdt','bntusdt','www22btc','www22eth','www22dusd','etdogusdt',
    'wptusdt','fcsusdt','ldsusdt','ineusdt','keousdt','tngusdt','cs1usdt','nbcusdt','mwdusdt','crlusdt',
    'cwcusdt','www22wt','eoswt','gntbtc','linkbtc','omgbtc','powrbtc','waxbtc','zilbtc','bateth','zrxeth',
    'dgdeth','gnteth','ineeth','linketh','manaeth','omgeth','powreth','waxeth','zileth','bpayusdt','btcdusd','ethdusd'
           ]
step = 'step0'
typ = 'old'
region = symbol + 'OrderSeq'
# symbol = 'test100usdt'  # 行情计算


class Con:

    def now_time(self):
        now_time = int(time.time())
        return now_time

    def environment(self, env):
        if env == env_name:
            key = open_yaml.read()[env]['access-key'].split(',')[0]
            secret = open_yaml.read()[env]['secret-key'].split(',')[0]
            api_key = open_yaml.read()[env]['access-key'].split(',')[1]
            secret_key = open_yaml.read()[env]['secret-key'].split(',')[1]
            host = open_yaml.read()[env]['host']
            ws = open_yaml.read()[env]['ws']
            # print(api_key)
            if sex == 0:
                return key, secret, host, ws
            else:
                return api_key, secret_key, host, ws

    def sql(self, env):
        if env == env_name:
            host = open_yaml.read()[env]['db']['host']
            port = open_yaml.read()[env]['db']['port']
            user = open_yaml.read()[env]['db']['user']
            password = open_yaml.read()[env]['db']['password']
            database = open_yaml.read()[env]['dn']['database']
            return host, user, password, port, database

    def return_log(self, post_data, url, response):
        log_path = os.path.join(basedir, './Log')
        if not os.path.exists(log_path): os.mkdir(log_path)
        logname = os.path.join(log_path, '%s.log' % time.strftime('%Y_%m_%d'))
        file = os.path.join(log_path, logname)
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s:%(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S', filename=file, filemode='a')
        logger = logging.getLogger()
        return logger.info(post_data), logger.info(url), logger.info(response)


