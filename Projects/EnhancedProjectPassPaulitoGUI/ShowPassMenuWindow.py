# ShowPassMenuWindow.py
from PySide6.QtWidgets import QMainWindow
from ui_Show_Pass_Menu import Ui_MainWindow as Ui_ShowPassMenu
from AppState import AppState


class ShowPassMenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ShowPassMenu()
        self.ui.setupUi(self)

        # Connect buttons
        self.ui.Show_By_ID_Button.clicked.connect(self.open_show_by_id)
        self.ui.Show_By_Web_Button.clicked.connect(self.open_show_by_web)

    # ---------------------------------------------------------
    # Open "Show By ID" window
    # ---------------------------------------------------------
    def open_show_by_id(self):
            print("BUTTON CLICKED")
            from ShowByIDWindow import ShowByIDWindow
            print("IMPORT OK")
            self.show_by_id = ShowByIDWindow()
            print("WINDOW CREATED")
            self.show_by_id.show()
            print("WINDOW SHOWN")
            self.close()


    # ---------------------------------------------------------
    # Open "Show By Website" window
    # ---------------------------------------------------------
    def open_show_by_web(self):
        from ShowByWebWindow import ShowByWebWindow
        self.show_by_web = ShowByWebWindow()
        self.show_by_web.show()
        self.close()
