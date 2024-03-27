from time import sleep
import const
import save
import parse
import tocsv

save = save.SavePages()
save.access_site(const.URL)
sleep(3)
saved_pages = save.get_urls()
save.save_file(saved_pages)

parse_html = parse.ParseHtml()
to_csv = tocsv.ToCSV()
html = parse_html.get_filename()
sort_file = parse_html.natural_sort(html)
property_list = []
for file in sort_file:
    parse_html.open_file(file)
    parse_html.get_property_soup(file)
    to_csv.make_property_list(file)
    print(property_list[-1])
to_csv.list_to_csv(property_list)