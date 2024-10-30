import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

#find the website and customize it
driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")
driver.maximize_window()

time.sleep(3)

#serach for the search bar to find a product in flipkart
search_bar = driver.find_element(By.CSS_SELECTOR, value="input[placeholder='Search for Products, Brands and More']") 
search_bar.send_keys("Vivo t3x") #send a product name

#click enter to search the particular product
search_bar.send_keys(Keys.RETURN)

time.sleep(5)

#find the dropdown to customize the amount
dropdown_element = driver.find_element(By.CSS_SELECTOR ,value="div[class='tKgS7w'] select[class='Gn+jFg']")

select = Select(dropdown_element)

#customize the prize 
select.select_by_index(1)
time.sleep(3)

#choose desired phone
phone = driver.find_element(By.XPATH,value="(//div[@class='KzDlHZ'][normalize-space()='vivo T3x 5G (Crimson Bliss, 128 GB)'])[1]")
phone.click()
time.sleep(4)

#switch to new window
driver.switch_to.window(driver.window_handles[-1])
time.sleep(3)

#scroll down
driver.execute_script("window.scrollTo(0,600)")
time.sleep(4)

#add to cart
add_to_cart = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='QqFHMw vslbG+ In9uk2']"))
)
add_to_cart.click()
time.sleep(5)
    
#scroll down
driver.execute_script("window.scrollTo(0,600)")
time.sleep(3)

#incrementing the count of phone to 2
increment_product = driver.find_element(By.XPATH,value="(//button[normalize-space()='+'])[1]")
increment_product.click()
time.sleep(3)
