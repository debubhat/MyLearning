# -*- coding: utf-8 -*-
"""
Created on Sun Jun 03 21:06:01 2018

@author: Trader
"""

def initialize(context):
    context.run_once = False
    context.security = symbol('STK,AAPL,USD')
    #context.security = symbols('STK,AAPL,USD','STK,GOOG,USD')
    #context.security = symbol(STK,AAPL,USD)
    ## schedue_function(my_func, date_rules.every_day(),
    ##                time_rules.market_open(minutes=30))*/
    
def my_func(context_data):
    print "Inside my_func"
    
def before_trading_start(context_data):
    pass

def handle_data(context, data):
    #print (get_datetime().strftime("%Y-%m-%d %H:%M:%S %Z"))
    #dt = data.history(context.security,['open','high','low','close'],10,'1d')
    #dt = request_historical_data(context.security,'1 day','30 D')
    dt = request_historical_data(context.security,'5 min','60 MIN')
    #print (data.current(context.security, ['price','bid_price','bid_size','ask_price','ask_size']))
    print dt
    end()