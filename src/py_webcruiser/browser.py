import sys

from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QAction
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import QApplication, QLineEdit, QMainWindow, QToolBar, QTabWidget, QProgressBar

DEFAULT_HOME_URL = "https://www.google.com"


def normalize_url(raw_value: str) -> QUrl | None:
    text = raw_value.strip()
    if not text:
        return None

    url = QUrl.fromUserInput(text)
    if url.isValid() and url.scheme() in {"http", "https"}:
        return url

    return QUrl(f"https://www.google.com/search?q={text}")


class MiniBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Py-WebCruiser")
        self.setGeometry(100, 100, 1024, 768)

        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_current_tab)
        self.tabs.currentChanged.connect(self.current_tab_changed)
        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)

        self.setCentralWidget(self.tabs)

        self.status_bar = self.statusBar()
        self.progress_bar = QProgressBar()
        self.progress_bar.setMaximumWidth(120)
        self.status_bar.addPermanentWidget(self.progress_bar)

        nav_toolbar = QToolBar("Navigation")
        self.addToolBar(nav_toolbar)

        back_btn = QAction("Back", self)
        back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())
        nav_toolbar.addAction(back_btn)

        reload_btn = QAction("Reload", self)
        reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())
        nav_toolbar.addAction(reload_btn)

        forward_btn = QAction("Forward", self)
        forward_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())
        nav_toolbar.addAction(forward_btn)

        new_tab_btn = QAction("New Tab", self)
        new_tab_btn.triggered.connect(self.add_new_tab)
        nav_toolbar.addAction(new_tab_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        nav_toolbar.addWidget(self.url_bar)

        self.add_new_tab(QUrl(DEFAULT_HOME_URL), "Home")

    def add_new_tab(self, qurl=None, label="New Tab"):
        if qurl is None or not isinstance(qurl, QUrl):
             qurl = QUrl(DEFAULT_HOME_URL)

        browser = QWebEngineView()
        browser.setUrl(qurl)
        
        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)

        browser.urlChanged.connect(lambda qurl, browser=browser: 
                                   self.update_url_bar(qurl, browser))
        
        browser.loadProgress.connect(lambda p, browser=browser: self.update_loading_progress(p, browser))
        
        browser.loadFinished.connect(lambda _, browser=browser: 
                                     self.tabs.setTabText(self.tabs.indexOf(browser), browser.page().title()))

    def tab_open_doubleclick(self, i):
        if i == -1: # Double click on empty space
            self.add_new_tab()

    def current_tab_changed(self, i):
        if self.tabs.count() > 0 and i != -1:
            qurl = self.tabs.currentWidget().url()
            self.update_url_bar(qurl, self.tabs.currentWidget())
            self.setWindowTitle(self.tabs.tabText(i))
            self.progress_bar.setVisible(False)

    def close_current_tab(self, i):
        if self.tabs.count() < 2:
            return 
        self.tabs.removeTab(i)

    def navigate_to_url(self):
        url = normalize_url(self.url_bar.text())
        if url is None:
            return

        self.tabs.currentWidget().setUrl(url)

    def update_url_bar(self, url: QUrl, browser=None):
        if browser != self.tabs.currentWidget():
            return
        self.url_bar.setText(url.toString())
        self.url_bar.setCursorPosition(0)

    def update_loading_progress(self, progress, browser):
        if browser == self.tabs.currentWidget():
            self.progress_bar.setValue(progress)
            self.progress_bar.setVisible(progress < 100)


def main():
    app = QApplication(sys.argv)
    window = MiniBrowser()
    window.show()
    return app.exec()
