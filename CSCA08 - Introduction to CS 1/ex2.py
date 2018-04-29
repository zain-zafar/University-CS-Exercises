# Global variables. Feel free to play around with these
# but please return them to their original values before you submit.
a0_weight = 5
a1_weight = 7
a2_weight = 8
term_tests_weight = 20
exam_weight = 45
exercises_weight = 10
quizzes_weight = 5
a0_max_mark = 25
a1_max_mark = 50
a2_max_mark = 100
term_tests_max_mark = 50
exam_max_mark = 100
exercises_max_mark = 10
quizzes_max_mark = 5
exam_pass_mark = 40
overall_pass_mark = 50


def get_max(component_name):
    '''(str) -> float
    Given the name of a course component (component_name),
    return the maximum mark for that component. This is used to allow the GUI
    to display the "out of" text beside each input field.
    REQ: component_name must be one of: a0,a1,a2,exerises,midterm,exam
    >>> get_max('a0')
    25
    >>> get_max('exam')
    100
    REQ: component_name in {'a0', 'a1', 'a2', 'exercises', 'term tests',
    'quizzes', 'exam'}
    '''
    # DO NOT EDIT THIS FUNCTION. This function exists to allow the GUI access
    # to some of the global variables. You can safely ignore this function
    # for the purposes of E2.
    if(component_name == 'a0'):
        result = a0_max_mark
    elif(component_name == 'a1'):
        result = a1_max_mark
    elif(component_name == 'a2'):
        result = a2_max_mark
    elif(component_name == 'exercises'):
        result = exercises_max_mark
    elif(component_name == 'term tests'):
        result = term_tests_max_mark
    elif(component_name == 'quizzes'):
        result = quizzes_max_mark
    else:
        result = exam_max_mark

    return result


def percentage(raw_mark, max_mark):
    ''' (float, float) -> float
    Return the percentage mark on a piece of work that received a mark of
    raw_mark where the maximum possible mark of max_mark.
    >>> percentage(15, 20)
    75.0
    >>> percentage(4.5, 4.5)
    100.0
    REQ: raw_mark >=0
    REQ: max_mark > 0
    REQ: raw_max <= max_mark
    '''
    return raw_mark / max_mark * 100


def contribution(raw_mark, max_mark, weight):
    ''' (float, float, float) -> float
    Given a piece of work where the student earned raw_mark marks out of a
    maximum of max_marks marks possible, return the number of marks it
    contributes to the final course mark if this piece of work is worth weight
    marks in the course marking scheme.
    >>> raw_contribution(13.5, 15, 10)
    9.0
    REQ: raw_mark >=0
    REQ: max_mark > 0
    REQ: weight >= 0
    '''
    # start your own code here
def percentage(mark_received, marks_out_of):
    
    ''' (float, float) -> float
        Return the percentage mark on a piece of work that received a mark of
        marks_received where the maximum possible mark of max_marks.
        
        >>> percentage(20, 20)
        100.0
        >>> percentage(3.5, 4.0)
        87.5
        
        REQ: raw_mark >=0
        REQ: max_mark > 0
        REQ: raw_max <= max_mark
        '''
    return(mark_received/marks_out_of * 100)    

#-----------------------------------------------------------------------------
# Function for calculationg Term Mark
# User inserts their marks on assignments, exercises, quizzes, and tests
# The result is overall term mark 

def term_work_mark(a0_mark,a1_mark,a2_mark,exercises_mark,quiz_mark,test_marks):
    
    '''(float,float,float,float,float,float) -> (float) 
       
       Marks of assignments, exercises, quizzes, and tests, done by the student
       are entered. The function will return a percertage which corresponds to 
       each work divided by the works mark, and mutiplyed by the works weight.
       The final result is the average of each work added together which shows
       the term mark of the student. 
       
       >>> term_work_mark(25, 50, 100, 10, 5, 50)
       55.0
       
       >>> term_work_mark(20, 45, 70, 8, 4, 40)
       43.9
       
          REQ: a0_mark >=0
          REQ: a1_mark >=0
          REQ: a2_mark >=0
          REQ: exercises_mark >=0
          REQ: quiz_mark >=0
          REQ: test_marks >=0
          '''  
  # The average of each piece of work done by student is calculated
  # the averages of each work are added together to output the term work mark
  
    a0 = ((a0_mark / a0_max_mark)*a0_weight)
    a1 = ((a1_mark / a1_max_mark)*a1_weight)
    a2 = ((a2_mark / a2_max_mark)*a2_weight)
    exercises = ((exercises_mark / exercises_max_mark)*exercises_weight)
    quizzes = ((quiz_mark / quizzes_max_mark)*quizzes_weight)
    tests = ((test_marks / term_tests_max_mark)*term_tests_weight)
    
    return((float(a0))+(+float(a1))+(float(a2))+(+float(exercises)+
            (float(quizzes))+(float(tests))))

