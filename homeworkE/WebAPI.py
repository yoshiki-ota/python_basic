from bs4 import BeautifulSoup
import urllib.request as req


def main():
    pass


# 〇〇〇へアクセス
url = "https://news.ycombinator.com/"
res = req.urlopen(url)

soup = BeautifulSoup(res, "html.parser")
# 　<div class="〇〇〇".....>URLやタイトル名の情報<div>のクラス名を指定
tags = soup.find_all(class_="title")
# 　find_allはリスト形式で取得されるので、forで順番に取り出す。
# 　ポイントは取り出した情報からさらにタグ名を絞ってforで取り出すこと。


for tag in tags:
    # 一つづつ取り出した〇〇〇クラスの中の"a"タグの情報を取得
    for a in tag.select("a"):
        # aタグの中の　title="タイトル名"　というようなtitle=のあとの情報を取得する
        title_name = a.get('title')
        print(title_name)
        # aタグの中の　href="リンク先のURL"　というようなhref=のあとの情報を取得する
        url = a.get('href')
        print(url)

if __name__ == '__main__':
    main()
