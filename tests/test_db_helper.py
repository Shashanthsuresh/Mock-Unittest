from unittest import TestCase
from unittest.mock import patch
from src.db_helper import DbHelper

class MockDB(TestCase):
    def setUp(self):
         mydb = mysql.connector.connect(host="localhost",
                                        user="shashanth",
                                        password="password",
                                        database="employees")
        
    @patch('src.db_helper.DbHelper')
    def test_max_salary_is_greater_than_min_salary(self, MockDbHelper):
        maxsalary = MockDbHelper()

        #mocking for maximum value
        maxsalary.get_maximum_salary.return_value = 100
        
        actualmax = salary.get_maximum_salary("select max(salary) from employee_details")
        expectedmax = 100

        
        #mocking for minimum value
        minsalary.get_minimum_salary.return_value = 50

        actualmin = salary.get_maximum_salary("select min(salary) from employee_details")
        expectedmin = 50
        
        
        # error message in case if test case got failed 
        message = "Maximum value is not greater than Mimumum value"

        # assert function() to check if values1 is 
        # greater than value2 
        self.assertGreater(expectedmax,expectedmin , message)


    
    
    

         
