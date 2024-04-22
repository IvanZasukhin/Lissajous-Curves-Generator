import sys
import io
import numpy
import numpy as np
import matplotlib
import matplotlib.pylab as plt
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="Симулятор фигур Лиссажу">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>835</width>
    <height>687</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Симулятор фигур Лиссажу</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QVBoxLayout" name="verticalLayout">
    <item>
     <widget class="QTabWidget" name="tabWidget">
      <property name="currentIndex">
       <number>0</number>
      </property>
      <widget class="QWidget" name="main">
       <attribute name="title">
        <string>main</string>
       </attribute>
       <layout class="QVBoxLayout" name="verticalLayout_4">
        <item>
         <layout class="QHBoxLayout" name="horizontalLayout_2">
          <item>
           <layout class="QHBoxLayout" name="horizontalLayout_3">
            <property name="sizeConstraint">
             <enum>QLayout::SetDefaultConstraint</enum>
            </property>
            <item>
             <layout class="QHBoxLayout" name="horizontalLayout_7">
              <item>
               <layout class="QVBoxLayout" name="verticalLayout_3">
                <item>
                 <widget class="QSlider" name="frequencyY_slider">
                  <property name="sizePolicy">
                   <sizepolicy hsizetype="Maximum" vsizetype="Expanding">
                    <horstretch>2</horstretch>
                    <verstretch>20</verstretch>
                   </sizepolicy>
                  </property>
                  <property name="minimumSize">
                   <size>
                    <width>25</width>
                    <height>0</height>
                   </size>
                  </property>
                  <property name="minimum">
                   <number>0</number>
                  </property>
                  <property name="maximum">
                   <number>100</number>
                  </property>
                  <property name="value">
                   <number>50</number>
                  </property>
                  <property name="orientation">
                   <enum>Qt::Vertical</enum>
                  </property>
                 </widget>
                </item>
                <item>
                 <widget class="QLineEdit" name="frequencyY_lineEdit">
                  <property name="enabled">
                   <bool>true</bool>
                  </property>
                  <property name="sizePolicy">
                   <sizepolicy hsizetype="Ignored" vsizetype="Fixed">
                    <horstretch>1</horstretch>
                    <verstretch>0</verstretch>
                   </sizepolicy>
                  </property>
                  <property name="minimumSize">
                   <size>
                    <width>40</width>
                    <height>0</height>
                   </size>
                  </property>
                  <property name="maximumSize">
                   <size>
                    <width>40</width>
                    <height>16777215</height>
                   </size>
                  </property>
                  <property name="text">
                   <string>0.5</string>
                  </property>
                 </widget>
                </item>
                <item>
                 <widget class="QLabel" name="frequencyY_lable">
                  <property name="sizePolicy">
                   <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
                    <horstretch>1</horstretch>
                    <verstretch>0</verstretch>
                   </sizepolicy>
                  </property>
                  <property name="maximumSize">
                   <size>
                    <width>16777215</width>
                    <height>16777215</height>
                   </size>
                  </property>
                  <property name="text">
                   <string>ЧастотаY</string>
                  </property>
                 </widget>
                </item>
               </layout>
              </item>
             </layout>
            </item>
            <item>
             <layout class="QHBoxLayout" name="horizontalLayout_11">
              <item>
               <layout class="QVBoxLayout" name="verticalLayout_5">
                <item>
                 <widget class="QSlider" name="amplitudeY_slider">
                  <property name="sizePolicy">
                   <sizepolicy hsizetype="Maximum" vsizetype="Expanding">
                    <horstretch>0</horstretch>
                    <verstretch>20</verstretch>
                   </sizepolicy>
                  </property>
                  <property name="minimumSize">
                   <size>
                    <width>25</width>
                    <height>0</height>
                   </size>
                  </property>
                  <property name="minimum">
                   <number>0</number>
                  </property>
                  <property name="maximum">
                   <number>100</number>
                  </property>
                  <property name="value">
                   <number>50</number>
                  </property>
                  <property name="orientation">
                   <enum>Qt::Vertical</enum>
                  </property>
                 </widget>
                </item>
                <item>
                 <widget class="QLineEdit" name="amplitudeY_lineEdit">
                  <property name="enabled">
                   <bool>true</bool>
                  </property>
                  <property name="sizePolicy">
                   <sizepolicy hsizetype="Ignored" vsizetype="Fixed">
                    <horstretch>0</horstretch>
                    <verstretch>0</verstretch>
                   </sizepolicy>
                  </property>
                  <property name="minimumSize">
                   <size>
                    <width>20</width>
                    <height>0</height>
                   </size>
                  </property>
                  <property name="maximumSize">
                   <size>
                    <width>40</width>
                    <height>16777215</height>
                   </size>
                  </property>
                  <property name="text">
                   <string>0.5</string>
                  </property>
                 </widget>
                </item>
                <item>
                 <widget class="QLabel" name="amplitudeY_lable">
                  <property name="sizePolicy">
                   <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
                    <horstretch>1</horstretch>
                    <verstretch>0</verstretch>
                   </sizepolicy>
                  </property>
                  <property name="maximumSize">
                   <size>
                    <width>16777215</width>
                    <height>16777215</height>
                   </size>
                  </property>
                  <property name="acceptDrops">
                   <bool>false</bool>
                  </property>
                  <property name="styleSheet">
                   <string notr="true">.vertical{
     transform: rotate(180deg);
     writing-mode: vertical-lr;
     text-align: center;
}</string>
                  </property>
                  <property name="text">
                   <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;АмплитудаY&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
                  </property>
                  <property name="textInteractionFlags">
                   <set>Qt::LinksAccessibleByMouse</set>
                  </property>
                 </widget>
                </item>
               </layout>
              </item>
             </layout>
            </item>
           </layout>
          </item>
          <item>
           <widget class="QWidget" name="graphic" native="true">
            <property name="sizePolicy">
             <sizepolicy hsizetype="MinimumExpanding" vsizetype="Preferred">
              <horstretch>0</horstretch>
              <verstretch>0</verstretch>
             </sizepolicy>
            </property>
            <property name="inputMethodHints">
             <set>Qt::ImhSensitiveData</set>
            </property>
           </widget>
          </item>
         </layout>
        </item>
        <item>
         <layout class="QVBoxLayout" name="verticalLayout_1">
          <item>
           <layout class="QHBoxLayout" name="horizontalLayout_4">
            <item>
             <spacer name="horizontalSpacer_7">
              <property name="orientation">
               <enum>Qt::Horizontal</enum>
              </property>
              <property name="sizeHint" stdset="0">
               <size>
                <width>40</width>
                <height>20</height>
               </size>
              </property>
             </spacer>
            </item>
            <item>
             <widget class="QLabel" name="amplitudeX_lable">
              <property name="sizePolicy">
               <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
                <horstretch>1</horstretch>
                <verstretch>0</verstretch>
               </sizepolicy>
              </property>
              <property name="text">
               <string>АмплитудаX</string>
              </property>
             </widget>
            </item>
            <item>
             <widget class="QSlider" name="amplitudeX_slider">
              <property name="sizePolicy">
               <sizepolicy hsizetype="Expanding" vsizetype="Fixed">
                <horstretch>20</horstretch>
                <verstretch>0</verstretch>
               </sizepolicy>
              </property>
              <property name="inputMethodHints">
               <set>Qt::ImhNone</set>
              </property>
              <property name="minimum">
               <number>0</number>
              </property>
              <property name="maximum">
               <number>100</number>
              </property>
              <property name="value">
               <number>50</number>
              </property>
              <property name="tracking">
               <bool>true</bool>
              </property>
              <property name="orientation">
               <enum>Qt::Horizontal</enum>
              </property>
              <property name="invertedAppearance">
               <bool>false</bool>
              </property>
              <property name="invertedControls">
               <bool>false</bool>
              </property>
             </widget>
            </item>
            <item>
             <widget class="QLineEdit" name="amplitudeX_lineEdit">
              <property name="enabled">
               <bool>true</bool>
              </property>
              <property name="sizePolicy">
               <sizepolicy hsizetype="Ignored" vsizetype="Fixed">
                <horstretch>1</horstretch>
                <verstretch>0</verstretch>
               </sizepolicy>
              </property>
              <property name="minimumSize">
               <size>
                <width>40</width>
                <height>0</height>
               </size>
              </property>
              <property name="text">
               <string>0.5</string>
              </property>
             </widget>
            </item>
            <item>
             <spacer name="horizontalSpacer_3">
              <property name="orientation">
               <enum>Qt::Horizontal</enum>
              </property>
              <property name="sizeHint" stdset="0">
               <size>
                <width>40</width>
                <height>20</height>
               </size>
              </property>
             </spacer>
            </item>
           </layout>
          </item>
          <item>
           <layout class="QHBoxLayout" name="horizontalLayout_6">
            <item>
             <spacer name="horizontalSpacer_6">
              <property name="orientation">
               <enum>Qt::Horizontal</enum>
              </property>
              <property name="sizeHint" stdset="0">
               <size>
                <width>40</width>
                <height>20</height>
               </size>
              </property>
             </spacer>
            </item>
            <item>
             <widget class="QLabel" name="frequencyX_lable">
              <property name="sizePolicy">
               <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
                <horstretch>1</horstretch>
                <verstretch>0</verstretch>
               </sizepolicy>
              </property>
              <property name="text">
               <string>ЧастотаX   </string>
              </property>
             </widget>
            </item>
            <item>
             <widget class="QSlider" name="frequencyX_slider">
              <property name="sizePolicy">
               <sizepolicy hsizetype="MinimumExpanding" vsizetype="Fixed">
                <horstretch>20</horstretch>
                <verstretch>0</verstretch>
               </sizepolicy>
              </property>
              <property name="inputMethodHints">
               <set>Qt::ImhNone</set>
              </property>
              <property name="minimum">
               <number>0</number>
              </property>
              <property name="maximum">
               <number>100</number>
              </property>
              <property name="value">
               <number>50</number>
              </property>
              <property name="tracking">
               <bool>true</bool>
              </property>
              <property name="orientation">
               <enum>Qt::Horizontal</enum>
              </property>
              <property name="invertedAppearance">
               <bool>false</bool>
              </property>
              <property name="invertedControls">
               <bool>false</bool>
              </property>
             </widget>
            </item>
            <item>
             <widget class="QLineEdit" name="frequencyX_lineEdit">
              <property name="enabled">
               <bool>true</bool>
              </property>
              <property name="sizePolicy">
               <sizepolicy hsizetype="Ignored" vsizetype="Fixed">
                <horstretch>1</horstretch>
                <verstretch>0</verstretch>
               </sizepolicy>
              </property>
              <property name="minimumSize">
               <size>
                <width>40</width>
                <height>0</height>
               </size>
              </property>
              <property name="text">
               <string>0.5</string>
              </property>
             </widget>
            </item>
            <item>
             <spacer name="horizontalSpacer_2">
              <property name="orientation">
               <enum>Qt::Horizontal</enum>
              </property>
              <property name="sizeHint" stdset="0">
               <size>
                <width>40</width>
                <height>20</height>
               </size>
              </property>
             </spacer>
            </item>
           </layout>
          </item>
         </layout>
        </item>
        <item>
         <widget class="Line" name="line">
          <property name="sizePolicy">
           <sizepolicy hsizetype="Preferred" vsizetype="Fixed">
            <horstretch>50</horstretch>
            <verstretch>3</verstretch>
           </sizepolicy>
          </property>
          <property name="orientation">
           <enum>Qt::Horizontal</enum>
          </property>
         </widget>
        </item>
        <item>
         <layout class="QHBoxLayout" name="horizontalLayout_1">
          <item>
           <spacer name="horizontalSpacer_5">
            <property name="orientation">
             <enum>Qt::Horizontal</enum>
            </property>
            <property name="sizeHint" stdset="0">
             <size>
              <width>40</width>
              <height>20</height>
             </size>
            </property>
           </spacer>
          </item>
          <item>
           <widget class="QLabel" name="label_phaseX">
            <property name="text">
             <string>Начальная фаза по X(φx)</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QLineEdit" name="phaseX_lineEdit">
            <property name="minimumSize">
             <size>
              <width>40</width>
              <height>0</height>
             </size>
            </property>
            <property name="maximumSize">
             <size>
              <width>80</width>
              <height>16777215</height>
             </size>
            </property>
            <property name="text">
             <string>pi</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QLabel" name="label_phaseY">
            <property name="text">
             <string>Начальная фаза по Y(φy)</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QLineEdit" name="phaseY_lineEdit">
            <property name="sizePolicy">
             <sizepolicy hsizetype="Expanding" vsizetype="Fixed">
              <horstretch>0</horstretch>
              <verstretch>0</verstretch>
             </sizepolicy>
            </property>
            <property name="minimumSize">
             <size>
              <width>40</width>
              <height>0</height>
             </size>
            </property>
            <property name="maximumSize">
             <size>
              <width>80</width>
              <height>16777215</height>
             </size>
            </property>
            <property name="text">
             <string>0</string>
            </property>
           </widget>
          </item>
          <item>
           <spacer name="horizontalSpacer">
            <property name="orientation">
             <enum>Qt::Horizontal</enum>
            </property>
            <property name="sizeType">
             <enum>QSizePolicy::Expanding</enum>
            </property>
            <property name="sizeHint" stdset="0">
             <size>
              <width>155</width>
              <height>20</height>
             </size>
            </property>
           </spacer>
          </item>
          <item>
           <widget class="QPushButton" name="button_reset">
            <property name="sizePolicy">
             <sizepolicy hsizetype="Maximum" vsizetype="Fixed">
              <horstretch>0</horstretch>
              <verstretch>0</verstretch>
             </sizepolicy>
            </property>
            <property name="text">
             <string>Reset</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="button_render">
            <property name="text">
             <string>Render</string>
            </property>
           </widget>
          </item>
         </layout>
        </item>
       </layout>
      </widget>
      <widget class="QWidget" name="info">
       <attribute name="title">
        <string>info</string>
       </attribute>
       <layout class="QVBoxLayout" name="verticalLayout_2">
        <item>
         <widget class="QTextBrowser" name="textBrowser">
          <property name="html">
           <string>&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot; &quot;http://www.w3.org/TR/REC-html40/strict.dtd&quot;&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name=&quot;qrichtext&quot; content=&quot;1&quot; /&gt;&lt;style type=&quot;text/css&quot;&gt;
