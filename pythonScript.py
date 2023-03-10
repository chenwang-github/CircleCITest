from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

# 找到搜索框元素
search_box = driver.find_element_by_id("kw")

# 在搜索框中输入文本内容
search_box.send_keys("selenium")

# 使用class name属性值查找按钮元素
button_element = driver.find_element_by_class_name("s_btn")

# 点击按钮
button_element.click()

# 等待搜索结果页面中出现“selenium”关键字
wait = WebDriverWait(driver, 10)
search_result = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Selenium 4.8.0 Released!')]")))

# 输出搜索结果
print(search_result.text)

# 关闭浏览器
driver.quit()

print("python script execute successfuly")
