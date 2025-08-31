
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
@startuml "Biểu đồ Use Case chức năng Guest"

skinparam usecase {
    BackgroundColor BUSINESS
}

skinparam note {
    BackgroundColor LightSkyBlue
}

left to right direction

actor Guest

rectangle "Hệ thống" {
    usecase "Xem thông tin dịch vụ" as ViewService
    usecase "Xem thông tin gian hàng" as ViewBooth
    usecase "Xem thông tin lễ hội" as ViewFestival
    usecase "Tìm kiếm" as Search
    usecase "Đăng nhập" as Login
    usecase "Đăng ký" as Register
}

Guest -- ViewService
Guest -- ViewBooth
Guest -- ViewFestival
Guest -- Search
Guest -- Login
Guest -- Register

@enduml
```
</details> 

![Biểu đồ UML](https://www.plantuml.com/plantuml/png/VP0zJlGm48PxdsAKVk-mogUF7sb5GG3HMibWMt76Atko224gX2XeeAIZeOEEQYD4aRs8Ru8ILXQBO4i_UX_FEpCDB3stZHMXDZINNZRG1YnbGBWK002vB6lbNKlLFsUTX_ous3_uNnJYIdnpoF5VmimepKLzaTiM1ydY6GCxy0E7odWisJWIGfRiFEos65Y8WKfI5Y7RYzqji8xT0wdiQqZgc9rY0wpxDrB0Xg2AtLsfOH6xvmnaW1E3vmNwXIbngwUC9D3z4wcavSwntYhPsDs0ZjsZIT8E1ZOBQJUze_wbWTh4vKSp9WkKllpnz-f-TKqAICVbwtnCpPmoz6kexj_7n24g4nZzSDRnRZ2PRAoSO5eeeOswYQwhfVUwH7gcYLEagcti9m00)

#Chức năng Student
<details>
  
<summary>Code PlantUML</summary>

```plantuml
@startuml "Biểu đồ Use Case chức năng Student"

skinparam usecase {
    BackgroundColor BUSINESS
}

skinparam note {
    BackgroundColor LightSkyBlue
}

left to right direction

actor "Học sinh tham gia" as Student

rectangle "Hệ thống" {
    usecase "Tham gia lễ hội" as JoinFestival
    usecase "Xem lịch trình" as ViewSchedule
    usecase "Đặt suất tham gia" as BookSlot
}

Student -- JoinFestival
Student -- ViewSchedule
Student -- BookSlot

@enduml
```
</details> 

![Biểu đồ UML](https://www.plantuml.com/plantuml/png/TO-nIlOm58RtNCMX-tSF7_tvHKLSek8QqcCRcfuZoOaYuYWE8kZe1RYv2rz7lP7UYMcfr0vcF3pF-xxPHZ51KkTLR1rTcc0wI16jYGYt2l8hZMthm8cgV-mvG7cg3ux_Qwtkr2-7MFuIZbpTY6vlIfzmb3nU20X36EzGkO1M79DInah6Y_sXVx8G7JKWJOwkdId0HD2IAYHHQXGCrHudzY5JG_z2TJ7t_ymlJcOR_D3VGuPUtHHqo8xsC8gxCdvjd6CtmeysLuVFTsec_ipXjRODLidZclzw7dOV0Z4DkpTPhosPM-rPnX_Fos6pMNSlztN7SbzYjaXLwlmt)

#Chức năng Team học sinh
<details>
  
<summary>Code PlantUML</summary>

```plantuml
@startuml "Biểu đồ Use Case chức năng Team"

skinparam usecase {
    BackgroundColor BUSINESS
}

skinparam note {
    BackgroundColor LightSkyBlue
}

left to right direction

actor "Nhóm học sinh" as Team

rectangle "Hệ thống" {
    usecase "Quản lý gian hàng" as ManageBooth
    usecase "Quản lý chi phí" as ManageCost
    usecase "Quản lý doanh thu" as ManageRevenue
    usecase "Xem phản hồi khách" as ViewFeedback
}

Team -- ManageBooth
Team -- ManageCost
Team -- ManageRevenue
Team -- ViewFeedback

@enduml
```
</details> 

![Biểu đồ UML](https://www.plantuml.com/plantuml/png/TP2nJiCm48PtFyKfUz-XIWK22If1A68zdCEsafohn0OXnDI1YQ7g2u2O69ZOY9ZI5ycRO4TKQePwyF3h_-u-Uzeuh9slIaXIqxSh3zjrtsvWqH3CC5nIz-sd1DwkMC4LOPK8qHI6brXZ1RuX6LjF0i99KHQgjfxpcIrj3UaYEvqVPPbutcVOkaF0cL7QPSLZMdgAK4bt3fo5EkQGcvgaCvQ5GEb2FPdhxhk2OFWgeJ6i4y1ca1GYLf5LIP2SzEqBkD1Qiqh-D-_4amlV_tmmbDqlA8CCkdjZDSmvHqP5gRLE7qIaDh3KtTSUCBEDEzZFBR8EBduFkAHxOazZveQgC7ZWWlZ6GA6xTwa7xDhGmp5HVekoYByK7moJoKXud4MdSRJRkal7GyMKEFTLAVu0)

#Chức năng Staff
<details>
  
<summary>Code PlantUML</summary>

```plantuml
@startuml "Biểu đồ Use Case chức năng Staff"

