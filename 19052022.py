# -*- coding: utf-8 -*-
"""
Created on Thu May 19 17:52:08 2022

@author: APTECH
"""

"""
Bar chart

"""

product = ['ogranic', 'liquid', 'prevent', 'Ri-deliac', 'Yogout']
revence_hcm = [70,83,73,65,68]

'''Trực quan hoá dữ liệu với bar chart'''

import matplotlib.pyplot as plt

plt.bar(product, revence_hcm, color = "gray")
plt.title('Bieu do bar')
plt.xlabel('Phan loai san pham')
plt.ylabel('So luong')

plt.show()

'''
trục x -> phân loại
y -> khối lượng, số lượng
mục đích của biểu đồ bar là so sánh các biến phân loại
'''

