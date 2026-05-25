def update_record(student_records, ID, record_title, data):
    """
    Updates a student's record based on the given ID and record title.

    Args:
        student_records (list): Sorted list of student records (tuples).
        ID (str): Student ID to update.
        record_title (str): The field to update ('ID', 'Email', 'Mid1', 'Mid2').
        data (str/int): New data to set for the specified field.

    Returns:
        str: Message indicating the result ('Record updated', 
             'ID cannot be updated', or 'Record not found').
    """

    # WRITE YOUR CODE HERE
    if record_title == "ID":
        return "ID cannot be updated"
    
    start = 0
    end = len(student_records) - 1
    found = -1
    while start <= end:
        mid = (start + end) // 2
        if student_records[mid][0] == ID:
            found = mid
            break  
        elif student_records[mid][0] < ID:
            start = mid + 1
        else:
            end = mid - 1
    if found == -1:
        return "Record not found"
    record = list(student_records[found])

    if record_title == "Email":
        record[1] = data
    elif record_title == "Mid1":
        record[2] = data
    elif record_title == "Mid2":
        record[3] = data
    student_records[found] = tuple(record)

    return "Record updated"
    


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

if __name__ == "__main__":

    student_records = [
        ('aa02822', 'ea02822', 80, 65), 
        ('ea02822', 'updated@gmail.com', 80, 65), 
        ('fa08877', 'fa08877@st.habib.edu.pk', 75, 67), 
        ('gh04588', 'gh04588@st.habib.edu.pk', 33, 50)
    ]
    print(update_record(student_records, 'randomID', 'Mid2', 50))
    # Should print: 'Record not found'
    print(student_records)
    ''' Should print: [
        ('aa02822', 'ea02822', 80, 65),
        ('ea02822', 'updated@gmail.com', 80, 65), 
        ('fa08877', 'fa08877@st.habib.edu.pk', 75, 67), 
        ('gh04588', 'gh04588@st.habib.edu.pk', 33, 50)
    ]'''

    print()

    student_records = [
        ('aa02822', 'ea02822', 80, 65), 
        ('ea02822', 'ea02822@st.habib.edu.pk', 80, 65), 
        ('fa08877', 'fa08877@st.habib.edu.pk', 66, 67), 
        ('gh04588', 'gh04588@st.habib.edu.pk', 33, 50)
    ]
    print(update_record(student_records, 'ea02822', 'Email', 'updated@gmail.com'))
    # Should print: 'Record updated'
    print(student_records)
    '''Should print: [
        ('aa02822', 'ea02822', 80, 65), 
        ('ea02822', 'updated@gmail.com', 80, 65), 
        ('fa08877', 'fa08877@st.habib.edu.pk', 66, 67), 
        ('gh04588', 'gh04588@st.habib.edu.pk', 33, 50)
    ]'''

    print()

    student_records = [
        ('aa02822', 'ea02822', 80, 65), 
        ('ea02822', 'updated@gmail.com', 80, 65), 
        ('fa08877', 'fa08877@st.habib.edu.pk', 75, 67), 
        ('gh04588', 'gh04588@st.habib.edu.pk', 33, 50)
    ]
    print(update_record(student_records, 'fa08877', 'ID', 'change01'))
    # Should print: 'ID cannot be updated'
    print(student_records)
    ''' Should print: [
        ('aa02822', 'ea02822', 80, 65), 
        ('ea02822', 'updated@gmail.com', 80, 65), 
        ('fa08877', 'fa08877@st.habib.edu.pk', 75, 67), 
        ('gh04588', 'gh04588@st.habib.edu.pk', 33, 50)
    ]'''

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q6.py