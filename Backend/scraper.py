from bs4 import BeautifulSoup

def collect_reviews():
    with open("reviews.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    reviews = []
    for div in soup.find_all("div", class_="review"):
        reviews.append(div.text)

    return reviews
