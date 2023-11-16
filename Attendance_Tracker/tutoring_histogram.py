

student_names = {'be621': ['Brown', 'Ella'],
                 'ff100': ['Fitzroy', 'Farrah'],
                 'gm318': ['Graham', 'Moses'],
                 'ik992': ['Ingalls', 'Kelsey'],
                 'tc51': ['Taylor', 'Cora'],
                 'sj281': ['Smith', 'James'],
                 'sj152': ['Smith', 'Joe'],
                 'rh150': ['Ricks', 'Hunter'],
                 'wm97': ['Wong', 'Ming'],
                 'jd437': ['Jones', 'Devante'],
                 'kc870': ['Kumar', 'Chahna'],
                 'mp411': ['Malley', 'Patrick'],
                 'na559': ['Ng', 'Amy'],
                 'mx672': ['Morales', 'Xavier']}

# How many students came to tutoring each day?
#   keys: (str) Monday, Tuesday, Wednesday, Thursday, Friday
#   value: (int) count of students who came that day
students_per_day = {
    "Monday": 0,
    "Tuesday": 0,
    "Wednesday": 0,
    "Thursday": 0,
    "Friday": 0,
}

# How many days per week did each student attend tutoring?
#   keys: (str) studentID
#   value: (int) number of days the student went to tutoring this week
days_per_student = {}
for key in student_names:
    days_per_student[key] = 0
# -------------------------------------------------------------------------------
# DO NOT MODIFY ABOVE THIS LINE
# -------------------------------------------------------------------------------
def reset_weekly_data():
    '''
    Clear both students_per_day and days_per_student.
    Both should be empty.
    '''

    students_per_day = {}
    days_per_student = {}

# -------------------------------------------------------------------------------

def add_attendance_data( studentID, day ):
    '''
    Add attendance data.
    Updates the students per day dictionary.
    Updates the days per student dictionary.

    parameters: studentID (str)
                day (str)

    returns: no return value
    '''
    days_per_student[studentID] += 1
    students_per_day[day] += 1



    return

# --------------------------------------------------------------------------------

def print_day_histogram():
    '''
    Print a histogram showing how many students
    attended tutoring each day of the week.

    parameters: no parameters

    returns: no return value
    '''

    print( 'students per day\n' )

    for day, count in students_per_day.items():
        print(f"{day}: {count}")

    print( '' )

    return

# ---------------------------------------------------------------------------------

def print_attendance_report():
    '''
    Print a tutoring attendance report for the week.
    Alphabetical order by studentID
    studentID TWO SPACES First Last ONE SPACE days attended

    field width
    5 studentID
    20 First Last
    1 days attended
    '''

    print('attendance report\n')

    for x, y in student_names.items():
        netID = x
        name = f"{y[1]} {y[0]}"
        number = days_per_student[netID]
        print(f"{netID} {name} {number}")


    print( '' )

    return

# ----------------------------------------------------------------------------------
# DO NOT MODIFY BELOW THIS LINE
# ----------------------------------------------------------------------------------
def read_data_file( filename ):

    datafile = open( filename, "r" )

    textline = datafile.readline()
    while textline != '':
        studentID, day = textline.split()
        add_attendance_data( studentID, day )
        textline = datafile.readline()

    datafile.close()

    return

# ----------------------------------------------------------------------------------

def test( filename ):

    reset_weekly_data()
    read_data_file( filename )
    print_attendance_report()
    print_day_histogram()

    return

# ----------------------------------------------------------------------------------

def main():

    print( "choose a week (1-3): ", end="" )
    choice = int(input(''))
    print( '' )

    if choice == 1:
        test('test_data_1.txt')
    elif choice == 2:
        test('test_data_2.txt')
    else:
        test('test_data_3.txt')

    return


if __name__ == '__main__':
    main()
