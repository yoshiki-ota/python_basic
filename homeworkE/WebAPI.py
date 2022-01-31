import time

import requests as requests
import bs4


def search_site(base_url, food):
    response = requests.get(f"{base_url}/search/{food}")
    html = response.text
    return html


def get_site(base_url, html):
    soup = bs4.BeautifulSoup(html, 'lxml')
    recipe_previews = soup.find_all(class_="recipe-preview")

    recipes = []
    for site_preview in recipe_previews:
        site_title = site_preview.find(class_="title").text
        site_url = site_preview.find(class_="title").attrs['href']

        recipes.append({
            "title": site_title,
            "url": f"{base_url}{site_url}"})
    return recipes


def main():
    base_url = 'https://news.ycombinator.com/'
    food = 'トマト'

    html = search_site(base_url, food)
    dummy = get_site(base_url, html)

    for site in dummy:
        print(f"レシピ名 {site['title']}, URL:{site['url']}")


if __name__ == '__main__':
    start = time.time()  # 開始時間
    main()
    print(time.time() - start)  # 終了時間-開始時間＝かかった時間