p, li { white-space: pre-wrap; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=&quot; font-family:'MS Shell Dlg 2'; font-size:6.6pt; font-weight:400; font-style:normal;&quot;&gt;
&lt;p align=&quot;center&quot; style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-size:10pt; font-weight:600;&quot;&gt;Фигуры Лиссажу&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-size:10pt;&quot;&gt;Фигуры Лиссажу были впервые описаны французским физиком Жюлем Антуаном Лиссажу в 1857 году. Он использовал их для изучения акустических колебаний, но с тех пор они нашли применение в различных областях, включая физику, математику и инженерию.&lt;br /&gt;Компьютерное моделирование фигур Лиссажу позволяет исследователям изучать их свойства и поведение, а также генерировать сложные и эстетически приятные узоры.&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
          </property>
         </widget>
        </item>
       </layout>
      </widget>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>835</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""
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
        # uic.loadUi('untitled.ui', self)  # from ui file
        f = io.StringIO(template)
        uic.loadUi(f, self)
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
        self.phaseY_lineEdit.setText(str(0))
        self.phaseX_lineEdit.setText(str("pi"))

        self.frequencyY_lineEdit_changeValue()
        self.frequencyX_lineEdit_changeValue()
        self.amplitudeY_lineEdit_changeValue()
        self.amplitudeX_lineEdit_changeValue()

        self.button_render_clicked()

    def phaseY_lineEdit_changeValue(self):
        try:
            if "pi" not in str(self.phaseY_lineEdit.text()):
                self.phaseY_lineEdit.setText(str(eval(self.phaseY_lineEdit.text().replace(",", "."))))
        except ValueError:
            pass
        except SyntaxError:
            pass
        self.button_render_clicked()

    def phaseX_lineEdit_changeValue(self):
        try:
            if "pi" not in str(self.phaseX_lineEdit.text()):
                self.phaseX_lineEdit.setText(str(eval(str(self.phaseX_lineEdit.text).replace(",", "."))))
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
