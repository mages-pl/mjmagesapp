import os
import sys

os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--no-sandbox"

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon

app = QApplication(sys.argv)
app.setWindowIcon(QIcon("icon-mages.ico"))

# Zmiana user-agenta
profile = QWebEngineProfile.defaultProfile()
profile.setHttpUserAgent(
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
)


browser = QWebEngineView()
browser.setWindowTitle("MAGES Michał Jendraszczyk")
browser.setGeometry(100, 100, 1200, 800)
browser.load(QUrl("https://mages.pl"))
#browser.show()
browser.showMaximized()

sys.exit(app.exec_())