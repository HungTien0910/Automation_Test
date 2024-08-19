from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import UnexpectedAlertPresentException, TimeoutException

# Set up the WebDriver
driver = webdriver.Chrome()

try:
    # Mở trang đăng ký MyKingdom
    driver.get("https://www.mykingdom.com.vn/account/register")

    # Chờ đợi cho đến khi trường Tên xuất hiện
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'RegisterForm-FirstName')))

    # Nhập các thông tin vào form đăng ký sử dụng ID
    first_name = driver.find_element(By.ID, 'RegisterForm-FirstName')
    last_name = driver.find_element(By.ID, 'RegisterForm-LastName')
    phone = driver.find_element(By.ID, 'RegisterForm-phone')
    gender_select = Select(driver.find_element(By.ID, 'gender'))
    email = driver.find_element(By.ID, 'RegisterForm-email')
    password = driver.find_element(By.ID, 'RegisterForm-password')
    confirm_password = driver.find_element(By.ID, 'confirm-password')

    # Điền thông tin
    first_name.send_keys("Hung")
    last_name.send_keys("Tien")
    phone.send_keys("0812253226")
    gender_select.select_by_visible_text("Nam")  # Chọn giới tính Nam
    email.send_keys("Tienhung112255@gmail.com")
    password.send_keys("YourStrongPassword")
    confirm_password.send_keys("YourStrongPassword")

    # Chọn checkbox đồng ý với điều khoản
    agree_terms = driver.find_element(By.ID, 'agree-terms-acc')
    agree_terms.click()

    # Cuộn đến nút đăng ký
    register_button = driver.find_element(By.ID, 'register-button')
    driver.execute_script("arguments[0].scrollIntoView();", register_button)

    # Nhấp vào nút đăng ký
    register_button.click()

    try:
        # Bắt và xử lý cảnh báo (nếu có)
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        print(f"Alert text: {alert.text}")
        alert.accept()  # Hoặc alert.dismiss() nếu bạn muốn hủy bỏ
        print("Cảnh báo đã được xử lý.")
    except TimeoutException:
        print("Không có cảnh báo xuất hiện.")

    # Chờ đợi trang tải sau khi đăng ký
    WebDriverWait(driver, 10).until(EC.url_to_be("https://www.mykingdom.com.vn/"))

    # Kiểm tra URL hiện tại
    if driver.current_url == "https://www.mykingdom.com.vn/":
        print("Đăng ký thành công.")
    else:
        print("Đăng ký thất bại hoặc có thông báo lỗi.")

finally:
    # Đóng trình duyệt sau khi kiểm thử
    driver.quit()
