from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("user-data-dir=C:\\Users\\vigne\\AppData\\Local\Google\\Chrome\\User Data")

#chrome_options.add_argument("--disable-notifications")
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_argument("--disable-extensions")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# Replace 'path_to_chromedriver' with the actual path where you've placed the ChromeDriver executable.
driver = webdriver.Chrome(executable_path='chromedriver.exe', options=chrome_options)


# Navigate to Gmail login page
driver.get('https://mail.google.com/')

# Add your automation steps here, like filling in login credentials and logging in.

# Close the browser

time.sleep(60)
driver.quit()
