import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QColor, QIcon

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.start_button = QPushButton('Start', self)
        self.start_button.setObjectName("startButton")
        self.start_button.clicked.connect(self.start_button_clicked)

        self.close_button = QPushButton('Close', self)
        self.close_button.setObjectName("closeButton")
        self.close_button.clicked.connect(self.close_button_clicked)
        self.close_button.hide()

        vbox = QVBoxLayout()
        vbox.addWidget(self.start_button)
        vbox.addWidget(self.close_button)

        self.setLayout(vbox)
        self.setWindowTitle('Intelligent Image Management Limited')
        self.setFixedSize(500, 500)  # Set the window size to 500x500 pixels

        self.setStyleSheet('''
            #startButton {
                border-radius: 50px;
                background-color: blue;
                color: white;
                font-weight: bold;
                font-size: 16px;
                padding: 20px;
            }
            
            #closeButton {
                border-radius: 50px;
                background-color: green;
                color: white;
                font-weight: bold;
                font-size: 16px;
                padding: 20px;
            }
        ''')

        # Set the window icon
        app_icon = QIcon("icon.jpg")  # Replace with the path to your image
        app.setWindowIcon(app_icon)

    def start_button_clicked(self):
        self.start_button.hide()
        self.close_button.show()
        print("Start button clicked")

    def close_button_clicked(self):
        self.close_button.hide()
        self.start_button.show()
        print("Close button clicked")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = MyApp()
    my_app.show()
    sys.exit(app.exec_())
