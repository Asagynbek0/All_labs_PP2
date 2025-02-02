def histogram(mylist):
    for i in mylist:
        print('*' * i)
    
mylist=list(map(int,input("Input nums = ").split()))

histogram(mylist)