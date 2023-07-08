# # import sys
# # import requests
# # from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QDialog, QMessageBox
# # from PyQt5.QtGui import QColor, QIcon, QPixmap
# # from datetime import datetime
# # import socket
# # import uuid
# # from PyQt5.QtCore import QThread, pyqtSignal
# # from PyQt5.QtCore import Qt
# # import psutil
# # from browser_history.browsers import Chrome, Firefox, Edge
# # import datetime

# # class LoginDialog(QDialog):
# #     def __init__(self, parent=None):
# #         super().__init__(parent)
# #         self.initUI()

# #     def initUI(self):
# #         self.setWindowTitle('Login')
# #         self.setFixedSize(250, 150)

# #         self.username_label = QLabel('Username:', self)
# #         self.username_input = QLineEdit(self)
# #         self.password_label = QLabel('Password:', self)
# #         self.password_input = QLineEdit(self)
# #         self.password_input.setEchoMode(QLineEdit.Password)

# #         self.login_button = QPushButton('Login', self)
# #         self.login_button.clicked.connect(self.login_button_clicked)

# #         vbox = QVBoxLayout()
# #         vbox.addWidget(self.username_label)
# #         vbox.addWidget(self.username_input)
# #         vbox.addWidget(self.password_label)
# #         vbox.addWidget(self.password_input)
# #         vbox.addWidget(self.login_button)

# #         self.setLayout(vbox)

# #         # Set URL icon
# #         icon_url = "https://raw.githubusercontent.com/sorkerlimon/image/main/icon.jpg"  # Replace with the URL of your image
# #         response = requests.get(icon_url)
# #         if response.status_code == 200:
# #             pixmap = QPixmap()
# #             pixmap.loadFromData(response.content)
# #             self.setWindowIcon(QIcon(pixmap))

# #     def login_button_clicked(self):
# #         username = self.username_input.text()
# #         password = self.password_input.text()

# #         # Add your login logic here
# #         if username == 'limon' and password == 'limon@123':
# #             self.accept()
# #         else:
# #             QMessageBox.warning(self, 'Login Failed', 'Invalid username or password')



# # class IPThread(QThread):
# #     ip_address_retrieved = pyqtSignal(str, str)

# #     def run(self):
# #         local_ip_address = socket.gethostbyname(socket.gethostname())
# #         public_ip_address = requests.get('https://api.ipify.org').text
# #         self.ip_address_retrieved.emit(local_ip_address, public_ip_address)


# # class MyApp(QWidget):
# #     def __init__(self):
# #         super().__init__()
# #         self.initUI()

# #     def initUI(self):
# #         self.login_dialog = LoginDialog(self)
# #         self.login_dialog.exec_()

# #         if self.login_dialog.result() == QDialog.Accepted:
# #             self.start_button = QPushButton('Start', self)
# #             self.start_button.setObjectName("startButton")
# #             self.start_button.clicked.connect(self.start_button_clicked)

# #             self.close_button = QPushButton('Close', self)
# #             self.close_button.setObjectName("closeButton")
# #             self.close_button.clicked.connect(self.close_button_clicked)
# #             self.close_button.hide()

# #             vbox = QVBoxLayout()
# #             vbox.addWidget(self.start_button)
# #             vbox.addWidget(self.close_button)

# #             self.setLayout(vbox)
# #             self.setWindowTitle('Intelligent Image Management Limited')
# #             self.setFixedSize(500, 500)

# #             self.setStyleSheet('''
# #                 #startButton {
# #                     border-radius: 50px;
# #                     background-color: blue;
# #                     color: white;
# #                     font-weight: bold;
# #                     font-size: 16px;
# #                     padding: 20px;
# #                 }

# #                 #closeButton {
# #                     border-radius: 50px;
# #                     background-color: green;
# #                     color: white;
# #                     font-weight: bold;
# #                     font-size: 16px;
# #                     padding: 20px;
# #                 }
# #             ''')

# #             icon_url = "https://raw.githubusercontent.com/sorkerlimon/image/main/icon.jpg"  # Replace with the URL of your image

# #             response = requests.get(icon_url)
# #             if response.status_code == 200:
# #                 with open('icon.jpg', 'wb') as f:
# #                     f.write(response.content)
# #                 self.setWindowIcon(QIcon('icon.jpg'))

# #         else:
# #             sys.exit()

# #     def start_button_clicked(self):
# #         self.start_button.hide()
# #         self.close_button.show()
# #         # self.start_time = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
# #         self.start_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
        
# #         print("Start button clicked at", self.start_time)

# #         # Start IP retrieval thread
# #         self.ip_thread = IPThread()
# #         self.ip_thread.ip_address_retrieved.connect(self.on_ip_address_retrieved)
# #         self.ip_thread.start()

# #         # Check open browsers
# #         open_browsers = self.get_open_browsers()
# #         if open_browsers:
# #             print("Open browsers:")
# #             for browser in open_browsers:
# #                 print(browser)
# #         else:
# #             print("No browsers currently open.")

# #     def on_ip_address_retrieved(self, local_ip_address, public_ip_address):
# #         print("Local IP address:", local_ip_address)
# #         print("Public IP address:", public_ip_address)

# #         # Retrieve physical address (MAC address)
# #         physical_address = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
# #                                      for ele in range(0, 8 * 6, 8)][::-1])
# #         print("Physical address:", physical_address)

# #     def close_button_clicked(self):
# #         self.close_button.hide()
# #         self.start_button.show()
# #         # self.close_time = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
# #         self.close_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")

# #         print("Close button clicked at", self.close_time)
# #         self.calculate_time_difference()


# #         chrome = Chrome()
# #         chrome_outputs = chrome.fetch_history()

# #         firefox = Firefox()
# #         firefox_outputs = firefox.fetch_history()

# #         edge = Edge()
# #         edge_outputs = edge.fetch_history()

# #         # Combine histories from Chrome, Firefox, and Edge
# #         histories = chrome_outputs.histories + firefox_outputs.histories + edge_outputs.histories
# #         current_date = datetime.date.today()

# #         print("current data : ", current_date)
# #         domain_counts = {}

# #         # Iterate over the combined history and count occurrences of all domain urls
# #         for history in histories:
# #             url = history[1]
# #             timestamp = history[0]
# #             if timestamp.date() == current_date:
# #                 domain = url.split('//')[-1].split('/')[0]  # Extract the domain from the URL
# #                 if domain in domain_counts:
# #                     domain_counts[domain] += 1
# #                 else:
# #                     domain_counts[domain] = 1
# #                 print(f"{url} | {timestamp.strftime('%Y-%m-%d %I:%M:%S %p')}")
# #         # Calculate the total count
# #         total_count = sum(domain_counts.values())

# #         # Calculate the percentage for each domain and print the results
# #         for domain, count in domain_counts.items():
# #             percentage = (count / total_count) * 100
# #             print(f"{domain} Percentage: {percentage:.2f}%")


# #     def calculate_time_difference(self):
# #         start_datetime = datetime.datetime.strptime(self.start_time, "%Y-%m-%d %I:%M:%S %p")
# #         close_datetime = datetime.datetime.strptime(self.close_time, "%Y-%m-%d %I:%M:%S %p")
# #         time_difference = close_datetime - start_datetime

# #         hours = int(time_difference.total_seconds() // 3600)
# #         minutes = int((time_difference.total_seconds() % 3600) // 60)
# #         seconds = int(time_difference.total_seconds() % 60)

