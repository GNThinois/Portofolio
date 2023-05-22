import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget, QFileDialog
from PyQt5.QtCore import Qt
import pandas as pd
import os
import importlib.util

SCRIPTS_DIR = r"../Ilhup/scripts"
FILES_DIR = r"C:\Users\Thinois\Desktop\MSA"
RESULTS_DIR = r"C:\Users\Thinois\Desktop\MSA\FichiersOK"

class Option_IS(QWidget):
    def __init__(self, homePage):
        super().__init__()
        self.homePage = homePage
        self.initUI()

    def initUI(self):
        self.setWindowTitle('CSV Processor')
        self.setGeometry(300, 300, 300, 200)

        layout = QVBoxLayout()

        self.load_file_button = QPushButton('Select CSV File', self)
        self.load_file_button.clicked.connect(self.load_csv)
        layout.addWidget(self.load_file_button)

        self.file_label = QLabel('', self)
        layout.addWidget(self.file_label)

        self.load_script_button = QPushButton('Select Script', self)
        self.load_script_button.clicked.connect(self.load_script)
        layout.addWidget(self.load_script_button)

        self.script_label = QLabel('', self)
        layout.addWidget(self.script_label)

        self.run_button = QPushButton('Run', self)
        self.run_button.clicked.connect(self.run)
        layout.addWidget(self.run_button)

        self.setLayout(layout)
        self.show()

    def load_csv(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Open File', FILES_DIR, "CSV Files (*.csv);;All Files (*.*);;")
        if filename:
            self.df = pd.read_csv(filename, encoding='ISO-8859-1', delimiter=';')
            self.filename = filename
            self.file_label.setText(f"File loaded: {os.path.basename(filename)}")
        else:
            self.file_label.setText("No file selected.")

    def load_script(self):
        script_filename, _ = QFileDialog.getOpenFileName(self, 'Open File', SCRIPTS_DIR, "Python Files (*.py);;All Files (*.*);;")
        if script_filename:
            spec = importlib.util.spec_from_file_location("module.name", script_filename)
            self.script_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(self.script_module)
            self.script_label.setText(f"Script loaded: {os.path.basename(script_filename)}")
        else:
            self.script_label.setText("No script selected.")

    def run(self):
        if hasattr(self, 'df') and hasattr(self, 'script_module'):
            self.df = self.script_module.run(self.df)
            save_filename = os.path.join(RESULTS_DIR, f'{os.path.basename(self.filename)}_rdy.csv')
            self.df.to_csv(save_filename, index=False, encoding='utf-8-sig')

            # Display a success message
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setWindowTitle("Success")
            self.msg.setText("The operation has been completed successfully.")
            self.msg.setInformativeText(f"File saved as: {save_filename}")
            self.msg.show()
        else:
            # Display a failure message
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.setWindowTitle("Warning")
            self.msg.setText("An error happened.")
            self.msg.setInformativeText("Make sure both CSV file and script are selected.")
            self.msg.show()

        self.homePage.show()
        self.close()