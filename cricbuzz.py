from firstinningsbatting import fibat
from firstinningsbowlers import fibowl
from secondinningsbatting import secbat
from secondinningsbowlers import secbowl


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

path_to_chromedriver = '/Users/me/Desktop/chromedriver'

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(executable_path=r"chromedriver.exe", chrome_options=chrome_options)

print(r'''
  ____      _      _
 / ___|_ __(_) ___| |__  _   _ ________  ___  ___ ___  _ __ ___  ___
| |   | '__| |/ __| '_ \| | | |_  /_  / / __|/ __/ _ \| '__/ _ \/ __|
| |___| |  | | (__| |_) | |_| |/ / / /  \__ \ (_| (_) | | |  __/\__ \
 \____|_|  |_|\___|_.__/ \__,_/___/___| |___/\___\___/|_|  \___||___/

 _
| |__  _   _
| '_ \| | | |
| |_) | |_| |
|_.__/ \__, |
       |___/

 ____  _ _     _           _     _
|  _ \(_|_)___| |__   __ _| |__ | |__  ____
| |_) | | / __| '_ \ / _` | '_ \| '_ \|_  /
|  _ <| | \__ \ | | | (_| | |_) | | | |/ /
|_| \_\_|_|___/_| |_|\__,_|_.__/|_| |_/___|




''')
match_id = input("Enter match_id:")
fibat(match_id, driver)
fibowl(match_id, driver)
secbat(match_id, driver)
secbowl(match_id, driver)