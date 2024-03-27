import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import const

driver = ""
class SavePages(object):
    def access_site(self,url):
        global driver
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")
        driver = webdriver.Chrome(const.PATH,options=options)
        driver.implicitly_wait(10)
        driver.get(url)

    def get_urls(self):
        all_urls = []
        while True:
            rooms = driver.find_elements_by_css_selector("tr.js-cassette_link > td:nth-of-type(9) > a")
            urls = [room.get_attribute("href") for room in rooms]
            all_urls = all_urls + urls
            next_page = driver.find_elements_by_partial_link_text("次へ")
            if next_page:
                next_page[0].click()
                sleep(3)
            else:
                break
        return all_urls

    def write_file(self,dir_path, filename, file_content, mode='w'):
        with open(os.path.join(dir_path,filename),"w",encoding='utf-8') as f:
            f.write(file_content)
    
    def save_file(self,files):
        dir_name = os.path.dirname(os.path.abspath(__file__))
        for i, file in enumerate(files,1):
            driver.get(file)
            html = driver.page_source
            sleep(3)
            self.write_file(f"{dir_name}/html",f"number_{i}.html",html)