skinparam usecase {
    BackgroundColor BUSINESS
}

skinparam note {
    BackgroundColor LightSkyBlue
}

left to right direction

actor "Giáo viên/Nhân viên" as Staff

rectangle "Hệ thống" {
    usecase "Giám sát gian hàng" as MonitorBooth
    usecase "Đánh giá theo tiêu chí" as EvaluateCriteria
    usecase "Chấm điểm" as Score
    usecase "Phản hồi ban tổ chức" as FeedbackOrg
}

Staff -- MonitorBooth
Staff -- EvaluateCriteria
Staff -- Score
Staff -- FeedbackOrg

@enduml
```
</details> 

![Biểu đồ UML](https://www.plantuml.com/plantuml/png/TP7FIiD04CRl-nH3xiLNA0dr3sWLGXzWcsmtIvDPsSmMH3pruDKYtgtYGS4NCCVqHV8cJX891Z67aEpExvjllfcM91tv8eSWD4srzN3ODTKZB4e5aUHNaZNLUm9usAA6cEHg5GXHhWrUIoSByALAsh9R0Vo4CbbhPpscaSsjWt0HdyrdSIpkVZDewJ_WtEYCulLDc7lLGhbQ4P05rvv3QfnAo5WKGYR4vS69gVSMDgR-mADvLhzW_ns0B7kpGhI8H9qh24wRwXw81zgX3de7mm2TL05blIVGHY9azJFgJkZ2ek5keRMKZPd3Gxt733IZhAii47Vtd5dzsP6pZSoz91KvGyePEQQZhFbwApZmDlYYzvnOfyPLLrprodPuAmQM4e6QwkbdBHrph5Iwv1mldMuZwyQ6oMHaUpZzQscuwNeFloDPCLMO-Y8Ntm00)

#Chức năng Org
<details>
  
<summary>Code PlantUML</summary>

```plantuml
@startuml "Biểu đồ Use Case chức năng Ban tổ chức"

skinparam usecase {
    BackgroundColor BUSINESS
}

skinparam note {
    BackgroundColor LightSkyBlue
}

left to right direction

actor "Ban tổ chức" as Org

rectangle "Hệ thống" {
    usecase "Xét duyệt gian hàng" as ApproveBooth
    usecase "Phân công gian hàng" as AssignBooth
    usecase "Theo dõi sự kiện" as MonitorEvent
    usecase "Xử lý sự cố" as HandleIssue
}

Org -- ApproveBooth
Org -- AssignBooth
Org -- MonitorEvent
Org -- HandleIssue

@enduml
```
</details> 

![Biểu đồ UML](https://www.plantuml.com/plantuml/png/TP2zQiCm58LtFSN5UzuXTGWaq9-26-WgP5KMLgw2VWAXTChGEPJkfLk63eLs4fsS5z6RL4vSYDDsyN1yldlEqT0wQfoVAyXo6SFQmsuJmnFCB8SHJHzMnR1bWBir2iWfWelXkLCpGcmjSK4DdOEtdBN0FG60v6IrCDfZET9A6yXdnVHoN1JauPX1xVu3pgMeN56lSkLv2ob-vy1fCAqEfJISEQcH4CfSicUdrO1Qk3A2aDP8KIWEsII6Ht3f_mP5rkN-rCvkcsswwrV9uq18Yb0rBoZsXyuM2wENFDVQLNtgkcfU4LZpWU8NPAqK-0TpKt4DPVCfmSRm3hLCaRX7BZJAj6QyvEXEsiNm1ghvEY0iJTW34ugbubDh3u-K1iDWqAlRQRqsdNISrcczWsJ8iVHpHRu1)

#Chức năng Admin
<details>
  
<summary>Code PlantUML</summary>

```plantuml
@startuml
skinparam usecase {
    BackgroundColor BUSINESS
}

skinparam note {
    BackgroundColor LightSkyBlue
}

left to right direction

actor Admin

rectangle "Hệ thống" {
    usecase "Quản lý tài khoản" as ManageAccount
    usecase "Phân quyền & vai trò" as ManageRoles
    usecase "Cấu hình hệ thống" as ConfigSystem
    usecase "Sao lưu & khôi phục" as BackupRestore
}

