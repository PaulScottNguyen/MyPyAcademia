# ShowByIDWindow.py
import csv
import base64
import hashlib
from cryptography.fernet import Fernet

from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QStringListModel, Qt
from ui_Show_by_ID import Ui_MainWindow as Ui_ShowByID
from AppState import AppState


# ---------------------------------------------------------
# Decrypt password using master password (Fernet + SHA256)
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


class ShowByIDWindow(QMainWindow):
    def __init__(self):
        print("INIT START")  # Debug
        super().__init__()
        print("UI SETUP")    # Debug
        self.ui = Ui_ShowByID()
        self.ui.setupUi(self)
        print("LOAD IDS")    # Debug
        self.load_ids()
        print("CONNECT BUTTON")  # Debug
        self.ui.Menu_ID_Button.clicked.connect(self.go_back_to_menu)
        print("STYLE SET")   # Debug
        self.ui.listViewID.setStyleSheet("color: black; background: white;")
        print("INIT DONE")   # Debug

    # ---------------------------------------------------------
    # DELETE KEY HANDLER
    # ---------------------------------------------------------
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            self.delete_selected()
            return
        super().keyPressEvent(event)

    # ---------------------------------------------------------
    # DELETE SELECTED ENTRY
    # ---------------------------------------------------------
    def delete_selected(self):
        index = self.ui.listViewID.currentIndex()
        if not index.isValid():
            return

        text = index.data()  # "ID - website - username - password"
        target_id = text.split(" - ")[0]

        db_file = AppState.db_file

        # Read all rows except the one to delete
        rows = []
        with open(db_file, "r", newline="") as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                if row[0] != target_id:
                    rows.append(row)

        # Write updated CSV
        with open(db_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(rows)

        # Refresh list
        self.load_ids()

    # ---------------------------------------------------------
    # Load all IDs into QListView using a QStringListModel
    # ---------------------------------------------------------
    def load_ids(self):
        db_file = AppState.db_file
        master_password = AppState.master_password

        try:
            with open(db_file, "r", newline="") as db:
                reader = csv.reader(db)
                next(reader, None)
                data = list(reader)
        except FileNotFoundError:
            data = []

        display_list = []

        for row in data:
            id_val = row[0]
            website = row[1]
            username = row[2]
            encrypted_password = row[3]

            decrypted_password = decrypt_password(encrypted_password, master_password)

            display_list.append(
                f"{id_val} - {website} - {username} - {decrypted_password}"
            )

        model = QStringListModel()
        model.setStringList(display_list)
        self.ui.listViewID.setModel(model)
        print("CSV DATA:", data)

    # ---------------------------------------------------------
    # Return to Menu
    # ---------------------------------------------------------
    def go_back_to_menu(self):
        from MenuWindow import MenuWindow
        self.menu = MenuWindow()
        self.menu.show()
        self.close()
