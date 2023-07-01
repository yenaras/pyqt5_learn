#!/usr/bin/env python3
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        # Add a title
        self.setWindowTitle("Hello World")

        # Set vertical layout
        self.setLayout(qtw.QVBoxLayout())

        # Create a label
        my_label = qtw.QLabel("Pick something from the list below")
        # Change the font size of label
        my_label.setFont(qtg.QFont('Helvetica', 24))
        self.layout().addWidget(my_label)

        # Create an combo box
        my_combo = qtw.QComboBox(self,
                                 editable=True,
                                 insertPolicy=qtw.QComboBox.InsertAtBottom)
        # Add Items to the Combo Box
        my_combo.addItem("Pepperoni", "Something")
        my_combo.addItem("Cheese", 2)
        my_combo.addItem("Mushroom", qtw.QWidget)
        my_combo.addItem("Peppers")
        my_combo.addItems(["Spinach", "Pineapple", "Sausage"])
        my_combo.insertItem(2, "Third Thing")
        # Put combo box on the screen
        self.layout().addWidget(my_combo)

        # Create a button
        my_button = qtw.QPushButton("Press Me!",
                                    clicked=lambda: press_it())
        self.layout().addWidget(my_button)

        self.show()

        def press_it():
            my_label.setText(f"You picked {my_combo.currentText()}!")


app = qtw.QApplication([])
mw = MainWindow()

# run the app
app.exec_()
