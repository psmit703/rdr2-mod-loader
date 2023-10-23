import time
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import tkinter
from tkinter import filedialog


def main():
    window()


def window():
    app = QApplication(sys.argv)
    widget = QWidget()

    button1 = QPushButton(widget)
    button1.setText("Button1")
    button1.move(64, 32)
    button1.clicked.connect(button1_clicked)

    button2 = QPushButton(widget)
    button2.setText("Button2")
    button2.move(64, 64)
    button2.clicked.connect(button2_clicked)

    widget.setGeometry(50, 50, 320, 200)
    widget.setWindowTitle("Blaze Carson's RDR2 Mod Manager")
    widget.show()
    sys.exit(app.exec_())


def button1_clicked():
    print("Button 1 clicked")


def button2_clicked():
    print("Button 2 clicked")


if __name__ == '__main__':
    main()
