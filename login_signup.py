# Importing modules to connect all files together...
import hashlib
# from ..Login_System import *
# from database import cursor,connection,mysql
from modules.exception_handling import SignupError
from database import *

def signup():
    try:
        print("----SIGN UP ----")
        print("Please Provide the following information for\ncompletion of signup.")
        fname = input("Enter Your First Name: ").strip()
        lname = input("Enter Your Last Name: ").strip()
        age = int(input("Enter Age: "))
        gender = input("Male/Female/Other [Please Select M/F/O]: ").upper()
        if gender not in ["M","F","O"]:
            raise SignupError("Invalid Gender")
            return
        contact = input("Enter Contact no. (+91): ").strip()
        username = input("Please Enter Username: ")
        cursor.execute("SELECT username FROM user_data WHERE username =%s",(username,))
        if cursor.fetchone():
            print("Username Already Exists")
            return
        print("For Security Concern Enter New Password, so that you can login")
        password = input("New Password: ")
        hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
        confirm_password = input("Confirm Password Again: ")
        cnf_hashed = hashlib.sha256(confirm_password.encode('utf-8')).hexdigest()
        if hashed == cnf_hashed:
            password_hash = hashed
            query = """
                INSERT INTO user_data
                (fname,lname,age,gender,contact,username,password_hash) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
            values = (fname,lname,age,gender,contact,username,password_hash)
            cursor.execute(query,values)
            # if cursor.fetchone():
            #     print("Username Already Exists.")
            #     return
            connection.commit()
            print("Signup Successful !!")
        elif hashed != cnf_hashed:
            print("Password Did Not Match Retry")
            return
    except mysql.connector.Error as err:
        connection.rollback()
        print(err)
    except ValueError:
        print("Invalid Value Please Check Again...")
    except SignupError:
        print("Error...")

def login():
    try:
        print("-----LOGIN-----")
        username = input("Enter Username: ").strip()
        password = input("Enter Password: ").strip()

        hashed  = hashlib.sha256(password.encode()).hexdigest()

        query = """
        SELECT * FROM user_data WHERE username=%s AND password_hash = %s"""
        cursor.execute(query,(username,hashed))
        user = cursor.fetchone()

        if user:
            print("Login Successfull !!")
            print(f"Welcome {user[1]}")
        else:
            print("Invalid Username or Password")
    except mysql.connector.Error as err:
        print(err)