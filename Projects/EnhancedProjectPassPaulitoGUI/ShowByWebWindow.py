import csv
import base64
import hashlib
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QStringListModel, Qt
from cryptography.fernet import Fernet

from ui_Show_by_Web import Ui_MainWindow
from AppState import AppState
from MenuWindow import MenuWindow


# ---------------------------------------------------------
# SAME decrypt function used in ShowByIDWindow
# ---------------------------------------------------------
def decrypt_password(encrypted_text, master_password):
    try:
        key = hashlib.sha256(master_password.encode()).digest()
        key = base64.urlsafe_b64encode(key)

        f = Fernet(key)
        decrypted = f.decrypt(encrypted_text.encode()).decode()
        return decrypted
    except Exception:
        return "[DECRYPTION FAILED]"


class ShowByWebWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.load_websites()
        self.ui.Menu_Web_Button.clicked.connect(self.go_back_to_menu)
        self.ui.listViewWeb.setStyleSheet("color: black; background: white;")

    # ---------------------------------------------------------
    # DELETE KEY HANDLER
    # ---------------------------------------------------------
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            self.delete_selected()

    # ---------------------------------------------------------
    # DELETE SELECTED ENTRY
    # ---------------------------------------------------------
    def delete_selected(self):
        index = self.ui.listViewWeb.currentIndex()
        if not index.isValid():
            return

        text = index.data()  # "website - username - password"
        parts = text.split(" - ")
        website = parts[0]
        username = parts[1]

        db_file = AppState.db_file

        # Read all rows except the one to delete
        rows = []
        with open(db_file, "r", newline="") as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                if not (row[1] == website and row[2] == username):
                    rows.append(row)

        # Write updated CSV
        with open(db_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(rows)

        # Refresh list
        self.load_websites()

    # ---------------------------------------------------------
    # RETURN TO MENU
    # ---------------------------------------------------------
    def go_back_to_menu(self):
        self.menu_window = MenuWindow()
        self.menu_window.show()
        self.close()

    # ---------------------------------------------------------
    # LOAD AND GROUP BY WEBSITE
    # ---------------------------------------------------------
    def load_websites(self):
        db_file = AppState.db_file
        master_password = AppState.master_password

        if not master_password:
            print("Master password not set — cannot decrypt")
            return

        # Load CSV
        try:
            with open(db_file, "r", newline="") as db:
                reader = csv.reader(db)
                next(reader, None)
                data = list(reader)
        except Exception as e:
            print("CSV ERROR:", e)
            data = []

        # Group entries by website
        grouped = {}

        for row in data:
            if len(row) < 4:
                continue

            website = row[1]
            username = row[2]
            encrypted_password = row[3]

            decrypted = decrypt_password(encrypted_password, master_password)

            if website not in grouped:
                grouped[website] = []

            grouped[website].append((username, decrypted))

        # Build display list
        display_list = []
        for website, entries in grouped.items():
            for username, password in entries:
                display_list.append(f"{website} - {username} - {password}")

        # Apply to model
        model = QStringListModel()
        model.setStringList(display_list)
        self.ui.listViewWeb.setModel(model)
