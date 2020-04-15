from bs4 import BeautifulSoup
import requests
import csv

# html parser => lxml, html5lib

# methods => find, find_all

source = requests.get('https://coreyms.com/').text

# print(type(source))
# print(source)

soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify())

articles = soup.find_all('article')

# print(article.prettify())
# articles.pop(4)
csv_file = open('demo.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Headline', 'Summary', 'Video_Link'])

for article in articles:

    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)
    try:
        vid_src = article.find('iframe', class_="youtube-player")['src']
        # print(vid_src)

        vid_id = vid_src.split('/')[4].split('?')[0]
        # print(vid_id)
        youtube_link = f'https://www.youtube.com/watch?v={vid_id}'

    except Exception as e:
        youtube_link = None
    print(youtube_link)
    print()

    csv_writer.writerow([headline, summary, youtube_link])

csv_file.close()
