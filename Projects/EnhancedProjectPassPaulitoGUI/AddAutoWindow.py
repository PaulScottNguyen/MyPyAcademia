# AddAutoWindow.py
import csv
import secrets
import string
from PySide6.QtWidgets import QMainWindow, QMessageBox
from ui_Add_Auto import Ui_MainWindow as Ui_AddAuto
from AppState import AppState


class AddAutoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AddAuto()
        self.ui.setupUi(self)

        # Make generated password box read-only
        self.ui.Generated_Pass_Box.setReadOnly(True)

        # Connect buttons
        self.ui.Generate_Pass_Button.clicked.connect(self.generate_and_save)
        self.ui.Menu_Button_Add_Auto.clicked.connect(self.go_back_to_menu)

    # ---------------------------------------------------------
    # Return to Menu
    # ---------------------------------------------------------
    def go_back_to_menu(self):
        from MenuWindow import MenuWindow   # avoid circular import
        self.menu = MenuWindow()
        self.menu.show()
        self.close()

    # ---------------------------------------------------------
    # Generate + Save Password
    # ---------------------------------------------------------
    def generate_and_save(self):
        website = self.ui.Web_URL_Box_Add_Auto.text().strip().lower()
        username = self.ui.Username_Box_Add_Auto.text().strip()
        length = self.ui.Pass_Length.value()

        # Validate fields
        if not website or not username:
            self.show_error("Website and Username must not be empty.")
            return

        if length <= 0:
            self.show_error("Password length must be a positive number.")
            return

        # Generate password
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(characters) for _ in range(length))

        # Display generated password
        self.ui.Generated_Pass_Box.setText(password)

        # Encrypt password
        fernet = AppState.fernet
        db_file = AppState.db_file
        encrypted_password = fernet.encrypt(password.encode()).decode()

        # Get next ID
        new_id = self.get_next_id(db_file)

        # Save to database
        with open(db_file, "a", newline="") as db:
            writer = csv.writer(db)
            writer.writerow([new_id, website, username, encrypted_password])

        # Success popup
        self.show_success("Password generated and saved successfully!")

    # ---------------------------------------------------------
    # Get next ID (same as CLI)
    # ---------------------------------------------------------
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

    # ---------------------------------------------------------
    # Styled popups
    # ---------------------------------------------------------
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
