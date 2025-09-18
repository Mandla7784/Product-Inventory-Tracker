# 🧾 Python Inventory Management System

This is a simple **command-line inventory management system** built with Python. It allows users to:

- Add new products
- View available stock in a table format
- Search for a product by name
- Update stock levels
- Mark out-of-stock items
- Save the product list to a JSON file

> 🚧 This project is a work in progress and part of my internship learning journey at **Retail Store**.

---

## 🛠️ Features

- 📦 Add new products to the inventory
- 📋 Display all products in a formatted table
- 🔍 Search for a product by name
- 🧮 Update product stock quantity
- ❌ Automatically detect out-of-stock products
- 💾 Save inventory to `data.json`

---

## 📁 Project Structure

inventory-manager/
│
├── product.py # Product class definition
├── main.py # Main logic and user interaction
├── data.json # File to store saved product data (auto-generated)
├── README.md # You're here!

---

## 🧪 How to Run

1. **Clone the repo** or download the files:
   ```bash
   git clone https://github.com/your-username/inventory-manager.git
   cd inventory-manager
   ```

pip install prettytable

python --version 

python main.py  #use wich ever version you have for this 


+-------------+--------+----------+--------+--------------+
| ProductName | Price | Category | Stock | OutOfStock |
+-------------+--------+----------+--------+--------------+
| Laptop | 15000 | Tech | 5 | False |
| Apples | 30 | Grocery | 0 | True |
+-------------+--------+----------+--------+--------------+

📌 Todo (Future Improvements)
Add a menu-based UI for better CLI navigation

Load products from JSON on startup

Add data validation and error handling

Add product ID system for better tracking

👨‍💻 Author
Mandla Dyonase
Intern Python Developer
GitHub: Mandla7784

📜 License
This project is open-source and free to use for learning and development.

---

Let me know if you'd like the README to include screenshots, test instructions, or if you want me to help you build a menu system next. Keep going strong 💪.contact me : 0737871866
