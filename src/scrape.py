import requests
from bs4 import BeautifulSoup as bs


quotes_and_authors = {}
url = 'https://www.shopify.ca/blog/motivational-quotes'
web_page = requests.get(url)

soup = bs(web_page.content, 'lxml')
final_text = soup.get_text()
text_list = final_text.split('\n')
text_list_length = len(text_list)
#print(final_text_list_length)

quotation_mark1 = '“'
quotation_mark2 = '"'
hyphen = '—'
new_list = []
for i in text_list:
  if i in new_list:
    continue
  elif quotation_mark1 in i or quotation_mark2 in i and hyphen in i:
    new_list.append(i)
    
for j in new_list:
  sub_list = j.split(hyphen)
  if len(sub_list) < 2:
    sub_list = j.split('—')
    if len(sub_list) < 2:
      sub_list = j.split('―')
      if len(sub_list) < 2:
        sub_list = j.split('–')
  try:
    sub_list[0].lstrip().rstrip()
    sub_list[1].lstrip().rstrip()
    quotes_and_authors[sub_list[1]] = sub_list[0]
  except:
    pass
