class Vector2D: 
    #Wektor jako para punktów
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    def x(): #współżędna x wektora
        return self.x2 - self.x1
    def y(): #współżędna y wektora
        return self.y2 - self.y1
    def setx(arg): #funkcje pozwalające ustawić współżedne wektora
        self.x2 = self.x1 + arg
    def sety(arg):
        self.y2 = self.y1 + arg
    def length(): #długość wektora
        return sqrt(sqr(self.x)+sqr(self.y))

def Vector0(): #funkcja zwracająca wektor zerowy
    vec1 = Vector2D()
    vec1.x1 = 0
    vec1.x2 = 0
    vec1.y1 = 0
    vec1.y2 = 0
    return vec1

def addVector(vec1,vec2): #sumowanie wektorów
    vecR = Vector0
    vecR.setx(vec1.x+vec2.x)
    vecR.sety(vec1.y+vec2.y)
    return vecR

def minusVector(vec1): #F-cja zwracająca wektor o przeciwnym zwrocie
    vecR = vec1
    vecR.setx(-vec1.x)
    vecR.sety(-vec1.y)
    return vecR