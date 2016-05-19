# def display_movie(m):
#     print('original name:',m['org_name'])
#     print('trans name:',m['trans_name'])
#     print('year:',m['year'])
#     print()
# def create_movie(org_name,trans_name,year):
#     return {
#         'org_name':org_name,
#         'trans_name':trans_name,
#         'year':year
#     }
# movie0=create_movie('aa','bb',5)
# display_movie(movie0)
# def display_movies_list(m_list):
#     for x in range(len(m_list)):
#         print('movie#',str(x+1))
#         display_movie(m_list[x])
# movielist=[]
# movie1=create_movie('cc','dd',22)
# movielist.append(movie0)
# movielist.append(movie1)
# display_movies_list(movielist)
# def removemovies(m_list,movie):
#     m_list.remove(movie)
# def search(m_list,year):
#     litt=[]
#     for x in m_list:
#         if x['year']==year:
#             litt.append(x)
#     return litt
# a=search(movielist,22)
# display_movies_list(a)
# movie for movie in m_list if movie['year']==year
        #OOP
# class car:
#     manufacturer=''
#     year= -1
#     def print(self):
#         print('manufacturer:',str(self.manufacturer))
#         print('year:',str(self.year))
# c=car()
# c.manufacturer='toyo'
# c.year=2001
# c.print()
# class login:

# class signup:
#     userdict={
#         'user_name':'admin',
#         'password':'admin'
#     }
#     def add_user(self,userdict,user_name,password):
#         for x in
# class person:
#     def __init__(self,n,a,ad):                                                #constructor
#         self.name=n
#         self.age=a
#         self.address=ad
#         self.classes=[]
#     def sayhello(self):#methods
#         print('Hello, my name is',self.name)
#         print("i'm {0} year old".format(self.age))
#         print('my address is:',self.address)
# hoanh=person()
# hoanh.name='hoanh'
# hoanh.age=19
# hoanh.address='hanoi'
# hoanh.sayhello()
# me=person()
# me.name='raven'
# me.age=21
# me.address='tq'
# me.sayhello()
class math_student:
    def __init__(self,name,classes):
        self.name=name
        self.classes=classes
        self.x=-1
        self.y=-1
        oper=''
    def calculation(self):
        if self.oper=='+':
            return int(self.x)+int(self.y)
        elif self.oper=='-':
            return self.x-self.y
        elif self.oper == '*':
            return self.x*self.y
        elif self.oper == '/':
            return round(self.x/self.y,2)
        elif self.oper == '%':
            return self.x%self.y
        elif self.oper == '':
            return 'no operator'
        else:
            return 'error'

hoa=math_student('hoa','a3')
hoa.x=int(input('x?'))
hoa.y=int(input('y?'))
hoa.oper=input('operator?')
hoan=math_student('hoa','a3')
hoan.x=int(input('x?'))
hoan.y=int(input('y?'))
hoan.oper=input('operator?')
print(hoa.calculation())
print(hoan.calculation())