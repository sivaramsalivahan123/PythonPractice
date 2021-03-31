def main():
    array=["siva","ram","sivaram"]
    for n in array:
        print(n)
    for i,n in enumerate(array):
        print(i, n)
    for i in range(1,11): # the ending value is exclusive not inclusive
        if i%2==0:
            print(i)
    # one line condition
    x =25
    y=35
    print("X is greater") if x>y else print("Y is greater")
    # while loop
    var = 0
    while(var<4):
        print(var)
        var = var+1
if __name__ == "__main__":
    main()