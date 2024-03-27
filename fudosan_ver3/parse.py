from time import sleep
import os
import glob
import requests
from bs4 import BeautifulSoup
import re

class ParseHtml(object):
    def get_filename(self):
        html_path = glob.glob("html/*.html")
        return html_path

    def natural_sort(self,path):
        def str_to_int(a):
            return [int(b) if b.isdigit() else b for b in re.split('([0-9]+)', a) ]
        return sorted(path, key=str_to_int)

    def open_file(self,file):
        with open(file,"r",encoding="utf-8") as f:
            html = f.read()
        return html

    def get_property_soup(self,file):
        html = self.open_file(file)
        soup = BeautifulSoup(html,"lxml")
        return soup

    def get_property_title(self,file):
        property_title = self.get_property_soup(file).select_one("h1.section_h1-header-title").text
        return property_title
    
    def get_property_table(self,file):
        property_table = self.get_property_soup(file).select_one("table.property_view_table")
        return property_table
    
    def get_property_summary(self,file):
        get_property_summary = self.get_property_soup(file).select_one("table.data_table")
        return get_property_summary