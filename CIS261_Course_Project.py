#Sebastian SantaCruz
#CIS261
#CIS261 Course Project

def get_date(): 
  from_date = GetFromDate()
  to_date = GetToDate()
  return from_date, to_date
  
def GetFromDate():
  valid = False
  from_date = ""
  while not valid:
    from_date = input("Enter From Date (mm/dd/yyyy): ")
    if (len(from_date.split('/')) != 3 and from_date.upper() != 'ALL'):
      print("Invalid Date Format: ")
    else:
      valid = True
  return from_date

def GetToDate():
  valid = False
  to_date = ""
  while not valid:
    to_date = input("Enter To Date (mm/dd/yyyy): ")
    if (len(to_date.split('/')) != 3 and to_date.upper() != 'ALL'):
      print("Invalid Date Format: ")
    else:
      valid = True
  return to_date

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

def printInfo(emp_detail_list,):
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

def Write_Emp_Info(employee):
  file = open("employeeinfo.txt","a")
  file.write('{}|{}|{}|{}|{}|{}\n'.format(employee[0], employee[1], employee[2], employee[3], employee[4], employee[5]))

def ReadEmployeeInformation(from_date, emp_detail_list):
  file = open("employeeinfo.txt", "r")
  data = file.readlines()
  condition = True
  if from_date.upper() == 'ALL':
    condition = False
  for employee in data:
    employee = [x.strip() for x in employee.strip().split("|")]
    if not condition or from_date == employee[0]:
      emp_detail_list.append([employee[0], employee[1], employee[2], float(employee[3]), float(employee[4]), float(employee[5])])
  return emp_detail_list

if __name__ == "__main__":
  emp_detail_list = []
  emp_totals = {"tot_employees": 0, "tot_hours": 0, "tot_gross_pay": 0, "tot_tax": 0, "tot_net": 0}
    
  while True: 
    employee_name = get_employee_name()
    if employee_name.lower() == "end":
      break

    from_date, to_date = get_date()
    worked_hours = get_worked_hours()
    hourly_rate = get_hourly_rate()
    income_tax_rate = get_income_tax_rate()

    emp_detail = [from_date, to_date, employee_name, worked_hours, hourly_rate, income_tax_rate]
    Write_Emp_Info(emp_detail)
    emp_detail_list.append(emp_detail)
 
  printInfo(emp_detail_list)
  print_totals(emp_totals)