import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.browser=QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        #controls
        navbar=QToolBar()
        self.addToolBar(navbar)
        back_btn=QAction('Back',self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)
        front_btn=QAction('next',self)
        front_btn.triggered.connect(self.browser.forward)
        navbar.addAction(front_btn)
        reload=QAction('reload',self)
        reload.triggered.connect(self.browser.reload)
        navbar.addAction(reload)
        home_btn=QAction('home',self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)
        self.url_bar=QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)
    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))
    def navigate_to_url(self):
        url=self.url_bar.text()
        self.browser.setUrl(QUrl(url))
    def update_url(self,q):
        self.url_bar.setText(q.toString())
app=QApplication(sys.argv)
QApplication.setApplicationName("phoenix")
window=MainWindow()
app.exec_()