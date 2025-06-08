from aqt import mw, qt, gui_hooks, webview
import webbrowser

base_search_string = "https://www.jisho.org/search?keyword="
action_text = "Search on Jisho"

webview_ref = None

def search():
    if webview_ref == None:
        return

    text = webview_ref.selectedText()
    webbrowser.open(base_search_string + str(text), new=2)

def on_context_menu(webview: webview.AnkiWebView, menu: qt.QMenu):
    global webview_ref

    text = webview.selectedText()
    if len(text) == 0:
        return

    webview_ref = webview
    action = qt.QAction(action_text, mw)
    qt.qconnect(action.triggered, search)
    menu.addAction(action)

gui_hooks.webview_will_show_context_menu.append(on_context_menu)
