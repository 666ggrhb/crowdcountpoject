import mysql.connector    
# pip install eel
import eel
eel.init('interface')
@eel.expose
    
def accountexistfun1():
    try:
        conn= mysql.connector.connect(
                    host="rdsdata.cko9hcsgxavy.ap-south-1.rds.amazonaws.com",
                    user="admin",
                    passwd="password",
                    database="newcomp"
                    )
        x=int(input("\nuserno: "))
        y=input("\nname:  ")
        z=input("\ngender: ")
        q=input("\nreview about events: ")
        print('\n\n') 
        sql="INSERT INTO newcomps VALUES ({}, '{}', '{}','{}');".format(x,y,z,q)   
        cur=conn.cursor()
        cur.execute(sql)
        conn.commit()
    finally:
        signinmenuchoice()
        conn.close()
        return 0     
    
 


def signinmenuchoice():
    print('\n1.more review')
    print('\n2.see previous responses')
    print('\n3.exit')
    print('\n\n')
    choice = int(input('Enter your choice ...: '))            
    if choice ==1:
        accountexistfun3()
    if choice ==2:
        prevcomp()
    if choice == 3:
        exit
        
        
def accountexistfun3():
    try:
        conn= mysql.connector.connect(
                    host="rdsdata.cko9hcsgxavy.ap-south-1.rds.amazonaws.com",
                    user="admin",
                    passwd="password",
                    database="newcomp"
                    )
        x=int(input("\nuserno: "))
        y=input("\nname:  ")
        z=input("\ngender: ")
        q=input("\nreview about events: ")
        print('\n\n') 
        sql="INSERT INTO newcomps VALUES ({}, '{}', '{}', '{}');".format(x,y,z,q)   
        cur=conn.cursor()
        cur.execute(sql)
        conn.commit()
    finally:
        signinmenuchoice()
        conn.close()
        return 0      
    



def prevcomp():
    x=int(input("\nuserno: "))
    print('\n\n')  
    accountexistfun2(x) 
    
        
def accountexistfun2(x):
    try:
        conn= mysql.connector.connect(
                    host="rdsdata.cko9hcsgxavy.ap-south-1.rds.amazonaws.com",
                    user="admin",
                    passwd="password",
                    database="newcomp"
                    )
        cur=conn.cursor()
        query="select review from newcomps where userno={} ".format(x)
        cur.execute(query)
        data=cur.fetchall()
        print(data)  
    finally:
        signinmenuchoice()
        conn.close()
        return 0      
    


def adminloginmenu():
    x=int(input("\nloginid: "))
    y=input("\npassword:  ")
    print('\n\n')  
    adminmenu(x,y) 
    
def adminmenu(x,y):
    try:
        conn= mysql.connector.connect(
                    host="rdsdata.cko9hcsgxavy.ap-south-1.rds.amazonaws.com",
                    user="admin",
                    passwd="password",
                    database="admin"
            
                    )
        cur=conn.cursor()
        query="select *from adminids where loginid={} and password={}".format(x,y)
        cur.execute(query)
        data=cur.fetchall()
        if len(data)==0:
            print('account not exist')
        else:
            adminmenuchoice()
    finally:
        conn.close()
        return 0
    

def adminmenuchoice():
    print('\n1.new resposes')
    print('\n2.remove resposes')
    print('\n3.see total resposes')
    print('\n4.exit')
    print('\n\n')
    choice = int(input('Enter your choice ...: '))            
    if choice ==1:
        allnewcomp()
    if choice==2:
        delnewcom()
    if choice ==3:
        allprevcomp()
    if choice == 4:
        exit
        

        
def allnewcomp():
    try:
        conn= mysql.connector.connect(
                    host="rdsdata.cko9hcsgxavy.ap-south-1.rds.amazonaws.com",
                    user="admin",
                    passwd="password",
                    database="newcomp"
                    )
        cur=conn.cursor()
        query="select *from newcomps"
        cur.execute(query)
        data=cur.fetchall()
        print(data)     
    finally:   
        print("\n1. provide comments")
        print("\n2. exit")
        print('\n\n')
        choice=int(input())
        if choice==1:
            response()
        if choice==2:
            adminmenuchoice()   
        conn.close()
        return 0    
    
        
def response():
    try:
        conn= mysql.connector.connect(
                    
                    host="rdsdata.cko9hcsgxavy.ap-south-1.rds.amazonaws.com",
                    user="admin",
                    passwd="password",
                    database="newcomp"
                    )
        x=int(input("\nuserno: "))
        y=input("\nname:  ")
        z=input("\nregading response: ")
        q=input("\nenter response: ")
        print('\n\n') 
        sql="INSERT INTO newcomps VALUES ({}, '{}', '{}', '{}');".format(x,y,z,q)   
        cur=conn.cursor()
        cur.execute(sql)
        conn.commit()
    finally:
        adminmenuchoice()
        conn.close()
        return 0 
    

