
class MyClass():
   """описание класса"""
  #self это ссылка на обьект который мы создадим
   
   def __init__(self , file):
       self.file = file
       
      # self.value2=value2
    
      
   def DataCollection(self):
      dataCoil=[]
       # dataCollList=list(dataCoil)
      #dataCoil=' '
      a=1
     
      for i in self.file:
          if a==0:
             break
          
          i = self.file.readline()
          if i =='ENTITIES\n':
             for j in self.file:
                 j = self.file.readline()
                 if j =='AcDbCircle\n':
                   #  dataCoil+=j
                     for k in self.file:
                         k = self.file.readline()
                         if k =='ENDSEC\n':                             
                              break  
                         elif k == 'CIRCLE\n':
                              break   
                        # dataCoil+=k                  
                         dataCoil.append(k)
                 elif j =='ENDSEC\n':
                         a=0  # выход из условия
                         break   
                      
             
      return  dataCoil        
    
      
   def Scanner(self):
     
     returnList=[]
     k=-1
     dataColl=self.DataCollection()      
     for i in dataColl:
         returnList.append(float(i))

     dataColl.clear()
     for i in returnList:
        k+=1
        if k ==2:         
         localChar=i
         #if i != 0.0:   
        else:
         dataColl.append(round(i,2))
         if k==3:
             k=-1
          
     #for i in mYlist :
         
     return dataColl # mYlist
   

   #https://www.youtube.com/watch?v=mgGnsM4u4oQ
   

 #region
   #VVsolution+OpenDXF
   """ 
import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QVBoxLayout,QPushButton,QFileDialog,QWidget
import pyqtgraph
import matplotlib
import math
import os
from OpenRead import MyClass


class MainWindow(QtWidgets.QMainWindow,QWidget):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('C:\\Users\\UserName\\source\\repos\\Python\\VVsolution+OpenDXF\\design.ui', self)
        
        self.window_width,self.window_height = 1000,50
        self.setMinimumSize(self.window_width,self.window_height)
        layout=QVBoxLayout()
        self.setLayout(layout)
        
        btn= QPushButton('OpenFile')
        btn.clicked.connect(self.OpenFile)
        layout.addWidget(btn)

        self.graphWidget.showGrid(None, None, 0)
        self.graphWidget.plot([100,100],[100,0])

       
    def OpenFile(self):
         response = self.getFileName()
         file=open(response,encoding='utf=8')
         mass=MyClass(file)
         mass1 = mass.Scanner()
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

"""
#endregion