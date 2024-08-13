# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 18:42:50 2024

@author: Nguyenbichphuong
"""

a = float(input(" Nhap do dai canh a: "))
b = float(input(" Nhap do dai canh b: "))       
c = float(input(" Nhap do dai canh c: "))   
if a==b*b+c*c or b==a*a+c*c or c==a*a+b*b:
    print (" tam giac vuong ")
    #a=2 b=1 c=1
if a==b and b==c:
    print (" tam giac deu ")
if a==b or a==c or b==c:
    print (" tam giac can ")
    #a=4 b=4 c=5
if a*a> b*b+c*c or b*b> a*a+c*c or c*c> a*a+b*b:
    print (" tam giac tu ")
    #a=8 b=2 c=3
else:
    print (" tam giac nhon ")