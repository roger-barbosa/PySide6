#
# https://www.youtube.com/watch?v=8yXu-Z9bg5Q&list=PLfQ7GQSrl0_ung_Wt0PpgOICqA8k6dr3i&index=9
# Parei no minuto 13:22
import sys
import os
from qt_core import *

from gui.main_windows.ui_main_window import UI_MainWindow

# Main Window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Curso de Python")

        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # Toggle button
        self.ui.toggle_button.clicked.connect(self.toggle_button)

        # Btn home
        self.ui.btn_1.clicked.connect(self.show_page_1)  # Chama a função show_page_1 caso o botão 1 seja clicado

        # Btn widgets
        self.ui.btn_2.clicked.connect(self.show_page_2)  # Chama a função show_page_1 caso o botão 1 seja clicado

        # Btn settings
        self.ui.settings_btn.clicked.connect(self.show_page_3)  # Chama a função show_page_1 caso o botão 1 seja clicado

        # Chenge text
        self.ui.ui_pages.btn_change_text.clicked.connect(self.change_text)

        self.show()

    def change_text(self):
        text = self.ui.ui_pages.lineEdit.text()
        new_text = 'Olá, ' + text
        self.ui.ui_pages.label_3.setText(new_text)

    def reset_selection(self):
        for btn in self.ui.left_menu.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except:
                pass

    def show_page_1(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_1)
        self.ui.btn_1.set_active(True)

    def show_page_2(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_2)
        self.ui.btn_2.set_active(True)

    def show_page_3(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_3)
        self.ui.settings_btn.set_active(True)

    def toggle_button(self):
        # Get menu width
        menu_width = self.ui.left_menu.width()

        # Check width
        width = 50
        if menu_width == 50:
            width = 240

        # Start animation
        self.animation = QPropertyAnimation(self.ui.left_menu, b'minimumWidth')
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.animation.start()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
