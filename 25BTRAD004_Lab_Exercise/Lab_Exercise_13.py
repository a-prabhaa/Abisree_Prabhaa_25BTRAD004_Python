import csv
# Creating a sample employee CSV file
with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["ID", "Name", "Basic Salary", "HRA", "DA", "Deduction"])

    writer.writerow([101, "Rahul", 30000, 5000, 3000, 2000])
    writer.writerow([102, "Priya", 40000, 6000, 4000, 3000])
    writer.writerow([103, "Anjali", 25000, 4000, 2000, 1000])

# Function to calculate payroll
def calculate_payroll():
   total_payroll = 0
    print("\n========== PAYROLL SUMMARY ==========")

   try:
        with open("employees.csv", "r") as file:

            reader = csv.DictReader(file)

            for employee in reader:

                emp_id = employee["ID"]
                name = employee["Name"]

                basic = float(employee["Basic Salary"])
                hra = float(employee["HRA"])
                da = float(employee["DA"])
                deduction = float(employee["Deduction"])

                # Calculate gross salary
                gross_salary = basic + hra + da

                # Calculate net salary
                net_salary = gross_salary - deduction

                # Display employee salary details
                print("\nEmployee ID:", emp_id)
                print("Employee Name:", name)
                print("Basic Salary:", basic)
                print("HRA:", hra)
                print("DA:", da)
                print("Gross Salary:", gross_salary)
                print("Deductions:", deduction)
                print("Net Salary:", net_salary)

                total_payroll += net_salary

        print("\n====================================")
        print("Total Organization Payroll:", total_payroll)

    except FileNotFoundError:
        print("Error: Employee CSV file not found!")

    except ValueError:
        print("Error: Invalid numerical data in CSV file!")


# Calling the function
calculate_payroll()



