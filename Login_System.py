#This is a Signup/Login System but because there is no database i will use while loop to keep the code running
# and will make sure that data stores in dictionary temporarily...  [26/06/2026]

# Everything is working fine now it's time to add DB and i am going to use MySQL [22/07/2026]
# from modules.database import *
from modules.login_signup import login, signup
# from modules.database import *
# from modules.exception_handling import *
from database import cursor,connection,mysql
def mainmenu():
        while True:
                try:
                        message = """
                                Press 1 For Signup
                                Press 2 For Login
                                Press 3 For Exit"""
                        print(message)
                        choose = int(input("Choose Option: "))
                        # Functions for Signup and Login
                        if choose == 1:
                                signup()
                        elif choose == 2:
                                login()
                        elif choose == 3:
                                print("Thanks For Using Our Software")
                                exit()
                except ValueError:
                        print("...Please Enter Valid Value...")          

mainmenu()