# -*- coding: utf-8 -*-
"""
Created on Tue May 17 18:48:13 2022

@author: APTECH
"""
'''
Trực quan hoá dữ liệu Mapplotlib
Đây là thư viện nền tảng để vẻ các biểu đồ 
Các biểu đồ cơ bản:
-- scatter
-- line
-- bar
-- pie
'''

#line
import matplotlib.pyplot as plt

thunhap = [1,2,3,10]
tieudung = [2,3,-4, 9]


##########LINE

#plt.figure(figsize=(15,5))
#plt.plot(thunhap, tieudung)
#plt.title("My chart")
#plt.xlabel('Thu nhap')
#plt.ylabel('Chi tieu')

#########Scatter
#plt.plot(thunhap, tieudung, 'ro')
#plt.title("Bieu do scatter")
#plt.xlabel("thu nhap")
#plt.ylabel("chi tieu")

#########
#tieudung2 = [x**3 for x in tieudung ]
#plt.plot(thunhap, tieudung, 'ro', thunhap, tieudung2, 'y^')

########Vẽ 2 biểu đồ trên 1 khung hình
tieudung2 = [x**2 for x in tieudung]

#plt.subplot(2,1,1)
#plt.plot(thunhap, tieudung, 'ro')

#plt.subplot(2,1,2)
#plt.plot(thunhap, tieudung2, 'go')

######Vẽ 
fig,ax = plt.subplots(nrows=2, ncols=2)

ax[0,1].plot(thunhap, tieudung, 'ro')
ax[0,1].set_title('thu nhap')

ax[1,0].plot(thunhap, tieudung2, 'go')
ax[1,0].set_title('thu nhap 2')

tieudung4 = [x**4 for x in tieudung]
ax[0,0].plot(thunhap, tieudung4, 'bo')
ax[1,1].plot(thunhap, tieudung4, 'y^')

plt.show()
