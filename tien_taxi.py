# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 19:06:23 2024

@author: tinhtientaxi
"""

s = float(input (" Nhap quang dương di duoc (km): "))
tong_tien =0
if s<=1:
  print(" so tien phai tra là 20k ")
elif 1<s<4:
  print( " so tien phai tra la", (s*13),"k")
elif 4<=s<=8:
    print( " so tien phai tra la", (3*13+(s-3)*12), "k")
elif s>8:
    print( " so tien phai tra la", (3*13+5*12+(s-8)*10), "k")
else:
    print( " so tien phai tra la", (3*13+5*12+(s-8)*10)*0.92, "k")
    
