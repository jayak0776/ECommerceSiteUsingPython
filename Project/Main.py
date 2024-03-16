from Register import Register
from ProductPage import Products
print("----------------------------------------------------------------------------------------------------------------------------------------")
print("****WELCOME TO SHOPPING SITE****")
while True:
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    choice=input("Please Login Or Register[if login press l ,otherwise press r]:")
    if choice=="r":
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        username=input("Please Enter the User Name:")
        password=input("Enter The Password:")
        email=input("Enter The Email:")
        mobileno=int(input("Enter The Mobile Number:"))
        r=Register()
        r.reg(username,password,email,mobileno)
        print("*****Registration Successful*****")
    elif choice=="l":
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        username=input("Please Enter the User Name:")
        password=input("Enter The Password:")
        l=Register()
        res=l.login(username,password) 
        if res:
            print("*****Login Successfull*****") 
            p=Products()
            p.page()
            break
        else:
            print("We Have No Account,Please Register Now....")
       
            
      