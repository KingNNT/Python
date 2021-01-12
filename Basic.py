#First Application
print("Đây là chương trình đầu tiên");

a = 37;
b = 10;
print(a/b);		#Chia
print(a//b); 	#lấy thương nguyên
print(a%b);		#Chia lấy dư
print(2**3);	#Lũy thừa
print();		#Xuống dòng


#Kiểu số Decimal
from decimal import *
getcontext().prec = 30;
print(a+b);
print(Decimal(10)/b)
print();

#Kiểu phân số Fraction
from fractions import *
frac_1 = Fraction(6,9);
frac_2 = Fraction(5,10);
print(frac_1 + frac_2);
print();

#Kiểu số phức
c = complex(2,5);
print(c);
print("Phần thực là: ",c.real);
print("Phần ảo là: ",c.imag);
print();