Admin -- ManageAccount
Admin -- ManageRoles
Admin -- ConfigSystem
Admin -- BackupRestore
@enduml
```
</details> 

![Biểu đồ UML](https://www.plantuml.com/plantuml/png/TP0zIWGn583xESLZYkts3lk3eA2YEtY0aCbEmcJUMvCNOH4BAsjl8Cfs5Y9MkrW5lCVSn9aHXarXkdpmvNrvCy_2SMXivck36-540y4hARo2-mowin2ohXm5B9TaoS7YfZYxF2cAx24xSf3uF-7SL9gBUhkmGVMILMi69d0zXz8u9TaGPfcGJ0xcPMEwIqy5LbP1VjeUde1rUtZ6AlyRCZRcrw7Tlo7O-0qSNmpKcdgGW_1m8L1KQYub1UHKkzBn5U4sRDl38y84xeG1Tl7po5kHLJwrbkr-5q37TzIWawhEMXAkJLLiFQicrGf1O7y-0aowlFXbODDfEpbO_RR2PgKyanlMC_mVfjEqViH9t0YJsIDDtvufB4DZVm40)


### Quy trình hoạt động
Quy trình truy cập hệ thống lễ hội

<details>
  
<summary>Code PlantUML</summary>

```plantuml
@startuml
skinparam activity {
    BackgroundColor LightYellow
}

|Người dùng|
start
:Truy cập hệ thống;
if (Có tài khoản?) then (Yes)
  :Đăng nhập;
else (No)
  :Đăng ký tài khoản;
  :Đăng nhập;
endif
|#palegreen|Hệ thống|
:Xác thực tài khoản;
|Người dùng|
:Xem thông tin lễ hội;
:Xem thông tin gian hàng;
:Đăng ký tham gia (nếu muốn);
stop
@enduml
```
</details> 

![Biểu đồ UML](https://www.plantuml.com/plantuml/png/RO-nIWCn6CVtxoa-SBc-mjrWiOk3T79ent1Dat39boENACLp4d7LqK6eE0kABhQ8GuhlaJVnhbDBpH08F_BZznysdZaVZ8QcKbGpnmooqgiBvHTu1TYT4rPMmjb0iv7Lrk6P4j9FkTRs4gu1sh7uVKlh9uMp-4MYXQqHydCN5bYcrMkDCgtlq7Vt0ua2r1opKVn07vSAAsdJweME1ntdXDcKDmD0p3VtcniIIB8N5C1rmp4RsrrMnUyzH_7VFvgfERH7DTDSECwfFTrfQI6VnETo-tmlzsM7k_89D-Xb_EpyNX7gjBxjfpsgue09nGXbNFPxztebCpt4ZDBg9w09VSYWWCRR6ePTRZ3w3m00)

Quy trình của học sinh tham gia

<details>
  
<summary>Code PlantUML</summary>

```plantuml
@startuml "Quy trình của Học sinh tham gia"

skinparam activity {
    BackgroundColor LightYellow
}

|Học sinh tham gia|
start
:Đăng nhập hệ thống;
:Đăng ký tham gia lễ hội;
:Xem lịch trình sự kiện;
:Đặt suất tham gia;
:Xem kết quả và phản hồi;
stop
@enduml
```
</details> 

![Biểu đồ UML](https://www.plantuml.com/plantuml/png/RO-zIWGn4CVxUOhX7aERGniB6pijGsv9GhB9canE3izAn484nSfE4B7HmahO81PxBp9lOlRGhKoL-N_yXfad4f5owt1sb5T8SNZp6YMNLu47N6ub9bC5qg95PSGC85dZEn7hB2IPfQ4LdWFMjoUaLJ5alzWFBaGyD4hJIUDSE8CBWFK_k3LiryFEvcvpwHLwpVrxXvhBTSrmkVTgTpBjy3KLqN6v6dEFfWQEctOKRgJ-Eo1n-K1hAiTl0Tn_4gRC_GjDZD-YvVwRyBHwpxWSdh3JzUT7zaDb9meTp1k_oAs37m00)

Quy trình của nhóm gian hàng 

<details>
  
<summary>Code PlantUML</summary>

```plantuml
@startuml
skinparam activity {
    BackgroundColor LightYellow
}

