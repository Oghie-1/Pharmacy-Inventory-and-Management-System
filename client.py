

#Import all modules
import csv
from tempfile import NamedTemporaryFile
import shutil
import datetime
import pandas as pd

#____Intialiaze Current date______

d = datetime.datetime.now()
date = d.strftime("%d")
month=d.strftime("%m")
year= d.strftime("%Y")


##_------- Create Savings Function ___--------


def saving_info():
				print("\n******", d , "*****")
				print("_____----____-Saving", "____***")
				print("\n__Saved__")





def ticket_gen():
	print("=====||" , " -- Always Buy Aburo_Pharma -- ", "|| ====== ||\n")
	print("Date:", d.strftime("%x"))
	print("Time:", d.strftime("%X"))
	print("_____----____-Generating Reciept--__", "____***")
	print("\n__Thanks For Your Patronage__")


##_____------ CREATE ADMIN REGISTRAtion pprofile_______--------






##_____--------------- Login SYstem --------________



def admin_login_system_():
		print("=====||" , " -- Welcome to Aburo_Pharma -- ", "|| ====== ||\n")
		print("****///    ", "ADMIN", "    \\\****")
		print(" ")
		login_name= str(input("Username: "))
		login_psswrd = input("Passsword: ")
		con_login_psswrd = input("  Confirm Password: ")


		#passwrd error checker
		
		if login_psswrd == con_login_psswrd:
				timestamp = d
				print("---", "Loading", "---> \n")
				print("Wellcome", login_name, "*****", timestamp)
				system_init_()
		else:
				print("Invalid Password \n", "   Try Again!!")
				print("  ")
				return admin_login_system_()




###___------- Create supplier invoice  /  show invoice records /// Generate Customer -------- 

def system_init_():
	
    inp = input(" \n Enter 'Y'to create New Inventory || 'V' to view record | 'C' to generate Customer Invoice: \n")

		
    if inp == "Y":

        print("Generating Invoice Form \n" , "\nInput the required datafield below")
        supply_inventory()

				
    elif inp == "V":
        print("\n*******\n| Intializing Supply Record |****")
        rec_inp = input("\nInput 'CTR'for Customer Records, 'SUP' for Supplier's Record, 'EXT' to EXIT: ")


        if rec_inp == "CTR" :

            print("####---- Generating Customer  Records----###\n")
            customer_records()
            print("\n Press '1''to Return to Previous Menu | 3 to Logout")
            i = 1
            while i == 1:
                system_init_()
            if i == 3:
                admin_login_system()
                                        
        elif rec_inp == "SUP":
                                    
            print("####---- Generating SUPPLY  Records----###\n")
            supply_records()
            print("\n Press '1''to Return to Previous Menu | '2' to Cancel | 3 to Logout : ")



        elif rec_inp == "EXT":
            print("######____----Logging Out......")
            admin_login_system_()
				
					

    elif inp == "C":
        print("\n\n", "Intialize Customer Invoice", "-.--.---.---.")
        customer_invoice()





#--------- Input data for drugs supplied------


def supply_inventory():

		print ("  ")
		sup_name = input("Enter Suplier's Name: ")
		sup_id = input("Enter Supplier's ID: ")
		drug_name = input("Drug Name: ")
		drug_id = input("Drug ID: ")
		quantity = int(input("Enter quantity: "))
		unit_cost = int(input("Enter Per Unit Price: "))
		total_cost = quantity * unit_cost
		print(total_cost)



		columns = ['supplier_name', 'supplier_id', 'drug_name', 'quantity', 'unit_cost', 'total_cost',

						  'pur_date', 'pur_month', 'pur_year', ]
		
		row = {'supplier_name':sup_name, 'supplier_id':sup_id, 'drug_name': drug_name,'quantity':quantity, 'unit_cost':unit_cost,

			   'total_cost': total_cost, 'pur_date': date, 'pur_month':month, 'pur_year':year}

		for key, value in row.items():
				print(" ", " ")
				print(key, ":" , value,)    

				
		saving_info()
		system_init_()

	  


#---_________ Display Data


		

	   #with open('inventory.csv','w', newline='') as f:
		   #    writer = csv.DictWriter(f, fieldnames=columns, sep= ",")
			#   writer.writerow()
			   #writer.writerow(row)

			   #--------- Append data into a csv database------

			   #dt= pd.read_csv("inventory.csv")
			   #print(dt)
			   

def sales_records():
	dt = pd.read_csv("sales.csv")
    


def customer_invoice():

    i = 0
    medicine_name = []
    medicine_cost = []
    medicine_quantity = []

    while i != 1:
        
        customer_name = str(input("Ënter Customer Name: "))
        drug_name = input("Drug Name: ")
        quantity = int(input("Quantity: "))
        cost = int(input("Cost: "))
        total_cost = 0

        columns = ['customer_name', 'drug_name', 'quantity', 'cost', 'total_cost','pur_date', 'pur_month', 'pur_year', ]

        row = {'customer_name':customer_name, 'drug_name':drug_name,'quantity':quantity, 'cost':cost, 'total_cost': total_cost, 'pur_date': date, 'pur_month':month, 'pur_year':year}

        for value in row:
            medicine_name.append(drug_name)
            medicine_cost.append(cost)
            medicine_quantity.append(quantity)
        print(" ")
        i = int(input("Enter '0' to purchase another medcine | press 1 to print Bill: "))
    

    ticket_gen()
    
    print("\nCustomer:", customer_name)
    
    for x in range(len(medicine_name)):
        print("\n|",medicine_name[x],"|",medicine_quantity[x],"|",medicine_cost[x],"|", medicine_quantity[x] * medicine_cost[x])
        print("|==============================|")
        for x in range(len(medicine_name)):
            grandtotal += medicine_quantity[x] * medicine_cost[x]
            print(grandtotal)
	







admin_login_system_()





