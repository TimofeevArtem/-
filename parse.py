from concurrent.futures import wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep, time
from pathlib import Path
from selenium.webdriver.support import expected_conditions as EC

TERM_ARRAY = [0.25, 0.5, 0.75, 1, 2, 3, 4, 5, 7, 10, 15, 20]
download_dir = Path(__file__).parent / "downloads"
download_dir.mkdir(exist_ok=True)

options = webdriver.ChromeOptions()

options.add_experimental_option(
    "prefs",
    {
        "download.default_directory": str(download_dir.resolve()),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
    },
)
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 30)
driver.get("https://www.moex.com/ru/marketdata/indices/state/g-curve/archive/")
date_from = driver.find_element(By.CLASS_NAME, "UiInputCalendar_input_1x-4t")
date_from.clear()
date_from.send_keys("01.01.2014" + Keys.ENTER)

for i in TERM_ARRAY:
    term = driver.find_element(By.CLASS_NAME, "ui-input__field")
    term.click()
    term.send_keys(Keys.CONTROL, "a")
    term.send_keys(Keys.BACKSPACE)
    term.send_keys(str(i) + Keys.ENTER)
    sleep(1)
    load_data_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Получить ссылку для скачивания данных за всю историю"]')))
    load_data_button.click()

    

sleep(5)