#Welcome to subway
print("Welcome to Subway!")
print("Baked fresh daily and available in 6-inch and Footlong sizes")

submenu = ["Ultimate Chicken", "Ultimate Meatball", "BLT", "Buffalo Chicken", "Chicken Bacon", "Chicken Classic", "Chicken Strips", "Chicken Teriyaki", "Chicken Schnitzel", "Leg Ham", "Meatball Melt", "Pizza Melt", "Roast Beef", "Falafel", "Steak Melt", "Tuna Mayo", "Turkey", "Veggie", "Veggie Patty"]
submenu_price = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

orderItems = []
orderTotal = []
counter = 0

sidemenu = ["HamCheeseTomato Jaffle", "Meatball Pot", "Chipotle", "Avocado Toastie", "CheesyGarlic Toastie", "GarlicHerb Toastie", "Ultimate Toastie", "Chocolate Cookie", "Rainbow Cookie", "DoubleChocolate Cookie", "Raspberry Cookie", "Macadamnia Cookie", "Coke", "Sprite", "Coke NoSugar", "IcedTea", "Water Bottled", "Water Sparkling"]
sidemenu_price = [5, 5, 5, 4, 4, 4, 4, 2, 2, 2, 2, 4, 4, 4, 4, 3, 3]

order = input("Are you looking to order? Y/N ")
if order == "N":
    exit()
else:
    print("Thank you for choosing Subway!")





