  #VVsolution+OpenDXF
import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog,QWidget, QGridLayout, QMainWindow,QPushButton,QTextEdit
import matplotlib
import math
import os
from PyQt5.QtCore import Qt
from OpenRead import MyClass
from tkinter import *

class MainWindow(QtWidgets.QMainWindow,QWidget):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('design.ui', self)
       
       # layout = QGridLayout(self.centralwidget)
        btnOpenFile= QPushButton('OpenFile',self)
        btnOpenFile.move(10,10)
        btnOpenFile.setFixedSize(140,70)
        btnOpenFile.clicked.connect(self.OpenFile)
        btnTraje= QPushButton('Trajectory',self)
        btnTraje.move (10,80)
        btnTraje.setFixedSize(140,70)
        
        
        textBox=QTextEdit('GCode',self)       
        textBox.move (10,150)
        textBox.setFixedSize(280,210)
        myText= (2,5,7,8,3)#self.callFunction
        
        self.textBox.setText(myText)
        btnTraje.clicked.connect(textBox.textChanged(myText))
        
    def callFunction(self):
        myTextA = []
        myTextB = []
        returnText=[]
        for i in 30:
           myTextA.append((i+5)*2)
           myTextB .append((i-5)*2)
        self.Trajectory(self,myTextA,myTextB)
        for i in myTextA:
            returnText.append(myTextA[i])
            returnText.append(myTextB[i])
        return returnText
          

    def Trajectory(self,myTrajectorA=[],myTrajectorB=[]):       
        self.plot(myTrajectorA,myTrajectorB)
        self.graphWidget.plot([100,100],[100,0])
        
        

    def OpenFile(self):
         response = self.getFileName()
         file=open(response,encoding='utf=8')
         mass=MyClass(file)
         mass1 = mass.Scanner()
         exportMass=[]
         k=-1
         for i in mass1:
             k+=1
             exportMass.append(int(i))
             if k==2:
                 self.drawCircuit(exportMass[0],exportMass[1],exportMass[2])
                 exportMass.clear()
                 k=-1
         
         print(mass1)
         

    def getFileName (self):
        file_filter= 'Data file(*.txt *.dxf)'
        response= QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a file',
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter= 'Data file(*.txt *.dxf)'           
           )
        
        return response
    
    def plot(self,hour,temperature):
        self.graphWidget.plot(hour, temperature)

  #Костя, функция рисования окружности
    def drawCircuit(self, Xc, Yc, Rc):
        X = []
        Y = []
        for alpha in range(0,361):
            
            X.append(Rc*math.cos(math.pi*alpha/180)+Xc)
            Y.append(Rc*math.sin(math.pi*alpha/180)+Yc)
       
        self.graphWidget.plot(X, Y)

             
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet('''QWidget{font-size:20px;}''')
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

   
"""
   
"""