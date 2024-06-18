import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QFileDialog, QVBoxLayout, QMessageBox
import subprocess

class FileSorterApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('File Sorter')

        layout = QVBoxLayout()

        self.label = QLabel('Select Directory:')
        layout.addWidget(self.label)

        self.directoryInput = QLineEdit(self)
        layout.addWidget(self.directoryInput)

        self.browseButton = QPushButton('Browse', self)
        self.browseButton.clicked.connect(self.browseDirectory)
        layout.addWidget(self.browseButton)

        self.sortButton = QPushButton('Sort Files', self)
        self.sortButton.clicked.connect(self.sortFiles)
        layout.addWidget(self.sortButton)

        self.setLayout(layout)
        self.resize(400, 200)

    def browseDirectory(self):
        directory = QFileDialog.getExistingDirectory(self, 'Select Directory')
        if directory:
            self.directoryInput.setText(directory)

    def sortFiles(self):
        directory = self.directoryInput.text()
        if not directory:
            QMessageBox.warning(self, 'Input Error', 'Please select a directory first.')
            return
        
        try:
            # Run your Python script
            subprocess.run(['python', 'main.py', directory], check=True)
            QMessageBox.information(self, 'Success', 'Files sorted successfully!')
        except subprocess.CalledProcessError as e:
            QMessageBox.critical(self, 'Error', f'An error occurred: {e}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileSorterApp()
    ex.show()
    sys.exit(app.exec_())
