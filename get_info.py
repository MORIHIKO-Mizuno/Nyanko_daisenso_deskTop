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


def get_filter():
    filter_title_dict = {
        "ランク別": ["基本", "EX", "レア", "激レア", "超激レア", "伝説レア"],
        "形態別": ["1", "2", "3"],
        "特性別": ["超ダメージ", "極ダメージ", "打たれ強い", "超打たれ強い", "めっぽう強い",
                "渾身の一撃", "クリティカル",
                "バリアブレイカー", "悪魔シールド貫通", "波動", "烈波", "小烈波",
                "ふっとばす", "動きを止める", "動きを遅くする", "遠方攻撃", "全方位攻撃",
                "ゾンビキラー", "魂攻撃",
                "超生命体特効", "超獣特効",
                "魔女キラー", "使徒キラー",
                "連続攻撃", "1回攻撃", "攻撃力上昇", "攻撃力低下", "1度だけ生き残る", "お金x2", "対お城", "メタル", "呪い",
                "波動無効", "波動ストッパー", "烈波無効", "ふっとばす無効", "動きを止める無効", "動きを遅くする無効", "攻撃力低下無効",
                "ワープ無効", "古代の呪い無効", "毒撃無効", "攻撃無効"],
        "対属性別": ["白い敵", "赤い敵", "黒い敵", "浮いてる敵", "メタルな敵",
                 "天使", "エイリアン", "ゾンビ", "古代種", "悪魔",
                 "超生命体", "超獣",
                 "魔女", "使徒"]
    }
    return filter_title_dict


def df_filter(df,ranku,keitai,tokusei,taizokusei):
    converted_keitai = ["-"+i for i in keitai]
    return df[(df[""].isin(ranku))&df[""].isin(converted_keitai)&df["特性"].isin(tokusei)&df["特性"].isin(taizokusei)]


if __name__ == "__main__":
    get_ally_df(status_file_path).to_excel("Nyanko.xlsx")