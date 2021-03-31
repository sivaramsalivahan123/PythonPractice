class A:
    def greet(self):
        print("Inherited from A")
class B:
    def greet(self):
        print("Inherited from B")
class C(A,B):
    def greetC(self):
        self.greet()
        self.greet()
        print("I am from C")
def main():
    c1=C()
    c1.greetC()
if __name__== "__main__":
    main()