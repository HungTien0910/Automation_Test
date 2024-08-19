from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver
driver = webdriver.Chrome()

try:
    # Mở trang danh sách sản phẩm MyKingdom
    driver.get("https://www.mykingdom.com.vn/collections/all?sort=manual")

    # Chờ đợi cho đến khi trang sản phẩm tải hoàn tất
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'product-image-9615408890135')))

    # Tìm sản phẩm đầu tiên trong danh sách và nhấp vào nó
    first_product = driver.find_element(By.ID, 'product-image-9615408890135')
    first_product.click()

    # Chờ đợi cho đến khi trang chi tiết sản phẩm tải hoàn tất
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ProductSubmitButton-template--18711304896791__main')))

    # Nhấp vào nút "Thêm vào giỏ hàng"
    add_to_cart_button = driver.find_element(By.ID, 'ProductSubmitButton-template--18711304896791__main')
    driver.execute_script("arguments[0].scrollIntoView();", add_to_cart_button)
    driver.execute_script("arguments[0].click();", add_to_cart_button)

    # Chờ đợi cho đến khi thông báo hoặc trang giỏ hàng xuất hiện
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'CartDrawer')))

    # Kiểm tra xem sản phẩm đã được thêm vào giỏ hàng chưa
    cart_popup = driver.find_element(By.ID, 'CartDrawer')


    # if cart_popup.is_displayed():
    #     print("Sản phẩm đã được thêm vào giỏ hàng thành công.")
    # else:
    #     print("Không thể thêm sản phẩm vào giỏ hàng.")

finally:
    # Đóng trình duyệt sau khi kiểm thử
    driver.quit()
