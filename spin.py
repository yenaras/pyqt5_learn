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
        my_label.setFont(qtg.QFont("Helvetica", 24))
        self.layout().addWidget(my_label)

        # Create an spin box
        my_spin = qtw.QDoubleSpinBox(
            self,
            value=10,
            maximum=100,
            minimum=0,
            singleStep=5.5,
            prefix="#",
            suffix="!!!",
        )
        # Change font size of spinbox
        my_spin.setFont(qtg.QFont("Helvitica", 18))

        # Put spin box on the screen
        self.layout().addWidget(my_spin)

        # Create a button
        my_button = qtw.QPushButton("Press Me!", clicked=lambda: press_it())
        self.layout().addWidget(my_button)

        self.show()

        def press_it():
            my_label.setText(f"You picked #{my_spin.value()}!")


app = qtw.QApplication([])
mw = MainWindow()

# run the app
app.exec_()
