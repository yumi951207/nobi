import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = ""
class SavePages(object):
    def access_site(self,url):
        global driver
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")
        driver = webdriver.Chrome(executable_path=r"\Users\nobi1\OneDrive\デスクトップ\fudosan\tools\chromedriver.exe",
                          options=options)
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

save_pages = SavePages()
save_pages.access_site("https://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=030&bs=040&pc=20&smk=&po1=25&po2=99&shkr1=03&shkr2=03&shkr3=03&shkr4=03&sc=12204&ta=12&cb=0.0&ct=5.5&et=9999999&mb=0&mt=9999999&cn=9999999&tc=0401102&fw2=")
sleep(3)
saved_pages = save_pages.get_urls()
save_pages.save_file(saved_pages)

