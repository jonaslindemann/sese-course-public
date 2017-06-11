# Exercise 1 - User interface for our Mandelbrot code

Implement a simple user interface for our Mandelbrot code. The user interface should:

 * Show a window with widgets for iteration and density.
 * Implement a button which asks for a filename, executes the calculation and displays the image in the window.

Images can be displayed in the user interface using a label widget. The follwing code shows how this can be done in PyQt5:

Modify your import section of your code:

    # -*- coding: utf-8 -*-

    import sys

    from PyQt5.QtWidgets import *
    from PyQt5.QtGui import QPixmap # --- Required for QPixmap
    from PyQt5 import uic

Load the image using the following code:

    # ---- Load image in pixmap of label
    pixmap = QPixmap(filename)
    self.ui.imageLabel.setPixmap(pixmap)

imageLabel is the QLabel widget defined in the .ui-file.


