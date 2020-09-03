# coding: utf-8

# flake8: noqa

"""
    KS Trade API's



    The version of the OpenAPI document: 1.0

"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from openapi_client.api.margin_api import MarginApi
from openapi_client.api.margin_trading_api import MarginTradingApi
from openapi_client.api.normal_order_api import NormalOrderApi
from openapi_client.api.order_api import OrderApi
from openapi_client.api.positions_api import PositionsApi
from openapi_client.api.quote_api import QuoteApi
from openapi_client.api.reports_api import ReportsApi
from openapi_client.api.session_api import SessionApi
from openapi_client.api.smart_order_routing_api import SmartOrderRoutingApi
from openapi_client.api.super_multiple_order_api import SuperMultipleOrderApi

# import ApiClient
from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration
from openapi_client.exceptions import OpenApiException
from openapi_client.exceptions import ApiTypeError
from openapi_client.exceptions import ApiValueError
from openapi_client.exceptions import ApiKeyError
from openapi_client.exceptions import ApiAttributeError
from openapi_client.exceptions import ApiException
# import models into sdk package
from openapi_client.models.bracketcancel import Bracketcancel
from openapi_client.models.bracketmodify import Bracketmodify
from openapi_client.models.bracketplace import Bracketplace
from openapi_client.models.buy import Buy
from openapi_client.models.codcancel import Codcancel
from openapi_client.models.codmodify import Codmodify
from openapi_client.models.codplace import Codplace
from openapi_client.models.ctdmodify import Ctdmodify
from openapi_client.models.ctdplace import Ctdplace
from openapi_client.models.depth import Depth
from openapi_client.models.existing_mtf_order import ExistingMTFOrder
from openapi_client.models.existing_normal_order import ExistingNormalOrder
from openapi_client.models.existing_order import ExistingOrder
from openapi_client.models.existing_sm_order import ExistingSMOrder
from openapi_client.models.existing_sor_order import ExistingSOROrder
from openapi_client.models.fault import Fault
from openapi_client.models.gtccancel import Gtccancel
from openapi_client.models.gtcmodify import Gtcmodify
from openapi_client.models.gtcplace import Gtcplace
from openapi_client.models.history import History
from openapi_client.models.instrument import Instrument
from openapi_client.models.ltp_quote import LTPQuote
from openapi_client.models.margin_det import MarginDet
from openapi_client.models.market_details_quote import MarketDetailsQuote
from openapi_client.models.new_mtf_order import NewMTFOrder
from openapi_client.models.new_normal_order import NewNormalOrder
from openapi_client.models.new_order import NewOrder
from openapi_client.models.new_sm_order import NewSMOrder
from openapi_client.models.new_sor_order import NewSOROrder
from openapi_client.models.ohlc_quote import OHLCQuote
from openapi_client.models.open import Open
from openapi_client.models.order_info import OrderInfo
from openapi_client.models.orders import Orders
from openapi_client.models.positions import Positions
from openapi_client.models.req_margin import ReqMargin
from openapi_client.models.res_login import ResLogin
from openapi_client.models.res_logout import ResLogout
from openapi_client.models.res_mtf_mod import ResMTFMod
from openapi_client.models.res_mtf_order_cancel import ResMTFOrderCancel
from openapi_client.models.res_new_mtf_order import ResNewMTFOrder
from openapi_client.models.res_new_normal_order import ResNewNormalOrder
from openapi_client.models.res_new_order import ResNewOrder
from openapi_client.models.res_new_sm_order import ResNewSMOrder
from openapi_client.models.res_new_sor_order import ResNewSOROrder
from openapi_client.models.res_normal_order_cancel import ResNormalOrderCancel
from openapi_client.models.res_normal_order_mod import ResNormalOrderMod
from openapi_client.models.res_order_cancel import ResOrderCancel
from openapi_client.models.res_order_mod import ResOrderMod
from openapi_client.models.res_sm_order_cancel import ResSMOrderCancel
from openapi_client.models.res_sm_order_mod import ResSMOrderMod
from openapi_client.models.res_sor_order_cancel import ResSOROrderCancel
from openapi_client.models.res_sor_order_mod import ResSOROrderMod
from openapi_client.models.res_session2_fa import ResSession2FA
from openapi_client.models.res_session_init import ResSessionInit
from openapi_client.models.res_session_init_encryption import ResSessionInitEncryption
from openapi_client.models.res_session_init_redirect import ResSessionInitRedirect
from openapi_client.models.res_session_init_weblink import ResSessionInitWeblink
from openapi_client.models.sell import Sell
from openapi_client.models.sor import Sor
from openapi_client.models.stocks import Stocks
from openapi_client.models.todays import Todays
from openapi_client.models.trades import Trades
from openapi_client.models.tslocancel import Tslocancel
from openapi_client.models.tslomodify import Tslomodify
from openapi_client.models.tsloplace import Tsloplace
from openapi_client.models.user_credentials import UserCredentials
from openapi_client.models.user_details import UserDetails

