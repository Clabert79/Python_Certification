import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import urllib

url = 'https://www.albumoftheyear.org/ratings/6-highest-rated/2020/1'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

results = soup.find(id="centerContent")

album_rows = results.find_all("div", class_="albumListRow")

count = 0
for album_row in album_rows:
    count +=1
    # print(album_row, end="\n"*2)

    title_element = album_row.find("h2", class_="albumListTitle")
    print("Title: ", title_element.text)

    links = title_element.find_all("a")
    # print("Links: ", links)

    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}\n")

        print('-' * 10)
        # check page
        url_review = 'https://www.albumoftheyear.org' + link_url
        response_review = requests.get(url_review, headers=headers)

        soup_review = BeautifulSoup(response_review.content, 'html.parser')

        results = soup_review.find(id="centerContent")

        flex_containers = results.find_all("div", class_="flexContainer")

        for flex_container in flex_containers:

            wide_left_align_top = flex_container.find_all("div", class_="extLink")

            for ele in wide_left_align_top:
                links_review = ele.find_all("a")

                print(links_review)
                for link_review in links_review:
                    link_review_url = link_review["href"]
                    print(f"Apply here: {link_review_url }\n")


        break

    break


