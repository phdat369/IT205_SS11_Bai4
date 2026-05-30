# Phân tích
# Đề bài yêu cầu làm 1 menu gồm 5 chức năng, để làm được menu này thì chúng ta cần dùng vồng lặp while và kết thúc khi người dùng ấn 5
# Chức năng đầu tiên hiển thị danh sách sản phẩm thì chúng ta duyệt vòng lặp for và sau đó hiển thị theo định dạng của đề bài cho 
# Cần dùng thêm câu điều kiện để có thể ghi trạng thái cho từng đơn hàng
# Còn nếu mảng rỗng thì in ra là dánh sách sản phẩm rỗng 
# Chức năng thứ 2 là chức năng bán sản phẩm, đầu tiên là yêu cầu người dùng nhập mã sản phẩm và số lượng khách mua 
# Sau đó chuẩn hóa, kiểm tra số lượng sau khi check xong thì trừ số lượng hàng trong kho, tăng số lượng đã bán, tính tiền 
# Chức năng 3 là nhập kho, đầu tiên yêu cầu người dùng nhập mã sản phẩm cần thêm và nhập số lượng cần thêm 
# Sau đó chuẩn hóa, check xong có mã đơn hàng không , nếu hợp lệ thì thêm sản phẩm 
# Và chức năng cuối cùng là xem báo cáo doanh thu
# Chúng ta cần tính doanh thu của từng sản phẩm, doanh thu toàn cửa hàng, sản phẩm bán ra cao nhất, và sau đó in ra định dạng 
# Cần check thêm các Edge Cases và đề bài đã cho nữa

# Viết code

product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20,
        "sold": 5
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 3,
        "sold": 7
    }
]
while True:
    print("\n===== HỆ THỐNG VẬN HÀNH CỬA HÀNG YODY =====")
    print("1. Hiển thị danh sách sản phẩm và cảnh báo tồn kho")
    print("2. Bán sản phẩm cho khách hàng")
    print("3. Nhập thêm hàng vào kho")
    print("4. Xem báo cáo doanh thu")
    print("5. Thoát chương trình")
    choice = input("Nhập lựa chọn của bạn: ").strip()
    match choice:
        case "1":
            if len(product_list) == 0:
                print("Danh sách sản phẩm hiện đang trống.")
            else:
                print("\nDanh sách sản phẩm hiện tại:")
                for index, product in enumerate(product_list, start=1):
                    if product["quantity"] == 0:
                        status = "Hết hàng"
                    elif product["quantity"] <= 5:
                        status = "Sắp hết hàng"
                    else:
                        status = "Còn hàng"
                    print(
                        f"{index}. Mã SP: {product['product_id']} | "
                        f"Tên: {product['product_name']} | "
                        f"Giá: {product['price']} | "
                        f"Tồn kho: {product['quantity']} | "
                        f"Đã bán: {product['sold']} | "
                        f"Trạng thái: {status}"
                    )
        case "2":
            product_id = input(
                "Nhập mã sản phẩm khách muốn mua: "
            ).strip().upper()
            product_found = None
            for product in product_list:
                if product["product_id"] == product_id:
                    product_found = product
                    break
            if product_found is None:
                print("Không tìm thấy sản phẩm cần bán")
                continue
            quantity_buy = input(
                "Nhập số lượng khách mua: "
            ).strip()
            if not quantity_buy.isdigit() or int(quantity_buy) <= 0:
                print("Số lượng mua không hợp lệ")
                continue
            quantity_buy = int(quantity_buy)
            if quantity_buy > product_found["quantity"]:
                print("Số lượng trong kho không đủ để bán")
                continue
            product_found["quantity"] -= quantity_buy
            product_found["sold"] += quantity_buy
            total_money = quantity_buy * product_found["price"]
            print("Bán hàng thành công")
            print(f"Khách cần thanh toán: {total_money}")
        case "3":
            product_id = input(
                "Nhập mã sản phẩm cần nhập thêm: "
            ).strip().upper()
            product_found = None
            for product in product_list:
                if product["product_id"] == product_id:
                    product_found = product
                    break
            if product_found is None:
                print("Không tìm thấy sản phẩm cần nhập kho")
                continue
            quantity_import = input(
                "Nhập số lượng nhập thêm: "
            ).strip()
            if not quantity_import.isdigit() or int(quantity_import) <= 0:
                print("Số lượng nhập kho không hợp lệ")
                continue
            quantity_import = int(quantity_import)
            product_found["quantity"] += quantity_import
            print("Nhập kho thành công")
            print(f"Tồn kho mới: {product_found['quantity']}")
        case "4":
            total_revenue = 0
            max_sold = 0
            best_seller = ""
            print("\n===== BÁO CÁO DOANH THU CỬA HÀNG YODY =====")
            for index, product in enumerate(product_list, start=1):
                revenue = product["price"] * product["sold"]
                total_revenue += revenue
                print(
                    f"{index}. {product['product_name']} | "
                    f"Đã bán: {product['sold']} | "
                    f"Doanh thu: {revenue}"
                )
                if product["sold"] > max_sold:
                    max_sold = product["sold"]
                    best_seller = product["product_name"]
            if total_revenue == 0:
                print("Chưa có doanh thu phát sinh.")
            else:
                print(f"\nTổng doanh thu: {total_revenue}")
                print(f"Sản phẩm bán chạy nhất: {best_seller}")
        case "5":
            print("Thoát chương trình.")
            break
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")