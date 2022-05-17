# -*- coding: utf-8 -*-
"""
Created on Tue May 17 17:47:54 2022

@author: APTECH
"""

"""
List comprehension
=-> giups thao tac lay du lieu vaf tra ve ket qua la mot danh sach mot cach nhanh chong
"""
#myCharter = ['a', 'b', 'c', 'd']

#Tạo một list mới có tên myUpper chứa các ký tự chuỗi trong myCharter nhưng được viết hoa
#myUpper = [x.upper() for x in myCharter]
#print(myUpper)

myNum = [1,2,3,4,5,6,7,8,9,10]
#Hãy tạo danh sách myGereate5 là các số lớn hơn 5

#myGereate5 = [x for x in myNum if x > 5]
#print(myGereate5)

''"Hãy tạo ra danh sách mySquare là các số bình phương của các giá trị được lấy từ myNumber"

#mySquare = [x*x for x in myNum]
#print(mySquare)
'''
Hay tao danh sach myEvent la cac so chan trong myNum

'''

#myEvent = [x for x in myNum if x%2 == 0]
#mySquareEvent = [x*x for x in myNum if x%2 == 0]

#print(myEvent)
#print(mySquareEvent)

#def lapphuong(x):
    #return x**3
#print(lapphuong(4))

#khi can cai dat nhanh chong cac ham ko can ton thoi gian dinh nghia ham cu the ta co the su dung ham nac danh duoc goi la ngon ngu lambda
#ketqua = lambda x : x**3
#print(ketqua(10))

#ung dung cua lambda trong filter du lieu theo dieu kien

#myNumber = [10,9,23,32,3,1,2,3,4,5,6,7,8,43]
'''Hay lay ra danh sach cac so la so chan'''

#myEvent = list(filter(lambda x: (x%2 == 0) , myNumber))
#print(myEvent)

#my5 = list(filter(lambda x: (x%2 == 0 and x%5 == 0), myNumber))
#print(my5)

'''Chung ta lam lambda filter khi dieu kien loc la phuc tap, con dk loc don gian thi dung comprehension'''

'''tuong tu chung ta su dung map nhu filter'''

#hay tao ra mang danh sach lap phuong cac so trong myNumber
#mylapphuong = list(map(lambda x : x**3, myNum))
#print(mylapphuong)