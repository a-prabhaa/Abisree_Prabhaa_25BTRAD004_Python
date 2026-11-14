//ATTENDANCE TRACKER
# Attendance Tracker using Lists and Dictionaries
# Dictionary to store student attendance
attendance = {}
# Function to add a student
def add_student(name):
    if name not in attendance:
        attendance[name] = []
        print(name, "added successfully.")
    else:
        print("Student already exists.")
# Function to mark attendance
def mark_attendance(name, status):
    if name in attendance:
        if status == "P" or status == "A":
            attendance[name].append(status)
            print("Attendance updated successfully.")
        else:
 print("Invalid status! Enter P or A.")
    else:
        print("Student not found.")
# Function to display attendance
def display_attendance():
    print("\n--- Attendance Records ---")
    for name, records in attendance.items():
        print(name, ":", records)
# Function to calculate attendance percentage
def calculate_percentage(name):
    if name in attendance:
        records = attendance[name]
        total = len(records)
        if total == 0:
            return 0
        present = records.count("P")
        percentage = (present / total) * 100
        return percentage
    return None
# Function to identify students below threshold
def check_shortage(threshold):
    print("\n--- Students Below Attendance Threshold ---")
    found = False
    for name in attendance:
percentage = calculate_percentage(name)
 if percentage < threshold:
            print(name, ":", round(percentage, 2), "%")
            found = True
    if not found:
        print("No students are below the threshold.")
# Adding students
add_student("Rahul")
add_student("Priya")
add_student("Anjali")
# Marking attendance
print("\n--- Marking Attendance ---")
mark_attendance("Rahul", "P")
mark_attendance("Rahul", "P")
mark_attendance("Rahul", "A")
mark_attendance("Priya", "P")
mark_attendance("Priya", "A")
mark_attendance("Priya", "A")
mark_attendance("Anjali", "P")
mark_attendance("Anjali", "P")
mark_attendance("Anjali", "P"
# Display records
display_attendance()
# Display attendance percentages
print("\n--- Attendance Percentage ---")
for name in attendance:
    percentage = calculate_percentage(name)
    print(name, ":", round(percentage, 2), "%")

# Check attendance shortage
check_shortage(75)

//SALES DATA ANALYZER

# Sales Data Analyzer using Lists and Dictionaries
# Dictionary to store product details
sales = {}
# Function to add a product
def add_product(name, quantity, price):
    if quantity < 0 or price < 0:
        print("Invalid quantity or price!")
    elif name not in sales:
        sales[name] = {
            "quantity": quantity,
            "price": price
        }
        print(name, "added successfully.")
    else:
        print("Product already exists. Use update_product().")
# Function to update product sales
def update_product(name, quantity):
    if name in sales:
        if quantity >= 0:
            sales[name]["quantity"] += quantity
            print("Sales updated successfully.")
        else:
            print("Invalid quantity!")
    else:
        print("Product not found.")
# Function to calculate product revenue
def product_revenue(name):
    if name in sales:
        return sales[name]["quantity"] * sales[name]["price"]
    return 0
# Function to display all product details
def display_sales():
    print("\n--- Product Sales Details ---")
    for name, details in sales.items():
        revenue = product_revenue(name)
        print("Product:", name)
        print("Quantity Sold:", details["quantity"])
        print("Price:", details["price"])
        print("Revenue:", revenue)
        print("--------------------")
# Function to calculate total sales
def total_sales():
    total = 0
    for name in sales:
        total += product_revenue(name)
    print("\nTotal Sales Revenue:", total)
# Function to find highest-selling product
def highest_selling_product():
    if not sales:
print("No sales records available.")
        return
    highest = max(sales, key=lambda x: sales[x]["quantity"])
    print("\nHighest Selling Product:", highest)
    print("Quantity Sold:", sales[highest]["quantity"])
# Function to compare product performance
def compare_sales():
    print("\n--- Product-wise Sales Performance ---")
    for name in sales:
        print(name, ":", product_revenue(name))
# Adding products
add_product("Laptop", 10, 50000)
add_product("Mobile", 20, 20000)
add_product("Headphones", 15, 2000)
# Updating sales
print("\n--- Updating Sales ---")
update_product("Laptop", 5)
update_product("Mobile", 10)
# Display sales details
display_sales()
# Calculate total revenue
total_sales()
# Find highest-selling product
highest_selling_product()
# Compare product performance
compare_sales()

