def useless(parameter_1, parameter_2, parameter_3):
    return("That was a waste of time")

def square_me(one_integer_or_float):
    return(one_integer_or_float * one_integer_or_float)


def student_data(name, age, student_number, enrolled):
    return ((str("<")+str(student_number)+str(",")+str(name)+str(",")
             +str(int(age))+str(",")+(str(bool(enrolled)))+str(">")))


if __name__ == "__main__":
    print("kk")
    print(useless(1,2,3))
    
