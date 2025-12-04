# import module classes
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont

class CalcApp(QWidget):
    def __init__(self):
        super().__init__()
        
        # app settings
        self.setWindowTitle('Calculator App')
        self.resize(250, 300)

        # all objects/widgets
        self.text_box = QLineEdit()
        self.text_box.setFont(QFont('Helvetica', 32))
        self.text_box.setStyleSheet("""
                                    QLineEdit {
                                        background: #c4def2;
                                        padding: 12px;
                                        border: 1px solid #c4def2;
                                        border-radius: 6px;
                                        font-size: 22px;
                                    }
                                """)
        self.grid = QGridLayout()

        self.button = ['7', '8', '9', '/',
                        '4', '5', '6', '*',
                        '1', '2', '3', '-',
                        '0', '.', '=', '+']

        self.operators = ['+', '-', '*', '/']

        row = 0
        col = 0
        for text in self.button:
            btn = QPushButton(text)
            btn.clicked.connect(self.button_click)
            # btn.setStyleSheet('QPushButton { font: 20pt Helvetica; padding: 10px; }')
            btn.setStyleSheet("""
                                QPushButton {
                                    background-color: #133a57;
                                    border: none;
                                    border-radius: 8px;
                                    padding: 10px;
                                    font: 20pt;
                                    color: white; 
                                    Helvetica;
                                }
                                QPushButton:hover {
                                    background-color: #164567;
                                }
                                QPushButton:pressed {
                                    background-color: #1a5179;
                                }
                            """)
            self.grid.addWidget(btn, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        self.clear = QPushButton('C') # clear button
        self.delete = QPushButton('DEL') # delete button
        self.clear.setStyleSheet("""
                                QPushButton {
                                    background-color: #efa314;
                                    border: none;
                                    border-radius: 8px;
                                    padding: 10px;
                                    font: 20pt;
                                    font-weight: bold;
                                    color: white; 
                                    Helvetica;
                                }
                                QPushButton:hover {
                                    background-color: #f1ad2e;
                                }
                                QPushButton:pressed {
                                    background-color: #f3b94b;
                                }
                            """)
        self.delete.setStyleSheet("""
                                QPushButton {
                                    background-color: #efa314;
                                    border: none;
                                    border-radius: 8px;
                                    padding: 10px;
                                    font: 20pt;
                                    font-weight: bold;
                                    color: white; 
                                    Helvetica;
                                }
                                QPushButton:hover {
                                    background-color: #f1ad2e;
                                }
                                QPushButton:pressed {
                                    background-color: #f3b94b;
                                }
                            """)
        
        master_layout = QVBoxLayout()
        master_layout.addWidget(self.text_box)
        master_layout.addLayout(self.grid)

        button_row = QHBoxLayout()
        button_row.addWidget(self.clear)
        button_row.addWidget(self.delete)
        master_layout.addLayout(button_row)
        master_layout.setContentsMargins(25, 25, 25, 25)

        self.setLayout(master_layout)

        self.clear.clicked.connect(self.button_click)
        self.delete.clicked.connect(self.button_click)

    # function for button click
    def button_click(self):
        button = app.sender() # what button was clicked
        text = button.text() # get the text value

        if text == '=':
            symbol = self.text_box.text()
            try:
                result = eval(symbol)
                self.text_box.setText(str(result))
            except Exception as e:
                self.text_box.setText('Error')
        
        elif text == 'C':
            self.text_box.clear()

        elif text =='DEL':
            current_text = self.text_box.text()
            self.text_box.setText(current_text[:-1])
        
        else:
            # improved from the tutorial: prevent two operators
            current_text = self.text_box.text()
            if current_text and current_text[-1] in self.operators and text in self.operators:
                self.text_box.setText(current_text[:-1] + text) # change to newest operator instead
                return 
            
            self.text_box.setText(current_text + text) # adding number to text box

if __name__ == '__main__':
    app = QApplication([])
    main_window = CalcApp()
    main_window.setStyleSheet('QWidget { background-color: #0c2436 }')
    main_window.show()
    app.exec_()
