import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMenuBar, QAction, QLabel, QHBoxLayout
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import Qt


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ChatBot Artemis")
        self.setWindowIcon(QIcon("icon.ico"))
        initialUrl = "https://chat.openai.com/chat"
        self.webEngineView = QWebEngineView()
        self.setCentralWidget(self.webEngineView)
        self.webEngineView.load(QUrl(initialUrl))
        # Create a menu bar
        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)
        # Create a File menu and add it to the menu bar
        file_menu = menu_bar.addMenu("seçenekler")
        # Create an Exit action and add it to the File menu
        exit_action = QAction("Kapat", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        # Add a separator to the menu bar
        menu_bar.addSeparator()
        # Create a Refresh action and add it to the File menu
        refresh_action = QAction("Yenile", self)
        refresh_action.triggered.connect(self.refreshPage)
        file_menu.addAction(refresh_action)
        # Create a label with the text "Artemis" and add it to the menu bar
        label = QLabel("Artemis", self)
        font = QFont()
        font.setBold(True)
        label.setFont(font)
        menu_bar.setCornerWidget(label)
    def refreshPage(self):
        self.webEngineView.reload()

app = QApplication(sys.argv)
window = Window()
window.setFixedSize(350,500)
window.move(0,0)
window.setWindowFlag(Qt.FramelessWindowHint, True)
window.show()
sys.exit(app.exec_())