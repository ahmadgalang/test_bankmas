from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_add_todo_item():
    driver = webdriver.Chrome()  # Ganti dengan webdriver sesuai browser yang Anda gunakan
    driver.get("https://todomvc.com/examples/knockoutjs/")
    todo_input = driver.find_element(By.CLASS_NAME, "new-todo")
    todo_input.send_keys("New Todo Item")
    todo_input.send_keys(Keys.ENTER)
    time.sleep(1)
    added_item = driver.find_element(By.XPATH, "//label[contains(., 'New Todo Item')]")
    assert added_item.is_displayed(), "Add Todo Item Test Failed."
    print("Add Todo Item Test Passed.")
    driver.quit()

def test_complete_todo_item():
    driver = webdriver.Chrome()  # Ganti dengan webdriver sesuai browser yang Anda gunakan
    driver.get("https://todomvc.com/examples/knockoutjs/")
    todo_input = driver.find_element(By.CLASS_NAME, "new-todo")
    todo_input.send_keys("New Todo Item")
    todo_input.send_keys(Keys.ENTER)
    time.sleep(1)
    checkbox = driver.find_element(By.CLASS_NAME, "toggle")
    checkbox.click()
    time.sleep(1)
    completed_item = driver.find_element(By.CLASS_NAME, "completed")
    assert completed_item.is_displayed(), "Complete Todo Item Test Failed."
    print("Complete Todo Item Test Passed.")
    driver.quit()

def test_filter_todo_item():
    driver = webdriver.Chrome()  # Ganti dengan webdriver sesuai browser yang Anda gunakan
    driver.get("https://todomvc.com/examples/knockoutjs/")
    todo_input = driver.find_element(By.CLASS_NAME, "new-todo")
    todo_input.send_keys("New Todo Item")
    todo_input.send_keys(Keys.ENTER)
    time.sleep(1)
    filter_completed = driver.find_element(By.LINK_TEXT, "Completed")
    filter_completed.click()
    time.sleep(1)

    # Pengecekan apakah ada elemen yang telah ditandai sebagai selesai
    try:
        filtered_item = driver.find_element(By.CSS_SELECTOR, ".completed")
        assert filtered_item.is_displayed(), "Filter Todo Item Test Failed."
        print("Filter Todo Item Test Passed.")
    except:
        print("No completed items found. Filter Todo Item Test Failed.")
        driver.quit()

def test_delete_todo_item():
    driver = webdriver.Chrome()  # Ganti dengan webdriver sesuai browser yang Anda gunakan
    driver.get("https://todomvc.com/examples/knockoutjs/")
    todo_input = driver.find_element(By.CLASS_NAME, "new-todo")
    todo_input.send_keys("New Todo Item")
    todo_input.send_keys(Keys.ENTER)
    time.sleep(1)
    
    # Menunggu elemen delete_button menjadi interaktif
    try:
        delete_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "destroy")))
        delete_button.click()
        time.sleep(1)
    except:
        print("Delete button not found or not clickable.")
    
    todo_items = driver.find_elements(By.CLASS_NAME, "todo")
    assert len(todo_items) == 0, "Delete Todo Item Test Failed."
    print("Delete Todo Item Test Passed.")
    driver.quit()

if __name__ == "__main__":
    print("Running Selenium Tests...")
    test_add_todo_item()
    test_complete_todo_item()
    test_filter_todo_item()
    test_delete_todo_item()
