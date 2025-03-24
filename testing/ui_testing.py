from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://example.com")
print("Title:", driver.title)
driver.quit()