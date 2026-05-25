def update_record(employee_records, ID, record_title, data):
    """
    Updates an employee record.

    Parameters:
    employee_records (list): List of tuples (ID, Position, Salary, Experience).
    ID (int): Employee ID.
    record_title (str): Field to update ("Position", "Salary", "Experience").
    data (str or int): New data.

    Returns:
    str: Message ("Record updated", "ID cannot be updated", "Record not found").
    """

    # WRITE YOUR CODE HERE
    if record_title=="ID":
        return 'ID cannot be updated'      
    for i in range(len(employee_records)):
        updatedRecord=list(employee_records[i])
        if updatedRecord[0]==ID:
            if "Position"==record_title:
                updatedRecord[1]=data
            elif "Salary"==record_title:
                updatedRecord[2]=data
            elif "Experience"==record_title:
                updatedRecord[3]=data
            employee_records[i]=tuple(updatedRecord)
            return 'Record updated'
    return 'Record not found'

#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    employee_records = [
        ('E001', 'Manager', 80000, 5), 
        ('E002', 'Developer', 60000, 2), 
        ('E003', 'Analyst', 50000, 1), 
        ('E004', 'Designer', 70000, 3)
        ]

    print(update_record(employee_records, 'E001', 'ID', 'E005'))
    # Should print: 'ID cannot be updated'
    print(employee_records)
    # Should print: [
    #   ('E001', 'Manager', 80000, 5), 
    #   ('E002', 'Developer', 60000, 2), 
    #   ('E003', 'Analyst', 50000, 1), 
    #   ('E004', 'Designer', 70000, 3)
    #   ]

    print(update_record(employee_records, 'E001', 'Position', 'Senior Manager'))
    # Should print: 'Record updated'
    print(employee_records)
    # Should print: [
    #   ('E001', 'Senior Manager', 80000, 5), 
    #   ('E002', 'Developer', 60000, 2), 
    #   ('E003', 'Analyst', 50000, 1), 
    #   ('E004', 'Designer', 70000, 3)
    #   ]

    employee_records = [
        ('E001', 'Manager', 80000, 5), 
        ('E002', 'Developer', 60000, 2), 
        ('E003', 'Analyst', 50000, 1), 
        ('E004', 'Designer', 70000, 3)
        ]
    print(update_record(employee_records, 'E005', 'Salary', 55000))
    # Should print: 'Record not found'
    print(employee_records)
    # Should print: [
    #   ('E001', 'Manager', 80000, 5), 
    #   ('E002', 'Developer', 60000, 2), 
    #   ('E003', 'Analyst', 50000, 1), 
    #   ('E004', 'Designer', 70000, 3)
    #   ]
    
    print(update_record(employee_records, 'E002', 'Position', 'Senior Developer'))
    # Should print: 'Record updated'
    print(employee_records)
    # Should print: [
    #   ('E001', 'Manager', 80000, 5), 
    #   ('E002', 'Senior Developer', 60000, 2), 
    #   ('E003', 'Analyst', 50000, 1), 
    #   ('E004', 'Designer', 70000, 3)
    #   ] 


    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################




# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q5.py