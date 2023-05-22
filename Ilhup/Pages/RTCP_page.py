from PyQt5.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Example Window')
        self.setGeometry(300, 300, 300, 200)

        layout = QVBoxLayout()

        label = QLabel('Example Label', self)
        layout.addWidget(label)

        self.setLayout(layout)
        self.show()

if __name__ == '__main__':
    app = QApplication([])
    ex = Example()
    app.exec_()
