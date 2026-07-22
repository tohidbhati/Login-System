# 🔐 Python Login System

A modular **Python Login & Signup System** using **MySQL** as the backend database. The project demonstrates secure user authentication using **SHA-256 password hashing**, exception handling, modular programming, and MySQL connectivity.

---

# 📌 Features

- User Signup
- User Login
- Password Hashing (SHA-256)
- MySQL Database Integration
- Modular Code Structure
- Custom Exception Handling
- Duplicate Username Validation
- Input Validation
- Easy to Extend

---

# 📂 Project Structure

```text
Login_System/
│
├── Login_System.py          # Main Entry Point
├── database.py              # MySQL Connection
├── README.md
│
├── modules/
│   ├── __init__.py
│   ├── signup.py
│   ├── login.py
│   ├── exception_handling.py
│   └── ...
│
└── requirements.txt
```

---

# 🛠 Technologies Used

- Python 3.11+
- MySQL Server
- mysql-connector-python
- hashlib
- Modular Programming

---

# 📦 Installation

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/Login_System.git
```

```bash
cd Login_System
```

---

## 2. Create Virtual Environment (Recommended)

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install mysql-connector-python
```

---

# ⚙️ MySQL Setup

Create a database.

```sql
CREATE DATABASE login_system;
```

Select the database.

```sql
USE login_system;
```

Create the user table.

```sql
CREATE TABLE user_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fname VARCHAR(50) NOT NULL,
    lname VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    gender CHAR(1) NOT NULL,
    contact VARCHAR(15) NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    hashed VARCHAR(64) NOT NULL
);
```

---

# 🔧 Configure Database

Open **database.py**

```python
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="login_system"
)

cursor = connection.cursor()
```

Replace:

- YOUR_PASSWORD
- database name
- username (if different)

---

# ▶ Running the Project

```bash
python Login_System.py
```

---

# 📖 Signup Workflow

1. Enter First Name
2. Enter Last Name
3. Enter Age
4. Select Gender
5. Enter Contact Number
6. Enter Username
7. Enter Password
8. Confirm Password
9. Password is hashed using SHA-256
10. Data is stored inside MySQL

---

# 🔑 Login Workflow

1. Enter Username
2. Enter Password
3. Password is hashed
4. Hash is compared with database
5. Login Successful if hashes match

---

# 🔒 Password Security

Passwords are **never stored in plain text**.

Instead,

```
User Password
      │
      ▼
SHA-256 Hash
      │
      ▼
Stored in Database
```

Example

Password

```
Hello123
```

Stored

```
0d4d8d9f9bb4e...
```

---

# 📚 Modules

## Login_System.py

Main menu and application entry point.

---

## database.py

Responsible for

- Database connection
- Cursor creation
- Commit
- Rollback

---

## signup.py

Responsible for

- Collecting user information
- Validation
- Password hashing
- Database insertion

---

## login.py

Responsible for

- Username verification
- Password verification
- User authentication

---

## exception_handling.py

Contains custom exceptions.

Example

```python
class SignupError(Exception):
    pass
```

---

# 📜 Sample Output

```
--------- SIGN UP ---------

Enter First Name : John
Enter Last Name  : Doe
Enter Age        : 22
Gender           : M
Contact          : 9876543210
Username         : johndoe

Password         : ********
Confirm Password : ********

Signup Successful!
```

---

```
--------- LOGIN ---------

Username : johndoe
Password : ********

Login Successful!

Welcome John
```

---

# ❌ Common Errors

## ModuleNotFoundError

```
No module named database
```

Solution

- Verify project structure.
- Run the project from the root directory.
- Check import statements.

---

## Unknown column 'hashed'

Your database table does not contain a column named `hashed`.

Run

```sql
DESCRIBE user_data;
```

or create the column.

---

## Duplicate Username

If username already exists

```
Username already exists.
```

Choose another username.

---

## Password Mismatch

```
Passwords do not match.
```

Re-enter the password correctly.

---

# 🚀 Future Improvements

- Forgot Password
- Email Verification
- OTP Authentication
- bcrypt Password Hashing
- Argon2 Password Hashing
- Password Strength Checker
- Admin Dashboard
- User Dashboard
- Role-Based Authentication
- Logging
- Profile Editing
- Delete Account
- Change Password
- Session Management
- Remember Me
- GUI Version (Tkinter / PyQt)
- REST API using Flask/FastAPI
- JWT Authentication
- Docker Support

---

# 🧠 Learning Concepts Covered

- Python Functions
- Modular Programming
- Packages
- MySQL CRUD
- SQL Queries
- Password Hashing
- Exception Handling
- Input Validation
- Database Transactions
- Authentication
- Project Structure

---

# 📄 Requirements

```
Python >= 3.11
mysql-connector-python
MySQL Server
```

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Added feature"
```

4. Push

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Tohid Bhati**

Cybersecurity Enthusiast | Python Developer | Web Application Security Learner

- GitHub: https://github.com/yourusername
- LinkedIn: https://linkedin.com/in/yourusername

---

## ⭐ If you found this project useful, consider giving it a star on GitHub!
