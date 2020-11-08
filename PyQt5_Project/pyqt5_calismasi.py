#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 7 Nov 2020

@author: Feyzu
"""
#%% Boş Bir Pencere

import sys #sistemsel işler için gerekli
from PyQt5 import QtWidgets

app=QtWidgets.QApplication(sys.argv)

win=QtWidgets.QWidget()
win.setWindowTitle("Boş bir widget")
win.show()

sys.exit(app.exec_()) 
#oluşturulan pencerenin sürekli açık kalmasını sağlar

#%% Yazı & Resim Ekleme
import sys
from PyQt5 import QtWidgets,QtGui

app=QtWidgets.QApplication(sys.argv)

win=QtWidgets.QWidget()
win.setWindowTitle("Yazı ve Resim Ekleme")

font=QtGui.QFont("Monospace",12)
########################################## Yazı Resim ###

content1=QtWidgets.QLabel(win) 
#win penceresinin içine yazı ekle
content1.setText("Hoşgeldiniz!")
#eklencek yazı setText ile ayarlanır
content1.move(110,40)
#yazı sola ve yukarı tam bitişik olmasın
#x ekseninde 20,yde 40 pixel boşluktan sonra olsun
content1.setFont(font)

content2=QtWidgets.QLabel(win)
content2.setPixmap(QtGui.QPixmap("/home/ubuntu/.config/spyder-py3/Code/PyQt5_Project/pika2.png"))
#resmin path'ini verin.
#ya da aynı klasöre atıp tırnak içine direkadi.png yazin
content2.move(20,60)
########################################### Button ###

font_button=QtGui.QFont("TypeWriter",10)

button1=QtWidgets.QPushButton(win)
button1.setText("Giriş")
button1.move(40,350)
button1.setFont(font_button)

button2=QtWidgets.QPushButton(win)
button2.setText("Çıkış")
button2.move(200,350)
button2.setFont(font_button)
###################################################
win.setGeometry(200,100,700,500)
#200,100 de başlasın(x,y eksenleri)
# 700,500 de  genişlik ve yüksekliği
win.show()

sys.exit(app.exec_())


#%%  Horizontal


import sys 
from PyQt5 import QtWidgets,QtGui

app=QtWidgets.QApplication(sys.argv)

win=QtWidgets.QWidget()
win.setWindowTitle("Horizontal Box Layout")


horizontal=QtWidgets.QHBoxLayout()

button1=QtWidgets.QPushButton("Giriş")
button2=QtWidgets.QPushButton("Çıkış")

horizontal.addWidget(button1)
horizontal.addWidget(button2)
horizontal.addStretch()

win.setLayout(horizontal)


win.setGeometry(200,100,700,500)
win.show()

sys.exit(app.exec_()) 

#%% vertical Layout and stretch

import sys 
from PyQt5 import QtWidgets,QtGui

app=QtWidgets.QApplication(sys.argv)

win=QtWidgets.QWidget()
win.setWindowTitle("Vertical Box Layout")


ver=QtWidgets.QVBoxLayout()

button1=QtWidgets.QPushButton("Giriş")
button2=QtWidgets.QPushButton("Çıkış")

ver.addStretch()
ver.addWidget(button1)
ver.addWidget(button2)


win.setLayout(ver)


win.setGeometry(200,100,700,500)
win.show()

sys.exit(app.exec_()) 

#%% vertical Layout and sağ aşağı stretch

#vertical içine horizontal eklemek istiyorum.


import sys 
from PyQt5 import QtWidgets,QtGui

app=QtWidgets.QApplication(sys.argv)

win=QtWidgets.QWidget()
horizontal=QtWidgets.QHBoxLayout()

win.setWindowTitle("Horizontal and Vertical Box Layout")


ver=QtWidgets.QVBoxLayout()

button1=QtWidgets.QPushButton("Giriş")
button2=QtWidgets.QPushButton("Çıkış")

horizontal.addStretch()
horizontal.addWidget(button1)
horizontal.addWidget(button2)

ver.addStretch()
ver.addLayout(horizontal)


win.setLayout(ver)
win.setGeometry(200,100,700,500)
win.show()

sys.exit(app.exec_()) 

#%% Butonlara fonksiyon vermek


import sys 
from PyQt5 import QtWidgets,QtGui,QtTest

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__() #QWidget'in özelliklerini almak için
        
        self.txt=QtWidgets.QLabel("Welcome to Page!")
        self.button1=QtWidgets.QPushButton("Login")
        self.button2=QtWidgets.QPushButton("Exit")
        
        #butonlara fonk ekle
        self.button1.clicked.connect(self.login)
        self.button2.clicked.connect(self.ext)

        ver=QtWidgets.QVBoxLayout()
        hor=QtWidgets.QHBoxLayout()
        
        ver.addStretch()
        hor.addStretch()  
        ver.addWidget(self.txt)
        ver.addWidget(self.button1)
        ver.addWidget(self.button2)
        hor.addStretch()
        #ver.addStretch()#alttan üstten ortala
        


        hor.addLayout(ver)
        #yatayın içine dikey eklicem

        self.setLayout(hor)
        self.setGeometry(200,100,500,500)
        self.show()

    def login(self):
        self.txt.setText("The software is starting. Please wait..")
        QtTest.QTest.qWait(2000) #2 sn bekle
        self.txt.setText("Opened!!")
        
    def ext(self):
        self.txt.setText("Ending program. Please wait..")
        QtTest.QTest.qWait(1000) #2 sn bekle
        self.close() #pencereyi kapat


app=QtWidgets.QApplication(sys.argv)
window=Window()

sys.exit(app.exec_()) 

#%% Kullanıcıdan veri almak

import sys 
from PyQt5 import QtWidgets,QtGui,QtTest

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__() #QWidget'in özelliklerini almak için
        
        self.txt=QtWidgets.QLabel(" ×× PyQt5 Program ××")
        self.input=QtWidgets.QLineEdit() #kullanıcıdan veri alma
        self.input.setPlaceholderText("Enter your name")
        
        self.button1=QtWidgets.QPushButton("Login")
        self.button2=QtWidgets.QPushButton("Exit")
        
        #butonlara fonk ekle
        self.button1.clicked.connect(self.login)
        self.button2.clicked.connect(self.ext)

        ver=QtWidgets.QVBoxLayout()
        hor=QtWidgets.QHBoxLayout()
        
        ver.addStretch()
        hor.addStretch()  
        ver.addWidget(self.txt)
        ver.addWidget(self.input)
        ver.addWidget(self.button1)
        ver.addWidget(self.button2)
        hor.addStretch()
        #ver.addStretch()#alttan üstten ortala
        


        hor.addLayout(ver)
        #yatayın içine dikey eklicem

        self.setLayout(hor)
        self.setGeometry(200,100,500,500)
        self.show()

    def login(self):
        name=self.input.text()
        self.txt.setText("Welcome "+name)
        
        
    def ext(self):
        self.txt.setText("Ending program. Please wait..")
        QtTest.QTest.qWait(1000) #2 sn bekle
        self.close() #pencereyi kapat
   


app=QtWidgets.QApplication(sys.argv)
window=Window()

sys.exit(app.exec_()) 


#%%  Checkbox eklemek

import sys #sistemsel işler için gerekli
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        
        ver=QtWidgets.QVBoxLayout()
        self.txt=QtWidgets.QLabel("")
        self.input1=QtWidgets.QLineEdit()
        self.input1.setPlaceholderText("User Name")
        self.input2=QtWidgets.QLineEdit()
        self.input2.setPlaceholderText("Password")
        
        self.remem=QtWidgets.QCheckBox("Remember me")

        self.button1=QtWidgets.QPushButton("Log in")
        self.button1.clicked.connect(self.giris)
        
        ver.addWidget(self.txt)
        ver.addWidget(self.input1)
        ver.addWidget(self.input2)
        ver.addWidget(self.remem)
        ver.addWidget(self.button1)
        
        
        self.setLayout(ver)
        self.show()
        
    def giris(self):
        #print(self.hatirla.isChecked())
        if(self.remem.isChecked()):
            self.txt.setText("I will remember you <3")
        else:
            self.txt.setText("I will forget you")
app=QtWidgets.QApplication(sys.argv)
window=Window()
sys.exit(app.exec_()) 

#%% Resim Görüntüleyici


import sys 
from PyQt5 import QtWidgets,QtGui

class Window(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        
        ver=QtWidgets.QVBoxLayout()
        
        font1=QtGui.QFont("Century Gothic",16)
        
        
        self.txt=QtWidgets.QLabel("Image viewer") 
        self.txt.setFont(font1)
        self.browse= QtWidgets.QPushButton("Browse..")
        self.close_button= QtWidgets.QPushButton("Close")
        self.image=QtWidgets.QLabel()
        self.browse.clicked.connect(self.open_image)
        self.close_button.clicked.connect(self.close_image)
        
        ver.addWidget(self.txt)
        ver.addStretch()
        ver.addWidget(self.image)
        ver.addStretch()
        ver.addWidget(self.browse)
        ver.addWidget(self.close_button)
        
        self.setLayout(ver)
        self.setGeometry(200,100,500,500)
        self.setWindowTitle("Image Viewer")
        self.show()
        self.close_button.close() #close button'ı gösterme
        
        
    def open_image(self):
        image_url= QtWidgets.QFileDialog.getOpenFileName(self,"Pls pick an image")
        print(image_url[0])
        self.image.setPixmap(QtGui.QPixmap(image_url[0]))
        self.close_button.show() #kapatma tuşu gözüksün
        
    def close_image(self):
        self.image.setPixmap(QtGui.QPixmap(""))
        self.close_button.close()
            
app=QtWidgets.QApplication(sys.argv)
window=Window()
sys.exit(app.exec_()) 

#%%  Menü

from PyQt5.QtWidgets import *
import sys

class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        menubar=self.menuBar()
        dosya=menubar.addMenu("File")
        duzen=menubar.addMenu("Edit")
        ara=menubar.addMenu("Search")
        kaynak=menubar.addMenu("Source")
        view=menubar.addMenu("View")
        yardım=menubar.addMenu("Help")
        
        
        dosya_ac=QAction("Open",self)
        dosya_ac.setShortcut("Ctrl+O")
        yeni_dosya=QAction("New file",self)
        yeni_dosya.setShortcut("Ctrl+N")
        cikis=QAction("Quit",self)
        
        
        dosya.addAction(dosya_ac)
        dosya.addAction(yeni_dosya)
        dosya.addAction(cikis)
        
        panes=view.addMenu("Panes")
        pane1=QAction("Editor",self)
        pane2=QAction("IPython Console",self)
        
        panes.addAction(pane1)
        panes.addAction(pane2)
        
        self.setGeometry(200,100,500,500)
        self.show()
        
    
app=QApplication(sys.argv)
window=Window()
sys.exit(app.exec_()) 


