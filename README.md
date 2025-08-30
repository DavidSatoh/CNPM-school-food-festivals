
# CNPM-school-food-festivals

## Sơ đồ hệ thống

### 1. Context Diagram
![Context Diagram](diagrams/ContextDG.drawio.png)

### 2. ERD Diagram
![ERD Diagram](diagrams/Erd.drawio.png)

### 3. Use Case Diagram
![Use Case Diagram](diagrams/UseCase.drawio.png)

# I. Tổng quan dự án

## Mục tiêu

Xây dựng một **website/app** phục vụ công tác tổ chức **lễ hội ẩm thực học đường** tại trường, cho phép học sinh/nhóm học sinh đăng ký gian hàng & tham gia sự kiện, ban tổ chức quản lý – xét duyệt – phân công – theo dõi tiến độ, giáo viên/nhân viên hỗ trợ giám sát/đánh giá, và admin vận hành hệ thống. Hệ thống cũng hỗ trợ thu thập phản hồi, chấm điểm – xếp hạng gian hàng, báo cáo tổng hợp sau sự kiện.

## Phạm vi

Phạm vi bao gồm các chức năng chính:

* **Quản lý sự kiện** (tạo/sửa/xoá sự kiện, cấu hình thời gian – khu vực – tiêu chí chấm điểm, mini game/đổi thưởng nếu có).
* **Đăng ký tham gia** (đăng ký người tham gia, **đăng ký gian hàng** với mô tả món, nhu cầu dụng cụ/nguyên liệu, số lượng thành viên…).
* **Xét duyệt** (duyệt/ từ chối đăng ký, phản hồi yêu cầu bổ sung, phân công khu vực, theo dõi tiến độ chuẩn bị).
* **Quản lý gian hàng** (cập nhật thông tin, nhập nguyên liệu, theo dõi chi phí, ghi nhận doanh thu, tồn kho đơn giản).
* **Tương tác – truyền thông** (xem thông tin sự kiện, thông báo, lịch, bản đồ gian hàng, mini game/bình chọn công khai…).
* **Bình chọn – đánh giá – phản hồi** (bình chọn của học sinh/khách, phiếu chấm điểm của giáo viên/BTC, phản hồi hai chiều).
* **Báo cáo – xếp hạng** (bảng điểm, top gian hàng theo tiêu chí, lãi/lỗ, thống kê tham gia, nhật ký hoạt động).
* **Quản trị hệ thống** (quản lý tài khoản, phân quyền vai trò, cấu hình tiêu chí, danh mục dịch vụ/dụng cụ mặc định, sao lưu dữ liệu).

## Giả định và ràng buộc

* Hệ thống phục vụ **một trường** hoặc **sự kiện nội bộ** của trường; không nhằm thay thế ERP/CRM quy mô lớn.
* **Không tích hợp thanh toán online**; doanh thu/chi phí do nhóm tự ghi nhận (input thủ công).
* Xét duyệt, phân công và cập nhật tiến độ có thể được **thực hiện thủ công** bởi Ban tổ chức qua giao diện quản trị.
* Hệ thống ưu tiên **web-first**, hỗ trợ mobile responsive; ứng dụng di động là tuỳ chọn.
* Bảo mật ở mức **tài khoản – vai trò**; không xử lý dữ liệu nhạy cảm ngoài phạm vi sự kiện (KHÔNG lưu CMND/CCCD, số tài khoản…).
* Tối ưu cho **tải vừa** (hàng nghìn người dùng nội bộ/truy cập cùng lúc ở mức trung bình khi diễn ra sự kiện).

---

# II. Yêu cầu chức năng

## Các tác nhân (Actor)

Hệ thống có **5 tác nhân** chính:

