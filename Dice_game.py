import random 

#First this dice game gives our user a chance to roll the dice once /chnace to roll it Twice/or exit the game at all 
#if the user doesnt pick between 3 options they gey hit with a error message saying "Invalid option or choice"
#When the app runs it will randomly pick a number between 1-6 (You can set the numbers to whatever)
#Secondly, it will print whatever number you picked then it will ask you if you want to roll again or roll multiple dice
# i set a loop and spilt it into 2 options and a error messsage if you picked a different invalid choice

def roll_dice(Rolls):
    for i in range(0,Rolls):
        number = random.randint(1,6)
        print("-" +str(number) + "-")
       
def menu():
    print("1.Roll a Dice")
    print("2. Roll Multiple dice")  
    print("3. Close the Game")  
    
menu()
option = int(input("Enter your pick here:"))

while option != 3:
    if option == 1:
        roll_dice(1)

    elif option == 2:
        Rolls = int(input("How many rolls?"))
        roll_dice(Rolls)
    else: 
        print("Invalid choice")

    print()
    menu()
    option = int(input("Enter here:"))


print("Thanks for playing our dice game")

       