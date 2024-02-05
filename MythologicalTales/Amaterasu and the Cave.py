class Amaterasu:
    def __init__(self):
        self.隠れる = True

    def 洞窟に隠れる(self):
        print("アマテラスが洞窟に隠れて、世界が暗くなった。")
    
    def 洞窟から出る(self):
        self.隠れる = False
        print("アマテラスが洞窟から出て、世界に光が戻った。")

class 神々:
    def __init__(self, name):
        self.name = name

    def 鏡を置く(self):
        print(f"{self.name}が鏡を洞窟の外に置いた。")

def 物語():
    amaterasu = Amaterasu()
    amaterasu.洞窟に隠れる()
    
    神 = 神々("天照")
    神.鏡を置く()
    
    amaterasu.洞窟から出る()

物語()
