from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Даём странице загрузиться
    time.sleep(2)

    # Заполняем поля согласно HTML разметке
    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("Ivan")
    
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    
    # Нажимаем кнопку Submit
    button = browser.find_element(By.ID, "submit_button")
    button.click()
    
    # Ждём появления результата
    time.sleep(5)
    
    # Ищем элемент с результатом (обычно появляется после отправки)
    result_element = browser.find_element(By.ID, "result")
    result_text = result_element.text
    print(f"Проверочный код: {result_text}")

finally:
    # Даём время скопировать код
    time.sleep(30)
    browser.quit()
