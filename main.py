import sys
from PyQt5.QtWidgets import QApplication,QDialog,QPushButton,QMessageBox
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
import backtrackigMyGraph
import map_coloring
import arc_consistency


class MainFrame(QDialog):

    nodes_connect_list = [['n2'],['n3','n4'],['n0','n3','n5','n6','n8'],['n1','n2','n5','n6','n7','n8']
                       ,['n1','n6','n7'],['n2','n3','n6','n8'],['n2','n3','n4','n5','n7','n8','n9']
                       ,['n3','n4','n6'],['n2','n3','n5','n6'],['n6']]

    
    nodes_domain_list = []

    coloring = [[],[],[],[],[],[],[],[],[],[]]

    count = 0
    def __init__(self):
        super(MainFrame,self).__init__()
        loadUi('Graphics.ui',self)
        self.setWindowTitle("This Is Main Frame")

        self.algorithm_comboBox.addItem("None")
        self.algorithm_comboBox.addItem("Backtracking")
        self.algorithm_comboBox.addItem("Own Method")

        self.ordering_comboBox.addItem("None")
        self.ordering_comboBox.addItem("MRV")

        self.filtering_comboBox.addItem("None")
        self.filtering_comboBox.addItem("Arc Consistency")

        self.algorithm_comboBox.activated.connect(self.algorithmComboboxSelect)
        self.filtering_comboBox.activated.connect(self.filtering_comboBoxSelect)
        self.ordering_comboBox.activated.connect(self.ordering_comboBoxSelect)
        
        self.start_pushButton.clicked.connect(self.start_pushButtonClicked)
        self.refresh_pushButton.clicked.connect(self.refresh_pushButtonClicked)
        self.next_pushButton.clicked.connect(self.next_pushButtonClicked)
        self.node_number_label.setText(str(self.count))

    def next_pushButtonClicked(self):
        print("next")
        if(len(self.nodes_domain_list) == len(self.nodes_connect_list)):
            print("All Nodes Domain are Entered...")
            QMessageBox().warning(self, "Notification Message..", "<h1>All Nodes Domain Have Been Entered<\h1>", QMessageBox.Ok)
        else:
            domain = list((self.node_domain_lineEdit.text()).upper())#RGBCY
            print(domain)
            self.nodes_domain_list.append(domain)
            print(self.nodes_domain_list)
            self.count = self.count+1
            if(self.count < len(self.nodes_connect_list)):
                self.node_number_label.setText(str(self.count))
            else:
                QMessageBox().warning(self, "Notification Message..", "<h1>All Nodes Domain Have Been Entered<\h1>", QMessageBox.Ok)
        
    def start_pushButtonClicked(self):
        algorithm_comboBox_text = self.algorithm_comboBox.currentText()
        filtering_comboBox_text = self.filtering_comboBox.currentText()
        ordering_comboBox_text = self.ordering_comboBox.currentText()
        print(algorithm_comboBox_text)
        if([] in self.coloring):
            QMessageBox().information(self, "Notification Message..", "<h1>Impossible to coloring...<\h1>", QMessageBox.Ok)
            print("Nothing")
        else:
            if(algorithm_comboBox_text == "None"):
                if(filtering_comboBox_text == "None"):
                    if(ordering_comboBox_text == "None"):
                        self.selected_label.setText("The Graph Before Coloring")
                    else:
                        self.selected_label.setText("The Graph is Colored Using "+ordering_comboBox_text)
                else:
                    self.selected_label.setText("The Graph is Colored Using "+filtering_comboBox_text)
            else:
                print(algorithm_comboBox_text)
                self.selected_label.setText("The Graph is Colored Using "+algorithm_comboBox_text)
            
            widget.hide()
            widget.show()

    def refresh_pushButtonClicked(self):
        self.selected_label.setText("The Graph Before Coloring")
        widget.hide()
        widget.show()
        self.ordering_comboBox.setCurrentIndex(0)
        self.filtering_comboBox.setCurrentIndex(0)
        self.algorithm_comboBox.setCurrentIndex(0)
        self.coloring = [[],[],[],[],[],[],[],[],[],[]]
        self.nodes_domain_list.clear()
        self.count = 0
        self.node_number_label.setText(str(self.count))
        
        
        
    def algorithmComboboxSelect(self,index):
        item_select = self.algorithm_comboBox.itemText(index)
        print(item_select)
        self.ordering_comboBox.setCurrentIndex(0)
        self.filtering_comboBox.setCurrentIndex(0)
        #print(self.algorithm_comboBox.itemData(index))
        if(item_select == "Backtracking"):
            coloring_temp = [[],[],[],[],[],[],[],[],[],[]]
            colours_name = ['R','G','B','C','Y']
            obj = backtrackigMyGraph.main()
            print("In Graph2 : ",obj)
            print(len(obj))
            if(0 not in obj):
                for x in range(len(obj)):
                    coloring_temp[x] = list(colours_name[obj[x]-1])


                print(coloring_temp)
                self.coloring = coloring_temp
            else:
                print("Graph Color Impossible")
                self.refresh_pushButtonClicked()
                
            

            

        if(item_select == "Own Method"):
            coloring_temp = [[],[],[],[],[],[],[],[],[],[]]
            obj  = map_coloring.main()
            print("In Graph2 : ",obj)
            print(len(obj))
            if("[N]" not in obj):
                print("Ok")
                for x in range(len(obj)):
                    coloring_temp[x] = list(obj[x])


                print(coloring_temp)
                self.coloring = coloring_temp
                obj.clear()
            else:
                print("Graph Color Impossible")
                self.refresh_pushButtonClicked()
                obj.clear()
            



        
    
    def filtering_comboBoxSelect(self,index):
        item_Select = self.filtering_comboBox.itemText(index)
        print(item_Select)
        self.ordering_comboBox.setCurrentIndex(0)
        self.algorithm_comboBox.setCurrentIndex(0)

        if(len(self.nodes_domain_list) < len(self.nodes_connect_list)):
            QMessageBox().warning(self, "Notification Message..", "<h1>Enter The Domain Of All Nodes First..<\h1>", QMessageBox.Ok)
            self.filtering_comboBox.setCurrentIndex(0)

        else:
            if(item_Select == "Arc Consistency"):
                print("Arc Consistency YES")
                obj = arc_consistency.main(self.nodes_domain_list)
                print("Arc Consistency ............",obj)
                if(obj == True):
                    QMessageBox().warning(self, "Notification Message..", "<h1>According to entered domain graph is consistent..<\h1>", QMessageBox.Ok)
                else:
                    QMessageBox().warning(self, "Notification Message..", "<h1>According to entered domain graph is not consistent..<\h1>", QMessageBox.Ok)
                    
            
            
            
    def ordering_comboBoxSelect(self,index):
        item_Select = self.ordering_comboBox.itemText(index)
        print(item_Select)
        self.filtering_comboBox.setCurrentIndex(0)
        self.algorithm_comboBox.setCurrentIndex(0)
        if(len(self.nodes_domain_list) < len(self.nodes_connect_list)):
            QMessageBox().warning(self, "Notification Message..", "<h1>Enter The Domain Of All Nodes First..<\h1>", QMessageBox.Ok)
            self.ordering_comboBox.setCurrentIndex(0)

        else:
            nodes_domain_list_temp_store = list(self.nodes_domain_list)
            nodes_domain_list_temp = list(nodes_domain_list_temp_store)
            nodes_colors = [[],[],[],[],[],[],[],[],[],[]]

            if(item_Select == "MRV"):
                #print(self.nodes_domain_list.index(max(self.nodes_domain_list, key=len)))
                print("MRV YES")
                if([] in self.nodes_domain_list):
                    QMessageBox().warning(self, "Notification Message..", "<h1>Coloring is impossible because one or more entered domain is empty.....<\h1>", QMessageBox.Ok)
                else:
                    isPossible = True
                    for x in range(len(self.nodes_connect_list)):
                        print("X : ",x)
                        index = nodes_domain_list_temp.index(min(nodes_domain_list_temp, key= len))
                        print(index)
                        color = nodes_domain_list_temp[index][:1]
                        nodes_domain_list_temp[index] = nodes_domain_list_temp[index][:1]
                        print(color)
                        for y in range(len(self.nodes_connect_list[index])):
                            print("Y : ",y)
                            node = self.nodes_connect_list[index][y]
                            node_number = int(node[1:])
                            print(node_number)
                            print(list(nodes_domain_list_temp[index][0]),">>>>>>>>>",len(self.nodes_domain_list[node_number]))
                            if((len(self.nodes_domain_list[node_number])==1) and (list(nodes_domain_list_temp[index][0]) == self.nodes_domain_list[node_number])):
                                print("Impossible")
                                isPossible = False
                                break
                            if(nodes_domain_list_temp[index][0] in self.nodes_domain_list[node_number]):
                                nodes_domain_list_temp[node_number].remove(nodes_domain_list_temp[index][0])
                                isPossible = True

                        if(isPossible == False):
                            print("Impossible")
                            break
                        print(color)
                        nodes_colors[index] = list(color)
                        self.nodes_domain_list = list(nodes_domain_list_temp)
                        nodes_domain_list_temp[index] = list(['None','None','None','None','None','None','None','None'])
                    print("Finally : ",nodes_colors)
                    self.nodes_domain_list = list(nodes_domain_list_temp_store)
                    if(([] in nodes_colors) or (isPossible == False)):
                        QMessageBox().warning(self, "Notification Message..", "<h1>According to entered domain coloring is impossible.....<\h1>", QMessageBox.Ok)
                    else:
                        self.coloring = list(nodes_colors)
                    
                    
       
    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black,2,Qt.SolidLine))
        
        if(self.coloring[0] == ['R']):
            painter.setBrush(Qt.red)
        if(self.coloring[0]==['G']):
            painter.setBrush(Qt.green)
        if(self.coloring[0]==['Y']):
            painter.setBrush(Qt.yellow)
        if(self.coloring[0]==['B']):
            painter.setBrush(Qt.blue)
        if(self.coloring[0]==['C']):
            painter.setBrush(Qt.cyan)
            
        c1 = painter.drawEllipse(50,20,50,50)
        painter.drawText( 75,45,"n0")
        #painter.drawRect(50, 20,50,50) 
        
        #painter.setBrush(QtGui.QColor(0,255,0))
        #painter.fillEllipse( 20,  50, 100, 40, Qt.magenta )
        #painter.setBrush(Qt.red)

        
        if(self.coloring[1] == ['R']):
            painter.setBrush(Qt.red)
        if(self.coloring[1]==['G']):
            painter.setBrush(Qt.green)
        if(self.coloring[1]==['Y']):
            painter.setBrush(Qt.yellow)
        if(self.coloring[1]==['B']):
            painter.setBrush(Qt.blue)
        if(self.coloring[1]==['C']):
            painter.setBrush(Qt.cyan)    
        c2 = painter.drawEllipse(260,20,50,50)
        painter.drawText( 285,45,"n1")
        #painter.drawRect(260,20,50,50)
        

        if(self.coloring[2] == ['R']):
            painter.setBrush(Qt.red)
        if(self.coloring[2]==['G']):
            painter.setBrush(Qt.green)
        if(self.coloring[2]==['Y']):
            painter.setBrush(Qt.yellow)
        if(self.coloring[2]==['B']):
            painter.setBrush(Qt.blue)
        if(self.coloring[2]==['C']):
            painter.setBrush(Qt.cyan)
        c3 = painter.drawEllipse(120,90,50,50)
        painter.drawText( 145,115,"n2")
        #painter.drawRect(120,90,50,50)

        if(self.coloring[3] == ['R']):
            painter.setBrush(Qt.red)
        if(self.coloring[3]==['G']):
            painter.setBrush(Qt.green)
        if(self.coloring[3]==['Y']):
            painter.setBrush(Qt.yellow)
        if(self.coloring[3]==['B']):
            painter.setBrush(Qt.blue)
        if(self.coloring[3]==['C']):
            painter.setBrush(Qt.cyan)
        c4 = painter.drawEllipse(190,90,50,50)
        painter.drawText( 215,115,"n3")
        #painter.drawRect(190,90,50,50)
        

        if(self.coloring[4] == ['R']):
            painter.setBrush(Qt.red)
        if(self.coloring[4]==['G']):
            painter.setBrush(Qt.green)
        if(self.coloring[4]==['Y']):
            painter.setBrush(Qt.yellow)
        if(self.coloring[4]==['B']):
            painter.setBrush(Qt.blue)
        if(self.coloring[4]==['C']):
            painter.setBrush(Qt.cyan)   
        c5 = painter.drawEllipse(330,90,50,50)
        painter.drawText( 355,115,"n4")
        #painter.drawRect(330,90,50,50)
        

        if(self.coloring[5] == ['R']):
            painter.setBrush(Qt.red)
        if(self.coloring[5]==['G']):
            painter.setBrush(Qt.green)
        if(self.coloring[5]==['Y']):
            painter.setBrush(Qt.yellow)
        if(self.coloring[5]==['B']):
            painter.setBrush(Qt.blue)
        if(self.coloring[5]==['C']):
            painter.setBrush(Qt.cyan)
        c6 = painter.drawEllipse(50,160,50,50)
        painter.drawText( 75,185,"n5")
        #painter.drawRect(50,160,50,50)
        

        if(self.coloring[6] == ['R']):
            painter.setBrush(Qt.red)
        if(self.coloring[6]==['G']):
            painter.setBrush(Qt.green)
        if(self.coloring[6]==['Y']):
            painter.setBrush(Qt.yellow)
        if(self.coloring[6]==['B']):
            painter.setBrush(Qt.blue)
        if(self.coloring[6]==['C']):
            painter.setBrush(Qt.cyan)
        c7 = painter.drawEllipse(190,160,50,50)
        painter.drawText( 215,185,"n6")
        #painter.drawRect(190,160,50,50)
        


        if(self.coloring[7] == ['R']):
            painter.setBrush(Qt.red)
        if(self.coloring[7]==['G']):
            painter.setBrush(Qt.green)
        if(self.coloring[7]==['Y']):
            painter.setBrush(Qt.yellow)
        if(self.coloring[7]==['B']):
            painter.setBrush(Qt.blue)
        if(self.coloring[7]==['C']):
            painter.setBrush(Qt.cyan)
        c8 = painter.drawEllipse(330,160,50,50)
        painter.drawText( 355,185,"n7")
        #painter.drawRect(330,160,50,50)
        


        if(self.coloring[8] == ['R']):
            painter.setBrush(Qt.red)
        if(self.coloring[8]==['G']):
            painter.setBrush(Qt.green)
        if(self.coloring[8]==['Y']):
            painter.setBrush(Qt.yellow)
        if(self.coloring[8]==['B']):
            painter.setBrush(Qt.blue)
        if(self.coloring[8]==['C']):
            painter.setBrush(Qt.cyan)
        c9 = painter.drawEllipse(120,230,50,50)
        painter.drawText( 145,255,"n8")
        #painter.drawRect(120,230,50,50)
        

        if(self.coloring[9] == ['R']):
            painter.setBrush(Qt.red)
        if(self.coloring[9]==['G']):
            painter.setBrush(Qt.green)
        if(self.coloring[9]==['Y']):
            painter.setBrush(Qt.yellow)
        if(self.coloring[9]==['B']):
            painter.setBrush(Qt.blue)
        if(self.coloring[9]==['C']):
            painter.setBrush(Qt.cyan)
        c10 = painter.drawEllipse(260,230,50,50)
        painter.drawText( 285,255,"n9")
        #painter.drawRect(260,230,50,50)
        
        

        painter.drawLine(93, 63, 127, 97)#c1&c3
        painter.drawLine(267, 63, 233, 97)#c2&c4
        painter.drawLine(303, 63, 337, 97)#c2&c5
        painter.drawLine(170, 115, 190, 115)#c3&c4
        painter.drawLine(127, 133, 93, 167)#c3&c6
        painter.drawLine(145, 140, 145, 230)#c3&c9
        painter.drawLine(163, 133, 197, 167)#c3&c7
        painter.drawLine(233, 133, 337, 167)#c4&c8
        painter.drawLine(215, 140, 215, 160)#c4&c7
        painter.drawLine(337, 133, 237, 168)#c5&c7
        painter.drawLine(355, 140, 355, 160)#c5&c8
        painter.drawLine(93, 203, 127, 237)#c6&c9
        painter.drawLine(100, 185, 190, 185)#c6&c7
        painter.drawLine(98, 175, 197, 133)#c6&c4
        painter.drawLine(197, 203, 163, 237)#c7&c9
        painter.drawLine(233, 203, 267, 237)#c7&c10
        painter.drawLine(240, 185, 330, 185)#c7&c8

        


        
app=QApplication(sys.argv)
widget = MainFrame()
widget.show()
sys.exit(app.exec_())