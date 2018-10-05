from PyQt5.QtWidgets import *
import sys
import math

Data = ''


class Button:
    def __init__(self, text, results):
        self.b = QPushButton(str(text))
        self.text = text
        self.results = results
        self.b.clicked.connect(lambda: self.handleInput(
            self.text))  # Important because we need to pass only function name with arguments here that is why we use lambda here

    def handleInput(self, v):
        global Data
        try:
            if self.results.text() == 'INVALID!':
                self.results.setText("")
            if self.results.text() != '':
                if self.results.text()[-1] in ['*', '+', '-', '/'] and v in ['-', '*', '+', '/', '√', 'CBRT', "SIN",
                                                                             "COS", "LOG", "MOD", "TAN", "MOD"]:
                    return
                elif v == 'CBRT':
                    self.results.setText(str(round(float(eval(self.results.text())) ** (1 / 3), 4), ))
                elif v == 'MOD':
                    if '.' in self.results.text():
                        self.results.setText(str(abs(float(self.results.text()))))
                    else:
                        self.results.setText(str(abs(int(self.results.text()))))
                elif v == 'LOG':
                    self.results.setText(str(math.log10(abs(float(eval(self.results.text()))))))
                elif v == 'SQUARE':
                    if '.' in self.results.text():
                        self.results.setText(str(float(self.results.text()) ** 2))
                    else:
                        self.results.setText(str(int(self.results.text()) ** 2))
                elif v == "SIN":
                    self.results.setText(str(math.sin(float(eval(self.results.text())))))
                elif v == "COS":
                    self.results.setText(str(math.cos(float(eval(self.results.text())))))
                elif v == "TAN":
                    self.results.setText(str(math.tan(float(eval(self.results.text())))))
                elif v == 'x!':
                    if '.' in str(eval(self.results.text())):
                        self.results.setText("INVALID!")
                    else:
                        self.results.setText(str(math.factorial(abs(int(eval(self.results.text()))))))
                elif self.results.text()[-1] == '/' and v == 0:
                    return
                elif v == "=":
                    if self.results.text()[-1] in ['*', '-', '.', '+', '/']:
                        return
                    res = eval(self.results.text())
                    self.results.setText(str(res))
                elif v == "AC":
                    self.results.setText("")
                elif v == "DEL":
                    self.results.setText(self.results.text()[:-1])
                elif v == "√" and self.results.text() != '':
                    self.results.setText(str(float(self.results.text()) ** 0.5))
                elif v == "√" and self.results.text() == '':
                    return
                else:
                    current_value = self.results.text()
                    new_value = current_value + str(v)
                    self.results.setText(new_value)
            else:
                if type(v) == int:
                    current_value = self.results.text()
                    new_value = current_value + str(v)
                    self.results.setText(new_value)
        except:
            self.results.setText("INVALID!")
        Data = self.results.text()


class Widget1():
    def setup(self, MainWindow, res):
        self.widget = QWidget()
        self.grid = QGridLayout()
        self.results = QLineEdit()
        self.results.setText(res)

        row = 3
        col = 0
        self.cb = QComboBox()
        self.cb.addItems(["Basic Mode", "Advanced Mode"])
        self.grid.addWidget(self.cb, 0, 1, 1, 2)
        self.grid.addWidget(self.results, 1, 0, 2, 4)
        buttons = ["AC", "DEL", "√", "/",
                   7, 8, 9, "*",
                   4, 5, 6, "-",
                   1, 2, 3, "+",
                   0, ".", "="]
        for button in buttons:
            if col > 3:
                col = 0
                row += 1

            buttonObject = Button(button, self.results)

            if button == 0:
                self.grid.addWidget(buttonObject.b, row, col, 1, 2)
                col += 1
            else:
                self.grid.addWidget(buttonObject.b, row, col, 1, 1)

            col += 1

        self.widget.setLayout(self.grid)
        MainWindow.setCentralWidget(self.widget)


class Widget2():
    def setup(self, MainWindow, res):
        self.widget = QWidget()
        self.grid = QGridLayout()
        self.results = QLineEdit()
        self.results.setText(res)

        row = 3
        col = 0
        self.cb = QComboBox()
        self.cb.addItems(["Advance Mode", "Normal Mode"])
        self.grid.addWidget(self.cb, 0, 1, 1, 2)
        self.grid.addWidget(self.results, 1, 0, 2, 4)
        buttons = ["AC", "DEL", "SIN", "COS",
                   7, 8, 9, "MOD",
                   4, 5, 6, "TAN",
                   1, 2, 3, "LOG",
                   0, "SQUARE", "CBRT", 'x!']
        for button in buttons:
            if col > 3:
                col = 0
                row += 1
            buttonObject = Button(button, self.results)

            self.grid.addWidget(buttonObject.b, row, col, 1, 1)

            col += 1

        self.widget.setLayout(self.grid)
        MainWindow.setCentralWidget(self.widget)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.widget1 = Widget1()
        self.widget2 = Widget2()
        self.startWidget1("")

    def startWidget1(self, res):
        global Data
        self.widget1.setup(self, res)
        Data = self.widget1.results.text()
        self.widget1.cb.currentIndexChanged.connect(self.selectionchange1)
        self.show()

    def startWidget2(self, res):
        global Data
        self.widget2.setup(self, res)
        Data = self.widget2.results.text()
        self.widget2.cb.currentIndexChanged.connect(self.selectionchange2)
        self.show()

    def selectionchange1(self, i):
        global Data
        res = Data
        self.startWidget2(res)

    def selectionchange2(self, i):
        global Data
        res = Data
        self.startWidget1(res)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())




