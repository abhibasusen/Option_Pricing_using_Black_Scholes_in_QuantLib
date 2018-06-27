# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 15:42:09 2018

@author: ABHIBASU SEN
"""

from QuantLib import *
import matplotlib.pyplot as plot
import numpy
from IPython.display import display
import utils

underlying_value=input('What is the underlying value?')
risk_free_rate=input('What is the risk free rate?')
volatility=input('What is the volatility?')
t1=input('What is day today?')
t2=input('What is month now?')
t3=input('What is year now?')
t4=input('What is the exercise day?')
t5=input('What is the exercise month?')
t6=input('What is the exercise year?')
today = Date(t1, t2, t3)
Settings.instance().evaluationDate = today
option = EuropeanOption(PlainVanillaPayoff(Option.Call, underlying_value),
EuropeanExercise(Date(t4, t5, t6)))
u = SimpleQuote(underlying_value)
r = SimpleQuote(risk_free_rate)
sigma = SimpleQuote(volatility)
riskFreeCurve = FlatForward(0, TARGET(), QuoteHandle(r), Actual360())
volatility = BlackConstantVol(0, TARGET(), QuoteHandle(sigma), Actual360())
process = BlackScholesProcess(QuoteHandle(u),
YieldTermStructureHandle(riskFreeCurve),
BlackVolTermStructureHandle(volatility))
engine = AnalyticEuropeanEngine(process)
option.setPricingEngine(engine)
print 'The option npv is'
print option.NPV()
print 'The option delta is'
print option.delta()
print 'The option gamma is'
print option.gamma()
print 'The option vega is'
print option.vega()
f, ax = plot.subplots()
xs = numpy.linspace(80.0, 120.0, 400)
ys = []
for x in xs:
    u.setValue(x)
    ys.append(option.NPV())
ax.set_title('Option value')
_ = ax.plot(xs, ys)