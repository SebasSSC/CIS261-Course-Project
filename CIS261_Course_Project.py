#Sebastian SantaCruz
#CIS261
#CIS261 Course Project

def get_employee_name():
    print("-----------------------")
    employee_name = input("Enter employee name or 'End' to see summarize: ")
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
def display_employee_details(employee_name, worked_hours, hourly_rate, gross_pay, income_tax_rate, income_tax, net_pay):
    print("Employee Name:", employee_name)
    print("Total Hours Worked: %.2f" % worked_hours)
    print("Hourly Rate: %.2f" % hourly_rate)
    print("Gross Pay: %.2f" % gross_pay)
    print("Income Tax Rate: %.2f" % income_tax_rate, "%")
    print("Income Tax: %.2f" % income_tax)
    print("Net Pay: %.2f" % net_pay)
    print("-----------------------")
def display_total_summary(total_employees, total_worked_hours, total_gross_pay, total_income_taxes, total_net_pay):
    print("Total Summary:")
    print("-----------------------")
    print("Total Employees:", total_employees)
    print("Total Hours Worked: %.2f" % total_worked_hours)
    print("Total Gross Pay: %.2f" % total_gross_pay)
    print("Total Income Taxes: %.2f" % total_income_taxes)
    print("Total Net Pay: %.2f" % total_net_pay)
    print("-----------------------")
def main():
  total_employees = 0
  total_worked_hours = 0
  total_gross_pay = 0
  total_income_taxes = 0
  total_net_pay = 0
  
  while True:
  
        employee_name = get_employee_name()
        if employee_name == "End":
            break
          
        worked_hours = get_worked_hours()
        hourly_rate = get_hourly_rate()
        income_tax_rate = get_income_tax_rate()
        net_pay, income_tax, gross_pay = calculate_payroll(worked_hours, hourly_rate, income_tax_rate)


        total_employees += 1
        total_worked_hours += worked_hours
        total_gross_pay += gross_pay
        total_income_taxes += income_tax
        total_net_pay += net_pay  
        display_employee_details(employee_name, worked_hours, hourly_rate, gross_pay, income_tax_rate, income_tax, net_pay)

  display_total_summary(total_employees, total_worked_hours, total_gross_pay, total_income_taxes, total_net_pay)
main()