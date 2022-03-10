from pickle import NONE
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QLabel, QLineEdit, QPushButton, \
    QGridLayout, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtCore import pyqtSignal
from src.Database import Database
from src.MyMd5 import MyMd5
from src.OpenCapture import OpenCapture
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import pyqtSlot,QTimer,Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from multiprocessing import Process, Queue
from src.Process import process_admin_rg, process_student_rg
import multiprocessing  
import psutil

from .Face import AdminRgFace
import cv2
from .GlobalVariable import *
class FaceLoginPage(QWidget):
    emit_show_parent = pyqtSignal()
    def __init__(self) -> None:
        super().__init__()
        self.label = QLabel(self)
        self.label.resize(480,530)
        self.timer = QTimer()
        self.timer.timeout.connect(self.get_result)
        self.timer.start(500)
        self.open_capture = OpenCapture(None,None)
        self.timer.start(500)
        self.open_capture.emit_img.connect(self.set_normal_img)
        self.open_capture.start()
        self.setWindowModality( Qt.ApplicationModal )
        self.face_rg = AdminRgFace()
        self.show()
     
    def get_result(self):
        self.timer.stop()
        print("int")
        rgbImage = cv2.cvtColor(self.open_capture.frame, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(rgbImage, cv2.COLOR_RGB2GRAY)
        location_faces = models.detector(gray)
        if len(location_faces) == 1:
            raw_face = models.predictor(gray, location_faces[0])
            result = self.face_rg.rg_face(self.open_capture.frame, rgbImage, raw_face)
            if result:       
                self.emit_show_parent.emit()
                self.open_capture.close()
        #psutil.Process(self.p.pid).kill()
        print("kill")


        self.timer.start(500)
    def closeEvent(self, event):
      
        if self.timer.isActive():
            print("tingzhi")   
            self.timer.stop()   
        self.open_capture.close()
  



    @pyqtSlot(QImage)
    def set_normal_img(self, image):
        self.label.setPixmap(QPixmap.fromImage(image))
        self.label.setScaledContents(True) 
    




# class FaceLoginPage(QWidget):
#     emit_show_parent = pyqtSignal()
#     def __init__(self) -> None:
#         super().__init__()
#         self.label = QLabel(self)
#         self.label.resize(480,530)
#         self.timer = QTimer()
#         self.timer.timeout.connect(self.get_result)
     
#         self.Q1 = Queue()  # open_capture
#         self.Q2 = Queue()
#         self.share = multiprocessing.Value("b",False)
#         self.open_capture = OpenCapture(self.Q1, self.Q2)
#         self.p = Process(target=process_admin_rg, args=(self.Q1,self.share))
#         self.p.daemon = True
#         self.p.start()
       
#         self.open_capture.emit_img.connect(self.set_normal_img)
#         self.open_capture.start()
#         self.open_capture.timer3.start(1000)
#         self.timer.start(500)
#         self.setWindowModality( Qt.ApplicationModal )
#         self.show()
     
#     def get_result(self):
#         self.timer.stop()
#         print("int")
#         if self.share.value == True:
#             self.emit_show_parent.emit()
#             self.open_capture.close()
#             psutil.Process(self.p.pid).kill()
#             print("kill")


#         self.timer.start(500)
#     def closeEvent(self, event):
#         if self.open_capture.timer3.isActive():
#             self.open_capture.timer3.stop()
#         if self.timer.isActive():
#             print("tingzhi")   
#             self.timer.stop()   
#         self.open_capture.close()
#         psutil.Process(self.p.pid).kill()



#     @pyqtSlot(QImage)
#     def set_normal_img(self, image):
#         self.label.setPixmap(QPixmap.fromImage(image))
#         self.label.setScaledContents(True) 
    
