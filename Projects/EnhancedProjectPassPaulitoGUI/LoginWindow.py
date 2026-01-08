# LoginWindow.py
import os
import csv
import base64
import hashlib
from cryptography.fernet import Fernet

from PySide6.QtWidgets import QMainWindow, QMessageBox
from ui_Login import Ui_MainWindow
from MenuWindow import MenuWindow
from AppState import AppState


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Login_Button.clicked.connect(self.handle_login)

    def handle_login(self):
        master_password = self.ui.Master_Password.text().strip()

        if not master_password:
            msg = QMessageBox(self)
            msg.setWindowTitle("Error")
            msg.setText("Master password cannot be empty.")
            msg.setIcon(QMessageBox.Warning)

            # ✔ Make text black and semi‑bold
            msg.setStyleSheet("""
                QMessageBox {
                    background: white;
                }
                QMessageBox QLabel {
                    color: black;
                    font-weight: 600;   /* semi-bold */
                    font-size: 14px;
                }
            """)

            msg.exec()

            return

        # --- Derive Fernet key (same as CLI) ---
        key = hashlib.sha256(master_password.encode()).digest()
        fernet_key = base64.urlsafe_b64encode(key)
        fernet = Fernet(fernet_key)

        # --- Derive unique database filename ---
        hashed = hashlib.sha256(master_password.encode()).hexdigest()
        db_file = f"Database_{hashed}.txt"

        # --- Create or load database ---
        if not os.path.exists(db_file):
            with open(db_file, "w", newline="") as db:
                writer = csv.writer(db)
                writer.writerow(["ID", "Website", "Username", "Password"])
        # else: database already exists

        # --- Save to global app state ---
        AppState.fernet = fernet
        AppState.db_file = db_file
        AppState.master_password = self.ui.Master_Password.text()


        # --- Open Menu Window ---
        self.menu = MenuWindow()
        self.menu.show()
        self.close()
