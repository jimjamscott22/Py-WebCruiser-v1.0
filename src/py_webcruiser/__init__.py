import sys

from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QAction
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import QApplication, QLineEdit, QMainWindow, QToolBar


class MiniBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MiniWeb")
        self.setGeometry(100, 100, 1024, 768)

        # 1. Initialize the Web Engine (The Central Widget)
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))
        self.setCentralWidget(self.browser)

        # 2. Initialize the Navigation Toolbar
        nav_toolbar = QToolBar("Navigation")
        self.addToolBar(nav_toolbar)

        # 3. Create Navigation Actions (Buttons)
        back_btn = QAction("Back", self)
        back_btn.triggered.connect(self.browser.back)  # Connect signal to engine slot
        nav_toolbar.addAction(back_btn)

        reload_btn = QAction("Reload", self)
        reload_btn.triggered.connect(self.browser.reload)
        nav_toolbar.addAction(reload_btn)

        forward_btn = QAction("Forward", self)
        forward_btn.triggered.connect(self.browser.forward)
        nav_toolbar.addAction(forward_btn)

        # 4. Create the URL Bar
        self.url_bar = QLineEdit()
        # Connect the 'Enter' key press to our custom slot
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        nav_toolbar.addWidget(self.url_bar)

        # Connect the engine's URL change event to update our URL bar
        self.browser.urlChanged.connect(self.update_url_bar)

    # --- Custom Slots ---
    def navigate_to_url(self):
        """Triggered when the user hits 'Enter' in the URL bar."""
        url_text = self.url_bar.text()
        # Basic validation to ensure the engine recognizes it as a web protocol
        if not url_text.startswith("http"):
            url_text = "https://" + url_text
        self.browser.setUrl(QUrl(url_text))

    def update_url_bar(self, q):
        """Triggered when the browser navigates to a new page."""
        self.url_bar.setText(q.toString())
        self.url_bar.setCursorPosition(0)


def main():
    """Launch the application."""
    app = QApplication(sys.argv)
    window = MiniBrowser()
    window.show()
    return app.exec()
