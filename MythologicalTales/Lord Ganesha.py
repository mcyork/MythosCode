class Ganesha:
    def __init__(self):
        self.badhaonKoDurKartaHai = True
        self.gyan = True
        self.saubhagya = True

    def badhaonKoDurKare(self):
        print("गणेश बाधाओं को दूर करते हैं और नई शुरुआत में सौभाग्य लाते हैं।")
    
    def gyanPradanKare(self):
        print("गणेश ज्ञान और बुद्धि के देवता हैं।")

# गणेश उत्सव की शुरुआत
def utsavShuruKare():
    ganesh = Ganesha()
    ganesh.badhaonKoDurKare()
    ganesh.gyanPradanKare()

utsavShuruKare()
