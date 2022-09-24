import mysql.connector
import random
import bill.invoice
mycon=mysql.connector.connect(host="localhost",user='root',passwd="shubh",database="zomato")
if mycon.is_connected():
    print('SUCCESS')
cursor = mycon.cursor()

j=1
n=input("Kindly enter your name: ")
#HERE WE ASK USER HIS/HER NAME
pn=int(input("Kindly enter your Phone no: "))
#USER_PHONE_NUMBER
c=input('KINDLY CHOOSE CUSINE FROM INDIAN/ITALIAN/CONTINENTAL(IN CAPS):  ')
#Preffered cuisine out of three options
x = int(input("enter 0 for booking and 1 for delivery :"))
#choice of delivery or booking
if x ==0:
    i=1
    #IF BOOKING IS CHOSEN
    print("you have opted for booking","the",c,"restaurants are: ")
    k= "select RID,RNAME,RRATING from restaurants where RCUISINE=%s"
    g=(c,)
    cursor.execute(k,g)
    data=cursor.fetchall()
    for row in data:
        print(row)
    r = input("enter Restaurant's unique ID: ")
    m= input('DO YOU WANT TO SEE THE MENU? (Y/N): ')
    if m == "Y":
        if c== "INDIAN" :
            file = open(r'C:\Users\user\Desktop\INDIAN.txt',"r",encoding="UTF-8")
            ind= file.read()
            print(ind)
            file.close()
        elif c== "ITALIAN" :
            file = open(r'C:\Users\user\Desktop\ITALIAN.txt',"r",encoding="UTF-8")
            ita= file.read()
            print(ita)
            file.close()
        else:
            file = open(r'C:\Users\user\Desktop\CONTINENTAL.txt','r',encoding="UTF-8")
            con= file.read()
            print(con)
            file.close()
    #r = input("enter Restaurant's unique ID: ")
    t = int(input("enter time of booking: "))
    s = int(input("enter No of seats required: "))
    b= "B"+str(random.randint(100,999))
    st = "INSERT INTO booking(BID,RID,SEATS_REQD,NAME,PH_NO,TIME) VALUES ('{}','{}',{},'{}',{},{})".format(b,r,s,n,pn,t)
    cursor.execute(st)
    bill.invoice.invoice(str(n),str(pn),str(b),str(r),str(s),str(t))
    mycon.commit()
     

   

if x==1:
    add = input("Kindly enter your residential address : ")
    ar=input("Kindly enter the name of your area: ")
    g=(ar,c)
    print('YOU HAVE OPTED FOR DELIVERY',"THE",c,"RESTAURANTS IN",ar, "ARE: ")
    s="select RID,RNAME,RRATING from restaurants where RAREA=%s and RCUISINE=%s "
    cursor.execute(s,g)
    data1=cursor.fetchall()
    for row in data1:
        print(row)
    r1=input("select RID for reqd area: ")
    if ar not in ["HADAPSAR","KHARADI","KALYANI NAGAR"]:
        print ("Sorry we don't deliver there")
        ar=input("Kindly enter the name of your area (in caps) (HADAPSAR/KALYANI NAGAR/KHARADI):  ")
    m= input('DO YOU WANT TO SEE THE MENU? (Y/N): ')
    if m == "Y":
        if c== "INDIAN" :
            file = open(r'C:\Users\user\Desktop\INDIAN.txt',"r",encoding="UTF-8")
            ind= file.read()
            print(ind)
            file.close()
        elif c== "ITALIAN" :
            file = open(r'C:\Users\user\Desktop\ITALIAN.txt',"r",encoding="UTF-8")
            ita= file.read()
            print(ita)
            file.close()
        elif c== "CONTINENTAL" :
            file = open(r'C:\Users\user\Desktop\CONTINENTAL.txt','r',encoding="UTF-8")
            con= file.read()
            print(con)
            file.close()
           
    h=(r1,)
    y="select RDELIVERY from restaurants where RID=%s"
    cursor.execute(y,h)
    d=cursor.fetchall()
    if d[0]==('NO',):
        print("THIS RESTAURANT DOESN'T DELIVER FOOD PLS SELECT ANOTHER RESTAURANT")
        r1=input("select RID from the above list: ")
        h=(r1,)
        y="select RDELIVERY from restaurants where RID=%s"
        cursor.execute(y,h)
        d=cursor.fetchall()
    j= "D"+str(random.randint(100,999))
    T = "INSERT INTO delivery(DID,RID,CNAME,D_ADDRESS,NUMBER,AREA) VALUES ('{}','{}','{}','{}',{},'{}')".format(j,r1,n,add,pn,ar)
    cursor.execute(T)
    bill.invoice.dinvoice(str(n),str(pn),str(j),str(r1),str(ar))
    mycon.commit()
print('ORDER PLACED,THANK YOU')  