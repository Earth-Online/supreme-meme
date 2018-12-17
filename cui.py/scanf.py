from ctypes import *
msvcrt = cdll.msvcrt
num1 = c_int()
num2 = c_int()  
print("input a int number:")  
msvcrt.scanf(b"%d-%d",byref(num1),byref(num2))  
print(str(num1.value)+'\t'+str(num2.value))