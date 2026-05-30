import random
a=input("Enter your name:")
print('Welcome to my Game\n',a)


choice={ 1 :
         'Snake 🐍',
      2  :
          'Water 💧',
      3  :
          'Gun  🔫'
}

while True:
       

    user=int((input(f'Enter you choice {a}:\n {choice}:')))
    computer=random.randint(1,3)
    print(f'Computer choice is ==' ,choice[computer],'\n Your choice is == ',choice[user])


    def check(user,computer):
            if user==computer:
                print("Its Draw 👎 ")
            elif user==1 and computer==2:
                print("You Win 🏆")
           
            elif user==2 and computer==3:
                print("You Win 🏆")
              
            elif user==3 and computer==1:
                print("You Win 🏆")
              
            else:
                print("Computer Win 😆 ")
                
           

    check(user,computer)
    print("Game Over 🔚")
    print("〰〰〰〰〰〰〰 🅿 L 🅰 Y -- 🅰 G 🅰 ℹ N 〰〰〰〰〰〰〰")
    print('⏬')
    user_exit=(input("Press Enter to continue\n -----🅾 R----- \n type 'quit' to exit :"))
    if user_exit == 'quit':
        break
    else:
        continue
