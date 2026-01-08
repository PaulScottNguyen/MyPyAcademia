# AddManualWindow.py

import csv
from PySide6.QtWidgets import QMainWindow, QMessageBox
from ui_Add_Manual import Ui_MainWindow as Ui_AddManual
from AppState import AppState# so this window can access fernet + db_file

class AddManualWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AddManual()   # ✔ Correct UI class
        self.ui.setupUi(self)

        # Connect buttons
        self.ui.Save_Pass_Manually_Button.clicked.connect(self.save_manual_password)
        self.ui.Menu_Manual_Button.clicked.connect(self.go_back_to_menu)

    def go_back_to_menu(self):
        from MenuWindow import MenuWindow   # import inside function
        self.menu = MenuWindow()
        self.menu.show()
        self.close()


    def save_manual_password(self):
        website = self.ui.Manual_URL_Box.text().strip().lower()
        username = self.ui.Manual_Username_Box.text().strip()
        password = self.ui.Manual_Pass_Box.text().strip()

        if not website or not username or not password:
            self.show_error("All fields must be filled before saving.")
            return

        fernet = AppState.fernet
        db_file = AppState.db_file

        encrypted_password = fernet.encrypt(password.encode()).decode()
        new_id = self.get_next_id(db_file)

        with open(db_file, "a", newline="") as db:
            writer = csv.writer(db)
            writer.writerow([new_id, website, username, encrypted_password])

        self.show_success("Password saved successfully!")

        self.ui.Manual_URL_Box.clear()
        self.ui.Manual_Username_Box.clear()
        self.ui.Manual_Pass_Box.clear()

    def get_next_id(self, db_file):
        try:
            with open(db_file, "r", newline="") as db:
                reader = csv.reader(db)
                next(reader, None)
                data = list(reader)
                last_id = int(data[-1][0]) if data else 0
        except FileNotFoundError:
            last_id = 0
        return last_id + 1

    def show_error(self, message):
        msg = QMessageBox(self)
        msg.setWindowTitle("Error")
        msg.setText(message)
        msg.setIcon(QMessageBox.Warning)
        msg.setStyleSheet("""
            QMessageBox QLabel {
                color: black;
                font-weight: 600;
                font-size: 14px;
            }
        """)
        msg.exec()

    def show_success(self, message):
        msg = QMessageBox(self)
        msg.setWindowTitle("Success")
        msg.setText(message)
        msg.setIcon(QMessageBox.Information)
        msg.setStyleSheet("""
            QMessageBox QLabel {
                color: black;
                font-weight: 600;
                font-size: 14px;
            }
        """)
        msg.exec()
