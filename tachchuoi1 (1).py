# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
s = (" Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp.HCM")
S1 = s.split(", ")
for i in S1:
    print(i)
S2 = s. replace("P.", "").replace("Q.", "").replace("Tp.", "").split(",")
for u in S2:
    print(u)
    
    
    