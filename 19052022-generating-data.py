"""
Phast sinh dữ liệu
Ứng dụng trong mô hình máy học
Numpy hỗ trợ phát sinh dữ liệu

"""

import numpy as np
import matplotlib.pyplot as plt

#arr = np.arange(1,100,3) #phát sinh 1 khoản có step được chỉ định 
#print(arr)

#arr2 = np.arange(10.)
#print(arr2)

#arr3 = np.arange(0.5, 10, 0.8)
#print(arr3)


#arr4 = np.linspace(1, 10,100)
#print(arr4)


"""
Cho hàm số y = 2x + 1
hãy vẽ đồ thị trong đoạn [2, 10]
"""
x = np.linspace(2,10,3)
y = 2*x*x + 1

plt.plot(x,y)
plt.show()
print(x)
print(y)