menu = input("Are you looking to purchase a sandwich today or just side menu items? Please enter 'yes' for the Sub Menu or 'no' for the Side Menu:\n")
if menu == "yes":
    print(submenu)
    subOrder = input("What are you after? Select 1 (e.g Ultimate Chicken)\n")
    if subOrder == "Ultimate Chicken":
        orderItems.append(submenu[0])
        orderTotal.append(submenu_price[0])
        counter=counter+1
    
    elif subOrder == "Ultimate Meatball":
         orderItems.append(submenu[1])
         orderTotal.append(submenu_price[1])
         counter=counter+1
    
    elif subOrder == "BLT":
         orderItems.append(submenu[2])
         orderTotal.append(submenu_price[2])
         counter=counter+1
        
    elif subOrder == "Buffalo Chicken":
         orderItems.append(submenu[3])
         orderTotal.append(submenu_price[3])
         counter=counter+1
    
    elif subOrder == "Chicken Bacon":
         orderItems.append(submenu[4])
         orderTotal.append(submenu_price[4])
         counter=counter+1

    elif subOrder == "Chicken Classic":
         orderItems.append(submenu[5])
         orderTotal.append(submenu_price[5])
         counter=counter+1

    elif subOrder == "Chicken Strips":
         orderItems.append(submenu[6])
         orderTotal.append(submenu_price[6])
         counter=counter+1

    elif subOrder == "Chicken Teriyaki":
         orderItems.append(submenu[7])
         orderTotal.append(submenu_price[7])
         counter=counter+1

    elif subOrder == "Chicken Schnitzel":
         orderItems.append(submenu[8])
         orderTotal.append(submenu_price[8])
         counter=counter+1

    elif subOrder == "Leg Ham":
         orderItems.append(submenu[9])
         orderTotal.append(submenu_price[9])
         counter=counter+1

    elif subOrder == "Meatball Melt":
         orderItems.append(submenu[10])
         orderTotal.append(submenu_price[10])
         counter=counter+1

    elif subOrder == "Pizza Melt":
         orderItems.append(submenu[11])
         orderTotal.append(submenu_price[11])
         counter=counter+1

    elif subOrder == "Roast Beef":
         orderItems.append(submenu[12])
         counter=counter+1

    elif subOrder == "Falafel":
         orderItems.append(submenu[13])
         orderTotal.append(submenu_price[13])
         counter=counter+1

    elif subOrder == "Steak Melt":
         orderItems.append(submenu[14])
         orderTotal.append(submenu_price[14])
         counter=counter+1

    elif subOrder == "Tuna Mayo":
         orderItems.append(submenu[15])
         orderTotal.append(submenu_price[15])
         counter=counter+1

    elif subOrder == "Turkey":
         orderItems.append(submenu[16])
         orderTotal.append(submenu_price[16])
         counter=counter+1

    elif subOrder == "Veggie Only":
         orderItems.append(submenu[17])
         orderTotal.append(submenu_price[17])
         counter=counter+1
    
    elif subOrder == "Veggie Patty":
         orderItems.append(submenu[18])
         orderTotal.append(submenu_price[18])
         counter=counter+1
    else: 
        print("Not on menu!")
    

    finished = input("Have you finished ordering? Y/N: ")
    if finished =="N":
        nextOrder= True
        while nextOrder == True:
            print(sidemenu)
            sidemenuInput = input("What are you looking for in the side menu? (e.g Coke) ")
            if sidemenuInput == "HamCheeseTomato Jaffle":
                orderItems.append(sidemenu[0])
                orderTotal.append(sidemenu_price[0])
                counter=counter+1
                      
            
            elif sidemenuInput == "Meatball Pot":
                orderItems.append(sidemenu[1])
                orderTotal.append(sidemenu_price[1])
                counter=counter+1
                    

            elif sidemenuInput == "Chipotle":
                orderItems.append(sidemenu[2])
                orderTotal.append(sidemenu_price[2])
                counter=counter+1
                    

            elif sidemenuInput == "Avocado Toastie":
                orderItems.append(sidemenu[3])
                orderTotal.append(sidemenu_price[3])
                counter=counter+1
                    

            elif sidemenuInput == "CheesyGarlic Toastie":
                orderItems.append(sidemenu[4])
                orderTotal.append(sidemenu_price[4])
                counter=counter+1
                    

            elif sidemenuInput == "GarlicHerb Toastie":
                orderItems.append(sidemenu[5])
                orderTotal.append(sidemenu_price[5])
                counter=counter+1
                    

            elif sidemenuInput == "Ultimate Toastie":
                orderItems.append(sidemenu[6])
                orderTotal.append(sidemenu_price[6])
                counter=counter+1
                    

            elif sidemenuInput == "Chocolate Cookie":
                orderItems.append(sidemenu[7])
                orderTotal.append(sidemenu_price[7])
                counter=counter+1
                    

            elif sidemenuInput == "Rainbow Cookie":
                orderItems.append(sidemenu[8])
                orderTotal.append(sidemenu_price[8])
                counter=counter+1
                    

            elif sidemenuInput == "DoubleChocolate Cookie":
                orderItems.append(sidemenu[9])
                orderTotal.append(sidemenu_price[9])
                counter=counter+1
                    

            elif sidemenuInput == "Raspberry Cookie":
                orderItems.append(sidemenu[10])
                orderTotal.append(sidemenu_price[10])
                counter=counter+1
                    

            elif sidemenuInput == "Macadamia Cookie":
                orderItems.append(sidemenu[11])
                orderTotal.append(sidemenu_price[11])
                counter=counter+1
                    

            elif sidemenuInput == "Coke":
                orderItems.append(sidemenu[12])
                orderTotal.append(sidemenu_price[12])
                counter=counter+1
                    
                    
                     
            elif sidemenuInput == "Sprite":
                orderItems.append(sidemenu[13])
                orderTotal.append(sidemenu_price[13])
                counter=counter+1
                    

            elif sidemenuInput == "Coke NoSugar":
                orderItems.append(sidemenu[14])
                orderTotal.append(sidemenu_price[14])
                counter=counter+1
                    

            elif sidemenuInput == "Water Bottled":
                orderItems.append(sidemenu[15])
                orderTotal.append(sidemenu_price[15])
                counter=counter+1
                    

            elif sidemenuInput == "Water Sparkling":
                orderItems.append(sidemenu[16])
                orderTotal.append(sidemenu_price[16])
                counter=counter+1
            
            else:
                print("Not on menu!")
            finished2 = input("Have you finished ordering? Y/N: ")
            if finished2 == "N":
                nextOrder = True
            else:
                nextOrder = False
                    
        
        else:
            nextOrder = False
   

elif menu == "no":
    print(sidemenu)
    sidemenuOrder = input("What are you looking for in the side menu? (e.g CheesyGarlic Toastie)\n")
else:
    print("Invalid!")

y=0
print ("Here is your order:")
print ("     ")
print ("***********")
while y <counter:
   
    print ("Item: "+ (orderItems[y]))
    print ("Cost: $"+str(orderTotal[y]))
    y=y+1
print ("***********")
print ("     ")
#print(orderItems)
#print(orderTotal)
#print(counter)