import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
	"""Tests for the class Employee."""

	def setUp(self):
		"""
		Create a improvement of salary and a raise of different amount for
		each salary methods.
		"""
		self.star_employee = Employee('younggi', 'seo', 2800)
		self.senior_employee = Employee('Luke', 'Konrath', 5500)
		self.raised_salary = [7800, 8500]

	def test_give_default_raise(self):
		"""Test that a default raise(5000) to star_employee is given
		properly."""
		self.assertEqual(self.raised_salary[0], self.star_employee.give_raise())

	def test_give_custom_raise(self):
		"""Test that a custom raise(3000) to senior_employee is given
		properly."""
		self.assertEqual(self.raised_salary[1],
		                 self.senior_employee.give_raise())


unittest.main()