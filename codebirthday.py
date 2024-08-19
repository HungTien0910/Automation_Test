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
    # Chờ đợi cho đến khi trường Tên xuất hiện
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'email')))

    # Nhập các thông tin vào form đăng ký sử dụng ID
    email = driver.find_element(By.ID, 'email')
    name1 = driver.find_element(By.ID, 'custom#vtv_first_child_name')
    day1 = driver.find_element(By.ID, "label-DD")
    month1 = driver.find_element(By.ID, "label-MM")
    year1 = driver.find_element(By.ID, "label-YYYY")
    gender1 = driver.find_element(By.CSS_SELECTOR, "button[aria-controls='custom#vtv_first_child_gender-selector-dropdown']")

    name2 = driver.find_element(By.ID, 'custom#vtv_second_child_name')
    day2 = driver.find_element(By.ID, 'label-DD')
    month2 = Select(driver.find_element(By.ID, 'label-MM'))
    year2 = driver.find_element(By.ID, 'label-YYYY')
    gender2 = driver.find_element(By.CSS_SELECTOR, "button[aria-controls='custom#vtv_second_child_gender-selector-dropdown']")

    # Điền thông tin
    email.send_keys("Tienhung112255@gmail.com")
    name1.send_keys("Hung")
    day1.send_keys("1")
    month1.send_keys("1")
    year1.send_keys("2003")
    gender1.select_by_visible_text("Nam")

    #email.send_keys("Tienhung112255@gmail.com")
    name2.send_keys("Hungt")
    day2.send_keys("3")
    month2.send_keys("1")
    year2.send_keys("2003")
    gender2.select_by_visible_text("Nữ")

    # Cuộn đến nút đăng ký
    register_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='btn-form-submit']")
    driver.execute_script("arguments[0].scrollIntoView();", register_button)

    # Nhấp vào nút
    register_button.click()

    try:
        success_banner = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "section[data-testid='banner-success']"))
        )
        print("Đăng ký thành công.")
    except TimeoutException:
        print("Đăng ký thất bại hoặc có thông báo lỗi.")

finally:
    # Đóng trình duyệt sau khi kiểm thử
    driver.quit()
