class Employee():
	"""To show the employees' info."""

	def __init__(self, f_name, l_name, annual_salary=''):
		self.f_name = f_name
		self.l_name = l_name
		self.annual_salary = annual_salary

	def show_profile(self):
		full_profile = self.f_name + ' ' + self.l_name
		return full_profile.title()

	def give_raise(self):
		if self.annual_salary < 30000:
			raised_salary = self.annual_salary + 5000
		else:
			raised_salary = self.annual_salary + 3000
		return raised_salary


star_employee = Employee('younggi', 'seo', 28000)
senior_employee = Employee('Luke', 'Konrath', 5500)

print("- The evaluated employees list: \n 1. " + star_employee.show_profile() +
      "\n "
                                                                        "2. " +
      senior_employee.show_profile() +
      "\n\n- The improvement of the salary in 2019: \n 1. Rising Star Members "
      ": $" +
      str(star_employee.give_raise())
      + "\n 2. Current Star Members: $" + str(senior_employee.give_raise()))
