'''
User regular expressions 
to find out the occurances of the numbers
from the whatsapp messages
and compute the total expense

Reference to understand:
https://towardsdatascience.com/regular-expressions-in-python-a212b1c73d7f
'''

import re
import unittest

from cv2 import exp

def total_monthly_expense(whatsapp_msgs):
    """ 
    Return the total expenditure of the month from the whatsapp_msgs
    """
    total_expense = 0
    # Write your implementation here

    return total_expense

class Total_monthly_expense(unittest.TestCase):
    def test_month_01(self):
        whatsapp_msgs = "mess bill - 2000 hostel rent - 3000"
        total_expense = total_monthly_expense(whatsapp_msgs)
        self.assertEqual(total_expense, 5000)

    def test_month_02(self):
        whatsapp_msgs = """
student fee - 9000
200 for birthday
total 995 for vegitable today in the market
cost for the books was 2567 from the store
Spent 893 in swiggy this afternoon"""
        total_expense = total_monthly_expense(whatsapp_msgs)
        self.assertEqual(total_expense, 13655)

        whatsapp_msgs += " zommato - 200 and 399"
        total_expense = total_monthly_expense(whatsapp_msgs)
        self.assertEqual(total_expense, 14254)

    def test_month_03(self):
        whatsapp_msgs = """
today misc expences 599 + 845 + 325
yesterday it was in total 9000
I gave to watchman 2000 for gettting the items next day
cleared all EMIs for this month 239432
Paying EMIs is hard let's not take another loan in this life"""

        total_expense = total_monthly_expense(whatsapp_msgs)
        self.assertEqual(total_expense, 252201)

        whatsapp_msgs += " zommato - 200 and 399"
        total_expense = total_monthly_expense(whatsapp_msgs)
        self.assertEqual(total_expense, 252800)

    def test_month_04(self):
        whatsapp_msgs = """
just type the amounts for this month
no need of discription
894
123
86
900
300
325
955"""
        total_expense = total_monthly_expense(whatsapp_msgs)
        self.assertEqual(total_expense, 3583)

        whatsapp_msgs += " zommato - 200 and 399"
        total_expense = total_monthly_expense(whatsapp_msgs)
        self.assertEqual(total_expense, 4182)
    
    def test_month_05(self):
        whatsapp_msgs = """
this is simple one liner
345 923 52 12 34 59 29"""
        total_expense = total_monthly_expense(whatsapp_msgs)
        self.assertEqual(total_expense, 1454)

    def test_month_06(self):
        whatsapp_msgs = """
this is simple one liner
345 923 52 12 34 59 29"""
        total_expense = total_monthly_expense(whatsapp_msgs)
        self.assertEqual(total_expense, 1454)


if __name__ == '__main__':
  unittest.main(verbosity=2)
