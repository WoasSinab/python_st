karmand = []
dataFile = "perso_data.txt"

trash_file = "trash.txt"
trash = []

def load_data():
  
    f = open(dataFile, "r")
    
    for line in f:
      
        line = line.strip()
        if line == "":
            continue

        parts = line.split("|")
        
        emp = {
            "id": parts[0],
            "name": parts[1],
            "hours": parts[2],
            "mozd": parts[3]
        }
        
        karmand.append(emp)
        
    f.close()

def save_data():
  
    f = open(dataFile, "w")
    for i in karmand:
        line = i["id"] + "|" + i["name"]+ "|" + i["hours"] + "|" +i["mozd"] +"\n"
        f.write(line)
    f.close()

def add_karmand():
  
    # print("\n Add Employee")
    
    emp_id = input("karmand ID: ")
    name = input("Name: ")
    hours = input("Monthly Hours: ")
    mozd = input("Hourly mozd: ")

    karmand.append({"id": emp_id, "name": name, "hours": hours, "mozd": mozd})
    save_data()
    print("saved.")

def search():
  
    search_id = input("enter id to search: ")

    found = False

    for emp in karmand:
        if emp["id"] == search_id:
            print(emp["id"], emp["name"], emp["hours"], emp["mozd"])
            found = True
            continue


    if found == False:
        print("karmand not found.")


def edit():

    # sarch_idd = input("enter id to edit: ")
    
    # for emp in karmand:
    #   if emp["id"] == sarch_idd:
    #     emp["name"] == new_name
    #     ...
    
    
    row = int(input("row to edit: ")) - 1
    
    if row < 0 or row >= len(karmand):
      print("row does'nt exist!")
      return
    
    new_name = input("New name: ")
    if new_name == "":
        new_name = karmand[row]["name"]
    karmand[row]["name"] = new_name
      
    new_id = input("New id: ")
    if new_id == "":
        new_id = karmand[row]["id"]
    karmand[row]["id"] = new_id
    
    new_hours = input("New hours work: ")
    if new_hours == "":
        new_hours = karmand[row]["hours"]
    karmand[row]["hours"] = new_hours
    
    new_mozd = input("New mozd cash: ")
    if new_mozd == "":
        new_mozd = karmand[row]["mozd"]
    karmand[row]["mozd"] = new_mozd
    
    save_data()
    
    print("Updated.")

def delete():

    row = int(input("row to delete: ")) - 1
    
    if row < 0 or row >= len(karmand):
      print("row is not exists")
      return
    
    
    item = karmand.pop(row)
    trash.append(item)
    
    save_data()
    save_data_trash()
    
    
    
    print("deletedd ...")
    
    

def salary_man():

    # row = int(input("Row: ")) - 1
    
    # hour = karmand[row]["hour"]
    # mozd = karmand[row]["mozd"]
    # # edameh majara .....
    
    search_id = input("enter id to search: ")
    
    
    # if not search_id:
    #   print("nadidam")
    #   return False
    
    
    found = False

    for emp in karmand:
      
        if emp["id"] == search_id:
          
            total = float(emp["hours"]) * float(emp["mozd"])
            tax = total * 0.05
            total_net = total - tax
            print("total cash =", total_net)
            found = True
            break
          
    if found == False:
      print("gashtam nabood nagard nist")

def salary_total():
  
    total = 0

    for emp in karmand:
        total = float(emp["hours"]) * float(emp["mozd"])
        tax = total * 0.05
        total_net = total - tax
        total += total_net

    print("Total salary:", total , "total tax: " , tax)
    
def load_data_trash():
  
    f = open(trash_file, "r")
    
    for line in f:
      
        line = line.strip()
        if line == "":
            continue

        parts = line.split("|")
        
        emp = {
            "id": parts[0],
            "name": parts[1],
            "hours": parts[2],
            "mozd": parts[3]
        }
        
        trash.append(emp)
        
        # print(trash)
        
    f.close()
    

def save_data_trash():
  
    f = open(trash_file, "w")
    for emp in trash:
        line = emp["id"] + "|" + emp["name"]+ "|" + emp["hours"] + "|" +emp["mozd"] +"\n"
        f.write(line)
    f.close()
 
 
def restore():
  
    load_data_trash()
    # print(trash)
  
    # if len(trash) == 0:
    #   print("trash khaliye!")
    #   return
    
    # for i, emp in enumerate(trash, start=1):
    #     print(i, emp)

    row = int(input("enter radif to restore: ")) - 1

    if row < 0 or row >= len(trash):
        print("radif eshtebahe")
        return

    item = trash.pop(row)
    karmand.append(item)
    
    print("Restored.")
    
    save_data()
    save_data_trash()

def menu():
  
    load_data()

    while 1:
        print("""
           1 Add
           2 Search
           3 Edit
           4 Delete
           5 Salary One
           6 Salary Total
           7 Restore
           0 Exit
           """)

        c = input("enter entekhab ")

        if c == "1": add_karmand()
        elif c == "2": search()
        elif c == "3": edit()
        elif c == "4": delete()
        elif c == "5": salary_man()
        elif c == "6": salary_total()
        elif c == "7": restore()
        # elif c == "8": load_data_trash()
        elif c == "0":
          
            save_data()
            print("khodafez")
            break
        else:
            print("entekhab ghalat!")

menu()