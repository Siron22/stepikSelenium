from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


link = "http://suninjuly.github.io/file_input.html"

try:   
    browser = webdriver.Chrome()
    browser.get(link)

    """
    first_name_input = browser.find_element(By.CSS_SELECTOR, "input[name='firstname']")
    first_name_input.send_keys('Обязалово!')
    
    last_name_input = browser.find_element(By.CSS_SELECTOR, "input[name='lastname']")
    last_name_input.send_keys('Обязалово!')
    
    email_input = browser.find_element(By.CSS_SELECTOR, "input[name='email']")
    email_input.send_keys('Обязалово!')
    
    """      
    # create test.txt file
    with open("test.txt", "w") as file:
        content = file.write("automationbypython")  
    
    # получаем путь к директории текущего исполняемого файла 
    current_dir = os.path.abspath(os.path.dirname(__file__))    
    
    # добавляем к этому пути имя файла 
    file_path = os.path.join(current_dir, 'test.txt')           
    
    
    inputs = ['Aleksey', 'Bychutkin', 'test@gmail.com', file_path]

    for element, value in zip(browser.find_elements(By.TAG_NAME, 'input'), inputs):
        element.send_keys(value)
        print(zip(browser.find_elements_by_tag_name('input'), inputs))    
    
    
    
    upload = browser.find_element(By.ID, "file")
    upload.send_keys(file_path)
       
    submit = browser.find_element(By.TAG_NAME, "button").click()   

    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()