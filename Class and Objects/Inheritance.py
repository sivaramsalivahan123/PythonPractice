class A:
    name=None
    def greet(self):
        print("Hello, welcome to inheritance")
class B(A):
    def wish(self):
        print("Have nice day")
class C(B):
    pass
def main():
    a1=A()
    b1=B()
    a1.name="Mommy"
    b1.name="Son"
    print(a1.name)
    a1.greet()
    print(b1.name)
    b1.greet()
    b1.wish()
    c1=C()
    c1.name="grandson"
    print(c1.name)
    c1.greet()
    c1.wish()

if __name__=="__main__":
    main()