# #         print("Time difference:", hours, "hours,", minutes, "minutes,", seconds, "seconds")

# #     def get_open_browsers(self):
# #         browsers = []
# #         for process in psutil.process_iter(['name']):
# #             if process.info['name'] == 'chrome.exe' and 'Google Chrome' not in browsers:
# #                 browsers.append('Google Chrome')
# #             elif process.info['name'] == 'firefox.exe' and 'Mozilla Firefox' not in browsers:
# #                 browsers.append('Mozilla Firefox')
# #             elif process.info['name'] == 'msedge.exe' and 'Microsoft Edge' not in browsers:
# #                 browsers.append('Microsoft Edge')
# #             # Add conditions for other browsers as needed

# #         return browsers


# # if __name__ == '__main__':
# #     app = QApplication(sys.argv)
# #     my_app = MyApp()
# #     my_app.show()
# #     sys.exit(app.exec_())


# #  # second backup
# # import sys
# # import requests
# # from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QDialog, QMessageBox
# # from PyQt5.QtGui import QColor, QIcon, QPixmap
# # from datetime import datetime
# # import socket
# # import uuid
# # from PyQt5.QtCore import QThread, pyqtSignal
# # from PyQt5.QtCore import Qt
# # import psutil
# # from browser_history.browsers import Chrome, Firefox, Edge
# # import datetime
# # from PyQt5.QtCore import QTimer
# # from PyQt5.QtGui import QTextCharFormat, QColor

# # class LoginDialog(QDialog):
# #     def __init__(self, parent=None):
# #         super().__init__(parent)
# #         self.initUI()

# #     def initUI(self):
# #         self.setWindowTitle('Login')
# #         self.setFixedSize(250, 150)

# #         self.username_label = QLabel('Username:', self)
# #         self.username_input = QLineEdit(self)
# #         self.password_label = QLabel('Password:', self)
# #         self.password_input = QLineEdit(self)
# #         self.password_input.setEchoMode(QLineEdit.Password)

# #         self.login_button = QPushButton('Login', self)
# #         self.login_button.clicked.connect(self.login_button_clicked)

# #         vbox = QVBoxLayout()
# #         vbox.addWidget(self.username_label)
# #         vbox.addWidget(self.username_input)
# #         vbox.addWidget(self.password_label)
# #         vbox.addWidget(self.password_input)
# #         vbox.addWidget(self.login_button)

# #         self.setLayout(vbox)

# #         # Set URL icon
# #         icon_url = "https://raw.githubusercontent.com/sorkerlimon/image/main/icon.jpg"  # Replace with the URL of your image
# #         response = requests.get(icon_url)
# #         if response.status_code == 200:
# #             pixmap = QPixmap()
# #             pixmap.loadFromData(response.content)
# #             self.setWindowIcon(QIcon(pixmap))

# #     def login_button_clicked(self):
# #         username = self.username_input.text()
# #         password = self.password_input.text()

# #         # Add your login logic here
# #         if username == 'limon' and password == 'limon@123':
# #             self.accept()
# #         else:
# #             QMessageBox.warning(self, 'Login Failed', 'Invalid username or password')



# # class IPThread(QThread):
# #     ip_address_retrieved = pyqtSignal(str, str)

# #     def run(self):
# #         local_ip_address = socket.gethostbyname(socket.gethostname())
# #         public_ip_address = requests.get('https://api.ipify.org').text
# #         self.ip_address_retrieved.emit(local_ip_address, public_ip_address)


# # class MyApp(QWidget):
# #     def __init__(self):
# #         super().__init__()
# #         self.initUI()

# #     def initUI(self):
# #         self.login_dialog = LoginDialog(self)
# #         self.login_dialog.exec_()

# #         if self.login_dialog.result() == QDialog.Accepted:
# #             self.start_button = QPushButton('Start', self)
# #             self.start_button.setObjectName("startButton")
# #             self.start_button.clicked.connect(self.start_button_clicked)

# #             self.close_button = QPushButton('Close', self)
# #             self.close_button.setObjectName("closeButton")
# #             self.close_button.clicked.connect(self.close_button_clicked)
# #             self.close_button.hide()

# #             self.timer = QTimer()
# #             self.timer.timeout.connect(self.update_time)

# #             self.time_elapsed = datetime.timedelta()

# #             self.timestamp_label = QLabel(self)

# #             vbox = QVBoxLayout()
# #             vbox.addWidget(self.start_button)
# #             vbox.addWidget(self.close_button)
# #             vbox.addWidget(self.timestamp_label) 

# #             self.setLayout(vbox)
# #             self.setWindowTitle('Intelligent Image Management Limited')
# #             self.setFixedSize(500, 500)

# #             self.setStyleSheet('''
# #                 #startButton {
# #                     border-radius: 50px;
# #                     background-color: blue;
# #                     color: white;
# #                     font-weight: bold;
# #                     font-size: 16px;
# #                     padding: 20px;
# #                 }

# #                 #closeButton {
# #                     border-radius: 50px;
# #                     background-color: green;
# #                     color: white;
# #                     font-weight: bold;
# #                     font-size: 16px;
# #                     padding: 20px;
# #                 }
# #             ''')

# #             icon_url = "https://raw.githubusercontent.com/sorkerlimon/image/main/icon.jpg"  # Replace with the URL of your image

# #             response = requests.get(icon_url)
# #             if response.status_code == 200:
# #                 with open('icon.jpg', 'wb') as f:
# #                     f.write(response.content)
# #                 self.setWindowIcon(QIcon('icon.jpg'))

# #         else:
# #             sys.exit()

# #     def start_button_clicked(self):
# #         self.start_button.hide()
# #         self.close_button.show()
# #         self.start_time = datetime.datetime.now()
# #         self.timestamp_label.setText("Start button clicked at {}".format(self.start_time.strftime("%Y-%m-%d %I:%M:%S %p")))
# #         self.timer.start(1000)

# #         # Start IP retrieval thread
# #         self.ip_thread = IPThread()
# #         self.ip_thread.ip_address_retrieved.connect(self.on_ip_address_retrieved)
# #         self.ip_thread.start()

# #         # Check open browsers
# #         open_browsers = self.get_open_browsers()
# #         if open_browsers:
# #             print("Open browsers:")
# #             for browser in open_browsers:
# #                 print(browser)
# #         else:
# #             print("No browsers currently open.")


# #     def update_time(self):
# #         current_time = datetime.datetime.now()
# #         self.time_elapsed = current_time - self.start_time
# #         current_time_str = current_time.strftime("%Y-%m-%d %I:%M:%S %p")
# #         total_seconds = int(self.time_elapsed.total_seconds())

# #         minutes, seconds = divmod(total_seconds, 60)
# #         hours, minutes = divmod(minutes, 60)
# #         days, hours = divmod(hours, 24)

# #         time_parts = []
# #         if days > 0:
# #             time_parts.append("{} day{}".format(days, "s" if days > 1 else ""))
# #         if hours > 0:
# #             time_parts.append("{} hour{}".format(hours, "s" if hours > 1 else ""))
# #         if minutes > 0:
# #             time_parts.append("{} minute{}".format(minutes, "s" if minutes > 1 else ""))
# #         if seconds > 0:
# #             time_parts.append("{} second{}".format(seconds, "s" if seconds > 1 else ""))

# #         elapsed_time_str = ', '.join(time_parts)

# #         current_time_html = '<span style="font-weight: bold; color: blue;">Current time:</span> {}'.format(current_time_str)
# #         elapsed_time_html = '<span style="font-weight: bold; color: green; border: 50px solid;">Elapsed time:</span> {}'.format(elapsed_time_str)

