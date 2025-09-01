
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
 
### Biểu đồ Use Case tổng quan

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
|#palegreen|Hệ thống|
:Xác thực tài khoản;
|Học sinh tham gia|
:Đăng ký tham gia lễ hội;
|Hệ thống|
:Ghi nhận đăng ký;
|Học sinh tham gia|
:Xem lịch trình sự kiện;
|Hệ thống|
:Hiển thị lịch trình;
|Học sinh tham gia|
:Đặt suất tham gia;
|Hệ thống|
:Xác nhận suất tham gia;
|Học sinh tham gia|
:Xem kết quả và phản hồi;
|Hệ thống|
:Hiển thị kết quả & phản hồi;
|Học sinh tham gia|
stop
@enduml
```
</details> 

![Biểu đồ UML](https://www.plantuml.com/plantuml/png/VL6_JlCm4D_lAKxzfEyXcgM2WGuiR6MqqYYsubo2unHLXAb230Y9Yecjg48iC30X9K8CwOluJRWMjQZWDaFi-vr_Vtpk5LOOMwOQEoVb6ArfNqXYw9fdWNtNt8POA0Qi52d6IdG0YaHHBWpN8hHgfEmOBm3vEn1X4fkifE5XfZE3nogMzZJIEZk7Iu3A8rV1oXwwYxl5X68awUhN7ALhhj7oVqfn0DM_NEWeDb54hF7JgQ0xQ1_3LVd6IpjJcCZCrNCA_6uRdwJzsA2eNNErj7nG0VmsE9BgEnJXOhgcxbGVHEbIxIQKwq4M70qJnQBqLxpF-8GOOCesRqz-LxzRB4fNFzbD8m3VODR1lOTtf4zS_MdnZ1bp7BKpp2Nl25dtNks_m1RrluVeU_iiXrv4mpBLy0K0)

Quy trình của nhóm gian hàng 

<details>
  
<summary>Code PlantUML</summary>

```plantuml
@startuml "Quy trình của Nhóm gian hàng"

skinparam activity {
    BackgroundColor LightYellow
}

|Nhóm gian hàng|
start
:Đăng nhập hệ thống;
|#palegreen|Hệ thống|
:Xác thực tài khoản;
|Nhóm gian hàng|
:Đăng ký gian hàng;
|Hệ thống|
:Ghi nhận đăng ký;
|Nhóm gian hàng|
:Chuẩn bị thông tin gian hàng;
|Hệ thống|
:Lưu trữ thông tin gian hàng;
|Nhóm gian hàng|
:Quản lý chi phí, doanh thu;
|Hệ thống|
:Hiển thị báo cáo chi phí, doanh thu;
|Nhóm gian hàng|
:Xem phản hồi từ khách và giám khảo;
|Hệ thống|
:Tổng hợp & hiển thị phản hồi;
|Nhóm gian hàng|
:Điều chỉnh hoạt động gian hàng;
|Hệ thống|
:Cập nhật thông tin gian hàng;
|Nhóm gian hàng|
stop
@enduml
```
</details> 

![Biểu đồ UML](https://www.plantuml.com/plantuml/png/bPAnoXD14CVxVOhX4wnyWkzhFanXYY04B6AvkHmxoztD7fVTIF0i98L86eDOsEL88Q91HQiiLXjyZtqJXuF0aPm1hzXZv_xp_mtpl_kvbPLrHGutOxS4MuMlX914_qd2Kmm_2r1Q4c3OaheHOfvfAcKb2v29rGjjb_1I03-FPPAfoZYQ3KnkAXXfXVPvckVcXNWbH7tkLOiMB6wFxuuhKa0O3_iICFetOFdSaBeJzODIvgcgqfJgOUTBBMudeKdQwmz-XQs634qyxEYk3tM2PE5tfyxICzCdgA4TXE2uENNqEmxGnSDdWcdqQtO8lrXiDLsr7_tvxi1MqN_hx-WdZHcq8yXvzWGrb1ZsZs1c926xk4lAK4U_ehQmXcbe32HyzFVsyIPfmSAMoHRlDTZelq26l724HTYoEZG55rXYBl7Felz02lY-A-4XO7UQhks_WcBzQmS9QzuI0dAeZUKqelz8wkfs1-qFrCPd_sE_SsjASP_Ip1Mv-0i0)

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
|#palegreen|Hệ thống|
:Xác thực tài khoản;
|Giáo viên/Giám khảo|
:Theo dõi hoạt động lễ hội;
|Hệ thống|
:Hiển thị thông tin hoạt động;
|Giáo viên/Giám khảo|
:Chấm điểm theo tiêu chí;
|Hệ thống|
:Ghi nhận điểm số;
|Giáo viên/Giám khảo|
:Gửi nhận xét & phản hồi;
|Hệ thống|
:Lưu trữ nhận xét & phản hồi;
|Giáo viên/Giám khảo|
:Xem báo cáo tổng hợp;
|Hệ thống|
:Tổng hợp & hiển thị báo cáo;
|Giáo viên/Giám khảo|
stop
@enduml
```
</details> 

