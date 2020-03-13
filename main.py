import pymysql.cursors
conn=pymysql.connect(host="localhost",
                     user="root",
                     password="",
                     db="expense_manager",
                     charset="utf8mb4",
                     cursorclass=pymysql.cursors.DictCursor)
with conn.cursor() as cursor:
    a=print("WELCOME TO EXPENSE MANAGER")
    b=print("***************************")
    while True:
        c=print("ENTER A TO ADD EXPENSE: \nENTER V TO VIEW EXPENSE: \nENTER E TO EXIT")
        d=input("ENTER YOUR CHOICE :")
        if d=="a"or d=="A":
            a = input("enter the name of the expense: ")
            b = input("enter the amount of the expense: ")
            c = input("enter the reason : ")
            d = a, b, c
            sql = "INSERT INTO `expense`(`Name_of_expense`, `Amount`, `Reason`) VALUES ('{}',{},'{}')".format(a, b, c)
       # print(sql)
            cursor.execute(sql)
            print("DATA SAVED SUCCESFULLY")
            conn.commit()
        elif d=="v" or d=="V":
            sql="SELECT * FROM `expense`"
            result = cursor.execute(sql)
            data = cursor.fetchall()
            print(data)
        else:
            print("thank you")
            break
