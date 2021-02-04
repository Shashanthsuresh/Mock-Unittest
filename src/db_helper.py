
import mysql.connector

class DbHelper:
    def get_maximum_salary(self):
        '''
        Implement the logic to find and return maximum salary from employee table
        '''

        mydb = mysql.connector.connect(host="localhost",user="shashanth",password="password",database="employees")
    
        mycursor = mydb.cursor()
    
        mycursor.execute("select * from employee_details order by salary desc ")   #passing the query

        for row in mycursor.fetchone(): 
            return row
        

    def get_minimum_salary(self):
        '''
        Implement the logic to find and return minimum salary from employee table
        '''

        mydb = mysql.connector.connect(host="localhost",user="shashanth",password="password",database="employees")
    
        mycursor = mydb.cursor()
    
        mycursor.execute("select * from employee_details order by salary ")   #passing the query

        for row in mycursor.fetchone(): 
            return row


if __name__ == "__main__":
    db_helper = DbHelper()
    min_salary = db_helper.get_minimum_salary()
    max_salary = db_helper.get_maximum_salary()
    print(max_salary)
    print(min_salary)