# #         timestamp_html = '<div style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100%; text-align: center;">{}<br>{}</div>'.format(current_time_html, elapsed_time_html)

# #         self.timestamp_label.setText(timestamp_html)






# #     def on_ip_address_retrieved(self, local_ip_address, public_ip_address):
# #         print("Local IP address:", local_ip_address)
# #         print("Public IP address:", public_ip_address)

# #         # Retrieve physical address (MAC address)
# #         physical_address = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
# #                                      for ele in range(0, 8 * 6, 8)][::-1])
# #         print("Physical address:", physical_address)

# #     def close_button_clicked(self):
# #         self.close_button.hide()
# #         self.start_button.show()
# #         self.timer.stop()
        
# #         # self.close_time = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
# #         self.close_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")

# #         print("Close button clicked at", self.close_time)
# #         self.calculate_time_difference()


# #         chrome = Chrome()
# #         chrome_outputs = chrome.fetch_history()

# #         firefox = Firefox()
# #         firefox_outputs = firefox.fetch_history()

# #         edge = Edge()
# #         edge_outputs = edge.fetch_history()

# #         # Combine histories from Chrome, Firefox, and Edge
# #         histories = chrome_outputs.histories + firefox_outputs.histories + edge_outputs.histories
# #         current_date = datetime.date.today()

# #         print("current data : ", current_date)
# #         domain_counts = {}

# #         # Iterate over the combined history and count occurrences of all domain urls
# #         for history in histories:
# #             url = history[1]
# #             timestamp = history[0]
# #             if timestamp.date() == current_date:
# #                 domain = url.split('//')[-1].split('/')[0]  # Extract the domain from the URL
# #                 if domain in domain_counts:
# #                     domain_counts[domain] += 1
# #                 else:
# #                     domain_counts[domain] = 1
# #                 print(f"{url} | {timestamp.strftime('%Y-%m-%d %I:%M:%S %p')}")
# #         # Calculate the total count
# #         total_count = sum(domain_counts.values())

# #         # Calculate the percentage for each domain and print the results
# #         for domain, count in domain_counts.items():
# #             percentage = (count / total_count) * 100
# #             print(f"{domain} Percentage: {percentage:.2f}%")


# #     def calculate_time_difference(self):
# #         close_datetime = datetime.datetime.strptime(self.close_time, "%Y-%m-%d %I:%M:%S %p")
# #         time_difference = close_datetime - self.start_time

# #         hours = int(time_difference.total_seconds() // 3600)
# #         minutes = int((time_difference.total_seconds() % 3600) // 60)
# #         seconds = int(time_difference.total_seconds() % 60)

# #         print("Time difference:", hours, "hours,", minutes, "minutes,", seconds, "seconds")


# #     def get_open_browsers(self):
# #         browsers = []
# #         for process in psutil.process_iter(['name']):
# #             if process.info['name'] == 'chrome.exe' and 'Google Chrome' not in browsers:
# #                 browsers.append('Google Chrome')
# #             elif process.info['name'] == 'firefox.exe' and 'Mozilla Firefox' not in browsers:
# #                 browsers.append('Mozilla Firefox')
# #             elif process.info['name'] == 'msedge.exe' and 'Microsoft Edge' not in browsers:
# #                 browsers.append('Microsoft Edge')
# #             # Add conditions for other browsers as needed

# #         return browsers


# # if __name__ == '__main__':
# #     app = QApplication(sys.argv)
# #     my_app = MyApp()
# #     my_app.show()
# #     sys.exit(app.exec_())


#     #pyinstaller --onefile --noconsole
#     #pyinstaller --onefile --icon=icon.ico


# # import sys
# # import requests
# # from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QDialog, QMessageBox
# # from PyQt5.QtGui import QColor, QIcon, QPixmap
# # from datetime import datetime
# # import socket
# # import uuid
# # from PyQt5.QtCore import QThread, pyqtSignal
# # from PyQt5.QtCore import Qt
# # import psutil
# # from browser_history.browsers import Chrome, Firefox, Edge
# # import datetime
# # from PyQt5.QtCore import QTimer
# # from PyQt5.QtGui import QTextCharFormat, QColor
# # from pytz import timezone


# # class LoginDialog(QDialog):
# #     def __init__(self, parent=None):
# #         super().__init__(parent)
# #         self.initUI()

# #     def initUI(self):
# #         self.setWindowTitle('Login')
# #         self.setFixedSize(250, 150)

# #         self.username_label = QLabel('Username:', self)
# #         self.username_input = QLineEdit(self)
# #         self.password_label = QLabel('Password:', self)
# #         self.password_input = QLineEdit(self)
# #         self.password_input.setEchoMode(QLineEdit.Password)

# #         self.login_button = QPushButton('Login', self)
# #         self.login_button.clicked.connect(self.login_button_clicked)

# #         vbox = QVBoxLayout()
# #         vbox.addWidget(self.username_label)
# #         vbox.addWidget(self.username_input)
# #         vbox.addWidget(self.password_label)
# #         vbox.addWidget(self.password_input)
# #         vbox.addWidget(self.login_button)

# #         self.setLayout(vbox)

# #         # Set URL icon
# #         icon_url = "https://raw.githubusercontent.com/sorkerlimon/image/main/icon.jpg"  # Replace with the URL of your image
# #         response = requests.get(icon_url)
# #         if response.status_code == 200:
# #             pixmap = QPixmap()
# #             pixmap.loadFromData(response.content)
# #             self.setWindowIcon(QIcon(pixmap))

# #     def login_button_clicked(self):
# #         username = self.username_input.text()
# #         password = self.password_input.text()

# #         # Add your login logic here
# #         if username == 'limon' and password == 'limon@123':
# #             self.accept()
# #         else:
# #             QMessageBox.warning(self, 'Login Failed', 'Invalid username or password')



# # class IPThread(QThread):
# #     ip_address_retrieved = pyqtSignal(str, str)

# #     def run(self):
# #         local_ip_address = socket.gethostbyname(socket.gethostname())
# #         public_ip_address = requests.get('https://api.ipify.org').text
# #         self.ip_address_retrieved.emit(local_ip_address, public_ip_address)


# # class MyApp(QWidget):
# #     def __init__(self):
# #         super().__init__()
# #         self.initUI()

# #     def initUI(self):
# #         self.login_dialog = LoginDialog(self)
# #         self.login_dialog.exec_()

# #         if self.login_dialog.result() == QDialog.Accepted:
# #             self.start_button = QPushButton('Start', self)
# #             self.start_button.setObjectName("startButton")
# #             self.start_button.clicked.connect(self.start_button_clicked)

# #             self.close_button = QPushButton('Close', self)
# #             self.close_button.setObjectName("closeButton")
# #             self.close_button.clicked.connect(self.close_button_clicked)
# #             self.close_button.hide()

# #             self.timer = QTimer()
# #             self.timer.timeout.connect(self.update_time)

# #             self.time_elapsed = datetime.timedelta()

# #             self.timestamp_label = QLabel(self)

# #             vbox = QVBoxLayout()
# #             vbox.addWidget(self.start_button)
# #             vbox.addWidget(self.close_button)
# #             vbox.addWidget(self.timestamp_label) 

# #             self.setLayout(vbox)
# #             self.setWindowTitle('Intelligent Image Management Limited')
# #             self.setFixedSize(500, 500)