|Nhóm gian hàng|
start
:Đăng nhập hệ thống;
:Đăng ký gian hàng;
:Chuẩn bị thông tin gian hàng;
:Quản lý chi phí, doanh thu;
:Xem phản hồi từ khách và giám khảo;
:Điều chỉnh hoạt động gian hàng;
stop
@enduml
```
</details> 

![Biểu đồ UML](https://www.plantuml.com/plantuml/png/LP0nJiGm44Lxds8Em0cWMR4jGgA3qYIHnqeyZfBn8iHI80g4Q5XHqMr4XT1MKCMYSYxYcp1AWNPTkFZp_l-ZMVIiEmwkKNrjgTMTTg0BjYlBjt2dGDwfBchJ-K3bqZU-WpDhaA-gfl4twbwfzJccRmV6QW9CMp9hDMUgu-brUYG3X7dSjO0vFW7Blo5pyZ-iq--ULVGbXZn-4bpd-29u-X68BHr25y9y43HYBj12Ysbt1ANNX6890bnMJjGPaiOt2vpZ5zIOXW9XbROIbmOdWY1-tiRc-12W4FfPKj3dSM2ODZc-apaexzctQb5HAKVx0m00)

Quy trình của giáo viên/giám khảo

<details>
  
<summary>Code PlantUML</summary>

```plantuml
@startuml "Quy trình của Giáo viên/Giám khảo"

skinparam activity {
    BackgroundColor LightYellow
}

|Giáo viên/Giám khảo|
start
:Đăng nhập hệ thống;
:Theo dõi hoạt động lễ hội;
:Chấm điểm theo tiêu chí;
:Gửi nhận xét & phản hồi;
:Xem báo cáo tổng hợp;
stop
@enduml
```
</details> 

![Biểu đồ UML](https://www.plantuml.com/plantuml/png/TP2_JiCm4CPtFyMd3gpixLBHeGiB4WEC9ebYAx4TfPT2HPagn4g563fM5K8WChBKe_CYVXFECEFXPFc-FpzvkY3PKcTgZ2ww5QWDNrOXY_vTOgx3tc6fmwSzJNU3IiNZmOs4M5JQDhAL1Z8ZlTIqmhq0dpEPLMNhEflFNErQdEjIqNLHr-vMF0Yn_YzpBNv1n7Xu7ZQsXENNle6A_Wd4SslBYHXVgi8X3zyQoiNZdZ1iez-nl8x-CObtcbKpzhuPtkdeDmQKJCID7J8LUXRCe-_rNuN5NVWWdA1963PblAICgyBW9g5cQL3qhzp2oqCpOLBNY6bXS_usyGC0)

Quy trình của ban tổ chức

<details>
  
<summary>Code PlantUML</summary>

```plantuml
@startuml "Quy trình của Ban tổ chức"

skinparam activity {
    BackgroundColor LightYellow
}

|Ban tổ chức|
start
:Đăng nhập hệ thống;
:Xét duyệt gian hàng;
:Phân công vị trí;
:Theo dõi tiến độ sự kiện;
:Xử lý sự cố phát sinh;
:Tổng hợp báo cáo;
stop
@enduml
```
</details> 

![Biểu đồ UML](https://www.plantuml.com/plantuml/png/NP2nJiCm48PtFyMlFaQxL6Lb08a1HkDKiTNq72MNeeWoCJ2mq861ZSA0Af412PPQYC5v4Ry9bxBXuOR_vE__TDEQTSNDii3ej6d1LNmd2vF2cyPC4pY5HnYRmiwCbAeNZafTwIMqORTotE9QGTvCcqLU-OQo8r_u2iSkjtmnBmf_fMwKMlz3hTMXLetxX_wMSf1D-ww4xEx0CZUKJzJuFEuOMTDAoiYT86nyFcnER7mXcFWfVrSft0_UdUHdTkwHnIy7Tcd_G-WtAJoXJk432oSS6h0fT2ZYzrzif0sbZLj6xSWE4F4KhcYybhYCMmyZOoBAlbJJEMLoBVKB)

Quy trình của quản trị viên

<details>
  
<summary>Code PlantUML</summary>

```plantuml
@startuml "Quy trình của Quản trị viên"

skinparam activity {
    BackgroundColor LightYellow
}

|Quản trị viên|
start
:Đăng nhập hệ thống;
:Quản lý tài khoản;
:Phân quyền người dùng;
:Cấu hình hệ thống;
:Sao lưu & phục hồi dữ liệu;
stop
@enduml
```
</details> 

![Biểu đồ UML](https://www.plantuml.com/plantuml/png/PP2nIWD148RxUOgV53v4qWJJMXYiB9TBk5rkCtlkxKOEOo4M5ZQAjI1A44GnhRTORSXxx9ku5wnqYYd--Rz_c1atJbZd5ng3gM_XR7ndYIA5Lu6fJzqBPos5MonLVEC1KLCfheKL2uZ2gQLoBIu8kGv5KPNMU9vDZ3OMHwgKxdIkjJcdIwBL_xGLxPVJS7ktlUOIB5FtKKEcS0EN-psN8nh-SZf-myKdXKgQNiYJOncV6MU-JU6AmULkayAZmYn-xS59wjOUiZ_eR-Q9CD2xZSS1wYokYzxmaD4KFg5LDliHDSxKD9xpB7-7VW00)



