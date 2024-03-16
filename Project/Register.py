import csv


class Register:
    
    def reg(self,u,p,e,m):
        with open("userData.csv","a",newline="")as file:
            w=csv.writer(file)
            w.writerow([u,p,e,m])
   
    def login(self, u, p):
        with open("userdata.csv", "r", newline="") as file:
            read = csv.DictReader(file)
            for row in read:
                if row["username"] == u and row["password"] == p:
                    return True
            return False
   
                           
                                                