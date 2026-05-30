# Phân tích: 
# Đẩu tiên chúng ta cần có 1 biến ngoài cùng là để người dùng nhập số chi nhánh 
# Từ đó ta tạo một vòng lặp for theo số lần bằng số chi nhánh 
# Trong mỗi chi nhánh thì ta tạo thêm 1 vòng lặp lặp 2 lần vì mỗi chi nhánh có 2 lớp
# Trong vòng lặp for đó thì ta tạo thêm 1 biến để người dùng nhập vào số học viên  
# Và ta sử dụng vòng lặp while để để nếu mà nhập học viên âm thì bắt nhập lại còn khi nào nhập đúng thì mới thoát ra khỏi vòng lặp 
# Sau khi check xong xuống dưới thì ta dùng câu điều kiện để in ra thông báo đúng với số lượng học viên trong nhóm đó 

quantity_branch = int(input("Nhập số chi nhánh: "))
for branch in range(1,quantity_branch+1):
    print(f"Chi nhánh {branch}:")
    for class_room in range(1,3):
        student_quantity = int(input(f"Nhập số học viên đi học của lớp {class_room}:"))
        while student_quantity < 0 :
            print("Số học viên không hợp lệ. Vui lòng nhập lại")
            student_quantity = int(input(f"Nhập số học viên đi học của lớp {class_room}:")) 
        if student_quantity == 0:
            print("Lớp vắng toàn bộ. Bỏ qua kiểm tra trạng thái")
            continue 
        elif student_quantity >= 20:
            print(f"Chi nhánh {branch} - Lớp {class_room}: Lớp học ổn định")
        elif student_quantity < 20:
            print(f"Chi nhánh {branch} - Lớp {class_room}: Lớp cần được nhắc nhở theo dõi")