# #             self.setStyleSheet('''
# #                 #startButton {
# #                     border-radius: 50px;
# #                     background-color: blue;
# #                     color: white;
# #                     font-weight: bold;
# #                     font-size: 16px;
# #                     padding: 20px;
# #                 }

# #                 #closeButton {
# #                     border-radius: 50px;
# #                     background-color: green;
# #                     color: white;
# #                     font-weight: bold;
# #                     font-size: 16px;
# #                     padding: 20px;
# #                 }
# #             ''')

# #             icon_url = "https://raw.githubusercontent.com/sorkerlimon/image/main/icon.jpg"  # Replace with the URL of your image

# #             response = requests.get(icon_url)
# #             if response.status_code == 200:
# #                 with open('icon.jpg', 'wb') as f:
# #                     f.write(response.content)
# #                 self.setWindowIcon(QIcon('icon.jpg'))

# #         else:
# #             sys.exit()

# #     def start_button_clicked(self):
# #         self.start_button.hide()
# #         self.close_button.show()
# #         self.start_time = datetime.datetime.now()
# #         # self.start_time = datetime.now(timezone('Asia/Dhaka'))
# #         self.timestamp_label.setText("Start button clicked at {}".format(self.start_time.strftime("%Y-%m-%d %I:%M:%S %p")))
# #         self.timer.start(1000)

# #         # Start IP retrieval thread
# #         self.ip_thread = IPThread()
# #         self.ip_thread.ip_address_retrieved.connect(self.on_ip_address_retrieved)
# #         self.ip_thread.start()

# #         # Check open browsers
# #         open_browsers = self.get_open_browsers()
# #         if open_browsers:
# #             print("Open browsers:")
# #             for browser in open_browsers:
# #                 print(browser)
# #         else:
# #             print("No browsers currently open.")


# #     def update_time(self):
# #         current_time = datetime.datetime.now()
# #         self.time_elapsed = current_time - self.start_time
# #         current_time_str = current_time.strftime("%Y-%m-%d %I:%M:%S %p")
# #         total_seconds = int(self.time_elapsed.total_seconds())

# #         minutes, seconds = divmod(total_seconds, 60)
# #         hours, minutes = divmod(minutes, 60)
# #         days, hours = divmod(hours, 24)

# #         time_parts = []
# #         if days > 0:
# #             time_parts.append("{} day{}".format(days, "s" if days > 1 else ""))
# #         if hours > 0:
# #             time_parts.append("{} hour{}".format(hours, "s" if hours > 1 else ""))
# #         if minutes > 0:
# #             time_parts.append("{} minute{}".format(minutes, "s" if minutes > 1 else ""))
# #         if seconds > 0:
# #             time_parts.append("{} second{}".format(seconds, "s" if seconds > 1 else ""))

# #         elapsed_time_str = ', '.join(time_parts)

# #         current_time_html = '<span style="font-weight: bold; color: blue;">Current time:</span> {}'.format(current_time_str)
# #         elapsed_time_html = '<span style="font-weight: bold; color: green; border: 50px solid;">Working time:</span> {}'.format(elapsed_time_str)

# #         timestamp_html = '<div style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100%; text-align: center;">{}<br>{}</div>'.format(current_time_html, elapsed_time_html)

# #         self.timestamp_label.setText(timestamp_html)






# #     def on_ip_address_retrieved(self, local_ip_address, public_ip_address):
# #         print("Local IP address:", local_ip_address)
# #         print("Public IP address:", public_ip_address)

# #         # Retrieve physical address (MAC address)
# #         physical_address = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
# #                                      for ele in range(0, 8 * 6, 8)][::-1])
# #         print("Physical address:", physical_address)

# #     def close_button_clicked(self):
# #         self.close_button.hide()
# #         self.start_button.show()
# #         self.timer.stop()
        
# #         self.stop_time = datetime.datetime.now()
# #         # self.stop_time = datetime.now(timezone('Asia/Dhaka'))
# #         self.close_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
        
# #         self.start_time_str = self.start_time.strftime("%I:%M:%S %p")  # Format start time as HH:MM:SS AM/PM
# #         self.close_time_str = self.stop_time.strftime("%I:%M:%S %p")  # Format close time as HH:MM:SS AM/PM



# #         print("Start time:", self.start_time_str)
# #         print("Close time:", self.close_time_str)

# #         print("Close button clicked at", self.close_time)
# #         self.calculate_time_difference()


# #         chrome = Chrome()
# #         chrome_outputs = chrome.fetch_history()

# #         firefox = Firefox()
# #         firefox_outputs = firefox.fetch_history()

# #         edge = Edge()
# #         edge_outputs = edge.fetch_history()

# #         # Combine histories from Chrome, Firefox, and Edge
# #         histories = chrome_outputs.histories + firefox_outputs.histories + edge_outputs.histories
# #         current_date = datetime.date.today()

# #         print("current data : ", current_date)
# #         domain_counts = {}

# #         # Iterate over the combined history and count occurrences of all domain urls
# #         for history in histories:
# #             url = history[1]
# #             timestamp = history[0]
# #             if timestamp.date() == current_date and self.start_time_str <= str(timestamp.time()) <= self.close_time_str:
# #                 domain = url.split('//')[-1].split('/')[0]  # Extract the domain from the URL
# #                 if domain in domain_counts:
# #                     domain_counts[domain] += 1
# #                 else:
# #                     domain_counts[domain] = 1
# #                 print(f"{url} | {timestamp.strftime('%Y-%m-%d %I:%M:%S %p')}")

# #         total_count = sum(domain_counts.values())

# #         # Calculate the percentage for each domain and print the results
# #         for domain, count in domain_counts.items():
# #             percentage = (count / total_count) * 100
# #             print(f"{domain} Percentage: {percentage:.2f}%")


# #     def calculate_time_difference(self):
# #         close_datetime = datetime.datetime.strptime(self.close_time, "%Y-%m-%d %I:%M:%S %p")
# #         time_difference = close_datetime - self.start_time

# #         hours = int(time_difference.total_seconds() // 3600)
# #         minutes = int((time_difference.total_seconds() % 3600) // 60)
# #         seconds = int(time_difference.total_seconds() % 60)

# #         print("Time difference:", hours, "hours,", minutes, "minutes,", seconds, "seconds")


# #     def get_open_browsers(self):
# #         browsers = []
# #         for process in psutil.process_iter(['name']):
# #             if process.info['name'] == 'chrome.exe' and 'Google Chrome' not in browsers:
# #                 browsers.append('Google Chrome')
# #             elif process.info['name'] == 'firefox.exe' and 'Mozilla Firefox' not in browsers:
# #                 browsers.append('Mozilla Firefox')
# #             elif process.info['name'] == 'msedge.exe' and 'Microsoft Edge' not in browsers:
# #                 browsers.append('Microsoft Edge')
# #             # Add conditions for other browsers as needed

# #         return browsers


# # if __name__ == '__main__':
# #     app = QApplication(sys.argv)
# #     my_app = MyApp()
# #     my_app.show()
# #     sys.exit(app.exec_())


# #     #pyinstaller --onefile --noconsole
# #     #pyinstaller --onefile --icon=icon.ico






# # Last Backup

# import sys
# import requests
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QDialog, QMessageBox
# from PyQt5.QtGui import QColor, QIcon, QPixmap
# from datetime import datetime
# import socket
# import uuid
# from PyQt5.QtCore import QThread, pyqtSignal
# from PyQt5.QtCore import Qt
# import psutil
# from browser_history.browsers import Chrome, Firefox, Edge
# import datetime
# from PyQt5.QtCore import QTimer
# from PyQt5.QtGui import QTextCharFormat, QColor
# from pytz import timezone


