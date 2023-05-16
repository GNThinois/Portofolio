import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt


class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Home Page')
        self.setGeometry(300, 300, 300, 200)
        spacer_item = QSpacerItem(20, 40)  # Add vertical spacing


        layout = QVBoxLayout()

        layout.addItem(spacer_item)
        label = QLabel('Choisissez le type de traitement :', self)
        label.setStyleSheet("font-size: 20px; font-weight: bold;")
        label.setAlignment(Qt.AlignCenter)  # Center-align the text
        layout.addWidget(label)

        layout.addItem(spacer_item)

        option1_button = QPushButton('Fichiers IS', self)
        option1_button.setStyleSheet('QPushButton {background-color: #4CAF50; color: white; font-size: 18px;}')
        option1_button.clicked.connect(self.option1Clicked)
        layout.addWidget(option1_button)

        option2_button = QPushButton('Fichiers RTCP', self)
        option2_button.setStyleSheet('QPushButton {background-color: #f44336; color: white; font-size: 18px;}')
        option2_button.clicked.connect(self.option2Clicked)
        layout.addWidget(option2_button)

        option3_button = QPushButton('Fichier ABS', self)
        option3_button.setStyleSheet('QPushButton {background-color: #2196F3; color: white; font-size: 18px;}')
        option3_button.clicked.connect(self.option3Clicked)
        layout.addWidget(option3_button)

        layout.addItem(spacer_item)

        close_button = QPushButton('Close', self)
        close_button.setStyleSheet('QPushButton {background-color: #555555; color: white; font-size: 16px;}')
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)

        self.setLayout(layout)
        self.show()

    def option1Clicked(self):
        self.option1_screen = Option1Screen()  # Store reference to Option1Screen
        self.option1_screen.show()

    def option2Clicked(self):
        print('Option 2 clicked!')

    def option3Clicked(self):
        print('Option 3 clicked!')

class Option1Screen(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Option 1 Screen')
        self.setGeometry(300, 300, 300, 200)

        layout = QVBoxLayout()

        label = QLabel('This is Option 1 Screen!', self)
        layout.addWidget(label)

        back_button = QPushButton('Back', self)
        back_button.setStyleSheet('QPushButton {background-color: #555555; color: white; font-size: 16px;}')
        back_button.clicked.connect(self.goBack)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def goBack(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Set the Fusion style
    app.setStyle('Fusion')
    homePage = HomePage()
    sys.exit(app.exec_())
