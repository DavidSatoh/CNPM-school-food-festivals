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

![Biểu đồ UML](https://kroki.io/plantuml/svg/eNptUbFOwzAQ3f0Vpy7AULEjhsJSJCQYyg8cjuNYii8ltiMhxIg6MTAwMMJWmFC3ZmDIl_hPsJ00ohKT7-69e_fuPDMWa-t0yZDbqoa5E8YO8eTCt88cjKICbIEapMIJoIGFdZmgkXZVdBsNxUhOnBuBekeYq-69gkZ1n3QcyB_Ux4MW5vmOeI4E1revwIPamifCdS0H-CzTihg7gEu__QmOfPuFcEghccC7Ddy50B6qq9DuSB6xtAycTqej4-FNteQwqKdk0K4Ft0iyFGn5VRryQhJK3z5F6TcFfrvWqf7d-1vcGys0PLBHNgyM8_riCSDnwphx7l9oGQ6vuFqiFSx62QM1EkoBt1VlC5ZutAeLBksXG6P_f_pEE7dNS-3Bpg94RbmSbCYoC1__C7P0voE=)

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

![Biểu đồ UML](https://kroki.io/plantuml/svg/eNqVVkFv2zYUvutXPOTQnoL9gR0SO05aoMtaux0GDD2wEi0SlkhForwFWw7DMOwwDGhR9FAUA-oWPaTY0A7dLjaGHRTsf-if9JGUGUqWs8wHmfrE7_G9j-89cq9QJFdlmgR7blTMuMhITlIoCxqSgsK3AcCAhLM4l6WIhjKROQweTG4fjyaT4CzwGEKq_ul3eMzUZHY6SEqqKQmdKlASco1DxHMaKi5FEJBQ4fSjkhaqGU9UGVGxfrtPSeo-kOm0GX-ex81oP0o52jEW4NPvdnedgebfgsYOsuxbQ9JeEBEnFHZu1aufQLF69UTEkNSrHwHHzznUy_PU4H-EGvklhIsn_76vV7-KeAcjx9AB44qpYjQ3StifZ3mItPMQxMUPaNm4uQOkgH1vtv6txd_5kuoFqz9xtuICClwaZhzdE4b3Badfj-Y6vq3siAgGRbUIGcScCGDVS-1tQx5IqVhxrbUFqz6kjqgl3MK7eGyiE6xe_p4Zwh0Zo8JXTZ5Vf4OqXnKYMVkvX9voxjTmhaK5Y54F_6npLbMtBcegFcOkxJiNrcE2hX0HfEKTMBs-bEiE-fEzitu3NZOQ0ahMaD95UP2GXoY6kcTG3mAtmb3pp94rtUiQGKfdDoXVQu_SK-vAZ0SQmN7N5ZR7HpwFnpDbRDzWW91kuJbS2Bt6Cvap14lgLVw7ir4IOkTr9xbafUYlRNVfHDJmDKCTTzncwEKsFkKneLVw8h9SGj3CXhT07tusXv6j4ET7Ad_gOENby4VXG2MisLfF1xHsCJeVMOfVW_HJsd4BOzamDvp1c-524x_NSVIStU2Bo-pDBqhayGSXecTn9OqYH2k3Q_1Q9eoZOo5BvM4uI6aZzFVxnYgHuLK2YfL3PLSe90V6UJ5iTSjdKRcCn-t8sX0vy3I5p2N6olth8X_SBNu3lylXU7u1aYntxnmZYp4yrSS5sZkmkzJNSX46pkWZXE83c9gY7mGfWsN6-abEKHVnYN4pZFc7xYJKh1JMeXxlvBud1Aa8H4Z4KPfJfNfk7Inequ99xlgmtBXWTUyyevVubTzWyWROFgSJecFP6DE3s_dh9yvGI-yjD3dhaKChDx0Y6MCHRgYa-dChvjPcRI-yjGsFzUk_r1cvODxA54cYQXPi42F-eSK2oCZJWpg9whxkDyn36hq_uzpc3ibcN-9Tq9_7uOvkHtjuzYH2xF_Tzl-jfkNcY6325oPrphWYC5JG2_3Ewa1m4VC_C5gbkr4fdYq0gbsF2MB-bTVQp0oCUwPmg5_QDu0kawe3KblHRWRurvb_Iy7Rz-c=)

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

![Biểu đồ UML](https://kroki.io/plantuml/svg/eNp9kr1OwzAUhXc_xVX2vkOVij-pYiAUsVrOxbGS2JXtFCHEVCEGFiomNhYGJNiYaiGG9EX8JnXSEhEE9WDJx-fzPdf20FiqbVUWEMXCu3kFq4V3jzAxCCMaJpZ598pAruaSw0GFxkaEmFzIKdW0hMoga2zXBMKIKcu5VpVMR6pQGuJJcnS8lyTk5icjlf0PGAue2SS_iosKG6jACwtWgW50SIVGZoWShFBmg73NQ0ijUskLhOjQuzuwIfNC8mhb5DtjdI5l2Ks_QidWSEi9u2cZzLx7iYAaOBN4maCeCYY7OS6ohKx-bipssVgpm-2ECu9uIeR6Eh20H8KLGS363Gn9VkIu_PKrbJ0JUs1-nb16aJ9DZn75Pm1dY8WF_NOU15-t4wS5MBZ1c63tvcFg0Gu5J24a6kld3E7dRuvWmxDdsqtIhijT8MfWtkrgkw==)
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

![Biểu đồ UML](https://kroki.io/plantuml/svg/eNp1kT9KBDEUxvuc4jH93mGZRVERm7hiGzLPmTDZF0leFBGrRSxEcLHyABaCvbBTuhfJTcwss7JTmCLFx-_7EzINrDzHhYWiNKlbRtisUvcG84AwU_nSTeo-NdBmSTVIjhUSF0KE1tC18moBMaDuwXsB-ZRKt7V3kaqZs85DOZfHZwdSiod9Dzn-z3Bq6oZle1faiL3J4hUDO_C9DpXxqNk4EkJpznhxlLoXDcFQA9zk6NqoAlTYTRWiNyiqLW7Zp0ylbkV1MfTv5hfngxts6h4hQ-9mG3TiDB1iYHOj7NhxiYsefta52v98UbPlLwzeSt1gFS2O-c1rWn8zhJjWHzxeWzrXSuu4f_GwHCaTcfeePurY0_9ixBSpyr_6C6hBrsA=)

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

![Biểu đồ UML](https://kroki.io/plantuml/svg/eNp1krFOwzAQhnc_xcl736FKBQIJKkEoYjXOYVtJzlVsgxBi6sDEUPUFQEwMTGxETOmL5E2wWyo1Qz14-PV_d_-dbuy8aHyoK-CZ6dtFgPWyb1cwcwgTET-p-_ZTAq0XpOAKRc0Zc6WhuWhEDcGhTK4nBvFlQpaqsYGKia1sA9ksP50e5Tl73mfI-kPAmVHa5-VjVgVMUIV3HryFJulQmAalN5YYE9JHO5_q7ruGmPBVgjOkOQi3CclYsgpSFQI_6dsX8NG1JMX_O--C84vQ_3wQVN0vKCMIdPeWXLHOuSChMLPW64OI1AbmuvvaAybW-YP-wgrSMUvYAy7xHinOO2BusI6FN1wMvjJQ6u5dbge8NvhwjFjcxu2lLaWBYTQaBB5qm0xDadd1pw6KsjFSEY_iD026xNA=)

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

![Biểu đồ UML](https://kroki.io/plantuml/svg/eNp1UktOwzAQ3fsUo-wrrlAlKh8JClLUA7iO61hNbORMKiHEqgu2VIg9AbEAiQuQpXuR3IRJ0laNEF5Y9vi9mTdvPC6QOyzzDIJQN_W6hO2mqZ9hVkiIOG0ibepPAWa7Ngpi5ItFwFix1OaWO55DWUjRwu4Z0Aq5WCpnS5NENrMOwll8MZ3EMXs45hiL_xEutUoxXt6FWSlbUiYXCGjBtXFItJMCtTWMcYEED860ryystP8yJ9PUv5n-HAAverGMtRRuVCYhOG_qR0BqaGNUsFOwb6BLlUPhKwSluYHUv7YoSnRljaZqobWYDjnbJ1-ZlPC-orzSAlL1kjzz3x1zsuJZyVFGTqN0mg_ZUdr8fORkeGt83msW1skh6oZQ7ySHpqJhTsKwqV92Y-k4p1Imc_Lx2qnWsq5tGI2Gsg_RP5IOL33tw_U4LRtLk9An-QUdn87O)

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

![Biểu đồ UML](https://kroki.io/plantuml/svg/eNp1kr9qwzAQxnc9xeE975A6BBLon4Ab6CpkVRZ2TkGSA6F0ypA5lO6lW4YOhXYSnZwX0Zv0nDiQhFaDhk_f7-67Q33nufX1rIIk1TGsathtYniBqZMw4HSJIoatANytUEHKEXwMr52aMOZKjXNu-QxqJ0ULPDGgk3JRKmtqzAemMhbSaTa-HWYZez5l0Pj_gGutCp-Vy7SqZQtV8tGDN2BbHXJtpfDaIGNceLInl9GAO7izirHWyFFVEpJRDGvw9L5BlXR9j7GTh2ZLdesleTwoTeWK5q31UaGr-dyahUyN8cU5NSmadwTRfNF2LiHntMI_mPtCGsibbw0uhk8oae9r3CM3BjVNM1xI9BfpYviAqvk5IIJG2AMjjnklx84dlkQDQ693HveonaTppLNunXZakPUl5vQ1fgEjacuv)

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

![Biểu đồ UML](https://kroki.io/plantuml/svg/eNp1kcFKxDAQhu99iqEHb_sOuy2Cgopu8QFCmm1C00lNJkIRD548-wai7M2DiKctngq-R9_EtKvLdsHc8jFf5p_J3BGz5CsduVJhzSyrwDvBmRNwF0E4CeNlYY3HPDXaWEius9OL4yyL7qM9Bw39J5ypQlJWNon2YpC0WBGQATtwyJUVnJTBKGKcQvkir1S4DJRhoQXEJ337CCT79gmL-LfJX8b4yvebVwTdfQF1zwpKaQYQA3NwzpAVYsF5CENT7VJ2Lwg3vunbB4QjuGUKyHYfe97SaOGmVtpv1h5k94YS5CRVsFKDK1VkjSNRTbWMGdDf7z70KWX3qaAO2pqP1rAtXy-FC7OP6xnnh9nsIP0B3obbwUnvHZ2-PReYh4_-AQCltNg=)


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

![Biểu đồ UML](https://kroki.io/plantuml/svg/eNptkbFOwzAQhvd7ipNYkldIBiq6MKBODO1oJa5txTlHjgOqCBNCrDAyIBUxI4FgIRVicNX3yJvgdGopHiydft93_38e1Y5Z15Qa6kJRxSwrkWVOXSi3wCvAcE5YVghrGsrHRhuLZ0pIN-Nam0u4BmgnYvPWr54U5v6LRAtbIiTntllg1nevFcp-dYcu3A8kUlBzjMb-A51fKiyk6bsXOo6DzgmjGa_jMDVZ369vSCDJAZAC1zXHaGJ2tcJ_7zHS__ooV3NojyqmubCcU3u646WFZOqfs235nv2BHeRKprwMT_1n4DtFqPvV7RDtUaUHmlCMUPrlkHfPrwz7DSJG1Hc_DZbNYCROw9JMBaNgN3zFL6NSqew=)

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

![Biểu đồ UML](https://kroki.io/plantuml/svg/eNqFUj1OwzAU3n2KpyJxiHapYKADC1sZLdeyLTt2SJyiijBViKFComJiK6oQCwxMSIkQQ3IR3wQnJVFRU_Bi-Xvv-_Gzh7HFkU0CBb2zZAY2Kl41B-LyFwwjl98RiIUHLMcBMIF7CMVS6BBH_oyJFVNhZ3CFwK8jTCSLTKInx0aZCE4F4_acKmUu0TVCaYdcimp71C_vy7lmoLnL3kLgLr_1PS5fajZA6UGIFWURpbrSaCsp6o-LJ1If3_1WrARIbly21oM9bo2PLD5bFJTLbyrLR7GhbRuccLEJpaFcNtS96mMaVGoLwptBxj4aSOFF9a74yONzXQOL37w_8rvsw0KcuOzZtoVd6XowP8E7m_ekly77snDhGWuYFisIeTXOajoP4p8LbFMPO4hdb29CNKR64r_fN_NjG6Q=)

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

![Biểu đồ UML](https://kroki.io/plantuml/svg/eNqVUzFLw0AY3e9XfFRw8he0S7GDHYpQcKjjNQ25I8ldSC-VYhykg0gXizi4NXQQ0aKiUw-nK_6P-yd-jRRCmxbMcOG-vO-9d-_L1fuKxioJA6i0kyGo2LwKBo7VTxROmfkMweNUADNT4VUI6ftcRDSmIVBH8QFXQ7gkgM8xdXwvlonoNWQgY2hxj6lzNwjkBbkiJN3kSkkuTKrLu-VIeCCYXcwjYFbfgMJ1IrwaSQ8iGrhe7LoibRa-pKTaMZmTbz_wZaYcfCbtYiZqZVJrEd98F-oI3SA9YfzPiIDlZN1RzthgiV08C-haPUYG84VgxcVe-tbPe4IJW_22s6NEqZ2szgUBenfQX8TM_Ah6kuKYFEu2VZrc6pHIC2PomkyCky-lvSV6HTdEYK6JFPcclNUvGC8GzmBgpog2WYgFhMht-TOrH_BkuJ9FcAis6KZIu2tQiL9O0K3Vt-hyNdRM4TSsfkTWfek28h8oH5_6R759JSNSd0UP78AvZ3pYqQ==)

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

![Biểu đồ UML](https://kroki.io/plantuml/svg/eNp9kjFLAzEUx_d8ikcFV_d2KXZohy5Chzqe13AJvXs5rrlq8ZyKOLhYxKGbpYgoFhV0MWOK3yPfxJcKpbR6N7xL8n_v_0serz7QQabzJIbKUT4CndkXFBA68xhAU9qZgqG0z3jg1wn0hfuaqwpjg77ENMiCBIJQy6HUIzhnQN9hEPajTOXYa6hYZdCWkdDHPI7VKbtgrPjPs2Cri7Dq8mY5xgiQThcpCGeuQFOcYFRjxV4axDzKOMeitaEUrNq1s3C1faefvZdkq8gXa2XIakdwBT37KcFnzzQsJ85MCR87c-nhU0kGW6iWdGaMq4NrivaD8rXELYtycIMWDwnleq-EXOgemhJzCIVd7DKbQv62BNc1A9LKIU1nFuuyM_ukYR9SL6J_2u0fT2t_v-U0A868lpeVQLs8gROvhj5oZ-6oPVQ3T3dxnQ2VIGKzsWuPWvnQqJTVOfZogn8ATIdINg==)

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

![Biểu đồ UML](https://kroki.io/plantuml/svg/eNp9UrFOwzAQ3f0VJyH1I9qlagc6MDB0gNEkUWwlPYfEKVSEqQNDFyrEwNbQqUMFSLAkqhhc9T_8J5xSIbUkIoOj8917796Tu4nmsU5HIUsCiRGP-Qi4o-VY6gncMaCvx53Aj1WKbl-FKoYz6Qt96YWhumH3jGU9jqBt-QyOsOXKyVhFydrbx-0UfUBhi3UE1HsATecc_Q7LTiIeen7seZgNDjoZa1-Y3KnKD_qZhYRAKFsssdOgRMMrDW46IQoNvqS-MItK4A_rqZD7TRACW3xruE6JFG4P8I0C58K8Ijjmk5yMbTkDHZt1nb5feawENCS7HLZzWz4dIercQ-EpcM2XBC1pJ6xAL5CQdQgkCWBdaED3U6wuZkew5nhsuYbQbPacDpFAJExOK0oU_4bUoulDS7_4ZiNUUT5ULiO4MrmiwHJV5x_agnotCHfvKcViy7ej6YaHpCLW9dCl9_kDDZA7ng==)

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

![Biểu đồ UML](https://kroki.io/plantuml/svg/eNqNkj9LAzEYxvd8ipcKfojeUuygQweLDjqG63EJTd-cd0mleA7i4OCiOAv-oQiiWKGLPZxS-j3yTcylIuXaA29IyJs8v-dJ3mtliqZKDwQ0unoEKjVvyCC0xQuFrrazZ3Q1W1zDkJtXbBCS9TkmNKUDoKHiQ65GcEbAfTs07Mep1NhrSyFT6PCYqeNICHlKzgnJ12k58eakOb-ZX2IMyOzsPQFmiytQbrzFOCD5VkJFFKdRhPneyk5OmkfmMfTLTzeZBw59JkuPYLNZ87cozHf1eAXc9jl8HOXKZurCKY7_Mtln5gnhRI9scYGA8WJii3sOPfPlb1Nx2mV86YOQrArr6C7ZWAPzTaq8U4XcWUy0F3-4bv6J6rgHVIIoFdsuhy3GYUm_c7FLveAOrdctDpdPz8pthGwzIqjrvExIK8Ke-_V-AN2EKck=)

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
```
![Biểu đồ UML](https://kroki.io/plantuml/svg/eNqNVctq20AU3c9XXLxqwRFVH3ZqcAmkkIBDN_Giiy48etQaLI1caxTqZcmii1JIVtkmeNWCIYWuZEoXMv0P_UnvjKxoJD9ibywx95575p5z7KNI0ImIA59QW4QTaPS89M72GkAjGMZuJMgYz5nNxpQLaJwwGoLDssVXrkpiVj0_xRMQXra45kNVEE0j4QbEoYJaNHKhcXz-9kydOBYh3S4sr5aXfAij9A90u4SomXDwBpE7YBrQn8RTsLNkPoaP4SSA5XVRLgmzCypcSaLa99xAWCT5hSOX9DfWC8a11g_8CVL8DiL9yZvgBpT5TThfXvWbEOAoASMvS37ET0nMJGR-hw68MOAkW8zZZtCSz-rOJP_WEV4a0ENelwGICdVgCPUF9EtUZDcbg4_LJICfEsixOvDKgLN_97HOQqS3DEmHWTLjquOBC25ZvjsWHGg8Wga8R5mB4z3nHPwV3C33wJageY-ro9SIFEhtlChL7kII0hl8lphS_V92vtVakxKpA4fFHlWN3lWpX4n5mhrFaqwUB5UbX6cs9SrnmM-w9diLp7hxqVSW_OVy8di9ztT10Z2aBKP8cYsSBTdLOhS3DhfoNll2wzYSwbpTpmjIod8K7dSF8i6XO0TbeJEbt-LyMi9KufGGyGzPTN6yIzYm5uZdjrvNW9VAmDsSUZ-2HgrpZXNbIvA1xCf5a0F0G9aMbGIYeqirgE-xlEH3Us2_KmLaXR6R1mxt9h1_WNBO67W3Ws_20jn3Vn7T-ezlOLO1p-Xa-1nuUc8dYZX8exgMBv8B6NxnXA==)

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

![Biểu đồ UML](https://kroki.io/plantuml/svg/eNqFVE1r20AQve-vGHSu1bpNvwwuIS4kkLYU4h_g1QfWYnulyqsQH0soOZRCTQilp9bkUBzqQ6Ani9LD-o_sP-mMZMVrNaG6SNa-mTfz3pN7vV4y5FJloyHbHSue0hM4e8LkpxmspiY_B5XqnzICZfJraMCRwOdjoa8kqIiPoC-4wxj3VZyCszl0gI9hrLIglIol2Ff4IkEicPYFjyFAgrMSlInt8wM8wdYmn8p-2WUyVuGIBVxxj49DcDpHL18VJ4G3XbrHJY15AT6Wz_0CE6d9xtptWH1enco-yMgsFwm024ytp4PGC5yhBU0XXpv8G67LEbeaWnBaTxxzFdKwtbKHLrwpeyr9XcAgis3yUt6DEb5T-NMs5xnLBMHLRVrwyIV9ky8Ebql_IYkS8i6-9e7ljXoEXgt2XDgkg0Y06xbtphClCTxoWKyPscos_yh4lyEUTvTML2S-9lkQ2nWMDxV0ra6AqMsEhmgMA7yqadYKPOEudKIYkkjPUYU0m4BfbEFY2pyGKEVrwVMEH9DwsiD_SPmp4oC26YWMWDhElw9Lbf5D7bnQTWmdY5O_J9gXcTutV6NdS-_pWbwuC2VgC1GlLrS9t4I00L9vPgDq8IFG_SpuS9Yz0sfkn25ctmtr2XheZWOirzLS8Ue2gd4dC0w5JvgBEWWTYk2r_kTPFQT0_kwxRNp8TYz926hy-VxUuPuDUqCqbDuBTUx9pwh9EViFrpvljKIc6ZlgNZeaGPiupfdgE0NWN6q5UzPKBv9rzy66hv9YfwH5NuiK)

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

![Biểu đồ UML](https://kroki.io/plantuml/svg/eNp9VE1r20AQve-vGHS3qJr0y-ASkkICCaXQ_oHVR71LrJUq7Yb6WHLIoZeGUHpNyKG41NDQnixKD2v6P_RPOiPbzUqOo4tA82bevHkP7ZSaF9qkI_B2ZV2dGpif19UF6MJ-VwJ0Xd1AD14K-zOFoeQKhL1UQ48xHumsAG-tArwEnfCU5ThXRjLnSoO3L3kGMRKcqQZhZLt-gBXQoq7OlyPKcamTlMVc85CXCXh7r18cNZU4bLfuIjWu-RkibJ9EDSYrhowNBjD_ND9VQ1Cink1zGAwYo9Wg9xwX6EPgw5vCjCFqqm-zIkXxTgNplCdcJ7Su2_jQx4s0TVrYX4jXEnewlxKORVbPrhUzkrALEX3Y8mG_rqbShW9gWupevGhGHPZh24dDMidFW3ib6H8jniUOoeewPsKuevZHwzuDUHhvr6LmxDcRixO3j_GRBnTgOocR-sAAn9UCS8WPuQ97IoNc2Ene2Z3gpBehdKQ-PEHwAe2rGr6PFI-V--iSnSrBkhGaerg4h7ifOiSbSMFJXX0g2Bd5ByehFuNCe5UtYYmKXa2rUCWusU5Oju1vJ8preXl6l-23-I7pzzabjjz3OI7hxWw-oIObcXPFsf1mKKVfDbo40RDT9zPNEOkyBhjoV4JiQSe9wJDc2t9JVIARPvr7w2xQ0rEg2Gof15nrSmoZEmx3QuAus-7JDlqFf6F_HmDNjg==)

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

![Biểu đồ UML](https://kroki.io/plantuml/svg/eNp1VMtu00AU3c9XHGWLYpHSB0QKqppKrUTVDVnAcvxIPKo9DskYkXUWLBASFQu2jRBCRVRQwSpesHDEf8yfcMeO64lJvRnJ95z7OPfMHE4Vn6g0jtA6Ejqbp1hd6uwj1CT_LkMond2ijRORL2JchHr5OYFHx5eYcAYftxjjnkomaNmgFvgUlHo4ZGPKLzwx5lIZDE_gE_GtLCCp2IyfUgQq1NmlHJU5ZlMVxMznirt8GqDVf358VkR8d5N6Hua_YowElwjzqzVdBTxmrNfD6sNqLkeQ1N3NGL0eY0V3aD-lHrroOBhM0hm8IjxMJmY-i2FmFK-5CkzHG8wdB-dlUhXmv4mghGSpMOGy9y4eOTjR2Y3ALP-WmhJf0_uyr8ctD5PDd7vYdfAiX3iFLrd05FeCZE5IZ1kzSQ7fRdsqu-fgmV7-UXiVEhRv6hTMD2we45HCwIgWwjMzMNBX9bCec5876IcJxmF-TbPeiVVgzbymshGmiwOCnhpzyKLeO7OUausN97AgoqUOzD8FVy8XYmtt18FRvkgQ6eyT2FbRbVRc78KtSYH07bErXwX2Yo1R-hv9_e-Ux0YGnb2XltWKOzNfj9ZY_hMHL-u11x6x6I11dx46OKNMs3vQjTV3yLvHOvuByAicbstbmXxnu0qVY2s9O2TZQV08tEjNi7N75_9KsgelqyU57lo11OjsVXfhwrJmwxMNOfZJjr8_U5thQcwNJ9BBlXds3h9qmR4xsWXhh-QDeu3-AXB0-Hc=)

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

![Biểu đồ UML](https://kroki.io/plantuml/svg/eNp9VE1r20AUvO-vGHy3qNI0HwaX4BQSSCiU5tAeVx-1lsorV1qF-hxKD7k0lFJ6iwmlpCSkgfZiUXqQ6f_Yf9K3kmVLSokPsuG9N_Nm3sg7ieKxSkchOgOhs5MU8zOdfYSK8ysZQOnsFl0MuDQ_P8ENdHbpdhjjropimmkVwBNE8ZCNCVS4YsylQmdP8Ageob-XRUMqmvV9qkARwJkcFg3JJFH-iHlccYcnPjq7z58cFhXPYazfx_zD_EQOIQM9ux6j32eMSNF9TNA92BaO4nQCtyi-iuIRaar1m93FMVe-WaQ2t2bhaQmogvwntStB4vJzgddBpGcXkqXC9Jbb9fDQwp7OrkWtfQW9kFB-mSnP6WHdwoExeUT28ib0cpAUeg66NZ5HNKVnfxTepNSKt_nULdy6dZnn1-cYDxXIzIsxQrKUgT7VAguNG9zCvllBFhCnGK5uU-JLhPnvYtSopTFyqIdN3jCVFJ9TOlyjm_khneig9CC4n92xMMinkWn4LO6SUPmoxHFWXb706jqrbPj1K5pMPFtubwbfmVW-iHY2tiy8yC8VvHRCOyojX8KIGbaOu10dd5J_T43qb2nrmPYDC7uFG0WsFN1Uz6YmB0E-Fc1EUiSb6526weIVa_HaaxWxp7MbhOYyd5gpeYd_f6QtoAbjurHSp9Pmv0TppkuPNhlF6-VS332MG4vzH-vZV9lobIXV3mymdUXdyoK91Upic8kqE_b2IjKmgqA28J9Q7FBW6K_sH2KE5Vs=)

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

![Biểu đồ UML](https://kroki.io/plantuml/svg/eNqFVMtq1FAY3p-n-Jj9BFPtxYGR0gotWEXpLNyeXJwcmklick5hltKFi24sLlzaUUQoFi24miAuMvge5038T5IhFwfMJpD_8v3fhexnkqdSzUIMDoTOLxRWVzp_D5kW36IAUud3GOKF0svPEX3U-SXORXETDRjjroxTDDbUwDNwbyYiltBy4YqERxKDI8FjeITytmpRols_pgpkoPOraFo2ZPNM-jPmcckdnvkYHJ4-PikrnsPYeIzVu9VFNEUU6OVtgvGYjjKwGD6i5SPYFp7q_CNexemMeLV6zfHinEvfHNGZ2bLwrFong-InDUiioYQpV-eMcN_Ckc5vBebFjYKrl19Vs6--uXqZKc8Z4YGFl8XCLcnduU0z0fAcDFu7ty080cvfEq-NrMzz272MhxKToLgmZ1xzHAM9a6iawA63cGysjEq4S0wb2auttVnlsGFGg6UEI-zS7CRVc0OqUqCB8kNyYELSfJFw9HIhNoI7Fg6KRYxQ5x_EJgSnd13V6Edem-vaeL9tkzG8DltY_ELQSsu_1u9Z7V5ZXAucBbH50DPz4QYzu-bZ9ywclnqU2ZHwdP4doRFU9QNHiXseFJ-M0HOdv-mD2VtrtCZcSDoDPWzK2smfH6rX1EOleJ2Sx6FpbMvSR9_-P9cdy3hMIUVQJcbh7plKGOsZbe-SjzHFg34RlAjWddne67lc03UoGht83if76Rf0F3gLxh4=)

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

![Biểu đồ UML](https://kroki.io/plantuml/svg/eNptVc9rE0EUvu9f8cxFRWu0th6kSGsTo6CtNqu0UAjTzWR3aHY27szW1psU6UEEiydvRhFpsaDgKUE8bPH_2P_E92Y3O2viJTx2vu_9_l6WlWaxTsI-1Br3GuBloy8DmIc5uJ-Nj0AH2fhY-tDPxq8B7Q8CstFJaL7_8GqOc6HLe0JyeLyxvtpst8ETsdfn5efmptvcWFt52GmuuQ_cLYi5p5n0K4jGirvSabvrG03oMs12mOKOcxGa-5rHkvWBSy204MqZdlVrJVzpGjAFPlmzgLZOukg3EJXbsyCXs9AgNBr_88F6PbjUEukwhN0gG32O6q1nlwuf-DZLWY99JsVLHhtQFPuzkJVuKKR5ZmRRwY-YkDCII48rhdVO-lm7ce36tnySYGAJ_fTXtnTTjwIziehL7sLzOqEfasuZJ875u_NDnNyu4QQsBF8wg4-53-F71IyScHM6SEswCUH6UfqGshNFOpgKspAHSYcyQNfpcFvOwSo26EsI58ciGx_mbeV7rD_FXJyO1sZlgl3kHMmCg9lNkW4RaRXdJ5jXNxlsy-qC5vM4UB0vkj3hU0MbuE04oijGblaWrNa4AU8Vj5WhJGT9-zwPG9wXSsdMi0iqScvsl3_hN-EuNUfZPk0BFqDtURJ5it5sPovQpHqVLX0KcAtWTVUGYAs0-w-9fvRCOUYBMDd3p9wGuA12A-qFKXE-ZwOnxCwRw_QA4Q__fE_qm-nQK9RtHihQoaMiVKEkE6xcJaS3svGZQGr6EwNpXObz40l4x-KWCpptJ1EDJMbZaEjMIB2Sm3xhK0wiopgQvpWeJnSoviYwCNJT6CYHuAqaUiU1F3mSng3JLi9yXZufX-64U4EslRRlWpiN33p1SrACpzRmPG-mJ3qSShVsGkhHZNI-soldKsPEMYqBK_mIJOyjN8ciTFb58hSTgt1s9FvDc5JRBUg4U_lkIIPA6Awn-l5QLuV1KvKZ1GI1h1QrTrr8b7wAx0Oiq99NhxF4-ONU8Eslv1wjN04OYA_VKkFZcVN8c_qK2Ob4mehWujY6bsT4zVUa8SeJdWJjX0mnAjRhS5LpiWfvA1VcngfHWeayi39yfwEyFZKw)

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

![Biểu đồ UML](https://kroki.io/plantuml/svg/eNp1k7tKA0EUhvt5ioOlkBewkJAEIgRsTCcWy2azMyQ7K8ksmDpIChESxCKIYAgiUURFqx3EYhffY97Ec5K9g-WZ-f5z-2fqY2WNVOANYa8hjJ4GEC-MvgE1MuFKuqB4tBLQFpYEHj1Id4-d7p9BrXYILUu6nQkcQBdJHzyj7wS4GciSe0Kb3G8FE0ch3Db6VVDWL0ouJMvudjlTroF5lNG3YHOjNzac8-gZesHE6Jkqa7oBhoIkRl-R5mWrWQiWZiPqyLdUy8eaxIVvisYMnwIYGn0JiC8Fy5BdJ01ueS3heKg4UVa_T1nDRw-FtCePFQgSdBzV5YFNtNEfMEBoJmFgwh9F44Y2Y7hq5SR7S4J0kuyuGO0mS4K0u4xMqycHSX3GpI_RSLhcgd_PXTrm0adHk17bMBaS4xzxFIcdRN8VScGteI7y7Trv4SLaqMyBapFc8Ptu9LriV5n-37AyV7Asf3_YNrXEfXx0WxP1EndSbafgXTyP1sglbVU8LOtyCwv1Sg4mrZPf-A1YKkjjuiN7-JX-AK6QVFI=)

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

![Biểu đồ UML](https://kroki.io/plantuml/svg/eNp1ks1KAzEQx-95iqFHoS_Qg5S2YKHgxR4E8RC2dRPaZstucui5iAcRWsSDiGCRIlYKCp42iIddfI-8iZNuutuueEmYzG--_pN6JGko1WgIlQY3eqognRt9CzI08UL4IFmy4BApEy8lGnQEPqcVcnZwDtXqIbSo8DsTqEHb6BsPIi4YJkinGDlIvghxfos2WXBKvWNGBeJHRq85TJKVAs_EL4rseLO8BdvAUxp9Bx4z-tWzV7wcg8BrLcqBXYUP3EYZfW3D3jZhc2572QVPVEthlzXouqFgaPQlIHvPiXNarh1QgQjOhUMGyZPtxWoRGf0BA5TsShDiqloelSFFzPaFoMyy7-RyRtF57t23s6zOyFpyRl6AEBGgHXKfSQguin2ks-0SYGT0Ay9xe8to4tCPMGbJCnpqghPJP1kLOJ39vBv97P2D5rKmM7r5Ppm4JWpX1I6Jv-3XSmKvROW77LDkE5Ol81Lpel_08Ov-ArQoE3Y=)

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

![Biểu đồ UML](https://kroki.io/plantuml/svg/eNplkbFKBDEQhvs8xXClcC9gIccheCCI4HViEdfbJOAmx15SbCk-gCdWVrocIggHFlabwiKL7zFv4kQ2urcWgUzmm5n8_0xWlpfWFdcwmir0tw7ae_QPYEtsai3AylArWEqFzWfMhVpLECrUI3a-dwHj8QEcS6Pm3MA-nFme51Cgf0oVjKVsJA-5FnTkkeJEt2saeKPBqvDmIJNhy_pALJgZrufcEnyC_nHZn_-fdRVxU_R3OxhLPSJDX2aRS3dG6u0iKeiiXuPupWuRIlcxpg3dSiWkBZP3LDj9derrHf0mA0s-mgE-9IFC0o_NS0F1cQvFoODPh3YdNiDQb1VczTOpzMKHFkP-x4sZ-tcKLskRNlnoK1ryNyn-w3o=)

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

![Biểu đồ UML](https://kroki.io/plantuml/svg/eNpdkjFLAzEUx_d8ikdHobg7lHI4CFKnQwRxCNd6Ce0lck3FvaNLRRwcRI-bRATByQtOOfwe-Sa-XNLrXafk5f3eP-_9k_FS0VytsgUMIm71egX1g9WPoHJbFSIFxUzBQZk3DnMmbVWKAbk8uILhcAQxlRPJ4QjqTb1Gdm5-CQmHLn8iqTqWmHDE35fVZYLMZ8LAKRWKtICjT5mkSJ5zuGGYzeAQIqvv8VrzTftoxC8a9ix1qi8cpuYHU3cOJI2OoyYySEZUgLL6CRJm9XsCmdWvQTYw3W47Cjgo8XdtI4J2qVmYPARtoQ9dddh69RA0QoQIifucp0yBvN5ZGHcchlurPyi2XBVyj-9ZSnH1TjaP9owt9Okwf9zY6QfuA61F7fvsvIEFlvG9gq3z9caU3u_xTEzx-_wDmzzk8g==)

# III. Yêu cầu phi chức năng
## 1. Hiệu suất

* Thời gian tải trang ≤ 3 giây.

* Thời gian phản hồi API ≤ 1 giây.

* Hỗ trợ đồng thời ít nhất 100 người dùng (phù hợp môi trường trường học).

* Tối ưu hóa hình ảnh và tài nguyên tĩnh.

## 2. Bảo mật

* Mã hóa dữ liệu nhạy cảm (thông tin tài khoản, phản hồi).

* Bảo vệ chống các tấn công như SQL Injection

* Ghi log đầy đủ các hành động quan trọng (đăng nhập, đăng ký gian hàng, chấm điểm).

* Backup dữ liệu định kỳ (hằng ngày).

## 3. Khả năng mở rộng

* Kiến trúc module hóa, dễ thêm tính năng mới (ví dụ: mini game, bình chọn).

* Khả năng tích hợp với hệ thống trường học (portal sinh viên, LMS).

* Dễ dàng nâng cấp phiên bản.

* Có tài liệu API & hướng dẫn đầy đủ cho developers.

## 4. Giao diện người dùng

* Thiết kế responsive cho mọi thiết bị (máy tính, tablet, mobile).

* Thời gian học sử dụng ≤ 30 phút (phù hợp học sinh & giáo viên).

* Giao diện thống nhất & thân thiện, màu sắc trẻ trung.

## 5. Tương thích

* Hoạt động tốt trên trình duyệt phổ biến (Chrome, Firefox, Safari, Edge).

* Tương thích iOS & Android khi truy cập từ mobile.

* Hỗ trợ trình duyệt phát hành trong 2 năm gần đây.

* Tối ưu cho mạng chậm 
## 6. Độ tin cậy

* Đảm bảo Uptime ≥ 99.9% trong thời gian diễn ra lễ hội.

* Thời gian phục hồi sau sự cố < 4 giờ.

* Backup dữ liệu tự động hàng ngày.

* Có phương án dự phòng (ví dụ: truy cập offline bằng Excel/PDF xuất từ hệ thống).

## 7. Khả năng bảo trì

* Code viết theo chuẩn Clean Code 

* Có tài liệu kỹ thuật chi tiết cho từng module.

* Hỗ trợ rollback khi deploy thất bại.

# IV. Công nghệ

* Frontend: ReactJS → xây dựng giao diện người dùng.

* Backend: Flask (Python) → phát triển dịch vụ API.	

* API: Chuẩn REST API (có thể mở rộng GraphQL sau này).

* Cơ sở dữ liệu: MS SQL Server (lưu thông tin tài khoản, gian hàng, món ăn, phản hồi, điểm số).

* Bảo mật: Xác thực & phân quyền bằng JWT.

* Thông báo: Email (thông báo duyệt gian hàng, kết quả chấm điểm).

* Triển khai: Docker 

* Quản lý mã nguồn: Git + GitHub

# V. Yêu cầu thiết kế
Mô hình kiến trúc

Hệ thống sử dụng kiến trúc 3 lớp (Three-Tier Architecture):

* Client (Frontend)

Xây dựng bằng ReactJS.

Học sinh, giáo viên, ban tổ chức đăng nhập và thao tác qua giao diện web/mobile.

Gửi request đến API, hiển thị kết quả.

* Server (Backend - Flash API Python)

Presentation Layer: Tiếp nhận request từ client, xác thực người dùng, gọi service.

Business Logic Layer (Service Layer): Xử lý nghiệp vụ (xét duyệt gian hàng, quản lý suất tham gia, chấm điểm).

Data Access Layer (Repository): Tương tác CSDL, thực hiện CRUD.

* Database

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

![Biểu đồ UML](https://kroki.io/plantuml/svg/eNpzKC5JLCopzc1RUPI9vEUh4_CavAyF7MyHu_bnKZQUHd6VrMTFVZCYnJ2Ynqqg5JyTmZpXoqRQzaUABNFBqYnJJV7BsVy1SGqCU4vKUovgapzz80qK8nNyUotiIQIg-czk1FiYEQX5xZkl-UWVYFNSEksSkxKLgca4QFlwg3yDFYIDfRQgxoMVw-1XsNHVtUOxSsFKIcg1OETBMcCTC0UcohLuBjgLKoHsHGQOVBrNDVwOqXkpwKADAMqRajY=)

## Mô hình cơ sở dữ liệu 

Cơ sở dữ liệu – School Food Festival

Cơ sở dữ liệu sẽ bao gồm các bảng sau:

1. **Users**: Lưu thông tin người dùng của hệ thống, bao gồm tên đăng nhập, email, mật khẩu, vai trò (học sinh, giáo viên, ban tổ chức, quản trị viên...).

2. **Students (HocSinh)**: Lưu thông tin học sinh tham gia lễ hội, bao gồm họ tên, lớp học.

3. **Classes (LopHoc)**: Lưu thông tin các lớp học, là đơn vị để lập gian hàng.

4. **Events (SuKien)**: Lưu thông tin sự kiện lễ hội ẩm thực, bao gồm tên sự kiện, địa điểm tổ chức.

5. **Booths (GianHang)**: Lưu thông tin gian hàng của các lớp, bao gồm tên gian hàng, mô tả, trạng thái duyệt, vị trí trong sự kiện.

6. **BoothMembers (ThanhVienGianHang)**: Quản lý danh sách học sinh thuộc gian hàng, bao gồm vai trò trong nhóm (trưởng nhóm, phục vụ, thu ngân...).

7. **Foods (MonAn)**: Lưu thông tin các món ăn mà gian hàng cung cấp, bao gồm tên món ăn, giá bán.

8. **Votes (BinhChon)**: Lưu thông tin bình chọn món ăn từ người dùng, liên kết giữa người dùng và món ăn.

9. **Reviews (DanhGia)**: Lưu đánh giá của người dùng đối với gian hàng, bao gồm điểm số và bình luận.

10. **Transactions (GiaoDich)**: Ghi nhận các giao dịch tài chính của gian hàng (thu/chi, số tiền).


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

![Biểu đồ UML](https://kroki.io/plantuml/svg/eNqVVNuKwjAQfc9XBB8X_IFFxHVr18ULy7b4PmhpBmpGNF0Q3X_fsUlj1lRQ6EPnZHLmzC2jg4G9qbeV7E2-E9mX2VoRVTIl2si0OBj8gaonRKENmqNcljVhUutSnoSUL978TOSrRG3kYPA1Gw75LC90ArpcKtjx0cHsUZcML8DMFNQhNNkCViGwAsz3dEV-ffgprTPUygZ3Rhx6Tjs-C_DU4lNiUV209oJljS5f83FuHQRZPUOmbgjsfyeBcwtSTRASLLZdnB8IegptpVvr8WwjHanX4anDxlAOoZ3v2SFXwO09FuZfe7g72KWYvbVaYcDfSPdwrD1uoRPZka47scPB32W2qLNyC9JvrhnNbxz3Pj1Xx14PEmbvMVyQTbHGLVRBqDGrf1fkorVWHLBrUVzEW4kNfI3AS6RYgA3gjKf47-d6mbyMLMrmRf28Bn1nGCnBtfLD2FjPFHZOgJ4lKG5Gud2JoLhuT87nfp9OnlO4_XOwm50b1Du3T4XDo9kUfkgf9mg6Ja5PoIPbrgs7OLdo5O-aGNHfw9uqCTEq9Iaf6j_CucTi)

# Giao diện người dùng.

Giao diện người dùng sẽ bao gồm các trang sau:

1. Trang chủ: Hiển thị thông tin về lễ hội ẩm thực, sự kiện đang diễn ra, gian hàng nổi bật và món ăn được yêu thích.

2. Trang gian hàng: Hiển thị danh sách các gian hàng theo lớp, cho phép tìm kiếm, lọc theo tiêu chí (món ăn, giá, vị trí...) và xem chi tiết gian hàng.

3. Trang món ăn: Hiển thị danh sách các món ăn, cho phép người dùng xem chi tiết, giá, và gian hàng cung cấp.

4. Trang bình chọn & đánh giá: Cho phép người dùng bình chọn món ăn, đánh giá gian hàng, và xem kết quả xếp hạng theo thời gian thực.

5. Trang cá nhân: Hiển thị thông tin tài khoản người dùng, cho phép cập nhật thông tin, đổi mật khẩu, xem lịch sử bình chọn/đánh giá.

6. Trang quản lý:

* Ban tổ chức: Duyệt gian hàng, theo dõi sự kiện, thống kê kết quả.

* Giáo viên/nhân viên: Giám sát, chấm điểm gian hàng.

* Quản trị viên: Quản lý người dùng, gian hàng, sự kiện, dữ liệu hệ thống.







