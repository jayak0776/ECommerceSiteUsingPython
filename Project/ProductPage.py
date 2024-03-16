import csv
from PlaceOrder import PlaceOrd
class Products:
    def page(self):
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        print("******Products Page******")
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        with open("ProductData.csv", "r", newline="") as file:
            read = csv.DictReader(file)
            count=0
            print("**Mobile Page**")
            print("----------------------------------------------------------------------------------------------------------------------------------------")
            print("ID\t\t",end=" ")
            print("Product Name\t\t",end=" ")
            print("Price\t\t",end=" ")
            print("Category\t\t",end=" ")
            print("Stock\t\t",end=" ")
            print()
            for row in read:
                print(row["pid"],end="\t\t")
                print(row["pname"],end="\t\t")
                print(row["price"],end="\t\t")
                print(row["category"],end="\t\t")
                print(row["stock"],end="\t\t")
                print()
                count+=1
                if count==3:
                    break
            print("----------------------------------------------------------------------------------------------------------------------------------------")
            print("**Laptops Page**")
            print("----------------------------------------------------------------------------------------------------------------------------------------")
            print("ID\t\t",end=" ")
            print("Product Name\t\t",end=" ")
            print("Price\t\t",end=" ")
            print("Category\t",end=" ")
            print("Stock\t\t",end=" ")
            print()
            for row in read:
                count += 1
                if count >= 11:
                    print(row["pid"], end="\t\t")
                    print(row["pname"], end="\t\t")
                    print(row["price"], end="\t\t")
                    print(row["category"], end="\t\t")
                    print(row["stock"], end="\t\t")
                    print()
                if count == 13:  # Stop when reaching row 13
                    break
            print("----------------------------------------------------------------------------------------------------------------------------------------")
            print("**Smart TV's Page**")
            print("----------------------------------------------------------------------------------------------------------------------------------------")
            print("ID\t\t",end=" ")
            print("Product Name\t\t",end=" ")
            print("Price\t\t",end=" ")
            print("Category\t",end=" ")
            print("Stock\t\t",end=" ")
            print()
            for row in read:
                count += 1
                if count >= 16:
                    print(row["pid"], end="\t\t")
                    print(row["pname"], end="\t\t")
                    print(row["price"], end="\t\t")
                    print(row["category"], end="\t\t")
                    print(row["stock"], end="\t\t")
                    print()
                if count == 18:  # Stop when reaching row 13
                    break
            print("----------------------------------------------------------------------------------------------------------------------------------------")
            self.viewMore()
            
    def viewMore(self):
        with open("ProductData.csv", "r", newline="") as file:
            read = csv.DictReader(file)
            
        choi=input("Please Enter The Command View More[if Mobile press m and if Laptop l ,otherwise press t]:")
        if choi=="m":
                with open("ProductData.csv", "r", newline="") as file:
                    read = csv.DictReader(file)
                    c=0
                    print("----------------------------------------------------------------------------------------------------------------------------------------")
                    print("**Mobile Page**")
                    print("----------------------------------------------------------------------------------------------------------------------------------------")
                    print("ID\t\t",end=" ")
                    print("Product Name\t\t",end=" ")
                    print("Price\t\t",end=" ")
                    print("Category\t\t",end=" ")
                    print("Stock\t\t",end=" ")
                    print()
                    for row in read:
                        print(row["pid"],end="\t\t")
                        print(row["pname"],end="\t\t")
                        print(row["price"],end="\t\t")
                        print(row["category"],end="\t\t")
                        print(row["stock"],end="\t\t")
                        print()
                        c+=1
                        if c==10:
                            break
                    print("----------------------------------------------------------------------------------------------------------------------------------------")  
                    id=input("Enter the product id to buy:")
                    c=input("Enter Command To PlaceOrder Or Add To Cart[if Placeorder press p,otherwise press a]:")
                    if c=="a":
                        a=PlaceOrd()
                        a.addCart(id)
                    elif c=="p":
                        a=PlaceOrd()
                        a.buy(id) 
                    else:
                        print("Please Enter Valid Command...")  
                    print("----------------------------------------------------------------------------------------------------------------------------------------")   
        elif choi=="l":
                with open("ProductData.csv", "r", newline="") as file:
                    read = csv.DictReader(file)
                    print("----------------------------------------------------------------------------------------------------------------------------------------")
                    print("**Laptops Page**")
                    print("----------------------------------------------------------------------------------------------------------------------------------------")
                    print("ID\t\t",end=" ")
                    print("Product Name\t\t",end=" ")
                    print("Price\t\t",end=" ")
                    print("Category\t\t",end=" ")
                    print("Stock\t\t",end=" ")
                    print()
                    lap=0
                    for row in read:
                        lap=lap+1
                        if lap>=11:
                            print(row["pid"],end="\t\t")
                            print(row["pname"],end="\t\t")
                            print(row["price"],end="\t\t")
                            print(row["category"],end="\t\t")
                            print(row["stock"],end="\t\t")
                            print()
                        if lap==15:    
                            break    
                    print("----------------------------------------------------------------------------------------------------------------------------------------")  
                    id=input("Enter the product id to buy:")
                    c=input("Enter Command To PlaceOrder Or Add To Cart[if Placeorder press p,otherwise press a]:")
                    if c=="a":
                        a=PlaceOrd()
                        a.addCart(id)
                    elif c=="p":
                        a=PlaceOrd()
                        a.buy(id) 
                    else:
                        print("Please Enter Valid Command...")  
                    print("----------------------------------------------------------------------------------------------------------------------------------------") 
        elif choi=="t":
                with open("ProductData.csv", "r", newline="") as file:
                    read = csv.DictReader(file)
                    print("----------------------------------------------------------------------------------------------------------------------------------------")
                    print("**TV's Page**")
                    print("----------------------------------------------------------------------------------------------------------------------------------------")
                    print("ID\t\t",end=" ")
                    print("Product Name\t\t",end=" ")
                    print("Price\t\t",end=" ")
                    print("Category\t\t",end=" ")
                    print("Stock\t\t",end=" ")
                    print()
                    lap=0
                    for row in read:
                        lap=lap+1
                        if lap>=16:
                            print(row["pid"],end="\t\t")
                            print(row["pname"],end="\t\t")
                            print(row["price"],end="\t\t")
                            print(row["category"],end="\t\t")
                            print(row["stock"],end="\t\t")
                            print()
                        if lap==25:    
                            break       
                    print("----------------------------------------------------------------------------------------------------------------------------------------")  
                    id=input("Enter the product id to buy:")
                    c=input("Enter Command To PlaceOrder Or Add To Cart[if Placeorder press p,otherwise press a]:")
                    if c=="a":
                        a=PlaceOrd()
                        a.addCart(id)
                    elif c=="p":
                        a=PlaceOrd()
                        a.buy(id) 
                    else:
                        print("Please Enter Valid Command...")  
                    print("----------------------------------------------------------------------------------------------------------------------------------------")          
                                     
        else:    
            print("Please Enter Valid Command....") 
            self.viewMore()           
