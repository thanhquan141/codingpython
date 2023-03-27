# Tạo khung form để người dùng nhập thông tin cá nhân và sở thích ăn uống
name = input("Nhập tên của bạn: ")
age = int(input("Nhập tuổi của bạn: "))
height = float(input("Nhập chiều cao của bạn (mét): "))
weight = float(input("Nhập cân nặng của bạn (kg): "))
eating_habit = input("Nhập sở thích ăn uống của bạn (ít chất béo, trung bình, nhiều chất béo): ")

# Tính chỉ số BMI
bmi = weight / (height ** 2)

# In ra chỉ số BMI và phân loại BMI tương ứng
print("Chỉ số BMI của bạn là: {:.2f}".format(bmi))

if bmi < 18.5:
    print("Bạn đang gầy.")
elif bmi < 25:
    print("Bạn có cân nặng bình thường.")
elif bmi < 30:
    print("Bạn đang bị thừa cân.")
else:
    print("Bạn đang bị béo phì.")

# Suy ra chế độ ăn phù hợp để cân bằng cơ thể
if eating_habit == "ít chất béo":
    if bmi < 18.5:
        print("Bạn cần tăng cân bằng cách ăn thêm thực phẩm giàu chất béo như hạt, dầu ô liu, quả bơ, cá hồi, thịt gà.")
    elif bmi < 25:
        print("Bạn có thể duy trì chế độ ăn như hiện tại để giữ cân nặng ổn định.")
    else:
        print("Bạn cần giảm cân bằng cách ăn ít chất béo hơn và tập luyện thể thao thường xuyên.")
elif eating_habit == "trung bình":
    if bmi < 18.5:
        print("Bạn cần tăng cân bằng cách ăn thêm thực phẩm giàu chất béo như hạt, dầu ô liu, quả bơ, cá hồi, thịt gà.")
    elif bmi < 25:
        print("Bạn có thể duy trì chế độ ăn như hiện tại để giữ cân nặng ổn định.")
    else:
        print("Bạn cần giảm cân bằng cách ăn ít chất béo hơn và tập luyện thể thao thường xuyên.")
else:
    if bmi < 18.5:
        print("Bạn cần tăng cân bằng cách ăn thêm thực phẩm giàu chất béo như hạt, dầu ô liu, quả bơ, cá hồi, thịt gà.")
    elif bmi < 25:
        print("Bạn có thể duy trì chế độ ăn như hiện tại để giữ cân nặng ổn định.")
    else:
        print("Bạn cần giảm cân bằng cách ăn ít chất béo hơn và tập luyện thể thao thường xuyên.")