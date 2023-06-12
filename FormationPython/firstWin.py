from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout,QPushButton, QHBoxLayout, QLineEdit, QFrame, QLabel, QToolTip
from PyQt6 import *
#app = QApplication()
#win = QWidget()
#win.show()
#app.exec()


# Organiser dans une classe
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dijrisktra-Road")
        main_layout = QVBoxLayout(self)

        haut = QHBoxLayout()
        #button1 = QPushButton("Click me 1")
        #haut.addWidget(button1)
        text = QLabel("Dijstra Roads")
        haut.addWidget(text)

        bas = QHBoxLayout()
        button2 = QLineEdit("écrit ici...")
        bas.addWidget(button2)

        main_layout.addLayout(haut)
        main_layout.addLayout(bas)



app = QApplication()
win = MainWindow()
win.show()
app.exec()




