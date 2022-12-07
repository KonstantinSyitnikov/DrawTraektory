  #VVsolution+OpenDXF
import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor
from PyQt5.QtWidgets import QVBoxLayout,QPushButton,QFileDialog,QWidget,QLabel, QGridLayout,QApplication, QMainWindow
import pyqtgraph
import matplotlib
import math
import os
from PyQt5.QtCore import Qt
from OpenRead import MyClass


class MainWindow(QtWidgets.QMainWindow,QWidget):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.LoadUiWind()
        
       # layout.addWidget(self.label, 1, 0)  
       # self.graphWidget.showGrid(None, None, 0)
       # self.drawCircuit(0, 0, 20)

    def LoadUiWind(self):
        uic.loadUi('C:\\Users\\UserName\\source\\repos\\Python\\VVsolution-OpenDXF\\design.ui', self)
        self.pushButton.setFixedSize(140, 70)
        self.pushButton.clicked.connect(self.OpenFile)
        layout = QGridLayout(self.centralwidget)
        layout.addWidget(self.pushButton, 0, 0, alignment=Qt.AlignLeft)

    def OpenFile(self):
         response = self.getFileName()
         file=open(response,encoding='utf=8')
         mass=MyClass(file)
         mass1 = mass.Scanner()
         self.LoadUiWind()
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
        print(response)
        return response[0]
    
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

             
            
       
#вызывается так
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet('''QWidget{font-size:20px;}''')
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
   #endregion
   

    
     #region когда то созданное
   
''' public string Recording_Str(ref StreamReader streamReader)// KOMPAS
        {
            string str;
            while (!streamReader.EndOfStream)
            {
                str = streamReader.ReadLine();
                if (str == "DIMSTYLE")
                {

                    while (str != "XRECORD")
                    {
                        str = streamReader.ReadLine();
                        strja += str + Environment.NewLine;
                    }

                }

            }
            return strja;
        }

        public string Scanner()
        {


            using (TextReader tr = new StringReader(strja))
            {

                while ((str = tr.ReadLine()) != null)
                {
                    if (str == "AcDbPolyline")
                    {

                        str1 += str + Environment.NewLine;
                        for (int i = 0; i < 7; i++)
                        {
                            str = tr.ReadLine();
                        }
                        while (str != "ENDSEC")
                        {
                            str = tr.ReadLine();
                            for (int j = 0; j < 8; j++)
                            {
                                // str = tr.ReadLine();
                                NumberFormatInfo numberFormatInfo = new NumberFormatInfo()// решение проблемы точки и запятой
                                {
                                    NumberDecimalSeparator = ".", // решение проблемы точки и запятой
                                };
                                str1 += str + Environment.NewLine;
                                size = j;
                                str = tr.ReadLine();
                                str = tr.ReadLine();
                            }

                            for (int i = 0; i < 3; i++)
                            {
                                str = tr.ReadLine();
                                if (str == "LWPOLYLINE")
                                {
                                    break;
                                }
                            }
                            break;
                        }

                    }

                    if (str == "AcDbLine")
                    {

                        str1 += str + Environment.NewLine;
                        str = tr.ReadLine();
                        while (str != "ENDSEC")
                        {
                            str = tr.ReadLine();
                            for (int j = 0; j < 5; j++)
                            {
                                // str = tr.ReadLine();
                                NumberFormatInfo numberFormatInfo = new NumberFormatInfo()// решение проблемы точки и запятой
                                {
                                    NumberDecimalSeparator = ".", // решение проблемы точки и запятой
                                };
                                if (j == 2)
                                {
                                    str = tr.ReadLine();
                                    str = tr.ReadLine();
                                }
                                if (j == 4)
                                {
                                    break;
                                }

                                str1 += str + Environment.NewLine;
                                str = tr.ReadLine();
                                str = tr.ReadLine();
                            }
                            for (int i = 0; i < 3; i++)
                            {
                                str = tr.ReadLine();
                                if (str == "LINE")
                                {
                                    break;
                                }
                            }
                            break;
                        }

                    }

                    if (str == "AcDbCircle")
                    {

                        str1 += str + Environment.NewLine;
                        str = tr.ReadLine();

                        while (str != "ENDSEC")
                        {
                            // 

                            str = tr.ReadLine();
                            for (int j = 0; j < 3; j++)
                            {

                                // str = tr.ReadLine();

                                NumberFormatInfo numberFormatInfo = new NumberFormatInfo()// решение проблемы точки и запятой
                                {
                                    NumberDecimalSeparator = ".", // решение проблемы точки и запятой
                                };
                                if (j == 2)
                                {
                                    str = tr.ReadLine();
                                    str = tr.ReadLine();
                                }
                                str1 += str + Environment.NewLine;



                                str = tr.ReadLine();
                                str = tr.ReadLine();
                            }
                            for (int i = 0; i < 10; i++)
                            {
                                str = tr.ReadLine();
                                if (str == "CIRCLE")
                                {
                                    break;
                                }
                            }
                            break;
                        }
                    }




                }
            }

            return str1;
        }
        public string[] ForListBox()
        {
            string[] str2 = new string[300];
            int a = 0;
            using (TextReader tr = new StringReader(str1))
            {

                for (int i = 0; i < str1.Length; i++)
                {
                    str = tr.ReadLine();
                    str2[i] = str;
                    a = i;
                    if (str == null)
                    {

                        break;
                    }

                }

                scanner = new string[a];
                for (int i = 0; i < scanner.Length; i++)
                {
                    scanner[i] = str2[i];
                    if (str2 == null)
                    {
                        break;
                    }
                }

            }
            return scanner;
        }
        public int Size()
        {
            return size + 1;
        }
    }
}
'''
#endregion