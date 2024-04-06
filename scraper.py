from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # To run Chrome in headless mode

# Specify the path to your Chrome driver executable
chrome_driver_path = 'webdriver/chromedriver.exe'

# Set up the Chrome service
service = Service(chrome_driver_path)
service.start()

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=service, options=chrome_options)

year = 2011
month = 1
day = 1
url = 'https://www.wunderground.com/history/daily/us/ca/los-angeles/KLAX/date/' + str(year) + '-' + str(month) + '-' + str(day)

# Load the webpage
driver.get(url)

# Find the tbody element with the class ng-star-inserted
tbody_element = driver.find_element(By.CSS_SELECTOR, 'tbody.ng-star-inserted')

if tbody_element:
    print(tbody_element.text)  # Print the text content of the tbody element
else:
    print("Could not find the tbody element with class ng-star-inserted")

# Quit the driver
driver.quit()
