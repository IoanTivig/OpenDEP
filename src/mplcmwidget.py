# ------------------------------------------------------
# -------------------- mplwidget.py --------------------
# ------------------------------------------------------
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import StrMethodFormatter

class MplCMWidget(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)


        self.figure = plt.figure(figsize=(10.,10.))
        self.figure.subplots_adjust(left=0.13,right=0.97,bottom=0.11,top=0.985)
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.canvas.axes.set_xlabel('Frequency (Hz)',labelpad=5)
        self.canvas.axes.set_ylabel('CM factor',labelpad=5)
        self.canvas.axes.tick_params(labelsize='small')
        self.canvas.axes.grid(which='major', axis='both', color='lightgrey', linestyle='--')
        self.canvas.axes.yaxis.set_major_formatter(StrMethodFormatter('{x:,.3f}'))
        self.setLayout(layout)