# class LoginDialog(QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle('Login')
#         self.setFixedSize(250, 150)

#         self.username_label = QLabel('Username:', self)
#         self.username_input = QLineEdit(self)
#         self.password_label = QLabel('Password:', self)
#         self.password_input = QLineEdit(self)
#         self.password_input.setEchoMode(QLineEdit.Password)

#         self.login_button = QPushButton('Login', self)
#         self.login_button.clicked.connect(self.login_button_clicked)

#         vbox = QVBoxLayout()
#         vbox.addWidget(self.username_label)
#         vbox.addWidget(self.username_input)
#         vbox.addWidget(self.password_label)
#         vbox.addWidget(self.password_input)
#         vbox.addWidget(self.login_button)

#         self.setLayout(vbox)

#         # Set URL icon
#         icon_url = "https://raw.githubusercontent.com/sorkerlimon/image/main/icon.jpg"  # Replace with the URL of your image
#         response = requests.get(icon_url)
#         if response.status_code == 200:
#             pixmap = QPixmap()
#             pixmap.loadFromData(response.content)
#             self.setWindowIcon(QIcon(pixmap))

#     def login_button_clicked(self):
#         username = self.username_input.text()
#         password = self.password_input.text()

#         # Add your login logic here
#         if username == 'limon' and password == 'limon@123':
#             self.accept()
#         else:
#             QMessageBox.warning(self, 'Login Failed', 'Invalid username or password')



# class IPThread(QThread):
#     ip_address_retrieved = pyqtSignal(str, str)

#     def run(self):
#         local_ip_address = socket.gethostbyname(socket.gethostname())
#         public_ip_address = requests.get('https://api.ipify.org').text
#         self.ip_address_retrieved.emit(local_ip_address, public_ip_address)


# class MyApp(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.login_dialog = LoginDialog(self)
#         self.login_dialog.exec_()

#         if self.login_dialog.result() == QDialog.Accepted:
#             self.start_button = QPushButton('Start', self)
#             self.start_button.setObjectName("startButton")
#             self.start_button.clicked.connect(self.start_button_clicked)

#             self.close_button = QPushButton('Close', self)
#             self.close_button.setObjectName("closeButton")
#             self.close_button.clicked.connect(self.close_button_clicked)
#             self.close_button.hide()

#             self.timer = QTimer()
#             self.timer.timeout.connect(self.update_time)

#             self.time_elapsed = datetime.timedelta()

#             self.timestamp_label = QLabel(self)

#             vbox = QVBoxLayout()
#             vbox.addWidget(self.start_button)
#             vbox.addWidget(self.close_button)
#             vbox.addWidget(self.timestamp_label) 

#             self.setLayout(vbox)
#             self.setWindowTitle('Intelligent Image Management Limited')
#             self.setFixedSize(500, 500)

#             self.setStyleSheet('''
#                 #startButton {
#                     border-radius: 50px;
#                     background-color: blue;
#                     color: white;
#                     font-weight: bold;
#                     font-size: 16px;
#                     padding: 20px;
#                 }

#                 #closeButton {
#                     border-radius: 50px;
#                     background-color: green;
#                     color: white;
#                     font-weight: bold;
#                     font-size: 16px;
#                     padding: 20px;
#                 }
#             ''')

#             icon_url = "https://raw.githubusercontent.com/sorkerlimon/image/main/icon.jpg"  # Replace with the URL of your image

#             response = requests.get(icon_url)
#             if response.status_code == 200:
#                 with open('icon.jpg', 'wb') as f:
#                     f.write(response.content)
#                 self.setWindowIcon(QIcon('icon.jpg'))

#         else:
#             sys.exit()

#     def start_button_clicked(self):
#         self.start_button.hide()
#         self.close_button.show()
#         self.start_time = datetime.datetime.now()
#         # self.start_time = datetime.now(timezone('Asia/Dhaka'))
#         self.timestamp_label.setText("Start button clicked at {}".format(self.start_time.strftime("%Y-%m-%d %I:%M:%S %p")))
#         self.timer.start(1000)

#         # Start IP retrieval thread
#         self.ip_thread = IPThread()
#         self.ip_thread.ip_address_retrieved.connect(self.on_ip_address_retrieved)
#         self.ip_thread.start()

#         # Check open browsers
#         open_browsers = self.get_open_browsers()
#         if open_browsers:
#             print("Open browsers:")
#             for browser in open_browsers:
#                 print(browser)
#         else:
#             print("No browsers currently open.")


#     def update_time(self):
#         current_time = datetime.datetime.now()
#         self.time_elapsed = current_time - self.start_time
#         current_time_str = current_time.strftime("%Y-%m-%d %I:%M:%S %p")
#         total_seconds = int(self.time_elapsed.total_seconds())

#         minutes, seconds = divmod(total_seconds, 60)
#         hours, minutes = divmod(minutes, 60)
#         days, hours = divmod(hours, 24)

#         time_parts = []
#         if days > 0:
#             time_parts.append("{} day{}".format(days, "s" if days > 1 else ""))
#         if hours > 0:
#             time_parts.append("{} hour{}".format(hours, "s" if hours > 1 else ""))
#         if minutes > 0:
#             time_parts.append("{} minute{}".format(minutes, "s" if minutes > 1 else ""))
#         if seconds > 0:
#             time_parts.append("{} second{}".format(seconds, "s" if seconds > 1 else ""))

#         elapsed_time_str = ', '.join(time_parts)

#         current_time_html = '<span style="font-weight: bold; color: blue;">Current time:</span> {}'.format(current_time_str)
#         elapsed_time_html = '<span style="font-weight: bold; color: green; border: 50px solid;">Working time:</span> {}'.format(elapsed_time_str)

#         timestamp_html = '<div style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100%; text-align: center;">{}<br>{}</div>'.format(current_time_html, elapsed_time_html)

#         self.timestamp_label.setText(timestamp_html)






#     def on_ip_address_retrieved(self, local_ip_address, public_ip_address):
#         print("Local IP address:", local_ip_address)
#         print("Public IP address:", public_ip_address)

#         # Retrieve physical address (MAC address)
#         physical_address = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
#                                      for ele in range(0, 8 * 6, 8)][::-1])
#         print("Physical address:", physical_address)

#     def close_button_clicked(self):
#         self.close_button.hide()
#         self.start_button.show()
#         self.timer.stop()
        
#         self.stop_time = datetime.datetime.now()
#         # self.stop_time = datetime.now(timezone('Asia/Dhaka'))
#         self.close_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
        
#         # self.start_time_str = self.start_time.strftime("%I:%M:%S %p")  # Format start time as HH:MM:SS AM/PM
#         # self.close_time_str = self.stop_time.strftime("%I:%M:%S %p")  # Format close time as HH:MM:SS AM/PM

#         self.start_time_str = datetime.datetime.strptime(self.start_time.strftime("%I:%M:%S %p"), "%I:%M:%S %p").time()
#         self.close_time_str = datetime.datetime.strptime(self.stop_time.strftime("%I:%M:%S %p"), "%I:%M:%S %p").time()

#         # self.start_time_str = datetime.time(10, 1, 34)  # 11:18:34 AM
#         # self.close_time_str = datetime.time(10, 4, 34)    # 11:20:34 AM

