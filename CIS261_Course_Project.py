#Sebastian SantaCruz
#CIS261
#CIS261 Course Project

def get_date(): 
  from_date = input("From date (mm/dd/yyyy) : ")
  to_date = input("To date (mm/dd/yyyy) : ")
  return from_date, to_date
def get_employee_name():
    print()
    employee_name = input("Enter employee name or 'End' to terminate: ")
    return employee_name
def get_worked_hours():
    worked_hours = float(input("Enter hours worked : "))
    return worked_hours
def get_hourly_rate():
    hourly_rate = float(input("Enter hourly rate : "))
    return hourly_rate
def get_income_tax_rate():
    income_tax_rate = float(input("Enter income tax rate : "))
    return income_tax_rate
  
def calculate_payroll(worked_hours, hourly_rate, income_tax_rate):
  gross_pay = worked_hours * hourly_rate
  income_tax = gross_pay * (income_tax_rate / 100)
  net_pay = gross_pay - income_tax
  return net_pay, income_tax, gross_pay

def printInfo(emp_detail_list):
  total_employees = 0
  total_worked_hours = 0
  total_gross_pay = 0
  total_income_taxes = 0
  total_net_pay = 0
  
  for emp_list in emp_detail_list:
    from_date = emp_list[0]
    to_date = emp_list[1]
    employee_name = emp_list[2]
    worked_hours = emp_list [3]
    hourly_rate = emp_list[4]
    income_tax_rate = emp_list[5]

    net_pay, income_tax, gross_pay = calculate_payroll(worked_hours, hourly_rate, income_tax_rate)
    print (from_date, to_date, employee_name, f"{worked_hours:,.2f}", f"{hourly_rate:,.2f}", f"{gross_pay:,.2f}", f"{income_tax:,.2f}", f"{net_pay:,.2f}")
    total_employees += 1
    total_worked_hours += worked_hours
    total_gross_pay += gross_pay
    total_income_taxes += income_tax
    total_net_pay += net_pay

    emp_totals["tot_employees"] = total_employees
    emp_totals["tot_hours"] = total_worked_hours   
    emp_totals["tot_gross_pay"] = total_gross_pay
    emp_totals["tot_tax"] = total_income_taxes
    emp_totals["tot_net"] = total_net_pay

def print_totals(emp_totals):
  print(f"Total Number of Employees: {emp_totals['tot_employees']}")
  print(f"Total Hours Worked: {emp_totals['tot_hours']}")
  print(f"Total Gross Pay: {emp_totals['tot_gross_pay']}")
  print(f"Total Income Taxes: {emp_totals['tot_tax']}")
  print(f"Total Net Pay: {emp_totals['tot_net']}")


if __name__ == "__main__":
  emp_detail_list = []
  emp_totals = {}
  while True: 
    employee_name = get_employee_name()
    if (employee_name.lower()) == "end":
      break
      
    from_date, to_date = get_date()
    worked_hours = get_worked_hours()
    hourly_rate = get_hourly_rate()
    income_tax_rate = get_income_tax_rate()
   
    emp_detail = []
    emp_detail.insert(0, from_date)
    emp_detail.insert(1, to_date) 
    emp_detail.insert(2, employee_name)
    emp_detail.insert(3, worked_hours)
    emp_detail.insert(4, hourly_rate)
    emp_detail.insert(5, income_tax_rate)
    emp_detail_list.append(emp_detail)
    
printInfo(emp_detail_list)
print_totals(emp_totals)