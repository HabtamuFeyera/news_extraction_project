from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import Workbook
import os
import re
from datetime import datetime, timedelta

class NewsExtractor:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(["Title", "Date", "Description", "Picture Filename", "Search Phrase Count", "Money Presence"])

    def extract_news(self, search_phrase, category=None, num_months=1):
        self.driver.get(self.url)

        search_field = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Search']")))
        search_field.clear()
        search_field.send_keys(search_phrase)
        search_field.send_keys(Keys.RETURN)

        if category:
            category_link = self.wait.until(EC.presence_of_element_located((By.XPATH, f"//a[contains(text(), '{category}')]")))
            category_link.click()

        start_date = self.get_start_date(num_months)

        while True:
            articles = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//h2[contains(@class, 'title')]")))

            for article in articles:
                title = article.text.strip()
                date = article.find_element(By.XPATH, "./ancestor::div[contains(@class, 'container')]/preceding-sibling::div//time").get_attribute("datetime")
                description_element = article.find_element(By.XPATH, "./following-sibling::div[contains(@class, 'content')]")
                description = description_element.text.strip() if description_element else ""
                picture_url = description_element.find_element(By.XPATH, ".//img").get_attribute("src")
                search_phrase_count = title.count(search_phrase) + description.count(search_phrase)
                money_presence = self.contains_money(title, description)
                picture_filename = os.path.basename(picture_url)
                self.download_image(picture_url, picture_filename)
                self.ws.append([title, date, description, picture_filename, search_phrase_count, money_presence])

            if not self.navigate_to_next_page():
                break

        self.wb.save(f"output/news_data.xlsx")

    def get_start_date(self, num_months):
        today = self.get_today()
        return today - timedelta(days=num_months * 30)

    def get_today(self):
        return datetime.today()

    def contains_money(self, *texts):
        for text in texts:
            if re.search(r'\b(\$|dollars|USD)\b', text):
                return True
        return False

    def download_image(self, url, filename):
        self.driver.get(url)
        with open(f"output/{filename}", 'wb') as f:
            f.write(self.driver.find_element(By.TAG_NAME, 'img').screenshot_as_png)

    def navigate_to_next_page(self):
        try:
            next_page_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Next page')]")))
            next_page_button.click()
            return True
        except:
            return False

    def close_driver(self):
        self.driver.quit()
