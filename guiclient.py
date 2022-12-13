import sys
from PyQt5.QtWidgets import *
import PyQt5.QtCore as QCoreApplication
import socket
from threading import Thread

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(("127.0.0.1", 10001))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        self.__grid = QGridLayout()
        widget.setLayout(self.__grid)

        self.__ipserv = QLabel("Serveur ip")
        self.__port = QLabel("Port")
        self.__Message = QLabel("Message:")
        self.__screen = QTextBrowser()
        self.__result = QLabel("")
        self.__textipserv = QLineEdit("127.0.0.1")
        self.__textport = QLineEdit("10000")
        self.__mess = QLineEdit("")
        self.__connexion = QPushButton("Connexion")
        self.__envoi = QPushButton("Envoyer")
        self.__quit = QPushButton("Quitter")
        self.__supp = QPushButton("Effacer")

        # Ajouter les composants au grid ayout
        self.__grid.addWidget(self.__ipserv, 0, 0)
        self.__grid.addWidget(self.__port, 1, 0)
        self.__grid.addWidget(self.__textipserv, 0, 1)
        self.__grid.addWidget(self.__textport, 1, 1)
        self.__grid.addWidget(self.__connexion, 2, 0, 1, 4)
        self.__grid.addWidget(self.__screen, 3, 0, 4, 4)
        self.__grid.addWidget(self.__result, 3, 0)
        self.__grid.addWidget(self.__Message, 7, 0, 1, 1)
        self.__grid.addWidget(self.__mess, 7, 1)
        self.__grid.addWidget(self.__envoi, 8, 0, 1, 0)
        self.__grid.addWidget(self.__quit, 9, 1)
        self.__grid.addWidget(self.__supp, 9, 0)
        self.__envoi.clicked.connect(self.envoie)
        self.__supp.clicked.connect(self.effacer)
        self.__quit.clicked.connect(self.actionQuitter)
        self.setWindowTitle("Un logiciel de tchat")

    def InfoBox(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.exec()

    def envoie(self):
        i = 0
        while i < 4:
            i = i + 1
            self.__screen.append(str(i))

    def effacer(self):
        self.__mess.clear

    def actionQuitter(self):
        QCoreApplication.exit(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    app.exec()