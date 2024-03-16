import csv

class PlaceOrd:
    def buy(self, id):
        while True:
            quan=input("Enter the Quantity of that Product:")
            Total=0
            with open("ProductData.csv", "r", newline="") as file:
                read = csv.DictReader(file)
                for row in read:
                    if row["pid"] == id:
                        Total=Total+float(row["price"])
            print("----------------------------------------------------------------------------------------------------------------------------------------")            
            Total=Total*float(quan)
            print("Total Price:",Total)
            c=input("Can Proceed To Pay:[if Yes y]:")    
            if c=="y":
                print("----------------------------------------------------------------------------------------------------------------------------------------")
                print("*****Order Successfully Placed!*****")
                break     
            else:
                print("----------------------------------------------------------------------------------------------------------------------------------------")
                print("Please Enter The Valid Command...")      
                    
            
        
    
    def addCart(self, id):
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        found = False 
        with open("ProductData.csv", "r", newline="") as file:
            read = csv.DictReader(file)
            Total=0
            for row in read:
                if row["pid"] == id:
                    print("Items Added:")
                    print("ID:",row["pid"],end="    ")
                    print("Name:",row["pname"],end="    ")
                    print("Price:",row["price"],end="    ")
                    print("Category:",row["category"],end="    ")
                    print()
                    found = True
                    break  
                Total=Total+float(row["price"])
            print("-------------------------------------------------------------------")
            print("Total Amount:",Total)
            print("----------------------------------------------------------------------------------------------------------------------------------------")
            while True:
                choice=input("Please Enter Command To Proceed To Buy:[if Yes press y,otherwise n]:")
                if choice=="y":
                    quan=input("Enter the Quantity of that Product:")
                    Total=Total*float(quan)
                    c=input("Can Proceed to Buy:[if yes press y ]:")
                    print("----------------------------------------------------------------------------------------------------------------------------------------")
                    if c=="y":
                        print("----------------------------------------------------------------------------------------------------------------------------------------")
                        print("****Order Successfully Placed!****") 
                        break   
                else:
                    print("----------------------------------------------------------------------------------------------------------------------------------------")
                    print("Please Enter Valid Command...")    
        if not found:
            print("Product Is Not Found.")
        print("----------------------------------------------------------------------------------------------------------------------------------------")    

