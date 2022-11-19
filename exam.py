class Star_Cinema:
    hall_list=[]
    def  entry_hall(self,perameter):
        self.hall_list.append(perameter)
        
class Hall(Star_Cinema):
    def __init__(self,row , col , hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__rows = row
        self.__cols= col
        self. __hall_no = hall_no
        self.entry_hall(self)
    
    def entry_show(self , movie_name ,id, time):
        self.__id = id
        tuple = ( movie_name ,id, time)
        self.__show_list.append(tuple)
        list_2d = []
        for i in range (self.__rows):
            l=[]
            for j in range(self.__cols):
                st=f'{chr(i+65)}{j}'
                l.append(st)
            list_2d.append(l)
        d={self.__id : list_2d}
        self.__seats.update(d)
    
    def for_successfull_ticket(self,list,k):
        print('\n')
        print('#####  Ticket Booked Successfully!!  #####\n')
        print('---------------------------------------------------')
        print(f'Name: {self.__name}')
        print(f'Phone Number: {self.__number}\n')
        for tupl in self.__show_list:
            if tupl[1]==k:
                print(f'Movie Name: {tupl[0]}         Movie Time: {tupl[2]}')
                str=''
                for i in list:
                    str+=i+'  '
                print(f'Ticket: {str}')
                print(f'HALL: {self.__hall_no}')
        print("-----------------------------------------------------")

    def  book_seats(self , name ,number, key , list_of_tuple):
        self.__name=name
        self.__number=number
        for k in self.__seats:
            if k == key:
                booked_list=[]
                for tuple in list_of_tuple:
                    i=tuple[0]
                    j=tuple[1]
                    s=self.__seats[key][i][j]
                    if(s=='X'):
                        i=i+65
                        j=j+48
                        st=chr(i)+chr(j)
                        print('\n')
                        print('--------------------------------------------')
                        print(f'{st} seat were booked...plz try again!')
                        print('---------------------------------------------')
                        return
                    else:
                        booked_list.append(self.__seats[key][i][j])
                self.for_successfull_ticket(booked_list,key)
                for tuple in list_of_tuple:
                    i=tuple[0]
                    j=tuple[1]
                    self.__seats[key][i][j]='X'
                          
    
    def view_show_list(self):
        print('\n')
        print("-----------------------------------------------------------------------------")
        for tuple in self.__show_list:
            print(f'MOVIE NAME: {tuple[0]}        SHOW ID: {tuple[1]}        TIME: {tuple[2]}')
        print("-----------------------------------------------------------------------------")
    
    def view_available_seats(self,show_id):
        flag = True
        for tuple in self.__show_list:
            if tuple[1]==show_id:
                flag=False
                print('\n')
                print(f'MOVIE NAME: {tuple[0]}            TIME: {tuple[2]}')
                print('X for already booked seats')
                break
        if (flag==True):
            print('\n')
            print('------------------------------')
            print("Sorry ! Invalid show id")
            print('------------------------------')
            return 
        print ('\n')
        print('--------------------------------------------------------------------')
        for i in self.__seats[show_id]:
            string =''
            for j in i:
                string+=j+'         '
            print(string)
        print('--------------------------------------------------------------------')
            

ro=5
co=7
star = Hall(ro,co,'H-99')
id1='roy123'
id2 = 'roy456'
star.entry_show('superman' ,id1,'nov 18 2022 10:00pm')
star.entry_show('Ironman', id2, 'nov 18 2022 12:00pm')
while True:
    print('\n')
    print('1. VIEW ALL SHOWS TODAY')
    print('2. VIEW ABAILABLE SEATS')
    print('3. BOOK TICKET')
    n = int(input('ENTER OPTION: '))
    if (n==1):
        star.view_show_list()

    elif(n==2):
        string = input('ENTER SHOW ID: ')
        star.view_available_seats(string)

    elif(n==3):
        list =[]
        c_name= input('ENTER CUSTOMER NAME: ')
        c_number=input('ENTER CUSTOMER NUMBER: ')
        s_id=input('ENTER SHOW ID: ')
        ticket= int(input('ENTER NUMBER OF TICKETS: '))
        count = 0
        for i in range(ticket):
            if (s_id!=id1) and (s_id!=id2):
                print('\n')
                print('--------------------------------------------')
                print('Show Id Is Invalid')
                print('------------------------------------')
                break
            set = input('ENTER SEAT NO: ')
            if(ord(set[0])-65 >=0 and ord(set[0])-65<ro) and (ord(set[1])-48 >=0 and ord(set[1])-48<co)and len(set)==2:
                r = ord(set[0])-65
                c= ord(set[1])-48
                tupl = (r,c)
                list.append(tupl)
                count+=1
            else :
                print('\n')
                print('-------------------------------------------')
                print (f'Invalid seat - {set} plz try again')
                print('-----------------------------------------')
                break
        if (count==ticket):
            star.book_seats(c_name,c_number,s_id,list)
    else:
        print('\n')
        print('--------------------------------------------------')
        print('you press an invalid option!')
        print('--------------------------------------------------')
