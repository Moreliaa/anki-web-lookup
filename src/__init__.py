from aqt import mw, qt, gui_hooks, webview
import webbrowser

ACTION_TEXT = "Search '{keyword:}' on the web"

_webview_ref = None

def get_default_config():
    return  {
        "base_url": "https://www.jisho.org/search?keyword=",
    }

def search():
    global _webview_ref

    if _webview_ref == None:
        return

    config = mw.addonManager.getConfig(__name__)
    if config == None:
        config = get_default_config()

    text = _webview_ref.selectedText()
    _webview_ref = None
    webbrowser.open(config["base_url"] + str(text), new=2)

def on_context_menu(webview: webview.AnkiWebView, menu: qt.QMenu):
    global _webview_ref

    text = webview.selectedText()
    if len(text) == 0:
        return

    _webview_ref = webview
    text_format = ACTION_TEXT.format(keyword=text)
    action = qt.QAction(text_format, mw)
    qt.qconnect(action.triggered, search)
    menu.addAction(action)

gui_hooks.webview_will_show_context_menu.append(on_context_menu)
