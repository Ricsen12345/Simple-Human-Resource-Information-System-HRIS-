from birth_date import Birth
from address import Address

class Creator:
    
    '''
        Association class\n

        This class is used to prevent looping import because all methods
        inside this class are being used at several other classes\n

        __init__ (constructor) is not available\n

        Static methods:\n
        createBirth(), createAddress()
    '''
    
    @staticmethod
    def createBirth():
        
        '''
        Employee's method\n

        Automatically ask the user to insert information about his/her birth 
        place and birth date whilst validate them automatically and re-ask the 
        input until the user insert them using the correct format\n

        Correct format:\n
        Place   -> alphabet only\n
        Day     -> numeric only\n
        Month   -> numeric only\n
        Year    -> numeric only\n

        No argument is taken from the user\n
        Return  -> object from Birth class
        '''
        
        print('\nBirth place and birth date')
        
        # Validate each user's input
        place,day,month,year = '#','#','#','#' # Dummy variables
        while True:
            if place.isalpha() == False:
                place = input('City              : ')
            elif day.isnumeric() == False:
                day   = input('Day               : ')
            elif month.isnumeric() == False:
                month = input('Month (in number) : ')
            elif year.isnumeric() == False:
                year  = input('Year              : ')
            else:
                break
        
        # Convert day, month, year into int
        day = int(day)
        month = int(month)
        year = int(year)

        return Birth(place, day, month, year)


    @staticmethod
    def createAddress():
        
        '''
        Employee's method\n

        Automatically ask the user to insert information about his/her address
        whilst validate them automatically and re-ask the input until the user 
        insert them using the correct format\n

        Correct format:\n
        Street  -> alphabet + numerical only\n
        City    -> alphabet only\n
        State   -> alphabet only\n
        Country -> alphabet only\n

        No argument is taken from the user\n
        Return  -> address (instance attribute from Address class)
        '''
        
        print('\nMain Address')

        # Validate each user's input
        street,city,state,country = '#','#','#','#' # Dummy variables
        while True:
            if street.replace(' ','').isalnum() == False:
                street  = input('Street  : ')
            elif city.replace(' ','').isalpha() == False:
                city    = input('City    : ')
            elif state.replace(' ','').isalpha() == False:
                state   = input('State   : ')
            elif country.replace(' ','').isalpha() == False:
                country = input('Country : ')
            else:
                break
        
        return Address(street, city, state, country).address