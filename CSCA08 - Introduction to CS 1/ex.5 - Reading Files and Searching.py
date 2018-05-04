def function_names(file):
    '''(io.TextIOWrapper) -> list of str
        
    '''
    next_line = file.readlines()
    lister = []
    for line in next_line:
        gg = line.strip('\n')   
        if (gg.startswith('def')):
            index1 = gg.find(' ')
            index2 = gg.find('(')
            index1 = index1 + 1
            names_of_func = line[index1 : index2]
            lister = lister+[names_of_func]       
            
    return lister


def justified(file):
    next_line = file.readlines()
    justified=True
    for line in next_line:
        gg = line.strip('\n')
        if (gg.startswith(" ")):
            justified=False
        else:
            justified = justified
        
    return justified 
    
    
    