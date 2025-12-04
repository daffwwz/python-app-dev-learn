# import module classes
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout

class CalcApp(QWidget):
    def __init__(self):
        super().__init__()
        
        # app settings
        self.setWindowTitle('Calculator App')
        self.resize(250, 300)

        # all objects/widgets
        self.text_box = QLineEdit()
        self.grid = QGridLayout()

        self.button = ['7', '8', '9', '/',
                        '4', '5', '6', '*',
                        '1', '2', '3', '-',
                        '0', '.', '=', '+']

        self.clear = QPushButton('C') # clear button
        self.delete = QPushButton('DEL') # delete button

        row = 0
        col = 0
        for text in self.button:
            btn = QPushButton(text)
            btn.clicked.connect(self.button_click)
            self.grid.addWidget(btn, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        master_layout = QVBoxLayout()
        master_layout.addWidget(self.text_box)
        master_layout.addLayout(self.grid)

        button_row = QHBoxLayout()
        button_row.addWidget(self.clear)
        button_row.addWidget(self.delete)

        master_layout.addLayout(button_row)
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
            current_text = self.text_box.text()
            self.text_box.setText(current_text + text) # adding number to text box

if __name__ == '__main__':
    app = QApplication([])
    main_window = CalcApp()
    main_window.show()
    app.exec_()
