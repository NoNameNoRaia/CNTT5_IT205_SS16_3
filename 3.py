patients = [
    ["BN001", "Nguyen Van A", "Nam", "Viem Phoi"],
    ["BN002", "Tran Thi B", "Nu", "Sot Xuat Huyet"]
]

def display_menu():
    print("\n===== HỆ THỐNG QUẢN LÝ BỆNH NHÂN RIKKEI =====")
    print("Hiển thị danh sách bệnh nhân")
    print("Tiếp nhận bệnh nhân mới")
    print("Cập nhật chẩn đoán bệnh theo mã BN")
    print("Tìm kiếm và thống kê theo tên bệnh")
    print("Thoát chương trình")

# *** Chức năng 1: Hiển thị danh sách bệnh nhân ***
def display_patients(patient_list):
    print("\n----- DANH SÁCH BỆNH NHÂN ĐANG ĐIỀU TRỊ -----")
    if len(patient_list) == 0:
        print("Hiện không có bệnh nhân nào đang điều trị.")
        return
    
    for index, item in enumerate(patient_list, start=1):
        print(f"{index}. Mã: {item[0]} | Tên: {item[1]} | Giới tính: {item[2]} | Bệnh: {item[3]}")

# Hàm phụ trợ kiểm tra giới tính (Xóa khoảng trắng, chuyển về chữ thường)
def validate_gender(gender_input):
    cleaned = gender_input.strip().lower()
    return cleaned == "nam" or cleaned == "nu"

# *** Chức năng 2: Tiếp nhận bệnh nhân mới ***
def add_patient(patient_list):
    print("\n----- TIẾP NHẬN BỆNH NHÂN MỚI -----")
    
    # 1. Nhập và bắt lỗi Mã bệnh nhân
    while True:
        new_id = input("Nhập mã bệnh nhân: ")
        # Bẫy dữ liệu rỗng (hoặc chỉ chứa dấu cách)
        if len(new_id.strip()) == 0:
            print("Mã bệnh nhân không được để trống!")
            continue
        
        # Chuẩn hóa: Xóa khoảng trắng 2 đầu và viết hoa toàn bộ
        new_id = new_id.strip().upper()
        
        # Kiểm tra trùng mã bằng hàm phụ trợ find_patient_index
        if find_patient_index(patient_list, new_id) != -1:
            print("Mã bệnh nhân đã tồn tại trong hệ thống, vui lòng kiểm tra lại!")
            continue
        break

    # 2. Nhập và bắt lỗi Tên bệnh nhân
    while True:
        new_name = input("Nhập tên bệnh nhân: ")
        if len(new_name.strip()) == 0:
            print("Tên bệnh nhân không được để trống!")
            continue
        # Chuẩn hóa: Title case (Viết hoa chữ cái đầu mỗi từ)
        new_name = new_name.strip().title()
        break

    # 3. Nhập và bắt lỗi Giới tính
    while True:
        new_sex = input("Nhập giới tính Nam/Nu: ")
        if not validate_gender(new_sex):
            print("Giới tính không hợp lệ, vui lòng nhập lại!")
            continue
        # Chuẩn hóa hiển thị đẹp mắt: "Nam" hoặc "Nu"
        new_sex = "Nam" if new_sex.strip().lower() == "nam" else "Nu"
        break

    # 4. Nhập và bắt lỗi Chẩn đoán bệnh
    while True:
        new_disease = input("Nhập chẩn đoán bệnh: ")
        if len(new_disease.strip()) == 0:
            print("Chẩn đoán bệnh không được để trống!")
            continue
        # Chuẩn hóa: Capitalize (Viết hoa chữ cái đầu tiên của câu)
        new_disease = new_disease.strip().capitalize()
        break

    # Thêm vào danh sách lớn
    patient_list.append([new_id, new_name, new_sex, new_disease])
    print("Tiếp nhận bệnh nhân thành công!")

# Hàm phụ trợ tìm index bệnh nhân theo ID
def find_patient_index(patient_list, patient_id):
    # Chuẩn hóa mã tìm kiếm trước khi so sánh
    target_id = patient_id.strip().upper()
    for index, item in enumerate(patient_list):
        if item[0].strip().upper() == target_id:
            return index
    return -1

# *** Chức năng 3: Cập nhật chẩn đoán bệnh theo mã BN ***
def update_diagnosis(patient_list):
    print("\n----- CẬP NHẬT CHẨN ĐOÁN BỆNH -----")
    
    id_update = input("Nhập mã bệnh nhân cần cập nhật: ")
    if len(id_update.strip()) == 0:
        print("Mã bệnh nhân không được để trống!")
        return

    index = find_patient_index(patient_list, id_update)
    
    if index != -1:
        # Lấy thông tin bệnh nhân tìm thấy tại vị trí `index`
        patient = patient_list[index]
        print(f"Tìm thấy bệnh nhân: {patient[1]}")
        print(f"Chẩn đoán hiện tại: {patient[3]}")
        
        while True:
            update_sitk = input("Nhập chẩn đoán mới: ")
            if len(update_sitk.strip()) == 0:
                print("Chẩn đoán bệnh không được để trống!")
                continue
            # Chuẩn hóa chuỗi mới (Viết hoa chữ cái đầu)
            update_sitk = update_sitk.strip().capitalize()
            break
        
        # Cập nhật vào phần tử index số 3 (chẩn đoán bệnh) của list con
        patient_list[index][3] = update_sitk
        print("Cập nhật chẩn đoán bệnh thành công!")
    else:
        # Chuẩn hóa mã in ra màn hình thông báo lỗi giống mẫu đề bài
        print(f"Không tìm thấy hồ sơ mang mã {id_update.strip().upper()}!")

# *** Chức năng 4: Tìm kiếm và thống kê theo tên bệnh ***
def search_by_disease(patient_list):
    print("\n----- TÌM KIẾM BỆNH NHÂN THEO TÊN BỆNH -----")
    keyword = input("Nhập từ khóa tên bệnh: ")
    
    if len(keyword.strip()) == 0:
        print("Từ khóa tìm kiếm không được để trống!")
        return
    
    cleaned_keyword = keyword.strip().lower()
    count = 0
    print("Kết quả tìm kiếm:")
    
    for item in patient_list:
        # So sánh không phân biệt hoa thường bằng cách dùng .lower() và toán tử `in`
        if cleaned_keyword in item[3].lower():
            count += 1
            print(f"{count}. Mã: {item[0]} | Tên: {item[1]} | Giới tính: {item[2]} | Bệnh: {item[3]}")
            
    if count == 0:
        print("Không tìm thấy bệnh nhân nào phù hợp.")
        
    print(f"\nCó tổng cộng {count} bệnh nhân mắc bệnh liên quan đến '{keyword}'.")

# --- VÒNG LẶP CHÍNH CỦA CHƯƠNG TRÌNH ---
while True:
    display_menu()
    choice = input("Nhập lựa chọn của bạn: ").strip()

    match choice:
        case "1":
            display_patients(patients)
        case "2":
            add_patient(patients)
        case "3":
            update_diagnosis(patients)
        case "4":
            search_by_disease(patients)
        case "5":
            print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
            break
        case _:
            print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 5.")