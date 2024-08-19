from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.ui import Select
#from selenium.common.exceptions import UnexpectedAlertPresentException, TimeoutException

# Set up the WebDriver
driver = webdriver.Chrome()

try:
    # Mở trang đăng ký MyKingdom
    driver.get("https://www.mykingdom.com.vn/account")

    # Chờ đợi cho đến khi trường Email đăng nhập xuất hiện
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'CustomerEmail')))

    # Nhập thông tin đăng nhập
    login_email = driver.find_element(By.ID, 'CustomerEmail')
    login_password = driver.find_element(By.ID, 'CustomerPassword')

    login_email.send_keys("pat06112003@gmail.com")
    login_password.send_keys("Tuan-240611")

    # Nhấp vào nút đăng nhập
    login_button = driver.find_element(By.XPATH, "/html/body/main/div/div/div[2]/form/button")
    login_button.click()

    # Chờ đợi cho đến khi trang tài khoản cá nhân tải xong hoặc xác nhận đăng nhập thành công
    WebDriverWait(driver, 10).until(EC.url_contains("/account"))

    print("Đăng nhập thành công.")

finally:
    # Đóng trình duyệt sau khi kiểm thử
    driver.quit()