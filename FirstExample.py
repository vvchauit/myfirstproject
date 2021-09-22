def gia_tri_tuyet_doi(so):
#Hàm này trả về giá trị tuyệt đối
#của một số nhập vào"""
    if so >= 0:
        return so
    else:
     return -so
# Đầu ra: 5
print(gia_tri_tuyet_doi(5))
# Đầu ra: 8
print(gia_tri_tuyet_doi(-8))
# Đầu ra: Giá trị tuyệt đối của số nhập vào
num=int(input("Nhập số cần lấy giá trị tuyệt đối: "))
print (gia_tri_tuyet_doi(num))