def delnewcom():
    x=int(input("\nuserno: "))
    print('\n\n')  
    delnewcomfun(x)   
    


def delnewcomfun(x):
    try:
        conn= mysql.connector.connect(
                    
                    host="rdsdata.cko9hcsgxavy.ap-south-1.rds.amazonaws.com",
                    user="admin",
                    passwd="password",
                    database="newcomp"
                    )
        cur=conn.cursor()
        query="delete from newcomps where userno={}".format(x)
        cur.execute(query)
        conn.commit()
        print("deleted successfully")
        print("\n")
    finally:
        adminmenuchoice()
        conn.close()
        return 0           
    


        
        
def allprevcomp():
    try:
        conn= mysql.connector.connect(
                    
                    host="rdsdata.cko9hcsgxavy.ap-south-1.rds.amazonaws.com",
                    user="admin",
                    passwd="password",
                    database="newcomp"
                    )

        cur=conn.cursor()
        query="SELECT COUNT(userno) as total_ids FROM newcomps;"
        cur.execute(query)
        data=cur.fetchall()
        print(data)  
    finally:
        adminmenuchoice()
        conn.close()
        return 0       
    import eel

eel.init('interface') # Specify the folder containing your frontend files
eel.start('index.html') # This will start the app on http://localhost:8080
eel.accountexistfun1()() # Call the exposed backend function
eel.close()

eel.init('interface') # Specify the folder containing your frontend files
eel.start('index.html') # This will start the app on http://localhost:8080
eel.signinmenuchoice()() # Call the exposed backend function
eel.close() # Close the eel app

eel.init('interface') # Specify the folder containing your frontend files
eel.start('index.html') # This will start the app on http://localhost:8080
eel.accountexistfun3()() # Call the exposed backend function
eel.close() # Close the eel app

eel.init('interface') # Specify the folder containing your frontend files
eel.start('index.html') # This will start the app on http://localhost:8080
eel.accountexistfun3()() # Call the exposed backend function
eel.close() # Close the eel app

eel.init('interface') # Specify the folder containing your frontend files
eel.start('index.html') # This will start the app on http://localhost:8080
eel.prevcomp()() # Call the exposed backend function
eel.close() # Close the eel app

eel.init('interface') # Specify the folder containing your frontend files
eel.start('index.html') # This will start the app on http://localhost:8080
eel.accountexistfun2()() # Call the exposed backend function
eel.close() # Close the eel app

eel.init('interface') # Specify the folder containing your frontend files
eel.start('index.html') # This will start the app on http://localhost:8080
eel.adminloginmenu()() # Call the exposed backend function
eel.close() # Close the eel app

eel.init('interface') # Specify the folder containing your frontend files
eel.start('index.html') # This will start the app on http://localhost:8080
eel.adminmenu()() # Call the exposed backend function
eel.close() # Close the eel app

eel.init('interface') # Specify the folder containing your frontend files
eel.start('index.html') # This will start the app on http://localhost:8080
eel.adminmenuchoice()() # Call the exposed backend function
eel.close() # Close the eel app

eel.init('interface') # Specify the folder containing your frontend files
eel.start('index.html') # This will start the app on http://localhost:8080
eel.allnewcomp()() # Call the exposed backend function
eel.close() # Close the eel app

eel.init('interface') # Specify the folder containing your frontend files
eel.start('index.html') # This will start the app on http://localhost:8080
eel.response()() # Call the exposed backend function
eel.close() # Close the eel app

eel.init('interface') # Specify the folder containing your frontend files
eel.start('index.html') # This will start the app on http://localhost:8080
eel.delnewcom()() # Call the exposed backend function
eel.close() # Close the eel app      

eel.init('interface') # Specify the folder containing your frontend files
eel.start('index.html') # This will start the app on http://localhost:8080
eel.delnewcomfun()() # Call the exposed backend function
eel.close() # Close the eel app

eel.init('interface') # Specify the folder containing your frontend files
eel.start('index.html') # This will start the app on http://localhost:8080
eel.allprevcom()() # Call the exposed backend function
eel.close() # Close the eel app    

def main_menu():
    while True:
        print(' Main Menu')
        print("\n1. user login")
        print('\n2. admin login')
        print('\n3.  quit')
        print('\n\n')
        choice = int(input('Enter your choice ...:'))
        if choice == 1:
            accountexistfun1()
        if choice == 2:
            adminloginmenu()
        if choice == 3:
            break

if __name__ == "__main__":
    main_menu()
    eel.init('interface') # Specify the folder containing your frontend files
eel.start('index.html') # This will start the app on http://localhost:8080
eel.sleep(10) # Optional: Add a delay for the eel app to load
eel.close() # Close the eel app

 