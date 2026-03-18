import sys

from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QAction
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import QApplication, QLineEdit, QMainWindow, QToolBar

DEFAULT_HOME_URL = "https://www.google.com"


def normalize_url(raw_value: str) -> QUrl | None:
    text = raw_value.strip()
    if not text:
        return None

    url = QUrl.fromUserInput(text)
    if not url.isValid() or url.scheme() not in {"http", "https"}:
        return None

    return url


class MiniBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MiniWeb")
        self.setGeometry(100, 100, 1024, 768)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(DEFAULT_HOME_URL))
        self.setCentralWidget(self.browser)

        nav_toolbar = QToolBar("Navigation")
        self.addToolBar(nav_toolbar)

        back_btn = QAction("Back", self)
        back_btn.triggered.connect(self.browser.back)
        nav_toolbar.addAction(back_btn)

        reload_btn = QAction("Reload", self)
        reload_btn.triggered.connect(self.browser.reload)
        nav_toolbar.addAction(reload_btn)

        forward_btn = QAction("Forward", self)
        forward_btn.triggered.connect(self.browser.forward)
        nav_toolbar.addAction(forward_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        nav_toolbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url_bar)

    def navigate_to_url(self):
        url = normalize_url(self.url_bar.text())
        if url is None:
            return

        self.browser.setUrl(url)

    def update_url_bar(self, url: QUrl):
        self.url_bar.setText(url.toString())
        self.url_bar.setCursorPosition(0)


def main():
    app = QApplication(sys.argv)
    window = MiniBrowser()
    window.show()
    return app.exec()