1. **Guest** (khách/HS chưa đăng nhập) – xem thông tin sự kiện, gian hàng, tham gia bình chọn/mini game (nếu cho phép ẩn danh).
2. **Học sinh tham gia (Customer)** – cá nhân tham dự sự kiện, có thể bình chọn, đăng ký tham gia cá nhân, nhận thông báo.
3. **Nhóm học sinh (Stylist)** – đại diện gian hàng/nhóm thi: quản lý gian hàng, chi phí, doanh thu, tiến độ, phản hồi.
4. **Ban tổ chức trường (Manager)** – xét duyệt, phân công, theo dõi, quản lý sự kiện toàn cục.
5. **Giáo viên/Nhân viên** – giám sát, chấm điểm theo tiêu chí, phản hồi hiện trường.
6. **Admin** – quản trị hệ thống (tài khoản, vai trò, cấu hình, sao lưu).
   *(Ghi chú: Có thể gộp Admin vào Ban tổ chức nếu tổ chức nhỏ.)*

### Code PlantUML (actor diagram)

<details>
  
<summary>Code PlantUML</summary>

```plantuml
@startuml
actor Guest
actor "Học sinh tham gia" as Student
actor "Nhóm học sinh" as Team
actor "Giáo viên/Nhân viên" as Staff
actor "Ban tổ chức" as Org
actor Admin

' Kế thừa (nếu có quan hệ chung)
Guest <-- Student
Student <-- Team
Org <-- Admin

rectangle "Hệ thống lễ hội ẩm thực" as System {
}

Guest -- System : access
Student -- System : participate
Team -- System : manage booth
Staff -- System : evaluate
Org -- System : manage event
Admin -- System : system config
@enduml
```
</details> 

