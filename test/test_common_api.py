import unittest
import time

from openapi_client.api.api import KSTradeApi as TradingApi
from openapi_client.exceptions import ApiException, ApiValueError
from openapi_client.models import NewMTFOrder, NewNormalOrder, NewOrder, \
                        NewSMOrder, NewSOROrder, ExistingMTFOrder, ExistingNormalOrder, \
                        ExistingOrder, ExistingSMOrder, ExistingSOROrder, ReqMargin
from openapi_client.settings import host, access_token, userid, \
                        consumer_key, app_id, password, access_code, ip

class TestKSTradeApi(unittest.TestCase):
    ks_trade_api = TradingApi(host=host, access_token=access_token, userid=userid, \
                consumer_key=consumer_key, app_id=app_id, ip="127.0.0.1", \
                proxy_url="http://10.1.1.254:3128", proxy_user="nageshm", proxy_pass="augu_2020")

    def test_00_session_login_api(self):
        login_response = self.ks_trade_api.session_login_user(password=password)
        print("Login is successful. One time token is ", login_response.oneTimeToken)

    def test_01_generate_session2_fa(self):
        time.sleep(1)
        session_response = self.ks_trade_api.generate_session2_fa(access_code=access_code)
        print("Session is generated. Session token is ", session_response.sessionToken)

#----------------Order--------------------

    def test_02_place_order(self):
        print("\nPlacing order with ORDER type.")
        time.sleep(1)
        order = NewOrder(instrumentToken=727, tag="string", transactionType="BUY",\
                                variety="REGULAR", quantity=1, price=0, disclosedQuantity=0,\
                                validity="GFD", triggerPrice=0, product="NORMAL",smartOrderRouting="string")
        try:
            placed_order = self.ks_trade_api.place_order(order)
            print("\tOrder placed successfully. OrderID: "+placed_order)
            existant_order = ExistingOrder(placed_order, disclosedQuantity=0, price=0,\
            quantity=1, triggerPrice=0)
            modified_order = placed_order
            modified_order = self.ks_trade_api.modify_order(existant_order)
            print("\tOrder modified successfully. OrderID: "+modified_order)
            cancelled_order= self.ks_trade_api.cancel_order(modified_order, 'MTFO')
            print("\tOrder cancelled successfully.")
        except ApiException as e:
            if e.status in (-1,-22):
                print("\tOperation failed due to: ",e.reason)
            else:
                raise e


# ----------------Normal Order--------------------

    def test_03_place_normal_order(self):
        print("\nPlacing order with NORAML ORDER type.")
        time.sleep(1)
        order = NewNormalOrder(instrumentToken=727, tag="string", transactionType="BUY",\
                        variety="REGULAR", quantity=1, price=0, disclosedQuantity=0,\
                        validity="GFD", triggerPrice=0)
        try:
            placed_order = self.ks_trade_api.place_order(order)
            print("\tOrder placed successfully. OrderID: "+placed_order)
            existant_order = ExistingOrder(placed_order, disclosedQuantity=0, price=0,\
            quantity=1, triggerPrice=0)
            modified_order=placed_order
            modified_order = self.ks_trade_api.modify_order(existant_order)
            print("\tOrder modified successfully. OrderID: "+modified_order)
            cancelled_order= self.ks_trade_api.cancel_order(modified_order, 'MTFO')
            print("\tOrder cancelled successfully.")
        except ApiException as e:
            if e.status in (-1,-22):
                print("\tOperation failed due to: ",e.reason)
            else:
                raise e

# ----------------Multiple Order--------------------

    def test_04_place_multiple_order(self):
        print("\nPlacing order with MULTIPLE ORDER type.")
        time.sleep(1)
        order = NewSMOrder(tag="string", transactionType="BUY", instrumentToken=727,\
                    variety="REGULAR", quantity=1, price=0, disclosedQuantity=0, \
                    validity="GFD", triggerPrice=1005)
        try:
            placed_order = self.ks_trade_api.place_order(order)
            print("\tOrder placed successfully. OrderID: "+placed_order)
            existant_order = ExistingSMOrder(placed_order, disclosedQuantity=0,\
            price=0, quantity=1, triggerPrice=1000)
            modified_order = placed_order
            modified_order = self.ks_trade_api.modify_order(existant_order)
            print("\tOrder modified successfully. OrderID: "+modified_order)
            cancelled_order= self.ks_trade_api.cancel_order(modified_order, 'MTFO')
            print("\tOrder cancelled successfully.")
        except ApiException as e:
            if e.status in (-1,-22):
                print("\tOperation failed due to: ",e.reason)
            else:
                raise e


# ----------------SOR Order--------------------

    def test_05_place_sor_order(self):
        print("\nPlacing order with SOR ORDER type")
        time.sleep(1)
        order = NewSOROrder(tag="string", transactionType="BUY", instrumentToken=727,\
                    variety="REGULAR", quantity=1, price=0, validity="GFD")
        try:
            placed_order = self.ks_trade_api.place_order(order)
            placed_order = placed_order.nse.orderId if placed_order.nse.orderId else \
                                            placed_order.bse.orderId
            print("\tOrder placed successfully. OrderID: "+placed_order)
            existant_order = ExistingSOROrder(placed_order, quantity=12, price=350, \
                                            disclosedQuantity=10, triggerPrice=350)
            modified_order = placed_order
            modified_order = self.ks_trade_api.modify_order(existant_order)
            print("\tOrder modified successfully. OrderID: "+modified_order)
            cancelled_order= self.ks_trade_api.cancel_order(modified_order, 'MTFO')
            print("\tOrder cancelled successfully.")
        except ApiException as e:
            if e.status in (-1,-22):
                print("\tOperation failed due to: ",e.reason)
            else:
                raise e


