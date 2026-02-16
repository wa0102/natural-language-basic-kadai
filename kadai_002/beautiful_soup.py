from bs4 import BeautifulSoup
from urllib import request
import re

url = 'https://www.aozora.gr.jp/cards/000148/files/2371_13943.html'
response = request.urlopen(url)
soup = BeautifulSoup(response)
response.close()

main_text = soup.find('div', class_='main_text')

tags_to_delete = main_text.find_all(['rp', 'rt'])
for tag in tags_to_delete:
  tag.decompose()

main_text = main_text.get_text()

main_text = re.sub(r"[\u3000 \n \r]", "", main_text)

print(main_text)

text = "近頃は大分方々の雑誌から談話をしろしろと責められて、頭ががらん胴になったから、当分品切れの看板でも懸かけたいくらいに思っています。"

particles = ['は','が','を','に','の','と','から']

for p in particles:
    text = text.replace(p, f" {p} ")

words = text.split()
print(words)