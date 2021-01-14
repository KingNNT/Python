#String
#Chuỗi trần
print(r"C://Developer");

strA = "Ninh Ngọc";
strB = "Tuấn";
print(strA + strB);

strC = "KingNNT\n"
print(strC * 5);

#"in" : Check xem chuỗi này có tồn tại trong chuỗi kia hay không
strA = "KingNNT"
strB = "NNT"
strC = strB in strA
print(strC)
print(strA[0])
print(strA[-4])
print("Độ dài chuỗi: ",len(strA))
print("Lấy vị trí 1 dến 5 (Không tính thứ 5): ", strA[1:5])
print(strA[1:None])
print(strA[None:4:2]) #2 là bước nhảy

#HASH
strA = "HowKteam"
strA = strA[None:1] + "0" + strA[2:None];
print(strA);
print()
#Ép Kiểu
strA = "69"
strB = int(strA)
print(strB)

intA = 69
intB = str(intA)
print(intB)
print()