![Biểu đồ UML](https://www.plantuml.com/plantuml/png/PP0_JlD04CNxFSKepVTHHFI88j042GaAkC2msQnNyew3TpOI0agKYeA2WXAwG8NI9GM5J-ARC5d_aImgpyxxpPjvdWJ6agFF5MekIfX64xYjHsVrxbb3S9G1P-Z1EXm11hZYE3FKOnTPjV6GzN1YhWtw3fYwwhs0fQi-wL3W3shgrWldymuyHGAkTw-WnMsj4t1PsbO-cNb7Ils3ythx0op85y9_aaS4NMtWDiguT5So7iaUg1G6ZX_6u_xavjiqcnl5Fxqw-z9eHhAvIVbNQSyBMSZhtHD8_UQWtgvzwd_h9iDTOEFXNZsgTgVOjSqZGArD2DtcWRJ0afrs2sIZziSCH8-4ri1DKN2cqcyQo6Q9UPJ15E3ldEZxl2dKG0vDeGkQEwicXcRHvxy0)

## Các chức năng chính

### Guest

* **Tìm kiếm & xem thông tin sự kiện/gian hàng** (mô tả, thời gian, địa điểm, bản đồ gian hàng, nội quy, lịch).
* **Xem bảng xếp hạng/bình chọn công khai** (nếu sự kiện cho phép).
* **Tham gia mini game, bình chọn** (nếu cho phép không đăng nhập hoặc OTP/email xác thực nhanh).
* **Đăng ký/Đăng nhập** để tham gia sâu hơn.

### Học sinh tham gia (Customer)

* **Đăng ký tham gia cá nhân** sự kiện (nhận mã/QR, nhận thông báo).
* **Bình chọn** gian hàng, gửi **phản hồi** cho BTC.
* **Xem lịch sự kiện**, lịch biểu diễn/hoạt động, **nhận thông báo**.
* **Quản lý tài khoản** (cập nhật thông tin, đổi mật khẩu).

### Nhóm học sinh (Team)

* **Đăng ký gian hàng**: thông tin nhóm, món ăn, nhu cầu dụng cụ/nguyên liệu, công suất phục vụ.
* **Cập nhật tiến độ chuẩn bị**: checklist công việc, minh chứng.
* **Quản lý gian hàng**: mô tả, hình ảnh, menu/giá (nếu có), vị trí gian hàng.
* **Ghi nhận doanh thu – chi phí**; **xem lãi/lỗ** cơ bản.
* **Nhập nguyên liệu** & tồn kho đơn giản (tuỳ chọn).
* **Nhận phản hồi** từ BTC/GV, trả lời phản hồi.

### Giáo viên/Nhân viên

* **Xem thông tin sự kiện & phân công**.
* **Chấm điểm** gian hàng theo **bộ tiêu chí** (thang điểm, trọng số) – online/offline.
* **Ghi nhận vi phạm/biên bản** nếu cần.
* **Gửi phản hồi**/đề xuất hỗ trợ cho BTC.

### Ban tổ chức (Manager)

* **Tạo & cấu hình sự kiện**: thời gian, địa điểm, sơ đồ gian hàng, tiêu chí chấm điểm, cấu hình bình chọn/mini game.
* **Xét duyệt** đăng ký tham gia, đăng ký gian hàng; **phản hồi** yêu cầu bổ sung.
* **Phân công** khu vực, lịch trực, nhiệm vụ; **theo dõi tiến độ** các nhóm.
* **Quản lý danh sách** người tham gia; **gửi thông báo** đa kênh (email/app push/QR).
* **Quản lý bình chọn**: thời gian mở/đóng, phát hiện gian lận cơ bản (giới hạn tần suất/IP/OTP).
* **Báo cáo & Xếp hạng**: tổng hợp điểm BGK + bình chọn, bảng xếp hạng theo tiêu chí, export Excel/PDF.

### Admin

* **Quản lý tài khoản & vai trò** (Admin/BTC/Staff/Team/Student/Guest hạn chế).
* **Quản lý danh mục** (tiêu chí chấm điểm mặc định, danh mục dụng cụ/nguyên liệu tham khảo).
* **Cấu hình hệ thống** (logo, tên sự kiện, email server, sao lưu/khôi phục dữ liệu).
 
### Biểu đồ Use Case tổng quanquan

<details>
  
<summary>Code PlantUML</summary>

```plantuml
@startuml
@startuml
skinparam usecase {
  BackgroundColor BUSINESS
}

skinparam note {
  BackgroundColor LightSkyBlue
}

left to right direction

actor Guest
actor Student
actor Team
actor Staff
actor Org
actor Admin

Guest <|-- Student
Student <|-- Team
Org <|-- Admin

rectangle "Hệ thống lễ hội ẩm thực học đường" {

    together {
        rectangle "Chức năng Guest" as A {
            usecase "Xem thông tin sự kiện" as ViewEvent
            usecase "Xem danh sách gian hàng" as ViewBooths
            usecase "Xem thông tin nhóm" as ViewTeams
            usecase "Đăng nhập" as Login
            usecase "Đăng ký tài khoản" as Register
        }

        rectangle "Chức năng Học sinh tham gia" as B {
            usecase "Đăng ký tham gia" as StudentRegister
            usecase "Xem lịch sự kiện" as ViewSchedule
            usecase "Bình chọn gian hàng" as VoteBooth
            usecase "Quản lý thông tin cá nhân" as ManageProfile
        }
    }

    rectangle "Chức năng Nhóm học sinh" as C {
        usecase "Đăng ký gian hàng" as RegisterBooth
        usecase "Quản lý gian hàng" as ManageBooth
        usecase "Theo dõi phản hồi & đánh giá" as ViewFeedback
        usecase "Xem kết quả xếp hạng" as ViewRanking
    }

    rectangle "Chức năng Giáo viên/Nhân viên" as D {
        usecase "Đánh giá gian hàng" as EvaluateBooth
        usecase "Góp ý cho gian hàng" as GiveFeedback
        usecase "Xem báo cáo tổng hợp" as ViewReports
    }

    rectangle "Chức năng Ban tổ chức" as E {
        usecase "Duyệt đơn đăng ký" as ApproveRequests
        usecase "Quản lý gian hàng" as OrgManageBooths
        usecase "Quản lý sự kiện" as ManageEvent
        usecase "Tổng hợp kết quả & xếp hạng" as SummaryResults
    }

    rectangle "Chức năng Admin" as F {
        usecase "Cấu hình hệ thống" as SystemConfig
        usecase "Quản lý tài khoản" as ManageAccounts
        usecase "Phân quyền" as ManageRoles
    }

    ' Giữ khoảng cách giữa các khối
    A -[hidden]- C
    C -[hidden]- D
    D -[hidden]- E
    E -[hidden]- F
}

' Mapping Actor với Use Case
Guest -- ViewEvent
Guest -- ViewBooths
Guest -- ViewTeams
Guest -- Login
Guest -- Register

Student -- StudentRegister
Student -- ViewSchedule
Student -- VoteBooth
Student -- ManageProfile

Team -- RegisterBooth
Team -- ManageBooth
Team -- ViewFeedback
Team -- ViewRanking

Staff -- EvaluateBooth
Staff -- GiveFeedback
Staff -- ViewReports

Org -- ApproveRequests
Org -- OrgManageBooths
Org -- ManageEvent
Org -- SummaryResults

Admin -- SystemConfig
Admin -- ManageAccounts
Admin -- ManageRoles
@enduml
@enduml
```
</details> 

![Biểu đồ UML](https://www.plantuml.com/plantuml/png/bLR1Zjn44BtxAqfxI4uZVe13TcPd9qXX2JC9Ga8SEkqUTyjsjzTk3wmW1uGG1uH4X3WWX9GXuX040XIup0Xny8h_y9_GNPvjQXtFCfd3RlkvNtNLg-egtwaiAssTPr6LAbsmakLGLuApIi174S2OyJGfJQtZYSbC2UE7YpVEfej5z3WY36tiyFPxAf5saLwCirfuIYQM5go1qkCGgr9mguoE8iQjspwhHMLtwuMjOw6ldXu8beSNRBdShTygaztgECwLiuCMuFMFHwDWeFk_0z6EO-7J5SbxmNII2JYwssu_1olRxHETGDPkFmEt_bP1ktcU8_uxzyYN72wV_FDRk_rU9qSkyWZSpvf4M2bALABx4SiJHtlEGLz-gfCkq2DW5Ho7tVWBuX-zA_o1pHzkjrKQAdSqfCgvfv7tZX8VJ5T2s_tic6a9LRFc4XB5DCZcgKu2UMoCbTL1PslPlCW3qKkuXtVv5KQdPRlvfK32FPCeVUFcjFaBRFDKGIfDktdMHJSNYQgiA0FpSVI_cjx5j5HAIx2IvJvcj3NUfp1rW19s1KDz69R8rSSNN0wcPi6bYEjC39F7pSzQ0lU5f5_AZR42SpDCVRls8a66JeSCyMRji_H3vy2RJBD4t2_DKcM2I1Y4t2_YcKyro20bsfi41GVLen7GvD4eXYEWnE3t7je3AGp4pPyA2ea6d9DVAxZbBcAprhx4ctMG_rI8-17ZQJIOjxJT_6tXtFi17xfr0SxYcjoDETEfqiaXWitSiGPMglb9ltRcCz2jqTJ9i6x1tNxyqnNBQcRtAJ1hNXJWLEFIz9apjH8tn_p8kydz7zjklz69b-zPyL_4eZ2bhGw9UCmqsW2EQEVvKAGdzOMx4zPtohLsVw_gfUjxHL6QbPYBSzyAgrSf4zU-IQNSJEtVpOv86oSjCQBCjIAvzNAPBEeyP-N5N5HrTfXkE6oGUpgargJT_5Y3nCuWoHJgJhkehCWdHYzLScEyj9EIW8yvDxKUala-rkovJzKdb34tcRWMrcsOEHb_lJAU0EycYmSPFa3gFLQu-nX6xqaLnqA_Fu89GXCAdI1qGg4fGbCAdKRkyDlEew9GNa6SzAjs-vs2XyxvYOjWD_578p8H2HJc7CLmX16e6rBXCJJ-yEdWmFvG8AzelwTuwEG4xFNco7j2pyJz0ILb7Z3QtYWOcbQ47qWExVMJ05zh5W6bNG2_a1pMlwGTtBk00QPtguFwjoJ2Eu0lQ447j5Ui50ybUKVekCwpVm40)

### Biểu đồ Use Case chi tiết
#Chức năng Guest
<details>
  
<summary>Code PlantUML</summary>

```plantuml
@startuml
actor Guest

rectangle "Chức năng Guest" {
  usecase "Xem thông tin dịch vụ" as UC1
  usecase "Xem thông tin gian hàng" as UC2
  usecase "Xem thông tin lễ hội" as UC3
  usecase "Tìm kiếm" as UC4
  usecase "Đăng nhập" as UC5
  usecase "Đăng ký" as UC6
}

Guest -- UC1
Guest -- UC2
Guest -- UC3
Guest -- UC4
Guest -- UC5
Guest -- UC6
@enduml
```
</details> 

![Biểu đồ UML](https://www.plantuml.com/plantuml/png/VP2XJiKm58RzUOgJ-IkuTvjUCi4BG89jkgPjjXx8sc48Yg0mM1m6GG8EjOOWkXVfcx2CYWeo-UNxpFytrh7HJMO0njtrYEUJi0vW5DmnaeF0ebNHltEavO7adoxm3X0dApYpQt0b33eLlbRjD64N_HDNU1lzMu7CucLxjbDBpGXLU2MPukDEF4J_Y2hw5vtYKnvVX0-3lOxpZqcwpFNol2qW5UVFcnHK_mHz-4wsXdk0RJ4U3jkE38uvd78eSwXogA4HrArd_m80)
#Chức năng Student

<details>
  
<summary>Code PlantUML</summary>

```plantuml
@startuml
actor "Học sinh tham gia" as Student

rectangle "Chức năng Student" {
  usecase "Tham gia lễ hội" as UC1
  usecase "Xem lịch trình" as UC2
  usecase "Đặt suất tham gia" as UC3
}

Student -- UC1
Student -- UC2
Student -- UC3
@enduml
```
</details> 

![Biểu đồ UML](https://www.plantuml.com/plantuml/png/LSyn2i8m60NWFQTuPEzWlK2XYxiAhY4DJQ6DaFoPn4cSH73r00w2kz2EzYAvYR5KQCS77-z_V-P8MF9DpOIalGLVXUuguIgZGLeqA2l18HpMv0jbY36h90bJrWeyrw5xIfZ-PCe_u3Wmm3ibXOjaCtQW3jqPqT-heMwRBwPifvgVk4WDif-NqIDAfwY_XVPDS3wq3vgjYtB9ZeoD6v0amu5PJ6Sn-aoP8Zx-1G00)

#Chức năng Student

<details>
  
<summary>Code PlantUML</summary>

```plantuml
@startuml
actor "Nhóm học sinh" as Team

rectangle "Chức năng Team" {
  usecase "Quản lý gian hàng" as UC1
  usecase "Quản lý chi phí" as UC2
  usecase "Quản lý doanh thu" as UC3
  usecase "Xem phản hồi khách" as UC4
}

Team -- UC1
Team -- UC2
Team -- UC3
Team -- UC4
@enduml
```
</details> 

![Biểu đồ UML](https://www.plantuml.com/plantuml/png/TSunIWGn60NW_Z_5O_ejtDq3B6ml20gsFzcGFvZyAvEa4YjhAo-WM5bOsIbMyI9x4sCOS9hf7hoFnzkbp6CkCH2RV1mnd4lzY93JrwD1yYe3EE7ISYGQhSciBbWC-mRU3FJdGLrl1zmHK98rd5f_KKwVhufGl-4yAwG-g-jJL_kp1MZ4urRg-yJM2-nmP1LaAPFRpDsrZMsZs_RmoUD6wekHYMxfdkZlBLQhVkG_hsTvCyjRsbazb1X-0G00)

#Chức năng Staff



<details>
  
<summary>Code PlantUML</summary>

```plantuml
@startuml
actor "Giáo viên/Nhân viên" as Staff

rectangle "Chức năng Staff" {
  usecase "Giám sát gian hàng" as UC1
  usecase "Đánh giá theo tiêu chí" as UC2
  usecase "Chấm điểm" as UC3
  usecase "Phản hồi ban tổ chức" as UC4
}

Staff -- UC1
Staff -- UC2
Staff -- UC3
Staff -- UC4
@enduml
```
</details> 

![Biểu đồ UML](https://www.plantuml.com/plantuml/png/JP0nIWGn58RxTugVwHTnTm-mi8MT2E81OimcWPqtC7bZ8rPx0KNi7SL2mGiuPUOYSvCDcIdIvISV___nTa5KArrz9AMbQL5T-TWtUFJnbo-kNVpa-Lr11ToAEXo8MgD5iJqQL7it3JyQF9xOpjyLdWZeWj4gcBckHeYzm7h5SF63RIwxsr-MuFWIUtQmYOSuqq3IR0Vjuj-2hqiy3Vz_rnXV_JISweNObCHD8huOIV3DupvDopIyGsVXXT_ICr6sncgLXOgmBiEc35lQ6Nv8Dpi3)

#Chức năng Org


<details>
  
<summary>Code PlantUML</summary>

```plantuml
@startuml
actor "Ban tổ chức" as Org

rectangle "Chức năng Ban tổ chức" {
  usecase "Xét duyệt gian hàng" as UC1
  usecase "Phân công gian hàng" as UC2
  usecase "Theo dõi sự kiện" as UC3
  usecase "Xử lý sự cố" as UC4
}

Org -- UC1
Org -- UC2
Org -- UC3
Org -- UC4
@enduml
```
</details> 

![Biểu đồ UML](https://www.plantuml.com/plantuml/png/PT2nIiOm50NW_Jx5eVi_-BSFKEm3wA3W6jAG5Eij9EaWukJWxE0kRXqS19s2KtoHl8cX5blfTY1VJd9lxRomVhpfIKW_M1IdWk5JU8OqAKooW70uivh8Aka5wrwXQEOZyFS3Q-mkt14mEYM5o_GgJXxjU9l2euVkiZNnXVLSUzcSREcvYQyC6JzOx-LnAo-C6j36pmukXNTSTxcT5rZ-Ups5D_JnwzV959uMLT4zKHuBXyFyZRzuN6EvnefgnMtUqWy0)

#Chức năng Admin

<details>
  
<summary>Code PlantUML</summary>

```plantuml
@startuml
actor Admin

rectangle "Chức năng Admin" {
  usecase "Quản lý tài khoản" as UC1
  usecase "Phân quyền & vai trò" as UC2
  usecase "Cấu hình hệ thống" as UC3
  usecase "Sao lưu & khôi phục" as UC4
}

Admin -- UC1
Admin -- UC2
Admin -- UC3
Admin -- UC4
@enduml
```
</details> 

![Biểu đồ UML](https://www.plantuml.com/plantuml/png/JT0_IWD150Rm_ftYOujqAKnoWCXUG14FC4o6dI6Jjpf_114BiR3s1gAa42n4hB9OZNYFkOcpkiKq3xxtViN7M_iWN8WxIqA6tk5uipDCv9GCWZkhqBGw3wyI_7tFtV-vmGq1qIifV06dCHzU63Pz8QGdWwtknqK3uN7U7jNqHATdncMypiCTOuOhOH1S-fZiehPjFkmZT7fZZLBX0Q7CH-uckwpjcUXXVzuZPjZgz6bmKUnUJdH5jqH_pJ6VZvNgiAZ3iWuhMYlUZA_v1G00)

