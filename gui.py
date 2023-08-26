import webview
window = webview.create_window("My First App", url="web\\index.html")
webview.start(http_server=True, debug=True)