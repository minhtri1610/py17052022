# -*- coding: utf-8 -*-
"""
Created on Thu May 19 17:52:08 2022

@author: APTECH
"""
"""
Numpy-> thư viện hỗ trợ xứ lý toán học như tính toán, ma trận, được dùng trong phân tích và máy học

Các ký thuật cơ bản
1. tạo ma trận
2. indexing
3. slicing
4. reshape
5. mathematic function
"""
import numpy as np


'''
Array chứa danh sách các phần tử đồng nhất
List chứa danh sách các phần tử khác kiểu dữ liệu
'''
#tmpArr = np.array([1,2,34])
#print(type(tmpArr))

"""
Ma trận là khối dữ liệu có chiều

Với ma trận ta lưu ý:
1.dim là số chiều của ma trận
2.Shape Kích cỡ của ma trận -> kết quả của hàm shape là 1 tuple

"""

#matrix2d = np.array([[1,2,5],[3,4,6]])
#print(matrix2d.shape)
#print(matrix2d.ndim)

#matrix3x4d = np.array([[1,2,3,5],[1,2,3,5],[1,2,3,5]])

#print(matrix3x4d)
#print(matrix3x4d.shape)
#print(matrix3x4d.ndim)

"""\
    Numpy hỗ trợ reshape ma trận
    """
 
#matrix2d2x3 = np.array([[1,12,2], [1,2,3]])

#print(matrix2d2x3.shape)
#print(matrix2d2x3.ndim)

#matrix2d2x3.shape = (3,2)
#print(matrix2d2x3)
      
'''

Kỹ thuật slicing và index trên ma trận      
      '''
      # Nếu ma trận 1 chiều hay còn gọi là mảng thì  kỹ thuật slicing và indexcing gióng như trên list

"""
indexing và slicing trên ma trận 2D
"""

#matrix2d = np.array([[1,2,3],[3,4,5],[4,5,6]])
#print(matrix2d.ndim)
#print(matrix2d.shape)

#slicing 
#print(matrix2d[1:]) # #lấy bắt đầu từ dòng có chỉ số từ 1

#print(matrix2d[...,1]) # lấy tất cả các dòng có chỉ số là 1

#print(matrix2d[1,...]) # lấy tất cả các cột từ dòng 1

#print(matrix2d[..., 1:]) # láy tất cả các dòng bắt đầu từ dòng 1

#print(matrix2d[1:,1:])

#print(matrix2d[1:,[0,2]])

matrix = np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])

'''
4,5
7,8
10,11

3,5
6,8
'''

print(matrix[1:,1:])
print(matrix[1:3,[0,2]])                   
        




























