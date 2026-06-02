order_list = [
    "GE001 - PENDING",
    "GE002 - ASSIGNED",
    "GE003 - DELIVERING"
]

def display_menu():
    print('''
===== HỆ THỐNG ĐIỀU PHỐI GRAB EXPRESS =====
1. Hiển thị danh sách đơn hàng
2. Gán tài xế cho đơn hàng
3. Cập nhật trạng thái giao hàng
4. Hủy đơn hàng
5. Thoát chương trình''')

def find_order_index(input_code):
    cleaned_code = input_code.strip().upper()
    for i in range(len(order_list)):
        order_code = order_list[i].split("-")[0].strip()
        if order_code == cleaned_code:
            return i
    return -1

def main():
    while True:
        display_menu()
        choice = input("Nhập vào lựa chọn của bạn: ").strip()
        
        match choice:
            case "1":
                if len(order_list) == 0:
                    print("Danh sách đơn hàng hiện đang trống.")
                else:
                    print("\nDanh sách đơn hàng hiện tại:")
                    for i in range(len(order_list)):
                        print(f"{i+1}. {order_list[i]}")
                        
            case "2":
                input_code = input("Nhập mã đơn hàng cần gán tài xế: ")
                idx = find_order_index(input_code)
                
                if idx == -1:
                    print("Không tìm thấy mã đơn hàng.")
                else:
                    order_code, current_status = [part.strip() for part in order_list[idx].split("-")]
                    
                    if current_status == "PENDING":
                        order_list[idx] = f"{order_code} - ASSIGNED"
                        print(f"Gán tài xế thành công cho đơn hàng {order_code}.")
                    else:
                        print("Chỉ có thể gán tài xế cho đơn hàng đang chờ xử lý.")
                        
            case "3":
                input_code = input("Nhập mã đơn hàng cần cập nhật trạng thái: ")
                idx = find_order_index(input_code)
                
                if idx == -1:
                    print("Không tìm thấy mã đơn hàng.")
                else:
                    order_code, current_status = [part.strip() for part in order_list[idx].split("-")]
                    
                    match current_status:
                        case "PENDING":
                            print("Đơn hàng chưa được gán tài xế, không thể chuyển sang trạng thái giao hàng.")
                        case "ASSIGNED":
                            order_list[idx] = f"{order_code} - DELIVERING"
                            print(f"Đơn hàng {order_code} đã chuyển sang trạng thái: DELIVERING.")
                        case "DELIVERING":
                            order_list[idx] = f"{order_code} - COMPLETED"
                            print(f"Đơn hàng {order_code} đã chuyển sang trạng thái: COMPLETED.")
                        case "COMPLETED":
                            print("Đơn hàng đã hoàn tất, không thể cập nhật tiếp.")
                        case "CANCELLED":
                            print("Đơn hàng đã bị hủy, không thể cập nhật.")
                            
            case "4":
                input_code = input("Nhập mã đơn hàng cần hủy: ")
                idx = find_order_index(input_code)
                
                if idx == -1:
                    print("Không tìm thấy mã đơn hàng.")
                else:
                    order_code, current_status = [part.strip() for part in order_list[idx].split("-")]
                    
                    if current_status in ["PENDING", "ASSIGNED"]:
                        order_list[idx] = f"{order_code} - CANCELLED"
                        print(f"Đơn hàng {order_code} đã được hủy thành công.")
                    elif current_status == "DELIVERING":
                        print("Đơn hàng đang được giao, không thể hủy.")
                    elif current_status == "COMPLETED":
                        print("Đơn hàng đã hoàn tất, không thể hủy.")
                    elif current_status == "CANCELLED":
                        print("Đơn hàng đã được hủy trước đó.")
                        
            case "5":
                print("Thoát chương trình")
                break
                
            case _:
                print("Lựa chọn không hợp lệ, vui lòng nhập lại!")

if __name__ == "__main__":
    main()