from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Chrome driver
driver = webdriver.Chrome(r"C:/Users/DD/Documents/Py/chromedriver.exe")

# Navigate to the webpage
driver.get("https://www.nordpoolgroup.com/en/Market-data1/Dayahead/Area-Prices/LV/Hourly/?view=table")

# Wait for the table element to become visible
wait = WebDriverWait(driver, 10)
table = wait.until(EC.visibility_of_element_located((By.ID, "datatable")))

# Extract the rows of the table
rows = table.find_elements(By.TAG_NAME, "tr")

# Extract the prices from each row and store them in a list
prices = []
for row in rows[1:25]: # only extract the next day
    cols = row.find_elements(By.TAG_NAME, "td")
    price = cols[2].text.strip() # the price is in the second column
    prices.append(price)

# Write the prices to a text file
with open('energy_prices.txt', 'w') as file:
    for price in prices:
        file.write(price + '\n')

# Quit the Chrome driver
driver.quit()
