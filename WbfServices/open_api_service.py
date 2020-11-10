from WbfServices import wbf_signature
import requests
from WbfServices.wbf_config import Con
from WbfServices import wbf_config


class Order:

    def market_depth(self, sym, typ):
        """
        获取市场买卖盘
        :return:
        """
        request_path = '/open/api/market_dept'
        url = Con().environment(wbf_config.env_name)[-2] + request_path
        params = {"symbol": sym, "type": typ}
        try:
            res = requests.get(url=url, params=params)
            if res.status_code == 200:
                r = res.json()
                # print(r)
                return r
        except Exception as e:
            # print('error：{}'.format(e))
            Con().return_log(params, url, e)

    def lastprice(self, symbol):
        """
        获取最新成交价
        :param symbol:
        :return:
        """
        url = Con().environment(wbf_config.env_name)[-2] + '/open/api/market'
        params = {"symbol": symbol}
        try:
            result = requests.get(url, params=params)
            # print(result.json())
            if result.status_code == 200:
                last_price = result.json()['data'][symbol]
                if last_price is None:
                    return 0
                else:
                    print(last_price)
                    return last_price
        except Exception as e:
            # print("error:{}".format(e))
            Con().return_log(params, url, e)

    def order_place(self, types, p, secret_key):
        """
        创建订单
        :param p:
        :return:
        """
        request_path = '/open/api/create_order'
        result = wbf_signature.Signature(secret_key).post_sign(
            types, p, request_path, Con().environment(wbf_config.env_name)[-2])
        print('创建订单:{}'.format(result))

    def order_cancel(self, types, p, secret_key):
        """
        撤销订单
        :param p:
        :return:
        """
        request_path = '/open/api/cancel_order'
        result = wbf_signature.Signature(secret_key).post_sign(
            types, p, request_path, Con().environment(wbf_config.env_name)[-2])
        print('撤销订单:{}'.format(result))


if __name__ == '__main__':
    # Order().lastprice(wbf_config.symbol)
    Order().market_depth(wbf_config.symbol, 'step0')