#         print("Start time:", self.start_time_str)
#         print("Close time:", self.close_time_str)

#         print("Close button clicked at", self.close_time)
#         self.calculate_time_difference()


#         chrome = Chrome()
#         chrome_outputs = chrome.fetch_history()

#         firefox = Firefox()
#         firefox_outputs = firefox.fetch_history()

#         edge = Edge()
#         edge_outputs = edge.fetch_history()

#         # Combine histories from Chrome, Firefox, and Edge
#         histories = chrome_outputs.histories + firefox_outputs.histories + edge_outputs.histories
#         current_date = datetime.date.today()

#         print("current data : ", current_date)
#         domain_counts = {}

#         # Iterate over the combined history and count occurrences of all domain urls
#         for history in histories:
#             url = history[1]
#             timestamp = history[0]
#             if timestamp.date() == current_date and self.start_time_str <= timestamp.time() <= self.close_time_str:
#                 domain = url.split('//')[-1].split('/')[0]  # Extract the domain from the URL
#                 if domain in domain_counts:
#                     domain_counts[domain] += 1
#                 else:
#                     domain_counts[domain] = 1
#                 print(f"{url} | {timestamp.strftime('%Y-%m-%d %I:%M:%S %p')}")

#         total_count = sum(domain_counts.values())

#         # Calculate the percentage for each domain and print the results
#         for domain, count in domain_counts.items():
#             percentage = (count / total_count) * 100
#             print(f"{domain} Percentage: {percentage:.2f}%")


#     def calculate_time_difference(self):
#         close_datetime = datetime.datetime.strptime(self.close_time, "%Y-%m-%d %I:%M:%S %p")
#         time_difference = close_datetime - self.start_time

#         hours = int(time_difference.total_seconds() // 3600)
#         minutes = int((time_difference.total_seconds() % 3600) // 60)
#         seconds = int(time_difference.total_seconds() % 60)

#         print("Time difference:", hours, "hours,", minutes, "minutes,", seconds, "seconds")


#     def get_open_browsers(self):
#         browsers = []
#         for process in psutil.process_iter(['name']):
#             if process.info['name'] == 'chrome.exe' and 'Google Chrome' not in browsers:
#                 browsers.append('Google Chrome')
#             elif process.info['name'] == 'firefox.exe' and 'Mozilla Firefox' not in browsers:
#                 browsers.append('Mozilla Firefox')
#             elif process.info['name'] == 'msedge.exe' and 'Microsoft Edge' not in browsers:
#                 browsers.append('Microsoft Edge')
#             # Add conditions for other browsers as needed

#         return browsers


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     my_app = MyApp()
#     my_app.show()
#     sys.exit(app.exec_())


#     #pyinstaller --onefile --noconsole
#     #pyinstaller --onefile --icon=icon.ico










# 07-06-2023

import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QDialog, QMessageBox
from PyQt5.QtGui import QColor, QIcon, QPixmap
from datetime import datetime
import socket
import uuid
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtCore import Qt
import psutil
from browser_history.browsers import Chrome, Firefox, Edge
import datetime
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QTextCharFormat, QColor
from pytz import timezone


