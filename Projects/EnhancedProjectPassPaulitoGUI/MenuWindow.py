# MenuWindow.py
from PySide6.QtWidgets import QMainWindow
from ui_Menu import Ui_MainWindow
from AddManualWindow import AddManualWindow
from AddAutoWindow import AddAutoWindow



class MenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect button to open Add Manual window
        self.ui.Add_Pass_Manually_Button.clicked.connect(self.open_add_manual)

        self.ui.Add_Pass_Auto_Button.clicked.connect(self.open_add_auto)

        self.ui.Show_All_Button.clicked.connect(self.open_show_pass_menu)



    def open_add_manual(self):
        self.add_manual = AddManualWindow()
        self.add_manual.show()
        self.close()   # optional

    def open_add_auto(self):
        self.add_auto = AddAutoWindow()
        self.add_auto.show()
        self.close()

    def open_show_pass_menu(self):
        from ShowPassMenuWindow import ShowPassMenuWindow
        self.show_pass_menu = ShowPassMenuWindow()
        self.show_pass_menu.show()
        self.close()

