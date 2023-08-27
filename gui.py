
import PySimpleGUI as sg

name_list = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank']


# トップページ
# 左右に分けて、スケジュール、ガチャ、をそれぞれリストで表示する予定(余裕があったらリンクも貼りたい)
top_left_col = [
    [sg.Text('名前を選択してください:')],
    [sg.Combo(values=name_list, size=(20, len(name_list)), key='-COMBO-', enable_events=True)],
    [sg.Button('OK')],
]

top_right_col = [
    [sg.Multiline('', size=(30, 10), key='-OUTPUT-', autoscroll=True)],
]

top_layout = [
    [sg.Column(top_left_col), sg.VSeperator(), sg.Column(top_right_col)],
]


# 味方ステータス一覧
ally_layout = [
    [sg.Text('名前を選択してください:')],
    [sg.Combo(values=name_list, size=(20, len(name_list)), key='-COMBO-', enable_events=True)],
    [sg.Button('OK'), sg.Button('キャンセル')],
]
# 敵ステータス一覧
enemy_layout = [
    [sg.Text('名前を選択してください:')],
    [sg.Combo(values=name_list, size=(20, len(name_list)), key='-COMBO-', enable_events=True)],
    [sg.Button('OK'), sg.Button('キャンセル')],
]
# ステータス比較

compare_status_left_col = [
    [sg.Text('名前を選択してください:')],
    [sg.Combo(values=name_list, size=(20, len(name_list)), key='-COMBO-', enable_events=True)],
    [sg.Button('OK')],
]

compare_status_right_col = [
    [sg.Multiline('', size=(30, 10), key='-OUTPUT-', autoscroll=True)],
]

compare_status_layout = [
    [sg.Column(compare_status_left_col), sg.VSeperator(), sg.Column(compare_status_right_col)],
]

# 全体のコード　このシステムでは多機能をタブによって表現している
layout = [
    [sg.TabGroup([[
        sg.Tab('スケジュール', top_layout),
        sg.Tab('味方ステータス', ally_layout),
        sg.Tab('敵ステータス', enemy_layout),
        sg.Tab('ステータス比較', compare_status_layout),
        ]], tab_location='lefttop')]
]

# window option macではfontは20にする
window = sg.Window("にゃんこ大戦争DeskTop", layout, font=('meiryo', 12), resizable=True, grab_anywhere=True, auto_size_buttons=True)

# イベントループ
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'キャンセル':
        break
    elif event == 'OK':
        selected_name = values['-COMBO-']
        if selected_name:
            sg.popup(f'選択された名前: {selected_name}')

# ウィンドウを閉じる
window.close()