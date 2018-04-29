def percent_to_gpv(mark):   
    
    ''' (int) -> (float)
        
        REQ: 0 <= mark <= 100
        
        >>> percent_to_gpv(0)
        0.0
        >>> percent_to_gpv(36)
        0.0
        >>> percent_to_gpv(49)
        0.0
        >>> percent_to_gpv(50)
        0.7
        >>> percent_to_gpv(51)
        0.7
        >>> percent_to_gpv(52)
        0.7
        >>> percent_to_gpv(53)
        1.0
        >>> percent_to_gpv(55)
        1.0
        >>> percent_to_gpv(56)
        1.0
        >>> percent_to_gpv(61)
        1.7
        >>> percent_to_gpv(64)
        2.0
        >>> percent_to_gpv(67)
        2.3
        >>> percent_to_gpv(71)
        2.7
        >>> percent_to_gpv(78)
        3.3
        >>> percent_to_gpv(84)
        3.7
        >>> percent_to_gpv(87)
        4.0
        
        This program will take a mark ranging from 0-100, which is int value.
        Then the program will output a G.P.A which will correspond to the given
        percentage. 
        '''
    
# Below all the averages are posted, and the corresponding GPA will be returned
# We are easily able to make this possible by using "if" statements
# If entered average is 80, then the GPA returned will be 3.7
    if(85 <= mark <= 100):
        return(4.0)
    elif(80 <= mark <= 89):
        return(3.7)
    elif(77 <= mark <= 79):
        return(3.3)
    elif(73 <= mark <= 76):
        return(3.0)    
    elif(70 <= mark <= 72):
        return(2.7)   
    elif(67 <= mark <= 69):
        return(2.3)    
    elif(63 <= mark <= 66):
        return(2.0)  
    elif(60 <= mark <= 62):
        return(1.7)
    elif(57 <= mark <= 59):
        return(1.3)  
    elif(53 <= mark <= 56):
        return(1.0)       
    elif(50 <= mark <= 52):
        return(0.7)     
    elif(0 <= mark <= 49):
        return(0.0)           
    
# -----------------------------------------------------------------------------


def card_namer(value, suit):
    
    ''' (str, str) -> (str)
        
        No REQ
        
        >>> card_namer('Q','S')
        'Queen of Spades'
        
        >>> card_namer('A','F')
        'CHEATER!'
        
        >>> card_namer('T','C')
        '10 of Clubs'
        
        >>> card_namer('J','H')
        'Jack of Hearts'
        
        >>> card_namer('K','D')
        'King of Diamond'
        
        This function allows the user to input two string values. If the proper
        card number and suit are inputted, then the name of the card is 
        returned. Such as if user enters 'K' and 'D' then 'King of Diamond' 
        will be returned. Also, to prevent cheaters from entering fake cards,
        the function will find any non-matching number and suit, and return
        'CHEATER!' 
        '''
# These statements allow us to find all the possible suits of Aces, if 'A' is
# entered    
    if(value =='A' and suit =='D'):
        return("Ace of Diamonds")
    if (value == 'A' and suit == 'C'):
        return("Ace of Clubs")
    if(value== 'A' and suit == 'H'):
        return("Ace of Hearts")
    if(value== 'A' and suit == 'S'):
        return("Ace of Spades")    

# These statements allow us to find all the possible suits of numbers from 2-9
# including 2 and 9, if 2-9 is entered        
    if((value== '2' or value == '3' or value =='4' or value=='5' or value=='6'
         or value=='7' or value=='8' or value=='9')
          and suit == 'D'):
        return (str(value) +" of Diamonds")    
    
    if((value== '2' or value == '3' or value =='4' or value=='5' or value=='6'
         or value=='7' or value=='8' or value=='9')
          and suit == 'H'):
        return (str(value) +" of Hearts")  
    
    if((value== '2' or value == '3' or value =='4' or value=='5' or value=='6'
         or value=='7' or value=='8' or value=='9')
              and suit == 'C'):
        return (str(value) +" of Clubs")        
    
    if((value== '2' or value == '3' or value =='4' or value=='5' or value=='6'
         or value=='7' or value=='8' or value=='9')
              and suit == 'S'):
        return (str(value) +" of Spades") 
    
# These statements allow us to find all the possible suits of 10, if 'T' is
# entered            
    if(value == "T" and suit == 'C'):
        return ("10 of Clubs")
    if(value== "T" and suit == 'H'):
        return("10 of Hearts")
    if(value== 'T' and suit == 'S'):
        return("10 of Spades")
    if(value== 'T' and suit == 'D'):
        return("10 of Diamonds")     
    
# These statements allow us to find all the possible suits of Jack, if 'J' is
# entered        
    if(value == 'J' and suit == 'C'):
        return("Jack of Clubs")
    if(value== 'J' and suit == 'H'):
        return("Jack of Hearts")
    if(value== 'J' and suit == 'S'):
        return("Jack of Spades")
    if(value== 'J' and suit == 'D'):
        return("Jack of Diamonds")  
    
# These statements allow us to find all the possible suits of Queen, if 'Q' is
# entered
    if(value == 'Q' and suit == 'C'):
        return("Queen of Clubs")
    if(value== 'Q' and suit == 'H'):
        return("Queen of Hearts")
    if(value== 'Q' and suit == 'S'):
        return("Queen of Spades")
    if(value== 'Q' and suit == 'D'):
        return("Queen of Diamonds")   
    
# These statments allow us to find all the possible suits of Kings, if 'K' is
# entered
    if(value == 'K' and suit == 'C'):
        return("King of Clubs")
    if(value== 'K' and suit == 'H'):
        return("King of Hearts")
    if(value== 'K' and suit == 'S'):
        return("King of Spades")
    if(value== 'K' and suit == 'D'):
        return("King of Diamonds")   
    
# This final statement is for cheaters or any other false value entered:
    else:
        return "CHEATER!"
    