from PyQt6.QtWidgets import *
import sys


class girisekrani(QMainWindow):
    def __init__(self):
        super().__init__()
        def login():
            print("tt")
            self.close
            pencereAna = özelleştir()
            pencereAna.show()
        girişpenceresi = QWidget()
        Anaekran = QVBoxLayout()
          
            
        self.anabuton1= QPushButton('Profil')
        self.anabuton1.setFixedWidth(100)
        Anaekran.addWidget(self.anabuton1)
        self.anabuton1.clicked.connect(login)
        girişpenceresi.setLayout(Anaekran)
        self.setCentralWidget(girişpenceresi)



class özelleştir(QMainWindow):
    def __init__(self,xx="Başlıksız"):
        super().__init__()

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
        
        def onayla(self):
            pencere.showFullScreen()
        def tam_ekran(self):
            pencere.showFullScreen()
        def kapat(self):
            
            pencere.close()
        self.buton1= QPushButton('Tamamla')
        self.buton1.setFixedWidth(100)
        kalıp.addWidget(self.buton1)
        self.buton1.clicked.connect(onayla)

        self.buton2= QPushButton('çıkış')
        self.buton2.setFixedWidth(100)
        kalıp.addWidget(self.buton2)
        self.buton2.clicked.connect(kapat)


        self.buton3= QPushButton('Tam ekran')
        self.buton3.setFixedWidth(100)
        kalıp.addWidget(self.buton3)
        self.buton3.clicked.connect(tam_ekran)
        pencere.setLayout(kalıp)
        self.setCentralWidget(pencere)        

uygulama = QApplication([])
Anapencere = girisekrani()
Anapencere.show()
uygulama.exec()



