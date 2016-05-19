class vending:
    a={
        'name':['coke','energy','water'],
        'price':[7,10,5]
    }
    def cal(self,money,number):
        if self.a['price'][number-1]>money:
            return 'not enough money'
        elif number>3 or number<1:
            return 'error'
        else:
            return [self.a['name'][number-1],money-self.a['price'][number-1]]
a=vending()
print(a.cal(16,2))