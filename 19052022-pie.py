# -*- coding: utf-8 -*-
"""
Created on Thu May 19 17:52:08 2022

@author: APTECH
"""

"""
Pie chart

- Biến phân loại
- Khối lượng tương ứng

Mục đích: biểu diễn tỉ trọng của từng biến phân loại
"""

firms = ['Firm A', 'Frim B','Firm C', 'Frim D']
martket_share = [20,25,15,10]
explodes = [0,0.1,0,0]


'''Trực quan hoá dữ liệu với Pie chart
-> biểu thị tỉ trọng
'''

import matplotlib.pyplot as plt

plt.pie(martket_share, explode=explodes, labels=firms, shadow=True, startangle=30, autopct='%.2f%%')

plt.legend(title="Chú thích")
plt.axis("equal")
plt.show()

'''
'''

