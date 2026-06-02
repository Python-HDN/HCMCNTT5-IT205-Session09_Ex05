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
                    for i, item in enumerate(order_list):
                        print(f"{i+1}. {item}")
                        
            case "2":
                input_code = input("Nhập mã đơn hàng cần gán tài xế: ").strip().upper()
                
                # Chạy vòng lặp tìm kiếm trực tiếp trong case
                for idx, item in enumerate(order_list):
                    order_code = item.split("-")[0].strip()
                    if order_code == input_code:
                        order_code, current_status = [part.strip() for part in item.split("-")]
                        
                        if current_status == "PENDING":
                            order_list[idx] = f"{order_code} - ASSIGNED"
                            print(f"Gan tai xe thanh cong cho don hang {order_code}.")
                        else:
                            print("Loi: Chi co the gan tai xe cho don hang dang cho xu ly.")
                        break
                else:
                    print("Loi: Khong tim thay ma don hang.")
                        
            case "3":
                input_code = input("Nhập mã đơn hàng cần cập nhật trạng thái: ").strip().upper()
                
                # Chạy vòng lặp tìm kiếm trực tiếp trong case
                for idx, item in enumerate(order_list):
                    order_code = item.split("-")[0].strip()
                    if order_code == input_code:
                        order_code, current_status = [part.strip() for part in item.split("-")]
                        
                        match current_status:
                            case "PENDING":
                                print("Loi: Don hang chua duoc gan tai xe, khong the chuyen sang trang thai giao hang.")
                            case "ASSIGNED":
                                order_list[idx] = f"{order_code} - DELIVERING"
                                print(f"Don hang {order_code} da chuyen sang trang thai: DELIVERING.")
                            case "DELIVERING":
                                order_list[idx] = f"{order_code} - COMPLETED"
                                print(f"Don hang {order_code} da chuyen sang trang thai: COMPLETED.")
                            case "COMPLETED":
                                print("Loi: Don hang da hoan tat, khong the cap nhat tiep.")
                            case "CANCELLED":
                                print("Loi: Don hang da bi huy, khong the cap nhat.")
                        break
                else:
                    print("Loi: Khong tim thay ma don hang.")
                            
            case "4":
                input_code = input("Nhập mã đơn hàng cần hủy: ").strip().upper()
                
                # Chạy vòng lặp tìm kiếm trực tiếp trong case
                for idx, item in enumerate(order_list):
                    order_code = item.split("-")[0].strip()
                    if order_code == input_code:
                        order_code, current_status = [part.strip() for part in item.split("-")]
                        
                        if current_status in ["PENDING", "ASSIGNED"]:
                            order_list[idx] = f"{order_code} - CANCELLED"
                            print(f"Don hang {order_code} da duoc huy thanh cong.")
                        elif current_status == "DELIVERING":
                            print("Loi: Don hang dang duoc giao, khong the huy.")
                        elif current_status == "COMPLETED":
                            print("Loi: Don hang da hoan tat, khong the huy.")
                        elif current_status == "CANCELLED":
                            print("Loi: Don hang da duoc huy truoc do.")
                        break
                else:
                    print("Loi: Khong tim thay ma don hang.")
                        
            case "5":
                print("Thoat chuong trinh. Tam biet!")
                break
                
            case _:
                print("Loi: Lua chon khong hop le, vui long nhap lai!")

if __name__ == "__main__":
    main()