class Employee:
    def _init_(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def _init_(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def search_by_age(self, age):
        result = []
        for emp in self.employees:
            if emp.age == age:
                result.append(emp)
        return result

    def search_by_name(self, name):
        result = []
        for emp in self.employees:
            if emp.name == name:
                result.append(emp)
        return result

    def search_by_salary(self, operator, salary):
        result = []
        for emp in self.employees:
            if operator == ">" and emp.salary > salary:
                result.append(emp)
            elif operator == "<" and emp.salary < salary:
                result.append(emp)
            elif operator == ">=" and emp.salary >= salary:
                result.append(emp)
            elif operator == "<=" and emp.salary <= salary:
                result.append(emp)
        return result

    def display_employees(self, employees):
        if not employees:
            print("No matching employees found.")
        else:
            print("Employee ID\tName\tAge\tSalary")
            for emp in employees:
                print(f"{emp.emp_id}\t\t{emp.name}\t{emp.age}\t{emp.salary}")

if _name_ == "_main_":
    # Create Employee objects and add them to the database
    emp_db = EmployeeDatabase()
    emp_db.add_employee(Employee("161E90", "Raman", 41, 56000))
    emp_db.add_employee(Employee("161F91", "Himadri", 38, 67500))
    emp_db.add_employee(Employee("161F99", "Jaya", 51, 82100))
    emp_db.add_employee(Employee("171E20", "Tejas", 30, 55000))
    emp_db.add_employee(Employee("171G30", "Ajay", 45, 44000))

    # User input for search parameters
    print("Choose a search parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary (>, <, <=, >=)")
    choice = input("Enter your choice: ")

    if choice == "1":
        age = int(input("Enter the age to search for: "))
        result = emp_db.search_by_age(age)
    elif choice == "2":
        name = input("Enter the name to search for: ")
        result = emp_db.search_by_name(name)
    elif choice == "3":
        operator = input("Enter the operator (> or < or <= or >=): ")
        salary = float(input("Enter the salary to search for: "))
        result = emp_db.search_by_salary(operator, salary)
    else:
        print("Invalid choice!")

    # Display the search results
    emp_db.display_employees(result)