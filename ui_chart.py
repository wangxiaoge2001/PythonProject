from importlib.abc import PathEntryFinder
from PySide2.QtCore import QPointF
from PySide2.QtCore import Qt
from PySide2.QtCharts import QtCharts
from PySide2.QtGui import QPainter
from PySide2.QtGui import QGuiApplication
from PySide2.QtGui import QScreen
from PySide2.QtGui import QPixmap
from PySide2.QtCore import QObject
from PySide2.QtCore import SIGNAL
from PySide2.QtCore import QTime
from PySide2.QtWidgets import *
from functools import partial
import random
import csv_read
import time
import copy


class my_normal_chart(QObject):
    def __init__(self, chart_view, pnt, ui):
        super().__init__()
        self.chart = QtCharts.QChart()
        self.cv = chart_view
        self.parent_frame = pnt
        self.size_type = False
        self.formx = 0
        self.formy = 0
        self.posx = 0
        self.posy = 0
        self.ui = ui

    def change_size(self):
        if(not self.size_type):
            self.formx = self.parent_frame.frameSize().width()
            self.formy = self.parent_frame.frameSize().height()
            self.posx = self.parent_frame.x()
            self.posy = self.parent_frame.y()
            self.chart.setAnimationOptions(QtCharts.QChart.NoAnimation)
            self.parent_frame.setGeometry(0, 0, self.ui.stackedWidget.frameSize().width(),
                                          self.ui.stackedWidget.frameSize().height())
            self.parent_frame.raise_()
            self.size_type = True
        else:
            self.parent_frame.setGeometry(
                self.posx, self.posy, self.formx, self.formy)
            self.chart.setAnimationOptions(QtCharts.QChart.AllAnimations)
            self.size_type = False

    def finish_draw(self, anime=True):
        self.chart.setTheme(QtCharts.QChart.ChartThemeQt)
        if(anime):
            self.chart.setAnimationOptions(QtCharts.QChart.AllAnimations)
        self.cv.setRenderHint(QPainter.Antialiasing)
        self.cv.setChart(self.chart)


class my_pie_chart(my_normal_chart):
    def __init__(self, chart_view, pnt, ui):
        super().__init__(chart_view, pnt, ui)
        self.pie = QtCharts.QPieSeries()
        self.pie.clicked.connect(self.change_size)

    def load_data(self, type, data):
        n = len(type)
        for i in range(n):
            new_slice = QtCharts.QPieSlice()
            new_slice.setLabel(type[i]+" "+str(round(data[i], 4)*100)+"%")
            new_slice.setValue(data[i])
            new_slice.setLabelVisible(True)
            self.pie.append(new_slice)

    def finish_draw(self):
        self.chart.addSeries(self.pie)
        self.chart.legend().hide()
        super().finish_draw()


class my_bar_chart(my_normal_chart):
    def __init__(self, chart_view, pnt, ui):
        super().__init__(chart_view, pnt, ui)
        self.bar = QtCharts().QBarSeries()
        self.types = QtCharts.QBarCategoryAxis()
        self.values = QtCharts.QValueAxis()
        self.bar.clicked.connect(self.change_size)

    def load_data(self, groups_name, groups_data):
        n = len(groups_name)
        self.values.setRange(0, 10)
        self.types.append(groups_name)
        for i in range(n):
            new_barset = QtCharts.QBarSet(groups_name[i])
            for j in groups_data[i]:
                new_barset.append(j)
            self.bar.append(new_barset)

    def finish_draw(self):
        self.chart.addSeries(self.bar)
        self.chart.addAxis(self.types, Qt.AlignBottom)
        self.chart.addAxis(self.values, Qt.AlignLeft)
        super().finish_draw()


class my_line_chart(my_normal_chart):
    def __init__(self, chart_view, pnt, ui):
        super().__init__(chart_view, pnt, ui)
        self.line = QtCharts().QLineSeries()
        self.x = QtCharts().QValueAxis()
        self.y = QtCharts().QValueAxis()

    def load_data(self, dataX, dataY):
        n = len(dataX)
        for i in range(n):
            self.line.append(dataX[i], dataY[i])

    def finish_draw(self):
        self.chart.addSeries(self.line)
        self.chart.createDefaultAxes()
        self.chart.setAxisX(self.x)
        self.chart.setAxisY(self.y)
        super().finish_draw()


def setLine_example(gv):
    chart = my_line_chart(gv)
    n = random.randint(1, 10)
    x = []
    y = []
    for i in range(n):
        x.append(random.randint(3, 10))
        y.append(random.randint(2, 20))
    x.sort()
    chart.load_data(x, y)
    chart.axis_x().setRange(0, 10)
    chart.axis_y().setRange(0, 20)
    chart.finish_draw()


def set_page_1(chartviews, parent_frames, ui):
    global chart_sex
    chart_sex = my_pie_chart(chartviews[0], parent_frames[0], ui)
    chart_sex.load_data(["Boys", "Girls"], csv_read.sex_ratio)
    chart_sex.finish_draw()

    global chart_nationality
    chart_nationality = my_pie_chart(chartviews[1], parent_frames[1], ui)
    chart_nationality.load_data(csv_read.nation_name, csv_read.nation_ratio)
    chart_nationality.pie.setPieStartAngle(120)
    chart_nationality.pie.setPieEndAngle(480)
    chart_nationality.finish_draw()

    global chart_birthplace
    chart_birthplace = my_pie_chart(chartviews[2], parent_frames[2], ui)
    chart_birthplace.load_data(csv_read.place_name, csv_read.place_ratio)
    chart_birthplace.pie.setPieStartAngle(120)
    chart_birthplace.pie.setPieEndAngle(480)
    chart_birthplace.finish_draw()

    global chart_academic_year
    chart_academic_year = my_bar_chart(chartviews[3], parent_frames[3], ui)
    chart_academic_year.load_data(
        csv_read.academic_name, csv_read.academic_num)
    chart_academic_year.finish_draw()
