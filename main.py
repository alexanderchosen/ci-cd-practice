import sqlite3

def collect_and_save_user():
    print("--- User Data Collection Form ---")

### 1. Collect inputs first

first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
gender = input("Enter Gender: ")
age_group = input("Enter Age Group (e.g., 18-25, 26-35): ")
country = input("Enter Country of Residence: ")
location = input("Enter Current Location (City/State): ")

### 2. Connect to the database file

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

### 3. CRUCIAL: Force create the table right before inserting data

cursor.execute("""
CREATE TABLE IF NOT EXISTS user_profiles (
id INTEGER PRIMARY KEY AUTOINCREMENT,
first_name TEXT,
last_name TEXT,
gender TEXT,
age_group TEXT,
country_of_residence TEXT,
current_location TEXT
)
""")

### 4. Insert the collected data safely

cursor.execute("""
INSERT INTO user_profiles (first_name, last_name, gender, age_group, country_of_residence, current_location)
VALUES (?, ?, ?, ?, ?, ?)
""", (first_name, last_name, gender, age_group, country, location))

# 5. Commit changes and close
conn.commit()
conn.close()

print("\n[Success] Data successfully saved to users.db!")

if "name" == "main":
    collect_and_save_user()