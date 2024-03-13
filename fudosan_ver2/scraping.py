from time import sleep
import os
import glob
import requests
from bs4 import BeautifulSoup
import pandas as pd
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

class ToCSV(object):
    def make_property_list(self,file):
        property_list.append({
            "title":parse_html.get_property_title(file),
            "address":parse_html.get_property_table(file).select_one("tr:first-of-type > td").text,
            "access":parse_html.get_property_table(file).select_one("tr:nth-of-type(2) > td").text,
            "madori":parse_html.get_property_table(file).select_one("tr:nth-of-type(3) > td:first-of-type").text,
            "menseki":parse_html.get_property_table(file).select_one("tr:nth-of-type(3) > td:nth-of-type(2)").text,
            "old":parse_html.get_property_table(file).select_one("tr:nth-of-type(4) > td:first-of-type").text,
            "floor":parse_html.get_property_table(file).select_one("tr:nth-of-type(4) > td:nth-of-type(2)").text,
            "face":parse_html.get_property_table(file).select_one("tr:nth-of-type(5) > td:first-of-type").text,
            "type":parse_html.get_property_table(file).select_one("tr:nth-of-type(5) > td:nth-of-type(2)").text,
            "structure":parse_html.get_property_summary(file).select_one("tr:first-of-type > td:nth-of-type(2)").text
            })
        
    def list_to_csv(self,d_list):
        df = pd.DataFrame(d_list)
        df.to_csv('property_list.csv',index=None,encoding='utf-8-sig')

parse_html = ParseHtml()
to_csv = ToCSV()
html = parse_html.get_filename()
sort_file = parse_html.natural_sort(html)
property_list = []
for file in sort_file:
    parse_html.open_file(file)
    parse_html.get_property_soup(file)
    to_csv.make_property_list(file)
    print(property_list[-1])
to_csv.list_to_csv(property_list)