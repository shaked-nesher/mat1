# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 14:59:31 2021

@author: shaked nesher
"""


def pow1(z, num):
    sumpow = 1
    for i in range(num):
        sumpow *= z
    return float(sumpow)

def factorial(num):
    sumfactorial = 1
    for i in range(1, num + 1):
        sumfactorial *= i
    return float(sumfactorial)

def exponent(x: float) -> float:
    sumexponent = 1
    for i in range(1, 101):
        sumexponent += pow1(x, i) / factorial(i)
    return float(sumexponent)

def abs (x):
    if x<0:
        return float(-x)
    else:
        return float(x)

def Ln(x: float) -> float:
    if x == 1 or x<=0:
        return float(0)
    yn = x-1.0
    yn1=0
    tmp=yn
    while (abs(yn-yn1)>0.001):
        yn=tmp
        yn1= yn + 2 * ((x - exponent(yn)) / (x + exponent(yn)))
        tmp=yn1
    return float(yn1)


def XtimesY(x: float, y: float) -> float:
 try:
    if x > 0:
        sumxtimey=exponent(y * Ln(x))
        sumxtimey=('%0.6f' % sumxtimey)
        return float(sumxtimey)
    else:
        return float(0)
 except:
       return float(0)
def sqrt(x:float,y:float) -> float:
 try:
    if y>0 and x!=0:
        sumsqrt=XtimesY(y,1/x)
        sumsqrt=('%0.6f' % sumsqrt)
        return float(sumsqrt)
    else:
        return float(0)
 except:
       return float(0) 
def calculate(x:float) -> float:
 try:
    final=exponent(x)*XtimesY(7,x)*XtimesY(x,-1)*sqrt(x,x)
    final=('%0.6f' % final)
    return float(final)
 except:
    return float(0)




