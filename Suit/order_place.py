from WbfServices.wbf_config import Con
from WbfServices import wbf_config
from WbfServices.open_api_service import Order
from retrying import retry
from WbfServices.wbf_signature import Signature
import random


@retry(stop_max_attempt_number=20)
def create_order():
    """
    单个下单
    :return:
    """
    api_key = Con().environment(wbf_config.env_name)[0]
    secret_key = Con().environment(wbf_config.env_name)[1]
    request_path = '/open/api/create_order'
    host = Con().environment(wbf_config.env_name)[-2]
    side = ['BUY', 'SELL']
    tye = [1, 2, 3]
    symbol = wbf_config.symbols
    for sym in range(0, len(symbol)):
        price = abs(round(Order().lastprice(symbol[sym]) - round(random.random(), 2), 2))
        print(price)
        params = {
            'side': side[0],
            "type": tye[0],
            "volume": round(random.random() + 5, 2),
            "symbol": symbol[sym],
            "api_key": api_key,
            "time": Con().now_time(),
            "price": price
        }
        res = Signature(secret_key).post_sign(wbf_config.typ, params, request_path, host)
        print('下单响应:{}'.format(res))
        # p = {
        #     "order_id": res['data']['order_id'],
        #     "symbol": symbol[sym],
        #     "api_key": api_key,
        #     "time": Con().now_time()
        # }
        # Order().order_cancel(wbf_config.typ, p, secret_key)


if __name__ == '__main__':
    create_order()