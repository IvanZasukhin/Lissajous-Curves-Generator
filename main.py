import sys

import numpy
import numpy as np
import matplotlib
import matplotlib.pylab as plt
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow

matplotlib.use('QT5Agg')

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

init_frequencyY = 1.0  # Частота первого сигнала
init_frequencyX = 2.0  # Частота второго сигнала
init_amplitudeY = 0.5  # Амплитуда первого сигнала
init_amplitudeX = 0.5  # Амплитуда второго сигнала
value_line = 2
step_len_pi = np.pi


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)  # from ui file
        # self.setupUi(self)  # from py file (need to import class from generated .py file)
        self.value_line = value_line
        self.initUI()

    def initUI(self):
        # val
        self.amplitudeX_slider.valueChanged.connect(self.amplitudeX_changeValue)
        self.amplitudeX_lineEdit.editingFinished.connect(self.amplitudeX_lineEdit_changeValue)

        self.amplitudeY_slider.valueChanged.connect(self.amplitudeY_changeValue)
        self.amplitudeY_lineEdit.editingFinished.connect(self.amplitudeY_lineEdit_changeValue)

        self.frequencyX_slider.valueChanged.connect(self.frequencyX_changeValue)
        self.frequencyX_lineEdit.editingFinished.connect(self.frequencyX_lineEdit_changeValue)

        self.frequencyY_slider.valueChanged.connect(self.frequencyY_changeValue)
        self.frequencyY_lineEdit.editingFinished.connect(self.frequencyY_lineEdit_changeValue)

        self.phaseY_lineEdit.editingFinished.connect(self.phaseY_lineEdit_changeValue)
        self.phaseX_lineEdit.editingFinished.connect(self.phaseX_lineEdit_changeValue)

        self.button_reset.clicked.connect(self.button_reset_clicked)
        self.button_render.clicked.connect(self.button_render_clicked)

        # plot
        fig, self.ax = plt.subplots()
        self.graphic_program = FigureCanvas(fig)

        toolbar = NavigationToolbar(self.graphic_program, self.graphic_program)
        lay = QtWidgets.QVBoxLayout(self.graphic)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self.graphic_program)
        # add toolbar
        # self.addToolBar(QtCore.Qt.BottomToolBarArea, NavigationToolbar(self.graphic_program, self))

        # test data
        self.button_reset_clicked()

    def insert_ax(self):
        self.ax = self.graphic_program.figure.subplots()
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')

    def amplitudeX_changeValue(self, value):
        self.amplitudeX_lineEdit.setText(str(value / 100))

    def amplitudeX_lineEdit_changeValue(self):
        try:
            value = eval(self.amplitudeX_lineEdit.text().replace(",", "."))
            value = int(float(value) * 100)
            if self.amplitudeX_slider.minimum() > value or value > self.amplitudeX_slider.maximum():
                self.amplitudeX_slider.setMaximum(value + 50)
                self.amplitudeX_slider.setMinimum(value - 50)
            self.amplitudeX_slider.setValue(value)
        except ValueError:
            pass
        except SyntaxError:
            pass
        self.button_render_clicked()

    def amplitudeY_changeValue(self, value):
        self.amplitudeY_lineEdit.setText(str(value / 100))

    def amplitudeY_lineEdit_changeValue(self):
        try:
            value = eval(self.amplitudeY_lineEdit.text().replace(",", "."))
            value = int(float(value) * 100)
            if self.amplitudeY_slider.minimum() > value or value > self.amplitudeY_slider.maximum():
                self.amplitudeY_slider.setMaximum(value + 50)
                self.amplitudeY_slider.setMinimum(value - 50)
            self.amplitudeY_slider.setValue(value)
        except ValueError:
            pass
        except SyntaxError:
            pass
        self.button_render_clicked()

    def frequencyX_changeValue(self, value):
        self.frequencyX_lineEdit.setText(str(value / 100))

    def frequencyX_lineEdit_changeValue(self):
        try:
            value = eval(self.frequencyX_lineEdit.text().replace(",", "."))
            value = int(float(value) * 100)
            if self.frequencyX_slider.minimum() > value or value > self.frequencyX_slider.maximum():
                self.frequencyX_slider.setMaximum(value + 50)
                self.frequencyX_slider.setMinimum(value - 50)
            self.frequencyX_slider.setValue(value)
        except ValueError:
            pass
        except SyntaxError:
            pass
        self.button_render_clicked()

    def frequencyY_changeValue(self, value):
        self.frequencyY_lineEdit.setText(str(value / 100))

    def frequencyY_lineEdit_changeValue(self):
        try:
            value = eval(self.frequencyY_lineEdit.text().replace(",", "."))
            value = int(float(value) * 100)
            if self.frequencyY_slider.minimum() > value or value > self.frequencyY_slider.maximum():
                self.frequencyY_slider.setMaximum(value + 50)
                self.frequencyY_slider.setMinimum(value - 50)
            self.frequencyY_slider.setValue(value)
        except ValueError:
            pass
        except SyntaxError:
            pass
        self.button_render_clicked()

    def button_reset_clicked(self):

        self.frequencyY_lineEdit.setText(str(init_frequencyY))
        self.frequencyX_lineEdit.setText(str(init_frequencyX))
        self.amplitudeY_lineEdit.setText(str(init_amplitudeY))
        self.amplitudeX_lineEdit.setText(str(init_amplitudeX))

        self.frequencyY_lineEdit_changeValue()
        self.frequencyX_lineEdit_changeValue()
        self.amplitudeY_lineEdit_changeValue()
        self.amplitudeX_lineEdit_changeValue()

        self.button_render_clicked()

    def phaseY_lineEdit_changeValue(self):
        try:
            if "pi" not in str(self.phaseY_lineEdit.text()):
                self.phaseY_lineEdit.text = str(eval(self.phaseY_lineEdit.text().replace(",", ".")))
        except ValueError:
            pass
        except SyntaxError:
            pass
        self.button_render_clicked()

    def phaseX_lineEdit_changeValue(self):
        try:
            if "pi" not in str(self.phaseX_lineEdit.text()):
                self.phaseX_lineEdit.text = str(eval(str(self.phaseX_lineEdit.text).replace(",", ".")))
        except ValueError:
            pass
        except SyntaxError:
            pass
        self.button_render_clicked()

    def button_render_clicked(self):
        self.insert_ax()
        try:
            phaseX = float(eval(
                str(self.phaseX_lineEdit.text()).replace(",",
                                                         ".")) if "pi" not in str(
                self.phaseX_lineEdit.text()) else float(
                eval(
                    str(self.phaseX_lineEdit.text()).replace(",", ".").replace("pi", str(numpy.pi)))))
            phaseY = float(eval(
                str(self.phaseY_lineEdit.text()).replace(",",
                                                         ".")) if "pi" not in str(
                self.phaseY_lineEdit.text()) else float(
                eval(
                    str(self.phaseY_lineEdit.text()).replace(",", ".").replace("pi", str(numpy.pi)))))
            self.t = np.linspace(-step_len_pi, step_len_pi + 1, endpoint=True, num=(
                int((self.frequencyX_slider.value() / 100) + (self.frequencyY_slider.value() / 100) * 200)))
            self.x = (self.amplitudeX_slider.value() / 100) * np.sin(
                (self.frequencyX_slider.value() / 100) * self.t + phaseX)
            self.y = (self.amplitudeY_slider.value() / 100) * np.cos(
                (self.frequencyY_slider.value() / 100) * self.t + phaseY)
            line, = self.ax.plot(self.x, self.y, lw=2)

            m = 1 + 0.2
            self.ax.set_ylim((-m, m))
            self.ax.set_xlim((-m, m))

            self.graphic_program.draw()
        except ValueError:
            pass
        except SyntaxError:
            pass


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
