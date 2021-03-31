class Robot:
    __name=None
    __color=None
    __weight=None
    def __init__(self,name,color,weight):
        self.__name=name
        self.__color=color
        self.__weight=weight
    def introduce(self):
        print("Hello my Name is : "+self.__name)
class Owner:
    __name=None
    __personality=None
    __is_sitting=None
    robo=None
    def __init__(self,name,personality,is_sitting):
        self.__name=name
        self.__personality=personality
        self.__is_sitting=is_sitting
    def sit_down(self):
        self.__is_sitting=True
    def stand_up(self):
        self.__is_sitting=False
def main():
    r1=Robot("Tom","blue",25)
    r2=Robot("Jerry","orange",10)
    r1.introduce()
    r2.introduce()
    p1=Owner("Siva","Temper",False)
    p2=Owner("Ram","Cool",True)
    p1.robo=r1
    p2.robo=r2
    p1.robo.introduce()
if __name__ == "__main__":
    main()