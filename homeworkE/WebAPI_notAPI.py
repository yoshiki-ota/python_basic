import time
import requests
from bs4 import BeautifulSoup
import re


def main():
    pass


# トップページ情報取得
URL = "https://news.ycombinator.com/"
# 情報格納
rest = requests.get(URL)
# BeautifulSoupにページ内容を読み込ませる
soup = BeautifulSoup(rest.text, 'lxml')

# タイトル＆リンク作成
for x in soup.find_all(class_=re.compile('titlelink')):
    title_text = x.get_text()
    title_url = x.attrs['href']
    print(f"title: {title_text}, link: {title_url}")

if __name__ == '__main__':
    start = time.time()  # 開始時間
    main()
    print(time.time() - start)  # 終了時間-開始時間＝かかった時間
