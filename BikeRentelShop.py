class bikeshop:
    def __init__(self,stock):
        self.stock=stock
    def displaybike(self):
        print('total bikes',self.stock)
    def rentforbike(self,q):

        if q<=0:
            print('enter positive value or greater than zero')
        elif q>self.stock:
            print('enter the value less than stock')
        else:
            print('total prices',q*100)
            print('total bikes',self.stock-q)

while True:
    obj=bikeshop(100)
    usercall=int(input('''
1 display stocks
2 Rent a bike
3 Exit
    '''))

    if usercall==1:
        obj.displaybike()
    elif usercall==2:
        n=int(input('How much bikes do you want to rent : '))
        obj.rentforbike(n)
    else:
        break