# ----------------MTF Order--------------------

    def test_06_place_mtf_order(self):
        print("\nPlacing order with MTF ORDER type.")
        time.sleep(1)
        order = NewMTFOrder(tag="string", transactionType="BUY", instrumentToken=727,\
                variety="REGULAR", quantity=1, price=0, disclosedQuantity=0, \
                validity="GFD", triggerPrice=0)
        try:
            placed_order = self.ks_trade_api.place_order(order)
            print("\tOrder placed successfully. OrderID: "+placed_order)
            existant_order = ExistingMTFOrder(placed_order, disclosedQuantity=1,\
            price=0, quantity=1, triggerPrice=0)
            modified_order = placed_order
            modified_order = self.ks_trade_api.modify_order(existant_order)
            print("\tOrder modified successfully. OrderID: "+modified_order)
            cancelled_order= self.ks_trade_api.cancel_order(modified_order, 'MTFO')
            print("\tOrder cancelled successfully.")
        except ApiException as e:
            if e.status in (-1,-22):
                print("\tOperation failed due to: ",e.reason)
            else:
                raise e

#----------------------- POSITION ------------------------

    def test_07_positions_today(self):
        positions_today=self.ks_trade_api.positions_today()
        print("\nPosition Today",positions_today)

    def test_08_positions_open(self):
        positions_open=self.ks_trade_api.positions_open()
        print("Position Open", positions_open)

    def test_09_positions_stocks(self):
        positions_stocks=self.ks_trade_api.positions_stocks()
        print("Position Stock", positions_stocks)

#----------------------------------------------------------------------------------------------------------------------------
    def test_10_get_order_report(self):
        print("\nGenerating ORDER Report")
        time.sleep(1)
        get_order_report = self.ks_trade_api.get_order_report()
        print("\tOrder report generated successfully.")


    def test_11_get_order_report_by_order_id(self):
        print("\nGenerating ORDER Report by orderId")
        time.sleep(1)
        order = NewOrder(instrumentToken=727, tag="string", transactionType="BUY",\
                                variety="REGULAR", quantity=1, price=0, disclosedQuantity=0,\
                                validity="GFD", triggerPrice=0, product="NORMAL")
        placed_order = self.ks_trade_api.place_order(order)
        print("\tOrder placed with id: "+placed_order)
        get_order_report_by_order_id = self.ks_trade_api.get_order_report_by_order_id(placed_order)
        if get_order_report_by_order_id:
            print("\tOrder report generated succesfully")

#-------------------------------TRADE REPORT---------------------------------
    def test_12_get_trade_report(self):
        print("\nGenerating TRADE Report")
        time.sleep(1)
        get_trade_report = self.ks_trade_api.get_trade_report()
        if get_trade_report:
            print("\tTrade report genrated succesfully.")

    def test_13_get_trade_report_by_order_id(self):
        print("\nGenerating TRADE Report by orderId")
        time.sleep(1)
        order = NewOrder(instrumentToken=727, tag="string", transactionType="BUY",\
                                variety="REGULAR", quantity=1, price=0, disclosedQuantity=0,\
                                validity="GFD", triggerPrice=0, product="NORMAL")
        placed_order = self.ks_trade_api.place_order(order)
        print("\tOrder placed with id: "+placed_order)
        get_trade_report_by_order_id = self.ks_trade_api.get_trade_report_by_order_id(placed_order)
        if get_trade_report_by_order_id:
            print("\tTrade report received succesfully.")

#----------------------- Margin Required ------------------------

    def test_14_margin_required(self):
        orderInfo = [
        {"instrumentToken": 727, "quantity": 1, "price": 1300, "amount": 0, "triggerPrice": 1190},
        {"instrumentToken": 1374, "quantity": 1, "price": 1200, "amount": 0, "triggerPrice": 1150}
        ]
        margin_request = ReqMargin(transactionType="BUY",orderInfo=orderInfo)
        margin_required=self.ks_trade_api.margin_required(margin_request)
        print("\nMargin required tested.")


#----------------------- Quotes ------------------------

    def test_15_get_ltp_quote(self):
        instrumentTokens=110
        quote=self.ks_trade_api.get_ltp_quote(instrumentTokens)
        print("Tested get_ltp_quote with ", quote)

    def test_16_get_market_details_quote(self):
        instrumentTokens=110
        quote=self.ks_trade_api.get_market_details_quote(instrumentTokens)
        print("Tested get_market_details_quote with ", quote)

    def test_17_get_ohlc_quote(self):
        instrumentTokens=110
        quote=self.ks_trade_api.get_ohlc_quote(instrumentTokens)
        print("Tested get_ohlc_quote with ", quote)

    def test_18_get_instruments_details(self):
        instrumentTokens=110
        quote=self.ks_trade_api.get_instruments_details(instrumentTokens)
        print("Tested get_instruments_details with ", quote)

#----------------------- LOGOUT ------------------------

    def test_19_logout(self):
        logout=self.ks_trade_api.logout(userid)
        print("\nLogout successful")


if __name__ == '__main__':
    unittest.main
