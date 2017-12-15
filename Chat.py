# coding: utf-8

"""
A more interesting use of signals and slots, here instead of using built-in
slots we use our own custom functions.

For more information on Box Layouts: https://doc.qt.io/qt-5/qboxlayout.html

"""


from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import os
import sys
from random import randint

class MyWin(QWidget):
    width = 400
    height = 100

    def __init__(self):
        super(MyWin, self).__init__()
        self.initGUI()

    def initGUI(self):

        self.buttons = []
        self.welcome = QLabel(self)
        self.welcome.setPixmap(QPixmap('images/welcome.gif'))
        self.welcome.show()
        self.textField = QLabel()
        self.textField.setText("""
You see Amon (sleeping), BloodRedSkies (sleeping), Damien*vampire* (sexy), darkness (asleep), and
Diozil~SinnerWytch (sleeping) here.
look Damien*vampire*
Damien*vampire* A mystical, pale vampire from New Orleans (for hundreds of year now). He is sexy.
look darkness
darkness
A ghastly sight to see. He is sleeping.
look bloodRedSkies
I don’t know which “bloodRedSkies” you mean.
look Diozil~SinnerWytch
Once persecuted, her heavy velvet dress and scarlet rags seem at odds with the
manic laughter that fills the dungeon which is forever haunted by the shadow of
her love spell, called “Love’s Secret Domain”. She is sleeping.
look amon
I don’t know which “amon” you mean.
look voodoo doll
A stuffed doll that sometimes seems to be alive.
look
Sacred Altar
        """)
        self.textField.setObjectName("text1")
        self.textField2 = QTextEdit()
        self.textField2.setObjectName("text2")
        self.submit = QPushButton("Send Message")
        self.submit.setStyleSheet("""
            QPushButton {
                background-color: red;
                color: black;
                padding: 10px;
            }
        """)
        self.submit.clicked.connect(self.showDialog)

        # Set up the layouts
        vbox = QVBoxLayout()
        vbox.addWidget(self.welcome)
        vbox.addWidget(self.textField)
        vbox.addWidget(self.textField2)
        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.addWidget(self.submit, alignment=Qt.AlignRight)
        vbox.addLayout(self.buttonLayout)
        self.setLayout(vbox)

        self.setGeometry(30, 30, 800, 500)
        self.setWindowTitle('Sad Chat')
        self.setObjectName("main")
        self.show()

    def showDialog(self):
        em = QErrorMessage(self)
        em.showMessage("Failed to connect to server.")
        em.setStyleSheet("""
            QErrorMessage {
                background-color: red;
                color: black;
                padding: 30px;
            }
        """)

class examplePopup(QWidget):
    def __init__(self, name):
        super().__init__()

        self.name = name

        self.initUI()

    def initUI(self):
        lblName = QLabel(self.name, self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("""
     QWidget#main {
        background-color: black;
     }
     QLabel#text1 {
         background-color: #333;
         font-size: 12px;
         color: red;
         padding: 0 15px;
     }
     QTextEdit#text2 {
         background-color: #333;
         color: white;
         padding: 15px;
     }
     """)
    win = MyWin()
    sys.exit(app.exec_())
