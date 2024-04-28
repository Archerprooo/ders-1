from PyQt6.QtWidgets import *
import sys
class girişekranı(QMainWindow):
    def __init__(self,xx="Başlıksız"):
        Anauygulama = QApplication([])
        Anapencere = QWidget()
        Anaekran = QVBoxLayout()
        

        
        def login():
            Anapencere = özelleştir()
            özelleştir.show()
            
        self.anabuton1= QPushButton('Profil')
        self.anabuton1.setFixedWidth(100)
        Anaekran.addWidget(self.anabuton1)
        self.anabuton1.clicked.connect(login)
        Anapencere.setLayout(Anaekran)
        
        
        
        Anapencere.show()
        Anauygulama.exec()


class özelleştir(QMainWindow):
    
    def __init__(self,xx="Başlıksız"):
        
        def onayla(self):
            pencere.showFullScreen()
        def tam_ekran(self):
            pencere.showFullScreen()
        def kapat(self):
            pencere.close()

        uygulama = QApplication([])
        pencere =QWidget()
        


        kalıp = QVBoxLayout()
        pencere.setWindowTitle("Profil")

        kalıp.addWidget(QLabel('Kullanıcı Adınız?'))
        self.edit1=QLineEdit()
        self.edit1.setFixedWidth(100)
        kalıp.addWidget(self.edit1)

        kalıp.addWidget(QLabel('Şifreniz?'))
        self.edit2=QLineEdit()
        self.edit2.setFixedWidth(100)
        self.edit2.setEchoMode(QLineEdit.EchoMode.Password)
        kalıp.addWidget(self.edit2)

        kalıp.addWidget(QLabel('Mailiniz?'))
        self.edit3=QLineEdit()
        self.edit3.setFixedWidth(100)
        kalıp.addWidget(self.edit3)

        kalıp.addWidget(QLabel('Arka plan renginiz'))
        self.edit4=QColorDialog()
        kalıp.addWidget(self.edit4)
        
        self.buton1= QPushButton('Tamamla')
        self.buton1.setFixedWidth(100)
        kalıp.addWidget(self.buton1)
        self.buton1.clicked.connect(onayla)
        pencere.setLayout(kalıp)

        self.buton2= QPushButton('çıkış')
        self.buton2.setFixedWidth(100)
        kalıp.addWidget(self.buton2)
        self.buton2.clicked.connect(kapat)
        pencere.setLayout(kalıp)


        self.buton3= QPushButton('Tam ekran')
        self.buton3.setFixedWidth(100)
        kalıp.addWidget(self.buton3)
        self.buton3.clicked.connect(tam_ekran)
        pencere.setLayout(kalıp)
        
        pencere.show()
        uygulama.exec()


Anapencere = girişekranı()



