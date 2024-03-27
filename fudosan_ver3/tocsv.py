import pandas as pd
import parse
from bs4 import BeautifulSoup
import exefile

class ToCSV(object):
    def make_property_list(self,file):
        exefile.property_list.append({
            "title":exefile.parse_html.get_property_title(file),
            "address":exefile.parse_html.get_property_table(file).select_one("tr:first-of-type > td").text,
            "access":exefile.parse_html.get_property_table(file).select_one("tr:nth-of-type(2) > td").text,
            "madori":exefile.parse_html.get_property_table(file).select_one("tr:nth-of-type(3) > td:first-of-type").text,
            "menseki":exefile.parse_html.get_property_table(file).select_one("tr:nth-of-type(3) > td:nth-of-type(2)").text,
            "old":exefile.parse_html.get_property_table(file).select_one("tr:nth-of-type(4) > td:first-of-type").text,
            "floor":exefile.parse_html.get_property_table(file).select_one("tr:nth-of-type(4) > td:nth-of-type(2)").text,
            "face":exefile.parse_html.get_property_table(file).select_one("tr:nth-of-type(5) > td:first-of-type").text,
            "type":exefile.parse_html.get_property_table(file).select_one("tr:nth-of-type(5) > td:nth-of-type(2)").text,
            "structure":exefile.parse_html.get_property_summary(file).select_one("tr:first-of-type > td:nth-of-type(2)").text
            })
        
    def list_to_csv(self,d_list):
        df = pd.DataFrame(d_list)
        df.to_csv('property_list.csv',index=None,encoding='utf-8-sig')