class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Login')
        self.setFixedSize(250, 150)

        self.username_label = QLabel('Username:', self)
        self.username_input = QLineEdit(self)
        self.password_label = QLabel('Password:', self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton('Login', self)
        self.login_button.clicked.connect(self.login_button_clicked)

        vbox = QVBoxLayout()
        vbox.addWidget(self.username_label)
        vbox.addWidget(self.username_input)
        vbox.addWidget(self.password_label)
        vbox.addWidget(self.password_input)
        vbox.addWidget(self.login_button)

        self.setLayout(vbox)

        # Set URL icon
        icon_url = "https://raw.githubusercontent.com/sorkerlimon/image/main/icon.jpg"  # Replace with the URL of your image
        response = requests.get(icon_url)
        if response.status_code == 200:
            pixmap = QPixmap()
            pixmap.loadFromData(response.content)
            self.setWindowIcon(QIcon(pixmap))

    def login_button_clicked(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Add your login logic here
        if username == 'limon' and password == 'limon@123':
            self.accept()
        else:
            QMessageBox.warning(self, 'Login Failed', 'Invalid username or password')



class IPThread(QThread):
    ip_address_retrieved = pyqtSignal(str, str)

    def run(self):
        local_ip_address = socket.gethostbyname(socket.gethostname())
        public_ip_address = requests.get('https://api.ipify.org').text
        self.ip_address_retrieved.emit(local_ip_address, public_ip_address)


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.login_dialog = LoginDialog(self)
        self.login_dialog.exec_()

        if self.login_dialog.result() == QDialog.Accepted:
            self.start_button = QPushButton('Start', self)
            self.start_button.setObjectName("startButton")
            self.start_button.clicked.connect(self.start_button_clicked)

            self.close_button = QPushButton('Close', self)
            self.close_button.setObjectName("closeButton")
            self.close_button.clicked.connect(self.close_button_clicked)
            self.close_button.hide()

            self.timer = QTimer()
            self.timer.timeout.connect(self.update_time)

            self.time_elapsed = datetime.timedelta()

            self.timestamp_label = QLabel(self)

            vbox = QVBoxLayout()
            vbox.addWidget(self.start_button)
            vbox.addWidget(self.close_button)
            vbox.addWidget(self.timestamp_label) 

            self.setLayout(vbox)
            self.setWindowTitle('Intelligent Image Management Limited')
            self.setFixedSize(500, 500)

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

            icon_url = "https://raw.githubusercontent.com/sorkerlimon/image/main/icon.jpg"  # Replace with the URL of your image

            response = requests.get(icon_url)
            if response.status_code == 200:
                with open('icon.jpg', 'wb') as f:
                    f.write(response.content)
                self.setWindowIcon(QIcon('icon.jpg'))

        else:
            sys.exit()

    def start_button_clicked(self):
        self.start_button.hide()
        self.close_button.show()
        self.start_time = datetime.datetime.now()
        # self.start_time = datetime.now(timezone('Asia/Dhaka'))
        self.timestamp_label.setText("Start button clicked at {}".format(self.start_time.strftime("%Y-%m-%d %I:%M:%S %p")))
        self.timer.start(1000)

        # Start IP retrieval thread
        self.ip_thread = IPThread()
        self.ip_thread.ip_address_retrieved.connect(self.on_ip_address_retrieved)
        self.ip_thread.start()

        # Check open browsers
        open_browsers = self.get_open_browsers()
        if open_browsers:
            print("Open browsers:")
            for browser in open_browsers:
                print(browser)
        else:
            print("No browsers currently open.")


    def update_time(self):
        current_time = datetime.datetime.now()
        self.time_elapsed = current_time - self.start_time
        current_time_str = current_time.strftime("%Y-%m-%d %I:%M:%S %p")
        total_seconds = int(self.time_elapsed.total_seconds())

        minutes, seconds = divmod(total_seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)

        time_parts = []
        if days > 0:
            time_parts.append("{} day{}".format(days, "s" if days > 1 else ""))
        if hours > 0:
            time_parts.append("{} hour{}".format(hours, "s" if hours > 1 else ""))
        if minutes > 0:
            time_parts.append("{} minute{}".format(minutes, "s" if minutes > 1 else ""))
        if seconds > 0:
            time_parts.append("{} second{}".format(seconds, "s" if seconds > 1 else ""))

        elapsed_time_str = ', '.join(time_parts)

        current_time_html = '<span style="font-weight: bold; color: blue;">Current time:</span> {}'.format(current_time_str)
        elapsed_time_html = '<span style="font-weight: bold; color: green; border: 50px solid;">Working time:</span> {}'.format(elapsed_time_str)

        timestamp_html = '<div style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100%; text-align: center;">{}<br>{}</div>'.format(current_time_html, elapsed_time_html)

        self.timestamp_label.setText(timestamp_html)






    def on_ip_address_retrieved(self, local_ip_address, public_ip_address):
        print("Local IP address:", local_ip_address)
        print("Public IP address:", public_ip_address)

        # Retrieve physical address (MAC address)
        physical_address = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
                                     for ele in range(0, 8 * 6, 8)][::-1])
        print("Physical address:", physical_address)

    def close_button_clicked(self):
        self.close_button.hide()
        self.start_button.show()
        self.timer.stop()
        
        self.stop_time = datetime.datetime.now()
        # self.stop_time = datetime.now(timezone('Asia/Dhaka'))
        self.close_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
        
        # self.start_time_str = self.start_time.strftime("%I:%M:%S %p")  # Format start time as HH:MM:SS AM/PM
        # self.close_time_str = self.stop_time.strftime("%I:%M:%S %p")  # Format close time as HH:MM:SS AM/PM

        self.start_time_str = datetime.datetime.strptime(self.start_time.strftime("%I:%M:%S %p"), "%I:%M:%S %p").time()
        self.close_time_str = datetime.datetime.strptime(self.stop_time.strftime("%I:%M:%S %p"), "%I:%M:%S %p").time()

        # self.start_time_str = datetime.time(10, 1, 34)  # 11:18:34 AM
        # self.close_time_str = datetime.time(10, 4, 34)    # 11:20:34 AM

        print("Start time:", self.start_time_str)
        print("Close time:", self.close_time_str)

        print("Close button clicked at", self.close_time)
        self.calculate_time_difference()


        chrome = Chrome()
        chrome_outputs = chrome.fetch_history()

        firefox = Firefox()
        firefox_outputs = firefox.fetch_history()

        edge = Edge()
        edge_outputs = edge.fetch_history()

        # Combine histories from Chrome, Firefox, and Edge
        histories = chrome_outputs.histories + firefox_outputs.histories + edge_outputs.histories
        current_date = datetime.date.today()

        print("current data : ", current_date)
        domain_counts = {}

        # Iterate over the combined history and count occurrences of all domain urls
        for history in histories:
            url = history[1]
            timestamp = history[0]
            if timestamp.date() == current_date and self.start_time_str <= timestamp.time() <= self.close_time_str:
                domain = url.split('//')[-1].split('/')[0]  # Extract the domain from the URL
                if domain in domain_counts:
                    domain_counts[domain] += 1
                else:
                    domain_counts[domain] = 1
                print(f"{url} | {timestamp.strftime('%Y-%m-%d %I:%M:%S %p')}")

        total_count = sum(domain_counts.values())

        # Calculate the percentage for each domain and print the results
        for domain, count in domain_counts.items():
            percentage = (count / total_count) * 100
            print(f"{domain} Percentage: {percentage:.2f}%")


    def calculate_time_difference(self):
        close_datetime = datetime.datetime.strptime(self.close_time, "%Y-%m-%d %I:%M:%S %p")
        time_difference = close_datetime - self.start_time

        hours = int(time_difference.total_seconds() // 3600)
        minutes = int((time_difference.total_seconds() % 3600) // 60)
        seconds = int(time_difference.total_seconds() % 60)

        print("Time difference:", hours, "hours,", minutes, "minutes,", seconds, "seconds")


    def get_open_browsers(self):
        browsers = []
        for process in psutil.process_iter(['name']):
            if process.info['name'] == 'chrome.exe' and 'Google Chrome' not in browsers:
                browsers.append('Google Chrome')
            elif process.info['name'] == 'firefox.exe' and 'Mozilla Firefox' not in browsers:
                browsers.append('Mozilla Firefox')
            elif process.info['name'] == 'msedge.exe' and 'Microsoft Edge' not in browsers:
                browsers.append('Microsoft Edge')
            # Add conditions for other browsers as needed

        return browsers


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = MyApp()
    my_app.show()
    sys.exit(app.exec_())


    #pyinstaller --onefile --noconsole
    #pyinstaller --onefile --icon=icon.ico












    import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QDialog, QMessageBox
from PyQt5.QtGui import QColor, QIcon, QPixmap
from datetime import datetime
import socket
import uuid
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtCore import Qt
import psutil
from browser_history.browsers import Chrome, Firefox, Edge
import datetime
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QTextCharFormat, QColor
from pytz import timezone
import mysql.connector
from mysql.connector import Error

class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        self.user_id = None

    def initUI(self):
        self.setWindowTitle('Login')
        self.setFixedSize(250, 150)

        self.username_label = QLabel('Username:', self)
        self.username_input = QLineEdit(self)
        self.password_label = QLabel('Password:', self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton('Login', self)
        self.login_button.clicked.connect(self.login_button_clicked)

        vbox = QVBoxLayout()
        vbox.addWidget(self.username_label)
        vbox.addWidget(self.username_input)
        vbox.addWidget(self.password_label)
        vbox.addWidget(self.password_input)
        vbox.addWidget(self.login_button)

        self.setLayout(vbox)

        # Set URL icon
        icon_url = "https://raw.githubusercontent.com/sorkerlimon/image/main/icon.jpg"  # Replace with the URL of your image
        response = requests.get(icon_url)
        if response.status_code == 200:
            pixmap = QPixmap()
            pixmap.loadFromData(response.content)
            self.setWindowIcon(QIcon(pixmap))

    def login_button_clicked(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # # Add your login logic here
        # if username == 'limon' and password == 'limon@123':
        #     self.accept()
        # else:
        #     QMessageBox.warning(self, 'Login Failed', 'Invalid username or password')

                # Connect to the database
        try:
            cnx = mysql.connector.connect(
                host='192.168.100.25',
                port=3306,  # Specify the port number here
                user='iimi',
                password='limon@123',
                database='workflow'
            )

            cursor = cnx.cursor()

            # Execute the query
            query = "SELECT * FROM users WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))

            # Fetch the result
            result = cursor.fetchone()

            if result is not None:
                self.user_id = result[0]
                QMessageBox.information(self, 'Login Successful', 'Login successful!')
                self.accept()
            else:
                QMessageBox.warning(self, 'Login Failed', 'Invalid username or password')

            # Close the database connection
            cursor.close()
            cnx.close()

        except mysql.connector.Error as err:
            QMessageBox.critical(self, 'Database Error', f"Failed to connect to the database: {err}")



class IPThread(QThread):
    ip_address_retrieved = pyqtSignal(str, str)

    def run(self):
        local_ip_address = socket.gethostbyname(socket.gethostname())
        public_ip_address = requests.get('https://api.ipify.org').text
        self.ip_address_retrieved.emit(local_ip_address, public_ip_address)


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.login_dialog = LoginDialog(self)
        self.login_dialog.exec_()

        if self.login_dialog.result() == QDialog.Accepted:
            self.start_button = QPushButton('Start', self)
            self.start_button.setObjectName("startButton")
            self.start_button.clicked.connect(self.start_button_clicked)

            self.close_button = QPushButton('Close', self)
            self.close_button.setObjectName("closeButton")
            self.close_button.clicked.connect(self.close_button_clicked)
            self.close_button.hide()

            self.timer = QTimer()
            self.timer.timeout.connect(self.update_time)

            self.time_elapsed = datetime.timedelta()

            self.timestamp_label = QLabel(self)

            vbox = QVBoxLayout()
            vbox.addWidget(self.start_button)
            vbox.addWidget(self.close_button)
            vbox.addWidget(self.timestamp_label) 

            self.setLayout(vbox)
            self.setWindowTitle('Intelligent Image Management Limited')
            self.setFixedSize(500, 500)

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

            icon_url = "https://raw.githubusercontent.com/sorkerlimon/image/main/icon.jpg"  # Replace with the URL of your image

            response = requests.get(icon_url)
            if response.status_code == 200:
                with open('icon.jpg', 'wb') as f:
                    f.write(response.content)
                self.setWindowIcon(QIcon('icon.jpg'))

        else:
            sys.exit()

    def start_button_clicked(self):
        self.start_button.hide()
        self.close_button.show()
        self.start_time = datetime.datetime.now()
        # self.start_time = datetime.now(timezone('Asia/Dhaka'))
        self.timestamp_label.setText("Start button clicked at {}".format(self.start_time.strftime("%Y-%m-%d %I:%M:%S %p")))
        self.timer.start(1000)

        # Start IP retrieval thread
        self.ip_thread = IPThread()
        self.ip_thread.ip_address_retrieved.connect(self.on_ip_address_retrieved)
        self.ip_thread.start()

        # Check open browsers
        open_browsers = self.get_open_browsers()
        if open_browsers:
            print("Open browsers:")
            for browser in open_browsers:
                print(browser)
        else:
            print("No browsers currently open.")


    def update_time(self):
        current_time = datetime.datetime.now()
        self.time_elapsed = current_time - self.start_time
        current_time_str = current_time.strftime("%Y-%m-%d %I:%M:%S %p")
        total_seconds = int(self.time_elapsed.total_seconds())

        minutes, seconds = divmod(total_seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)

        time_parts = []
        if days > 0:
            time_parts.append("{} day{}".format(days, "s" if days > 1 else ""))
        if hours > 0:
            time_parts.append("{} hour{}".format(hours, "s" if hours > 1 else ""))
        if minutes > 0:
            time_parts.append("{} minute{}".format(minutes, "s" if minutes > 1 else ""))
        if seconds > 0:
            time_parts.append("{} second{}".format(seconds, "s" if seconds > 1 else ""))

        elapsed_time_str = ', '.join(time_parts)

        current_time_html = '<span style="font-weight: bold; color: blue;">Current time:</span> {}'.format(current_time_str)
        elapsed_time_html = '<span style="font-weight: bold; color: green; border: 50px solid;">Working time:</span> {}'.format(elapsed_time_str)

        timestamp_html = '<div style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100%; text-align: center;">{}<br>{}</div>'.format(current_time_html, elapsed_time_html)

        self.timestamp_label.setText(timestamp_html)






    def on_ip_address_retrieved(self, local_ip_address, public_ip_address):
        print("Local IP address:", local_ip_address)
        print("Public IP address:", public_ip_address)
        

        # Retrieve physical address (MAC address)
        physical_address = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
                                     for ele in range(0, 8 * 6, 8)][::-1])
        print("Physical address:", physical_address)

    def close_button_clicked(self):
        self.close_button.hide()
        self.start_button.show()
        self.timer.stop()
        
        self.stop_time = datetime.datetime.now()
        # self.stop_time = datetime.now(timezone('Asia/Dhaka'))
        self.close_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
        
        # self.start_time_str = self.start_time.strftime("%I:%M:%S %p")  # Format start time as HH:MM:SS AM/PM
        # self.close_time_str = self.stop_time.strftime("%I:%M:%S %p")  # Format close time as HH:MM:SS AM/PM

        self.start_time_str = datetime.datetime.strptime(self.start_time.strftime("%I:%M:%S %p"), "%I:%M:%S %p").time()
        self.close_time_str = datetime.datetime.strptime(self.stop_time.strftime("%I:%M:%S %p"), "%I:%M:%S %p").time()

        # self.start_time_str = datetime.time(10, 1, 34)  # 11:18:34 AM
        # self.close_time_str = datetime.time(10, 4, 34)    # 11:20:34 AM

        print("Start time:", self.start_time_str)
        print("Close time:", self.close_time_str)

        print("Close button clicked at", self.close_time)
        self.calculate_time_difference()
        self.save_data_to_database(self.login_dialog.user_id)


        chrome = Chrome()
        chrome_outputs = chrome.fetch_history()

        firefox = Firefox()
        firefox_outputs = firefox.fetch_history()

        edge = Edge()
        edge_outputs = edge.fetch_history()

        # Combine histories from Chrome, Firefox, and Edge
        histories = chrome_outputs.histories + firefox_outputs.histories + edge_outputs.histories
        current_date = datetime.date.today()

        print("current data : ", current_date)
        domain_counts = {}

        # Iterate over the combined history and count occurrences of all domain urls
        for history in histories:
            url = history[1]
            timestamp = history[0]
            if timestamp.date() == current_date and self.start_time_str <= timestamp.time() <= self.close_time_str:
                domain = url.split('//')[-1].split('/')[0]  # Extract the domain from the URL
                if domain in domain_counts:
                    domain_counts[domain] += 1
                else:
                    domain_counts[domain] = 1
                print(f"{url} | {timestamp.strftime('%Y-%m-%d %I:%M:%S %p')}")

        total_count = sum(domain_counts.values())

        # Calculate the percentage for each domain and print the results
        for domain, count in domain_counts.items():
            percentage = (count / total_count) * 100
            print(f"{domain} Percentage: {percentage:.2f}%")


    def save_data_to_database(self, user_id):
        local_ip_address = self.local_ip_address
        public_ip_address = self.public_ip_address
        physical_address = self.physical_address
        start_time = self.start_time.strftime("%Y-%m-%d %I:%M:%S %p")
        close_time = self.stop_time.strftime("%Y-%m-%d %I:%M:%S %p")

        sql = "INSERT INTO ip_time (user_id, local_ip_address, public_ip_address, physical_address, start_time, close_time) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (user_id, local_ip_address, public_ip_address, physical_address, start_time, close_time)

        self.cursor.execute(sql, values)
        self.db.commit()

        print("Data saved to the database.")

    def calculate_time_difference(self):
        close_datetime = datetime.datetime.strptime(self.close_time, "%Y-%m-%d %I:%M:%S %p")
        time_difference = close_datetime - self.start_time

        hours = int(time_difference.total_seconds() // 3600)
        minutes = int((time_difference.total_seconds() % 3600) // 60)
        seconds = int(time_difference.total_seconds() % 60)

        print("Time difference:", hours, "hours,", minutes, "minutes,", seconds, "seconds")


    def get_open_browsers(self):
        browsers = []
        for process in psutil.process_iter(['name']):
            if process.info['name'] == 'chrome.exe' and 'Google Chrome' not in browsers:
                browsers.append('Google Chrome')
            elif process.info['name'] == 'firefox.exe' and 'Mozilla Firefox' not in browsers:
                browsers.append('Mozilla Firefox')
            elif process.info['name'] == 'msedge.exe' and 'Microsoft Edge' not in browsers:
                browsers.append('Microsoft Edge')
            # Add conditions for other browsers as needed

        return browsers


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = MyApp()
    my_app.show()
    sys.exit(app.exec_())


    #pyinstaller --onefile --noconsole
    #pyinstaller --onefile --icon=icon.ico