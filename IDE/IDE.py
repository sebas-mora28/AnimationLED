# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IDE.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



from ventana_Emergente import Ui_VentanaEmergente
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1055, 715)
        MainWindow.setMinimumSize(QtCore.QSize(1055, 715))
        MainWindow.setMaximumSize(QtCore.QSize(1055, 715))
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QCodeEditor(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 1051, 681))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(11)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1055, 26))
        self.menubar.setAccessibleName("")
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menuConstruir = QtWidgets.QMenu(self.menubar)
        self.menuConstruir.setObjectName("menuConstruir")
        MainWindow.setMenuBar(self.menubar)
        self.actionCargar = QtWidgets.QAction(MainWindow)
        self.actionCargar.setObjectName("actionCargar")
        self.actionGuardar = QtWidgets.QAction(MainWindow)
        self.actionGuardar.setObjectName("actionGuardar")
        self.actionNuevo = QtWidgets.QAction(MainWindow)
        self.actionNuevo.setObjectName("actionNuevo")
        self.actionCompilar = QtWidgets.QAction(MainWindow)
        self.actionCompilar.setObjectName("actionCompilar")
        self.menufile.addAction(self.actionNuevo)
        self.menufile.addAction(self.actionCargar)
        self.menufile.addAction(self.actionGuardar)
        self.menuConstruir.addAction(self.actionCompilar)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuConstruir.menuAction())
        self.actionCargar.triggered.connect(self.cargarArchivo)
        self.actionGuardar.triggered.connect(self.guardarArchivo)
        self.actionNuevo.triggered.connect(self.nuevoProyecto)
        self.actionCompilar.triggered.connect(self.compilar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IDE"))
        self.menufile.setTitle(_translate("MainWindow", "Archivo"))
        self.menuConstruir.setTitle(_translate("MainWindow", "Construir "))
        self.actionCargar.setText(_translate("MainWindow", "Cargar"))
        self.actionCargar.setStatusTip(_translate("MainWindow", "Cargar Archivo"))
        self.actionCargar.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.actionGuardar.setText(_translate("MainWindow", "Guardar"))
        self.actionGuardar.setStatusTip(_translate("MainWindow", "Guardar Archivo"))
        self.actionGuardar.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionNuevo.setText(_translate("MainWindow", "Nuevo"))
        self.actionNuevo.setStatusTip(_translate("MainWindow", "Crear Nuevo Archivo"))
        self.actionNuevo.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionCompilar.setText(_translate("MainWindow", "Compilar"))
        self.actionCompilar.setStatusTip(_translate("MainWindow", "Compilar Programa"))
        self.actionCompilar.setShortcut(_translate("MainWindow", "Ctrl+R"))
    def cargarArchivo(self):
        archivo = QFileDialog.getOpenFileName(self,'Cargar Archivo','c:\\','Text files (*.txt)')
        if archivo[0]:
            with open(archivo[0], "rt") as buff:
                texto = buff.read()
                self.plainTextEdit.insertPlainText(texto)
    def guardarArchivo(self):
        opciones = QFileDialog.Options()
        archivo, _ = QFileDialog.getSaveFileName(self,'Guardar Archivo...','c:\\','Text files (*.txt)', options=opciones)
        with open(archivo, 'wt') as buff:
            buff.write(self.plainTextEdit.toPlainText())
    def nuevoProyecto(self):
        self.plainTextEdit.clear()
    def compilar(self):
        print(self.plainTextEdit.toPlainText())
        errores = ["Semantic error: Invalid data for time, an int is expected","Semantic error: Invalid data for sate, a bool is expected"]
        self.abrir_Ventana(errores)
    def abrir_Ventana(self, errores):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_VentanaEmergente()
        self.ui.setupUi(self.window)
        self.ui.mostrarErrores(errores)
        self.window.show()
        
from QCodeEditor import QCodeEditor

    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
