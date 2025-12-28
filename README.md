# 🏦 ATM Management System (Python)

A **console-based ATM Management System** built using **Python**, designed to simulate real-world ATM operations such as user authentication, balance handling, and transaction history management using file storage.

This project is ideal for beginners who want to understand **file handling, functions, and basic banking logic** in Python.

---

## 📌 Features

- 🔐 User login using **username and password**
- 👥 Supports **multiple users**
- 💰 Savings account balance management
- ➕ Deposit and ➖ Withdrawal operations
- 🧾 Individual **transaction history for each user**
- 📅 Date-wise transaction recording
- 💾 Data stored using **CSV / text files** (no database required)

---

## 📁 Project Structure
ATM-Management-System/
│
├── atm.py # Main ATM program
├── username_password.csv # Stores user login credentials
├── savings.csv # Stores user balances
├── transactions/
│ ├── user1_history.csv # Transaction history of user1
│ ├── user2_history.csv # Transaction history of user2
│ └── ...
└── README.md
