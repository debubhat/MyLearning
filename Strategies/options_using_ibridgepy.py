# -*- coding: utf-8 -*-
"""
Created on Sun Jun 03 21:06:01 2018

@author: Trader
"""

def initialize(context):
    context.run_once = True
    #context.security = symbol('AAPL')
    context.security = superSymbol(secType='OPT',symbol='AAPL',
                                   currency='USD',exchange='CBOE',expiry='20180615',strike=160,right='c')
    ## schedue_function(my_func, date_rules.every_day(),
    ##                time_rules.market_open(minutes=30))*/
    
def my_func(context_data):
    print "Inside my_func"
    
def before_trading_start(context_data):
    pass

def handle_data(context, data):
    print (get_datetime().strftime("%Y-%m-%d %H:%M:%S %Z"))
    print (data.current(context.security, ['price','bid_price','bid_size','ask_price','ask_size']))