![Biểu đồ UML](https://www.plantuml.com/plantuml/png/VP0nIyD05CVt-nIF2gxkxLBiq0vTX0vrZ6d87KdUXUIbMenJ4GSNYpXqinGHnQA2BjvunUzntyIx2gMqcWmlT_T____lxZLpyZ8gaXXgHyK8ADCloC4twj63jj0p2KEXd_70hHE8kFcQonfZUIGmzJ8l0SydCHGqWdC6zZlq_2ZCP863benb1bqHSZeEubYUiWl6olyoIxQw2AilRvPZ307jwI85RjGLaAqJ31kit4kzE0Yp8C2oiw6KhDxNCt-rVRS_VIyWujBcOgCAMU_nGC90VmfmtJE2vSIegSN7Hbqw-5Gqs3Qg8umQu-hWsbRzOVj9u5P4DRXb5m-9xNLP2P2x1zd60dok5xlCDXU_8y6r9xTQDQHjr69jEzDF1FkGEX7Tqsx_U5ht-wq0oenwhR1LG_j10YTEzLqXe-umTBvvkelhRQWMmZS7kywenEKaKzOCS50aCVi1)

Quy trình của ban tổ chức

<details>
  
<summary>Code PlantUML</summary>

```plantuml
@startuml
skinparam activity {
    BackgroundColor LightYellow
}

|Ban tổ chức|
start
:Đăng nhập hệ thống;
|#palegreen|Hệ thống|
:Xác thực tài khoản;
|Ban tổ chức|
:Xét duyệt gian hàng;
|Hệ thống|
:Ghi nhận kết quả xét duyệt;
|Ban tổ chức|
:Phân công vị trí;
|Hệ thống|
:Cập nhật sơ đồ vị trí;
|Ban tổ chức|
:Theo dõi tiến độ sự kiện;
|Hệ thống|
:Hiển thị tiến độ;
|Ban tổ chức|
:Xử lý sự cố phát sinh;
|Hệ thống|
:Ghi nhận & cập nhật sự cố;
|Ban tổ chức|
:Tổng hợp báo cáo;
|Hệ thống|
:Tạo & lưu trữ báo cáo;
|Ban tổ chức|
stop
@enduml
```
</details> 

![Biểu đồ UML](https://www.plantuml.com/plantuml/png/VPAnJiCm48PtFyL9I7s8TgdQWGuC30mm1YUAhQJda3Y5YZ1rOEX2XHZO6Zfrg009baI8mLNVms_2AHLIGo8oEBBl_k-_tt8_qKwiqt78aa1YvCJE61okvKJgATmoe6_WyC2FLOhkK8KgXXFf2ttXXQ6wPdUCPGC7GTlo2RYmvPfdh4AoxlPXEqCVKDXY4m7Lxa7Jka2_nxAZo0azF_Oyp4O7bOnrpqtEg-qx_SnIGY2KBLROQt6YvhK6DvqIGeClgIxCiZBuGpqMSZy9Gc2BRmrNAK7Xva3VQd0gp0i2Dn-KP6BBEUZOR9huOPMnCj2Gx7BOBcpvM5CqsMV2K-2QJmbQqanOYPuXeUWGI3B0fj68pcTO7SnhilRhiUK6GlErPtA2G2HCJYDA5FzUKWTuBTAllZq8xT07sguYk3Iv0avBWqzz1TKw4ExUKj2nBLzhtIqFIKMixw5Bx_C7)

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
|#palegreen|Hệ thống|
:Xác thực tài khoản;
|Quản trị viên|
:Quản lý tài khoản;
|Hệ thống|
:Cập nhật thông tin tài khoản;
|Quản trị viên|
:Phân quyền người dùng;
|Hệ thống|
:Ghi nhận phân quyền;
|Quản trị viên|
:Cấu hình hệ thống;
|Hệ thống|
:Lưu trữ cấu hình;
|Quản trị viên|
:Sao lưu & phục hồi dữ liệu;
|Hệ thống|
:Thực hiện sao lưu & phục hồi;
|Quản trị viên|
stop
@enduml
```
</details> 

![Biểu đồ UML](https://www.plantuml.com/plantuml/png/ZP0_Ipin6CVtl8e7Vl1x4UrIxA131qK77SFrI4BJ9p6NL8hd80uEBegpu1-wY6855tiufVHzv9sOkmgMQm-yuOxBa-_dy-NfP9OQwuQIP0E1cXew19fOCH9s3AS4uhD5am4poc6_gwGoq1ECswDKIdL2pWZ9zroOFI5O4ueh60d_Z3cfgAGrlvvV80FaOVQgWOVY4cnyto1ha_oVfZ9b9aqntrcPvAHrw1-IwlSzVlozW05NfQEzMTRwEPJ-gtQz3kvMFQewDXxx3sHW1Vv9iilz8yAn6uVY707POXgAEm5z_ubitRJDnTA3e5U3JVJOREA0-nVazJtLoBt5r5NXDqX-GqtSVQf0bed_e2DYafJqsrYxp4iHqMvTSR1SFI_72DbcH8CniqgJJefzDvJV)

### Luồng xử lí
Luồng xử lí đăng kí và đăng nhập

<details>
  
<summary>Code PlantUML</summary>

```plantuml
@startuml
actor "Khách" as guest
participant "Giao diện" as ui
participant "Hệ thống" as system
database "CSDL" as db

== Đăng ký ==

guest -> ui: 1. Truy cập form đăng ký
activate ui

guest -> ui: 2. Điền thông tin đăng ký\n(họ tên, email, SĐT, mật khẩu)
ui -> system: 3. Gửi thông tin đăng ký
activate system

system -> system: 4. Kiểm tra thông tin
alt Thông tin hợp lệ
    system -> db: 5. Lưu thông tin tài khoản
    activate db
    db --> system: 6. Xác nhận lưu thành công
    deactivate db

    system -> system: 7. Tạo mã xác thực email
    system -> guest: 8. Gửi email xác thực
    system --> ui: 9a. Thông báo đăng ký thành công
    ui --> guest: 10a. Chuyển đến trang xác thực email
else Thông tin không hợp lệ
    system --> ui: 9b. Trả về lỗi
    ui --> guest: 10b. Hiển thị thông báo lỗi
end
deactivate system
deactivate ui

== Đăng nhập ==

guest -> ui: 11. Truy cập form đăng nhập
activate ui

guest -> ui: 12. Nhập thông tin tài khoản
ui -> system: 13. Gửi thông tin đăng nhập
activate system

system -> db: 14. Kiểm tra thông tin trong CSDL
activate db
db --> system: 15. Kết quả xác thực
deactivate db

alt Tài khoản hợp lệ
    system --> ui: 16a. Thông báo đăng nhập thành công
    ui --> guest: 17a. Chuyển đến trang chính
else Tài khoản không hợp lệ
    system --> ui: 16b. Trả về lỗi
    ui --> guest: 17b. Hiển thị thông báo lỗi
end

deactivate system
deactivate ui
@enduml
```//www.plantuml.com/plantuml/png/ZLH1YzD06BtFhtZqfD0DHjsj5YeBA-p2Bbws1mzUfcbiXYQJsamMUvGzU11Xz-HrIqyA1GLFBU8XnV-HV-8toOPEnyRsb8JvlZVl-zvxEKuK7wiq2XdtL3n6upp8fbxG04ymIFr4iH6T2q-Ck5Hed0eUeo_ovKTPbAHYy_oCJg22V7ah1qL1CacK7x4-Lxp74n-DaykN5yL9lyTOfuFLpUfQ3Z3CVg7JOQou4mSl2BaDrq5td4xWvOlv26_ZSOJLRLMk2OihhdmgjVeUEmHB93z8ufBzf7ebfD7wHZuWYf-Xic-o2J_Y8cpYSdNJRIAYgnI6GRxucZvagT2GvGnjF75mcY_dmWAr-LGpi_9f8ZnrS4wyhYEeCJTW60yLkcjKOZSR8QHbCW1O0_LxRHmwkFZpFJLPgEnE4EauNynaqL5neGRzJGyS63oE7BmccI436bSYl8Uxam4y3Lhs-2QAHQH2Qf54-M8Q8yfcUAynjVe_l7AhLbCXKXlFgZqMDMRNHlszcC-vKwscbqrZO-F_KjPwhUzn7r7hIP1EQEDQgNpnM-h5oy4MfdwO-AO4m_BLLiBYrjCEfQtZYjocoxw8hKIexamKDFIbdw2CWSekN_QPiV4gDxxXSYClfNAZBP6foqpLyf_Ok9IRLqLHdRUiGBZrYR1liq9HUTcjImHznlIc_nRCjA5bPFUG-abNXNSf4TpmakNV8cB6B3kaTOzitvbpxRHUgzPwNf3DPL3wpU2pd-E8rfwMQ-rdkPsUEwQgD0h_0W00)

Luồng xử lí học sinh tham gia lễ hội

<details>
  
<summary>Code PlantUML</summary>

```plantuml
@startuml "Biểu đồ trình tự - Sinh viên tham gia"

actor "Sinh viên" as student
participant "Giao diện" as ui
participant "Hệ thống" as system
database "CSDL" as db
participant "Ban tổ chức" as org

== Đăng nhập ==

student -> ui: 1. Mở trang đăng nhập
activate ui
student -> ui: 2. Nhập tài khoản, mật khẩu
ui -> system: 3. Gửi thông tin đăng nhập
activate system
system -> db: 4. Kiểm tra tài khoản
activate db
db --> system: 5. Kết quả xác thực
deactivate db

alt Tài khoản hợp lệ
    system --> ui: 6a. Cho phép truy cập
    ui --> student: 7a. Hiển thị giao diện chính
else Không hợp lệ
    system --> ui: 6b. Trả về lỗi
    ui --> student: 7b. Hiển thị thông báo lỗi
end
deactivate system
deactivate ui

== Đăng ký tham gia lễ hội ==

student -> ui: 8. Chọn đăng ký tham gia
ui -> system: 9. Gửi yêu cầu tham gia
activate system
system -> org: 10. Chuyển yêu cầu xét duyệt
org -> system: 11. Phản hồi duyệt/không duyệt
system -> db: 12. Cập nhật trạng thái
system --> ui: 13. Thông báo kết quả
ui --> student: 14. Hiển thị kết quả
deactivate system
@enduml
```
</details> 

![Biểu đồ UML](https://www.plantuml.com/plantuml/png/XLDDQnDH5Ds_Nt6OjHbDhHy68gKLMgYAqFo1Dnza7icy6PFtGhEK8bs8O2WYhZHq8IbcKN2LGLnC_iZy4-_BPCpBaE8guTrpxxdtd3C7GyK7IiTzE8UYo2uqbfCYku8Qv3zb15LajsZWJD3_aSXl95J4OtG5TnZZlae6S3P51to8eT91A1LBQQxmHSgbWdCiU8A022vBa1RRzHEgqEWYcyXkEMKyL67C0gwunuSXdAEp5ozNbS3RRZtaqgpv6Jwrp_mL9Xbq6MktiVoql91ToAXOp5EqsuojjqFZERHeeUdYLP5zetCvuPOJ2sxE4oEkGWBMs_PSl2vdgloxG2zAYiMrl8UOtXHwL9fffeM1buUqyD35SP7D1LsP_o8I9UGTVDNjvO-P4NWjxBiuDGR5PjSjsaqZIHDuQ5YiZwYhMFnHUAi9YlDywgzallLP4DfzZFSLEjPK4EewHP-COG1GRRDMu35tSHGbIADybj9AUWpVN66m132uAWajF27mYLbUhiW_eBk90zcMpsN4mZwvV5fgynzgpqLdOCuP5Tax0_iYTjDwsxILz5u-JTPjeGni8QhKXRRtLf1w-Uz_7u2PyDwi-bNiIjPJqeUA7qkNQxsrR3ohiZ7ERxJHyOVUGE-E1QMS4lp04EcnETFkFyzd2e5vlrICa3PVasB_9gfSlX8Lxdwl5AXgsqvWSu-OZCTbO1KKcJ0bECaw5QpcKfC2tx7qxcrYoEf6DVThHbdW7VOSa6iwxhE_)

Luồng xử lí nhóm đăng kí gian hàng

<details>
  
<summary>Code PlantUML</summary>

```plantuml
@startuml "Biểu đồ trình tự - Nhóm gian hàng"

actor "Nhóm gian hàng" as team
participant "Giao diện" as ui
participant "Hệ thống" as system
database "CSDL" as db
participant "Ban tổ chức" as org

== Đăng nhập ==

team -> ui: 1. Truy cập form đăng nhập
activate ui
team -> ui: 2. Nhập thông tin tài khoản
ui -> system: 3. Gửi thông tin đăng nhập
activate system
system -> db: 4. Kiểm tra tài khoản
activate db
db --> system: 5. Kết quả xác thực
deactivate db

alt Hợp lệ
    system --> ui: 6a. Cho phép đăng nhập
    ui --> team: 7a. Hiển thị giao diện chính
else Không hợp lệ
    system --> ui: 6b. Trả về lỗi
    ui --> team: 7b. Thông báo lỗi
end
deactivate system
deactivate ui

== Đăng ký gian hàng ==

team -> ui: 8. Nhập thông tin gian hàng
ui -> system: 9. Gửi thông tin đăng ký
activate system
system -> org: 10. Chuyển yêu cầu xét duyệt
org -> system: 11. Phản hồi kết quả
system -> db: 12. Lưu thông tin gian hàng
system --> ui: 13. Thông báo kết quả đăng ký
ui --> team: 14. Hiển thị kết quả
deactivate system
@enduml
```
</details> 

![Biểu đồ UML](https://www.plantuml.com/plantuml/png/VPBFQXDH5CRtzoa-icymjlun42cjq4AB2Fe2T_wOUsdcpZYvjvYbTD656qiHjorTICI0HLSPnCKDliUyYUUGbDn94rS3SxzpldFExziTMbbQbmtGsjDrTUOmkwYhIzZIVpSAjgvkiOMNol_CqDVIGFahqsy98MERbsZTUu4SmgOo4mNrrR4kfB5e7MYP8o63SyCAEDryFwGNM5LN5uiMmz7Gffb8f9MH7APexRz-SSmlIA9cwPuqFEPdn5G-Zbc3lEmBqUjXzcbsPlemgfvE2lHwGl1es7eEfxlejF6cT2F4_8gtUPdHya41xwXFfKr9tIXysAQBi09M-L-ajzh0-YkD4vNNqniZd2RjOeakjjiugAk93kKRd1Pxpp_S8ucws6dZYE5aX4KsZ9Q5T9OambRW-eYgwkaVYtUEf7ZlhsFmYMzZaQHXdP032o9mKs1070G0t0smsFYnR6DVvIYK7nShimCW3KiPF1a_8V4Xpsl0VX_HNz8dIdvYb4W71FLeVWxrV-k8CV46ftNrWMLVz1fFLitRHVuwNyXIauIxteKg3S46EJdnluCetylBqpNO0_qAz6URePFFPk8SNihc0pwu6_4LCVBV7AVqgoEAOuk4_vzRGShGiKE1VgKu5dpIImh94lzAeZeKuUE_Fzo6JLOGTBORnmtxXYirW7HscY48YzOmsILKBXk8Vm00)

Luồng xử lí nhóm giáo viên/nhân viên chấm điểm gian hàng

<details>
  
<summary>Code PlantUML</summary>

```plantuml
@startuml "Biểu đồ trình tự - Giám khảo chấm điểm"

actor "Giám khảo" as staff
participant "Giao diện" as ui
participant "Hệ thống" as system
database "CSDL" as db
participant "Nhóm gian hàng" as team

== Đăng nhập ==

staff -> ui: 1. Truy cập form đăng nhập
activate ui
staff -> ui: 2. Nhập thông tin
ui -> system: 3. Gửi yêu cầu đăng nhập
activate system
system -> db: 4. Xác thực tài khoản
activate db
db --> system: 5. Kết quả xác thực
deactivate db

alt Thành công
    system --> ui: 6a. Cho phép truy cập
    ui --> staff: 7a. Hiển thị giao diện chấm điểm
else Thất bại
    system --> ui: 6b. Báo lỗi
    ui --> staff: 7b. Hiển thị thông báo lỗi
end
deactivate system
deactivate ui

== Chấm điểm ==

staff -> ui: 8. Chọn gian hàng để chấm
ui -> system: 9. Yêu cầu thông tin gian hàng
system -> db: 10. Lấy thông tin gian hàng
db --> system: 11. Dữ liệu gian hàng
system --> ui: 12. Hiển thị thông tin
ui --> staff: 13. Thông tin hiển thị

staff -> ui: 14. Nhập điểm + nhận xét
ui -> system: 15. Gửi kết quả chấm điểm
system -> db: 16. Lưu kết quả
system -> team: 17. Gửi phản hồi
deactivate system
@enduml
```
</details> 

![Biểu đồ UML](https://www.plantuml.com/plantuml/png/TLEzRXD16EptAKPkaKyuv0Si6KLnf4GYIeCBAFT-x5tbRi_OkmZNAIWG4b4AsbW8eI0YYA3o5HHdyHxt9doBVRdrSQbEkc_c-vcPtPzgFj4cYT4wa4LsRh2yAB9Bw4d-JGde8hj56qSodoSu4yNYKug0FfyJmbbyqcAC1pgTeEM2Mk1JKElXa8sflmpac2jjCJn5ICItoa9Wv6Rzc2hGeiWkr6ZLOpRLKS92hhdFfn5Q_UU79xQ2qD-adehyPuAHv0eYlrhJTSGJndezB3yipzK8YhQx6QFNO-pVTcW_XP5TT3mC9cQ6m9OnJ2VsFeTXRvIlkOu8lSdSyd2wQgf5_ei8MYfc99NNktVnoCDHaTr8pFAlnexuOkxfNfwx-jWUeT_5jeSN-Jo0rUMMFlcL99bJqbbLJ98ZzD5snkvuU5OiVckyCWJ5cwe52oENntYiCR2Y2GJs1WO0vGxhEtUvXxv8CHRvDTrw9vR54i3YLePtiKVGOniE1Jll7KQLwxNqi2WcKmVsduPVBEQoSRRluI2VfuYBxADickZN9gwzy2jIf4Btx39NaMki3Kf_Ox__a_BOiv3ilNAYHcW2hq-hcV_4mylAzYeZ3hrcT-UXXnFgD6j6rstkK7OFY-mxOYkmQUfRXdohhfARM5VF3aLsK0qN3gd-SBRlybzAzc2LQaM9kzOrDJexvLiugw9PoqHTZbsIuyyFup8SY7tX1Deh-uu5rHLerKlPOFW-vS0aCViB)

Luồng xử lí ban tổ chức quản lí sự kiện

<details>
  
<summary>Code PlantUML</summary>

```plantuml
@startuml "Biểu đồ trình tự - Ban tổ chức"

actor "Ban tổ chức" as org
participant "Giao diện" as ui
participant "Hệ thống" as system
database "CSDL" as db

== Đăng nhập ==

org -> ui: 1. Truy cập form đăng nhập
activate ui
org -> ui: 2. Nhập thông tin tài khoản
ui -> system: 3. Gửi thông tin
activate system
system -> db: 4. Kiểm tra tài khoản
activate db
db --> system: 5. Kết quả xác thực
deactivate db

alt Hợp lệ
    system --> ui: 6a. Hiển thị giao diện quản lý
    ui --> org: 7a. Truy cập thành công
else Không hợp lệ
    system --> ui: 6b. Báo lỗi
    ui --> org: 7b. Thông báo lỗi
end
deactivate system
deactivate ui

== Quản lý lễ hội ==

org -> ui: 8. Xét duyệt gian hàng
ui -> system: 9. Gửi yêu cầu
system -> db: 10. Cập nhật trạng thái

org -> ui: 11. Quản lý lịch trình
ui -> system: 12. Gửi dữ liệu
system -> db: 13. Lưu lịch trình

org -> ui: 14. Theo dõi báo cáo
ui -> system: 15. Yêu cầu dữ liệu
system -> db: 16. Truy vấn dữ liệu
db --> system: 17. Kết quả báo cáo
system --> ui: 18. Hiển thị báo cáo
ui --> org: 19. Báo cáo hiển thị
deactivate system
@enduml
```
</details> 

![Biểu đồ UML](https://www.plantuml.com/plantuml/png/VLDDQnDH5Ds_Nt78leDJQri3aP8ABRG8eWjTllbmvk7aJPoyAMPTn4Kt5X5nrr14AXOjw2Q3k9ZW_vX_uhrCqhoyIZT9u9rxpZttdEoCZ2nCESZGwQkcEYunEssgzp15_KsdC4rrXJNqfUQV7n2cJNKHTeIGeSaBTDm7o17o8X538bMX6afjqDbJCaT4x6yr0r2grVTzUe4XWbETC02ZySZ40n598mCvYj7PVVBma5yG1KBqUfYzcnth13fjffT3z7f2a2ZM7X1r5xw7fqKvHiYFU94N0_9auNbtTIHDJ6XxRjt3evRGfFLFWXkbOUepXPTftapFjIWLOzljkhZhOQ-fBfK5NrBFBRHVF1K5NMnuEE0Z3s0AQLDRW-Gm2h1cwToZgMRwn-1LIL2yhYSX-5fNeOXYUqx8p82EUJv4HYSL0B1OOEvnKthOvnKqcE84oJARbbyZgt_pAE5vZEFiOalQHsN7Ppf5oBv5d5541-qDqjlL0m_zUf8puAEwAHAGICiJB56nZcoVYsx4TehSYSVNs_FW6rxbatAxiUtXMNrX49LZsj6mVGqsapZXtb-4Eww_bkpwI-c4wT_niClNQ6jbO8fcEj497sUYLXlfUyvw9s4w_uivklxwGZXggk_8E9aRojIymxy_IeTeHN63JnddYEfVghrcI1-k65Nh-RM_snGtv_4VDTFFsWQwPVMtLjfgIJjTyBUT9YwHTYTy2gA_U45g3Vod53lKbNAGYNy0)

Luồng xử lí quản trị viên

<details>
  
<summary>Code PlantUML</summary>

```plantuml
@startuml "Biểu đồ trình tự - Quản trị viên"

actor "Quản trị viên" as admin
participant "Giao diện" as ui
participant "Hệ thống" as system
database "CSDL" as db

== Đăng nhập ==

admin -> ui: 1. Mở form đăng nhập
activate ui
admin -> ui: 2. Nhập thông tin
ui -> system: 3. Gửi yêu cầu
activate system
system -> db: 4. Xác thực
activate db
db --> system: 5. Kết quả
deactivate db

alt Thành công
    system --> ui: 6a. Hiển thị giao diện quản trị
    ui --> admin: 7a. Truy cập thành công
else Thất bại
    system --> ui: 6b. Báo lỗi
    ui --> admin: 7b. Hiển thị lỗi
end
deactivate system
deactivate ui

== Quản lý hệ thống ==

admin -> ui: 8. Quản lý tài khoản
ui -> system: 9. Gửi yêu cầu
system -> db: 10. Cập nhật dữ liệu

admin -> ui: 11. Phân quyền
ui -> system: 12. Gửi thông tin phân quyền
system -> db: 13. Lưu phân quyền

admin -> ui: 14. Sao lưu hệ thống
ui -> system: 15. Gửi yêu cầu
system -> db: 16. Thực hiện backup

system --> ui: 17. Hoàn tất
ui --> admin: 18. Hiển thị thông báo
deactivate system
@enduml
```
</details> 

![Biểu đồ UML](https://www.plantuml.com/plantuml/png/XP9FQnD16CRlyoaUSk_YLll7GAIqGWjMKPg3rza_PeTkTjDaff2ZzE2X5ui7ZpQA2CMY1K-xY8SDVe_v9hwpGyXa6l2qiE_pplE-x-_PcqW-bcgOexClT7sXCB_IzGV8SVEzo21rVOSDl5Aw-bBGJrrVubmqDqM7CHxBSepEcXhu13mPYeADw74HYn4l93g7WfT8oEMTbIYnMZ-Y2cIcwwjYq0ecqubCXopXaaTyag9pSFBqkAqa4MEz7kRlvnV504McgziHUZt6MbjiF84INOG1dklw4zwKuo7jvMZDyEASovHqgpsR0LxOvsJM_A86IMieOSfsd2uU1ZZKzQt0jBbHY7NrJItVio9cFwOhYRfu5E1rCulRvUxYfPZMI29iE6zl1NYcgpyIP-QiB4bTBUEvH3zhhebCR8PZ0B2miWjWcmSuCYYBrkuIW-NPSUR0QfkLC8sMLXSxrDiVgobYUm7NAis9G9zEyrKYqjLCh3MF0kmtinAvhZ-ATGwHDvqLfaNYxhe0dxgO2FWYY7dp6vcJblleTmDNAvjhWTEif1y-pCVtONhmmWS13imzR7Oa4bt_G6uEglp0XG5UPirdS-Yfhj_wPk7cmcqPBepS1j-RidRyzwVoH9uhnUk46ET6w9x5Tz_w_wxR580sfCXiOY8UdweHOnxeS8SubXGFI9C8jaevtFKestKHKJJMSDuZ_6gOity0)

### Luồng dữ liệu

<details>
  
<summary>Code PlantUML</summary>

```plantuml
@startuml "DFD cấp 2 - Hệ thống lễ hội ẩm thực"

!define PROCESS circle
!define EXTERNAL_ENTITY rectangle
!define DATA_STORE database

' External entities
EXTERNAL_ENTITY "Guest" as guest
EXTERNAL_ENTITY "Student" as student
EXTERNAL_ENTITY "Team" as team
EXTERNAL_ENTITY "Staff (Giám khảo/GV)" as staff
EXTERNAL_ENTITY "Organizer" as org
EXTERNAL_ENTITY "Admin" as admin

' Main processes
PROCESS "1.0\nQuản lý\nTài khoản" as acc_mgmt
PROCESS "2.0\nĐăng ký\nTham gia" as reg_event
PROCESS "3.0\nQuản lý\nGian hàng" as booth_mgmt
PROCESS "4.0\nĐánh giá\n- Chấm điểm" as eval_mgmt
PROCESS "5.0\nQuản lý\nSự kiện" as event_mgmt
PROCESS "6.0\nCấu hình\nHệ thống" as sys_config

' Data stores
DATA_STORE "D1 Users" as users
DATA_STORE "D2 Registrations" as registrations
DATA_STORE "D3 Booths" as booths
DATA_STORE "D4 Scores" as scores
DATA_STORE "D5 Events" as events
DATA_STORE "D6 Config" as config

' Guest flows
guest --> acc_mgmt : Đăng ký/Đăng nhập
acc_mgmt <--> users : Lưu/Xác thực user

' Student flows
student --> reg_event : Gửi thông tin đăng ký
reg_event <--> registrations : Ghi trạng thái tham gia
reg_event --> org : Yêu cầu phê duyệt

' Team flows
team --> booth_mgmt : Thông tin gian hàng
booth_mgmt <--> booths : Đọc/Ghi gian hàng
org --> booth_mgmt : Xét duyệt gian hàng

' Staff flows
staff --> eval_mgmt : Điểm + nhận xét
eval_mgmt <--> scores : Lưu kết quả
eval_mgmt --> team : Gửi phản hồi

' Organizer flows
org --> event_mgmt : Quản lý lịch trình/Báo cáo
event_mgmt <--> events : Lưu/Truy vấn sự kiện

' Admin flows
admin --> sys_config : Quản trị, phân quyền
sys_config <--> config : Lưu cấu hình hệ thống

@enduml
```
</details> 

![Biểu đồ UML](https://www.plantuml.com/plantuml/png/RPHFRpCr4CRl-oc6N01126__z80gr3G90Qcqa2oebI95hkFiMjdrfhQtjDnGXNf0I5ISk3KWX5fH2IHEYH27hVWU-qqOEzlridalqMJz_FoCnpC-K9f8dSOHDBeVTO7cor_di0LD-3XVtO8EyzMT223ALzy2nZzno9SFiVt-9srutXiJDkM2mMU3aqvlE0JA9OrO-RbtwlS6n-sZSU_O_yG_0yce9YAeABfjlpqU-YU37ao89kT4CSzx4tfNcab18c12SysPykfRDVefKxe1H45Weat1KASJnAr4hUDDaSz8R1KQWzVjGQPJUAlFiqKCip1V_fAq-b--NUo9Qvl8YGo8u5ypQKM933ObxKdCXLqc9Z87_fHm0NEPKAOKdlQbderNxxq_4f-dQ2mWoluU2J-xvvX9Wb-ABIWTnq6i7RDbcESVdcz403FBX2I6W1EhbomOiqicAi1stQJFYO0mknU1HSwJH8SravsrIROG8GHOdf5eGYV4zedX-OxdgvlOekoIH3Loj-usn6Q26JAtmZ8skngqPw0ERfzYNh-BS2Ig3MenTQt6D15J7fY2Teace7GYiPgL9cjqNy4NYabbaHIZsl8M35Z0bPP4yqIiPRBofIRVXaDJ7ENgL1Fim92Q9DOfqiryTg5dpglSqMk2FUZOKrc1Ew3jVvX6oLVA2spSR7vOTWDy0Au3MaKey7wUvbwfsJU4hG7AZ_xz8ssTPWjQJBTTC4R571LMnIGPCzTAYFVprHD7DFiBZJGNs0KlzfxJ6SV_bzEW8O8oNouC6MOB_5SqR8Kq80uJoi-onzGyLB-bC0-pHvYarzWAsgHgfhd8KsDe8TUyoFeklw3iSQyYsIyHPKkOhxwdBKomAiSqDdS-pHxqIofLCMPb7v6oV1WRsas6zR4J0--ihqZ05Uxc6ONBgcYUugPWbY__qN1XngWYD3fpyl92vg6TCxpH7xd9fNoTrlcKPt4pXwWRJlFoVqT3qD8CNUimMoH0ySUhwFTBlcmZNwRNS8dJAa2vuJR-zkahl8cD3Ur6rxbhYTRlcYl-MS25AUmtmgi8hMq9sPfGzpv0M7aUFE-0YKaQHzv_)

### Các trạng thái thực thể trong hệ thống
Trạng thái gian hàng

<details>
  
<summary>Code PlantUML</summary>

```plantuml
@startuml "Biểu đồ trạng thái Gian hàng"
[*] --> DangKy : Tạo mới gian hàng
DangKy --> ChoDuyet : Gửi thông tin
ChoDuyet --> DaDuyet : Ban tổ chức phê duyệt
ChoDuyet --> TuChoi : Bị từ chối
DaDuyet --> HoatDong : Bắt đầu lễ hội
HoatDong --> DaChamDiem : Staff chấm điểm
DaChamDiem --> KetThuc : Sự kiện kết thúc

state DangKy
state ChoDuyet
state DaDuyet
state TuChoi
state HoatDong
state DaChamDiem
state KetThuc

note right of DangKy : Nhóm học sinh đăng ký
note right of ChoDuyet : Đang chờ xét duyệt
note right of DaDuyet : Được phê duyệt
note right of TuChoi : Bị từ chối
note right of HoatDong : Gian hàng đang hoạt động
note right of DaChamDiem : Đã được chấm điểm
note right of KetThuc : Gian hàng kết thúc

TuChoi --> [*]
KetThuc --> [*]
@enduml
```
</details> 

![Biểu đồ UML](https://www.plantuml.com/plantuml/png/TLF1IiD05BplLxopq1_m8CK6AXIys9ju26cQNTfif7q1UoxIWmZsu454K8f85L7HKnRnaE9_x9_ujkmssu37oSxictcJROun766U3jdnpWaq6diGX3BfJ60Nkhfuo23LwbP08a89lBoN2RFdXjhYMP1FOYHoMwjN0SZBBva02idScRtJyVRf7jJg6YAkrJA2Kru-Go-VQ3N3RKqt9oYCHAiBetbPQ-Q275IiWop48AEPXbUy8QpckdZAOQZLEH3zHZ17iKvQF4m34QUaECAmtpUt5eyf2OLMqvHv32FenDZbUMJOMdt0W4Wp2GDT_A29MqICqGenjdkpm2NPd7d89hF0kREmccu_sFcCoOpGI2GS8UjNBHtoyZCrIIyZ60l9ASTgIc47vNTDuhMrkYBvUfrtS5OkSTD0VKWb-7tNQk7tLMV_NrYDvrNMtlnMPDjOuXdzT4Y0cfD9JUXtHuxA1V6ihUqEQpfNeJzlkq5htVHDpu0vWSFDMFReYVm1)

Trạng thái tham gia

<details>
  
<summary>Code PlantUML</summary>

```plantuml
@startuml "Biểu đồ trạng thái suất tham gia"
[*] --> DangKy : Học sinh đăng ký

DangKy --> ChoXacNhan : Gửi yêu cầu
ChoXacNhan --> DaXacNhan : Ban tổ chức chấp nhận
ChoXacNhan --> TuChoi : Bị từ chối

DaXacNhan --> SuDung : Tham gia lễ hội
SuDung --> HoanThanh : Hoàn tất sự kiện

TuChoi --> [*]
HoanThanh --> [*]

state DangKy
state ChoXacNhan
state DaXacNhan
state TuChoi
state SuDung
state HoanThanh

note right of DangKy : Đăng ký mới
note right of ChoXacNhan : Chờ phê duyệt
note right of DaXacNhan : Được duyệt
note right of SuDung : Đang tham gia
note right of HoanThanh : Kết thúc
note right of TuChoi : Không được duyệt
@enduml
```
</details> 

![Biểu đồ UML](https://www.plantuml.com/plantuml/png/RPB1IWCn48RlUOgXHw4lu45ABLWeUB47GJmisxe9RREbcnnwBk9118ju414i8cAbeE1fWtZ8udlCcpYnCLiNBxlycMycC_-aaQbeelHe2BMcG3FJKCpHN86QOBwG2IXk5m8oZVcZ8X6D815HZHrj7KEzlWEjI2QTAMn36yr539cGd0eKCyeSs0_6VDoXkpmzZE9z7ad2zz2i14pjKaEC-PDcPTJNBTacVHMQQuWvckUOVjJC62JzLhAQsDLq85mMcdENzlAJDXUkbqtmGBUqJ0Zi-g5WYEOKYBqHp0STrquZIOZaRiZKthjUd1SPcZSOa6LdaZ5_g-F96HPomWaZcrNVs-L5sNc8_jNhgclX-_KYNC2OJ4bFHC8Lf2VbFehBtoN02Csjg72Roo21vWx6t2wXfwSqaQhGfNEkyDShceVuVpJOIXor4bvCXTeqjOFvfoBGvd652hliSFjEnOfvvUf6N_RewR9l)

Trạng thái đánh giá


<details>
  
<summary>Code PlantUML</summary>

```plantuml
@startuml "Biểu đồ trạng thái phiếu đánh giá"
[*] --> KhoiTao : Staff mở phiếu

KhoiTao --> DangDanhGia : Điền tiêu chí
DangDanhGia --> HoanTat : Nộp đánh giá
DangDanhGia --> Huy : Bỏ đánh giá

HoanTat --> [*]
Huy --> [*]

state KhoiTao
state DangDanhGia
state HoanTat
state Huy

note right of KhoiTao : Phiếu được tạo
note right of DangDanhGia : Đang chấm điểm
note right of HoanTat : Đã gửi thành công
note right of Huy : Hủy bỏ
@enduml
```
</details> 

![Biểu đồ UML](https://www.plantuml.com/plantuml/png/PP6nIWGn48RxUOgfXNi12pb4y40GmUl48fwtIS1DZdDIR2a-W5fQwNA881nOM6qAYno-nxo94vR0kXOBCvll3___PtfBQasXle6BlKkSJ0xmn7WxLnxtyPnKLM7DyGLNndBt7G3AQIQFbDFocMEhXDuzMevt3iccZu0BaxOm1B9WvfMRAnBubEFp2dTFgNK6jKtjVpOqmXroVFY3GRaZCs8PCbTca32qB0dwRUYo_rDib2qq0CxBjBRQ4FfgKC5Pdrii_7not2oGk6lz21_t8Alav-wj5fsKSb-F12L3XjC6DSUjHJBfLL8kqfVJ8xxlOiRnlS4hQGIcItSjR_OB)

Trạng thái tài khoản 


<details>
  
<summary>Code PlantUML</summary>

```plantuml
@startuml "Biểu đồ trạng thái tài khoản"
[*] --> TaoMoi : Đăng ký

TaoMoi --> HoatDong : Được kích hoạt
HoatDong --> Khoa : Vi phạm / Bị khóa
HoatDong --> BiXoa : Người dùng xóa

Khoa --> MoKhoa : Ban tổ chức mở khóa
MoKhoa --> HoatDong

Khoa --> [*]
BiXoa --> [*]

state TaoMoi
state HoatDong
state Khoa
state MoKhoa
state BiXoa

note right of TaoMoi : Tài khoản vừa tạo
note right of HoatDong : Đang hoạt động
note right of Khoa : Tạm khóa
note right of MoKhoa : Được mở khóa lại
note right of BiXoa : Đã xóa
@enduml
```
</details> 

![Biểu đồ UML](https://www.plantuml.com/plantuml/png/NP8nImCn5CVtV8f7Hw6uEqWv70GvfqC4SGZNUWdj9NAcujxHHH471z7Z9X51SBB1AOVV8z_4b-lZp7NBw_kzV_f-kScLuPLPbWiO9TBRrHBQUsyVm5H-NQi2Z72r1EDU9So5zkj6ZTZPpZcCn_kGSPrg2NlGthKhPEVkXp7wCVGFDJS76Xk1-FtqjicH-SW5XAJQi1u8z97G7CaJ2PS2koNiGkBjBLxhllWGJUHfnnuN8VLPmjHzO-icWApB2LIgAJBX2eotZv0BRzzoABrzeLXYudyR9U2Y3E-AAeQwp8mstnJz89LXcewfZeekY36byLp9GXZG5_yAiyWmN7lxpi6W1JtaXqgvAiXazsXFgjYYQVyiwAI5Xq2lYDudTWCB79F30J8VUDTiV4zcQegVpny0)

# III. Yêu cầu phi chức năng
## 1. Hiệu suất

Thời gian tải trang ≤ 3 giây.

Thời gian phản hồi API ≤ 1 giây.

Hỗ trợ đồng thời ít nhất 100 người dùng (phù hợp môi trường trường học).

Tối ưu hóa hình ảnh và tài nguyên tĩnh.

## 2. Bảo mật

Mã hóa dữ liệu nhạy cảm (thông tin tài khoản, phản hồi).

Bảo vệ chống các tấn công như SQL Injection

Ghi log đầy đủ các hành động quan trọng (đăng nhập, đăng ký gian hàng, chấm điểm).

Backup dữ liệu định kỳ (hằng ngày).

## 3. Khả năng mở rộng

Kiến trúc module hóa, dễ thêm tính năng mới (ví dụ: mini game, bình chọn).

Khả năng tích hợp với hệ thống trường học (portal sinh viên, LMS).

Dễ dàng nâng cấp phiên bản.

Có tài liệu API & hướng dẫn đầy đủ cho developers.

## 4. Giao diện người dùng

Thiết kế responsive cho mọi thiết bị (máy tính, tablet, mobile).

Thời gian học sử dụng ≤ 30 phút (phù hợp học sinh & giáo viên).

Giao diện thống nhất & thân thiện, màu sắc trẻ trung.

## 5. Tương thích

Hoạt động tốt trên trình duyệt phổ biến (Chrome, Firefox, Safari, Edge).

Tương thích iOS & Android khi truy cập từ mobile.

Hỗ trợ trình duyệt phát hành trong 2 năm gần đây.

Tối ưu cho mạng chậm 
## 6. Độ tin cậy

Đảm bảo Uptime ≥ 99.9% trong thời gian diễn ra lễ hội.

Thời gian phục hồi sau sự cố < 4 giờ.

Backup dữ liệu tự động hàng ngày.

Có phương án dự phòng (ví dụ: truy cập offline bằng Excel/PDF xuất từ hệ thống).

## 7. Khả năng bảo trì

Code viết theo chuẩn Clean Code 

Có tài liệu kỹ thuật chi tiết cho từng module.

Hỗ trợ rollback khi deploy thất bại.

# IV. Công nghệ

Frontend: ReactJS → xây dựng giao diện người dùng.

Backend: Flask (Python) → phát triển dịch vụ API.	

API: Chuẩn REST API (có thể mở rộng GraphQL sau này).

Cơ sở dữ liệu: MS SQL Server (lưu thông tin tài khoản, gian hàng, món ăn, phản hồi, điểm số).

Bảo mật: Xác thực & phân quyền bằng JWT.

Thông báo: Email (thông báo duyệt gian hàng, kết quả chấm điểm).

Triển khai: Docker 

Quản lý mã nguồn: Git + GitHub

# V. Yêu cầu thiết kế
Mô hình kiến trúc

Hệ thống sử dụng kiến trúc 3 lớp (Three-Tier Architecture):

Client (Frontend)

Xây dựng bằng ReactJS.

Học sinh, giáo viên, ban tổ chức đăng nhập và thao tác qua giao diện web/mobile.

Gửi request đến API, hiển thị kết quả.

Server (Backend - Flash API Python)

Presentation Layer: Tiếp nhận request từ client, xác thực người dùng, gọi service.

Business Logic Layer (Service Layer): Xử lý nghiệp vụ (xét duyệt gian hàng, quản lý suất tham gia, chấm điểm).

Data Access Layer (Repository): Tương tác CSDL, thực hiện CRUD.

Database

MSSQL.

Lưu trữ dữ liệu như:

Tài khoản người dùng (Admin, Ban tổ chức, Giáo viên, Nhóm học sinh, Học sinh).

Gian hàng (thông tin, chi phí, doanh thu).

Phản hồi & đánh giá.

Lịch trình lễ hội.

Kết quả xếp hạng.

<details>
  
<summary>Code PlantUML</summary>

```plantuml
@startuml "Mô hình kiến trúc"

package "Client" {
    [ReactJS]
}

package "Server" {
    [Controller]
    [Service]
    [Repository]
}

database "Database" {
    [MS SQL Server]
}

[ReactJS] <--> [Controller] : REST API
[Controller] <--> [Service]
[Service] <--> [Repository]
[Repository] <--> [MS SQL Server]

@enduml
```
</details> 

![Biểu đồ UML](https://www.plantuml.com/plantuml/png/SoWkIImgAStDKL3oFRn58UFmchmCXUpCXxlsvocK51tUbQp4nLMGc9oTc9wgeEISavcQLwAaKCsb00JHGQc9oILUmR5SjKXgWbEBobABu6gSy_DAYl9pSbABOY428FdCvDHOc145-SMP9Vb5bM1JKX9B4fCIYu76k41PS8DyWnM20tqK8CQ35SFjLx3HrRL3iKh1IY78DJX4mJ70amj97AeIuGOO2oA1wXma3aGQmmrS3gbvAS2Wum80)

## Mô hình cơ sở dữ liệu 

Cơ sở dữ liệu – School Food Festival

Cơ sở dữ liệu sẽ bao gồm các bảng sau:

1. Users: Lưu thông tin người dùng của hệ thống, bao gồm tên đăng nhập, email, mật khẩu, vai trò (học sinh, giáo viên, ban tổ chức, quản trị viên...).

2. Students (HocSinh): Lưu thông tin học sinh tham gia lễ hội, bao gồm họ tên, lớp học.

3. Classes (LopHoc): Lưu thông tin các lớp học, là đơn vị để lập gian hàng.

4. Events (SuKien): Lưu thông tin sự kiện lễ hội ẩm thực, bao gồm tên sự kiện, địa điểm tổ chức.

5. Booths (GianHang): Lưu thông tin gian hàng của các lớp, bao gồm tên gian hàng, mô tả, trạng thái duyệt, vị trí trong sự kiện.

6. BoothMembers (ThanhVienGianHang): Quản lý danh sách học sinh thuộc gian hàng, bao gồm vai trò trong nhóm (trưởng nhóm, phục vụ, thu ngân...).

7. Foods (MonAn): Lưu thông tin các món ăn mà gian hàng cung cấp, bao gồm tên món ăn, giá bán.

8. Votes (BinhChon): Lưu thông tin bình chọn món ăn từ người dùng, liên kết giữa người dùng và món ăn.

9. Reviews (DanhGia): Lưu đánh giá của người dùng đối với gian hàng, bao gồm điểm số và bình luận.

10. Transactions (GiaoDich): Ghi nhận các giao dịch tài chính của gian hàng (thu/chi, số tiền).


<details>
  
<summary>Code PlantUML</summary>

```plantuml
@startuml "ERD - School Food Festival"

entity NguoiDung {
  *NguoiDungID : int <<PK>>
  TenDangNhap : string
  MatKhau : string
  Email : string
  VaiTro : string
}

entity HocSinh {
  *HocSinhID : int <<PK>>
  LopHocID : int <<FK>>
  HoTen : string
}

entity LopHoc {
  *LopHocID : int <<PK>>
  TenLopHoc : string
}

entity SuKien {
  *SuKienID : int <<PK>>
  TenSuKien : string
  DiaDiem : string
}

entity GianHang {
  *GianHangID : int <<PK>>
  LopHocID : int <<FK>>
  SuKienID : int <<FK>>
  TenGianHang : string
  MoTa : string
  TrangThaiDuyet : string
  ViTri : string
}

entity ThanhVienGianHang {
  *ThanhVienID : int <<PK>>
  HocSinhID : int <<FK>>
  GianHangID : int <<FK>>
  VaiTroTrongNhom : string
}

entity MonAn {
  *MonAnID : int <<PK>>
  GianHangID : int <<FK>>
  TenMonAn : string
  GiaBan : decimal
}

entity BinhChon {
  *BinhChonID : int <<PK>>
  NguoiDungID : int <<FK>>
  MonAnID : int <<FK>>
}

entity DanhGia {
  *DanhGiaID : int <<PK>>
  NguoiDungID : int <<FK>>
  GianHangID : int <<FK>>
  DiemSo : int
  BinhLuan : string
}

entity GiaoDich {
  *GiaoDichID : int <<PK>>
  GianHangID : int <<FK>>
  LoaiGiaoDich : string
  SoTien : decimal
}

SuKien ||--o{ GianHang
LopHoc ||--o{ HocSinh
LopHoc ||--o{ GianHang
HocSinh ||--o{ ThanhVienGianHang
GianHang ||--o{ ThanhVienGianHang
GianHang ||--o{ MonAn
NguoiDung ||--o{ BinhChon
MonAn ||--o{ BinhChon
NguoiDung ||--o{ DanhGia
GianHang ||--o{ DanhGia
GianHang ||--o{ GiaoDich

@enduml
```
</details> 

![Biểu đồ UML](https://www.plantuml.com/plantuml/png/bLDTgzim37tthp3tST0_C2wNhdEpZdumbj1taPfOa5WbTGQbtN-VCyMUcJEM2tsGZfHpZYLrVNFGkw5hvSlskv8hMTQ6g9K5qKKM-kRm1xGlGcZhqDtbgHa8rM0R-H1IVeZfLoK_IhHElhv-sx-z-LgbhGBRd0nSVUdcUhIDXu_WzWQ65DfsW6qAd06hdluWFwFyZkeIhM7nAScb3tJrjGGl6D-HDpL7onymAyUpx-7I744vx55R9k1ube1BwLCLWaBTpN5-GR0x29CEsVBNPZwAw2DIfukX2jAywdr3PS2lzwvTMZdxxU2SOzzjpHa3Vx0UuTnxji9WCZ3a5JuE_njlYsOdToJxoRBs6EQwENqw7Vuyy7Bt1aRaeclie4saDjxzPqEJMiXomVoF4XMZnGHE51HOumsmm9GiuLymol7oIcBKfwFxmm3s7yT82cl3DaBsdi4U232o9CCjgKBzrt3vTENpkLhH8t8AllG93hUJecdpL0vuTfiY18ixU5CYZZh0OUlYTpr3i_vfYP7-FtYSlH1hRIz3rufV)

# Giao diện người dùng 

Giao diện người dùng sẽ bao gồm các trang sau:

1. Trang chủ: Hiển thị thông tin về lễ hội ẩm thực, sự kiện đang diễn ra, gian hàng nổi bật và món ăn được yêu thích.

2. Trang gian hàng: Hiển thị danh sách các gian hàng theo lớp, cho phép tìm kiếm, lọc theo tiêu chí (món ăn, giá, vị trí...) và xem chi tiết gian hàng.

3. Trang món ăn: Hiển thị danh sách các món ăn, cho phép người dùng xem chi tiết, giá, và gian hàng cung cấp.

4. Trang bình chọn & đánh giá: Cho phép người dùng bình chọn món ăn, đánh giá gian hàng, và xem kết quả xếp hạng theo thời gian thực.

5. Trang cá nhân: Hiển thị thông tin tài khoản người dùng, cho phép cập nhật thông tin, đổi mật khẩu, xem lịch sử bình chọn/đánh giá.

6. Trang quản lý:

Ban tổ chức: Duyệt gian hàng, theo dõi sự kiện, thống kê kết quả.

Giáo viên/nhân viên: Giám sát, chấm điểm gian hàng.

Quản trị viên: Quản lý người dùng, gian hàng, sự kiện, dữ liệu hệ thống.







