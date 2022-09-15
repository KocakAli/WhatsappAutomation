from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import pandas
from selenium.webdriver.common.keys import Keys


excel_data = pandas.read_excel('data.xlsx', sheet_name='data') // first argument your workbook name and second argument your worksheet name



driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://web.whatsapp.com')
count = 1
input("Press Enter after you logged in with QR code.")
for column in excel_data['Contact'].tolist():
    try:
        url = 'https://web.whatsapp.com/send?phone=' + str(excel_data['Contact'][count]) + '&text=' + excel_data['Message'][0]
        driver.get(url)
        xpath_val = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
        wait = WebDriverWait(driver, 10)
        sleep(2)
        wait.until(EC.presence_of_element_located((By.XPATH, xpath_val))).send_keys(Keys.ENTER)
        sleep(5)
        print('Message sent successfully: ' + str(excel_data['Contact'][count]))
    except Exception as e:
        print('Message can not sent: ' + str(excel_data['Contact'][count]) + str(e))
    count = count + 1
driver.quit()
print("Script has done.")

