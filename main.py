#Learning Project - 
#This project is an attempt to develop a web browser.
#following code works for displaying and using a website 
#however since this code is not working on tiktok.com this project is abondoned for now 
#DALIS

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

def handle_load_finished(ok):
    if not ok:
        # Handle error case and provide default text
        print("Error loading web page")

app = QApplication(sys.argv)
window = QMainWindow()

view = QWebEngineView()
view.loadFinished.connect(handle_load_finished)
view.load(QUrl("https://www.google.com"))

window.setCentralWidget(view)
window.show()

sys.exit(app.exec_())
