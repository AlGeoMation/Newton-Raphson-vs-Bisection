#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 14:57:50 2026

@author: anvar
"""

A=float(input("Enter the number to find cube root of: "))
x=30 #float(input("Enter the initial guess for Newton's method: "))
iterationN=0

epsilon=0.0001

#Newton's Method
while True:
    x_n=x-(x**3-A)/(3*x**2)
    iterationN += 1
    if abs(x_n-x)<epsilon:
        break
    x=x_n

B=A
iterationB=0

lowV=0.0
highV=max(1.0, B)
answer=(lowV+highV)/2

#Bisectio Method
while abs(answer**3-B)>=epsilon:
    iterationB += 1
    if answer**3<B:
        lowV=answer
    else:
        highV=answer
    answer=(lowV+highV)/2

print("Newtonian Method: ", iterationN)
print("Bisection Method: ", iterationB)
    