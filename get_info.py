from bs4 import BeautifulSoup
import pandas as pd

# ローカルHTMLファイルのパス
top_file_path = "web/にゃんこ大戦争データベース.html"
status_file_path = "web/にゃんこ大戦争DB 味方ステータス 全キャラ.html"

# とりあえずHTMLファイルから情報を抽出してキャラのステータスのデータフレームを返す関数。


def get_ally_df(ally_path):
    # ローカルHTMLファイルのパス
    html_file_path = ally_path
    # HTMLファイルを開いて読み込む
    with open(html_file_path, "r", encoding="utf-8") as file:
        html_content = file.read()
    # BeautifulSoupを使用してHTMLを解析
    soup = BeautifulSoup(html_content, "html.parser")

    # クラスがhideのものを消す
    for hide_element in soup.find_all(class_='hide'):
        hide_element.decompose()

    data = soup.find("div", class_="maincontents").find("tbody")

    # 列名取得
    # ページから取得する様にしても良いかもしれない
    col_name = [
        "No.",
        "ランク",
        "img",
        "キャラクター名",
        "Lv",
        "体力",
        "KB",
        "速度",
        "攻撃力",
        "DPS",
        "範囲",
        "頻度F",
        "発生F",
        "射程",
        "コスト",
        "再生産F",
        "特性"
    ]

    # 各行のデータを取得
    row_list = []

    # todo: 特性が複数あるものを考慮する
    for row_data in data.find_all("tr", role="row"):
        row = [col.get_text() for col in row_data.find_all("td")]
        row_list.append(row)

    df = pd.DataFrame(row_list, columns=col_name)
    return df

if __name__ == "__main__":
    get_ally_df(status_file_path).to_excel("Nyanko.xlsx")