#-----------------------------------------------------------------------------

#The function final_mark generates the term mark of the student by adding up 
#the percentage received by the student on assignments,tests,quizzes
#tests, and also final exam

def final_mark(a0_mark,a1_mark,a2_mark,exercises_mark
               ,quiz_mark,test_marks,final_marks):
    
    '''  (float,float,float,float,float,float,float) -> (float)
          
          Given the marks scored by the student for
          assignments 0,1,2, and the percentage
          of the exercises, quizzes, tests, and final exam, the function will
          find the average of each and will return a percentage which 
          corresponds to the students final term mark. 
          
          
          >>> final_mark(25, 50, 100, 10, 5, 50,100)
          100.0
          
          >>> final_mark(20, 45, 70, 8, 4, 40, 73)
          76.75
          
          REQ: a0_mark >=0
          REQ: a1_mark >=0
          REQ: a2_mark >=0
          REQ: exercises_mark >=0
          REQ: quiz_mark >=0
          REQ: test_marks >=0
          REQ: final_marks >=0
          '''
  # Here the marks entered of the tests, quizzes, etc.
  # are divided by the total marks of each piece of work
  # then multiplyed by each of the pieces weight
  # the final variable adds up the total percentages of each peice, to 
  # generate the final term average of the student

    a0 = ((a0_mark / a0_max_mark)*a0_weight)
    a1 = ((a1_mark / a1_max_mark)*a1_weight)
    a2 = ((a2_mark / a2_max_mark)*a2_weight)
    exercises = ((exercises_mark / exercises_max_mark)*exercises_weight)
    quizzes = ((quiz_mark / quizzes_max_mark)*quizzes_weight)
    tests = ((test_marks / term_tests_max_mark)*term_tests_weight)  
    final = (final_marks / exam_max_mark)*exam_weight 
    
    return(a0+a1+a2+exercises+quizzes+tests+final)

#-----------------------------------------------------------------------------

# Function will return True if student receives >= 40 marks on exam and 
# receives >=50% on overall term mark, then return True
# if not, return False 

def is_pass(a0_mark,a1_mark,a2_mark,exercises_mark,quiz_mark,
            test_marks,final_marks):
    
    ''' (float,float,float,float,float,float,float) -> (bool)
    
        All the marks of the student on assignments, exercises, quizzes, tests,
        and final exam given, are calculated into average. If student scores
        higher or equal to 40 marks on the final exam, if false, then
        False is returned. If true, then the function checks if the student got 
        50% or greater overall term mark, if True, then return True. If False, 
        then return False. 
    
        >>> is_pass(20, 45, 70, 8, 4, 40, 41)
        True
       
        >>> is_pass(20, 45, 70, 8, 4, 40, 39)
        False
       
        >>> is_pass(10, 21, 12, 2, 1, 15, 23)
        False

        REQ: a0_mark >=0
        REQ: a1_mark >=0
        REQ: a2_mark >=0
        REQ: exercises_mark >=0
        REQ: quiz_mark >=0
        REQ: test_marks >=0
        REQ: final_marks >=0
        REQ for student to pass: final_marks >= 40 and add_up >= 50
        '''
    
 # All the averages are calculated for each peice of work
 # The function will check if exam marks scored are >= 40
 # if true then the program will check if term marks are >= 50%
 # if true, then returns True.
 # if false, returns False.   
 
    a0 = ((a0_mark / a0_max_mark)*a0_weight)
    a1 = ((a1_mark / a1_max_mark)*a1_weight)
    a2 = ((a2_mark / a2_max_mark)*a2_weight)
    exercises = ((exercises_mark / exercises_max_mark)*exercises_weight)
    quizzes = ((quiz_mark / quizzes_max_mark)*quizzes_weight)
    tests = ((test_marks / term_tests_max_mark)*term_tests_weight)  
    final = (final_marks / exam_max_mark)*exam_weight     
    add_up = a0+a1+a2+exercises+quizzes+tests+final

# Checking for True or False 

    if (final_marks >= 40):
        if(add_up >=50):
            return(True)
        
    else:
        return(False)
