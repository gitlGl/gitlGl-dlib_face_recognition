from PyQt5.QtWidgets import  QDialog,QLabel
class Help(QDialog):
    def __init__(self,):
        super().__init__()
        self.help  = QDialog()
        self.qlabel = QLabel(self.help)