from datetime import date

class Date:
    
    '''
    This class is intended to store dates given by the user
    (Birth date and Starting Day)\n
    
    list of parameters to be provided to create object:\n
    + day   : int (numeric)\n
    + month : int (numeric)\n
    + year  : int (numeric)\n

    There isn't any usable method in this class\n

    Properties(read-only):\n
    day, month, year, date
    '''

    def __init__(self,day,month,year):
        self.__day = day
        self.__month = month
        self.__year = year
        self.__date = self.__completeDate()
    
    def __completeDate(self):
        
        '''
        Encapsulated Method\n

        Automatically provide complete date because the user gives
        information about day, month, year separately\n

        No argument is taken from the user.
        return  -> Complete date (Ex: 6 September 2002)
        '''

        d = date(self.__year, self.__month, self.__day)
        return d.strftime('%d %B %Y') 
    
    @property
    def day(self):
        return self.__day
    
    @property
    def month(self):
        return self.__month

    @property
    def year(self):
        return self.__year
    
    @property
    def date(self):
        return self.__date


class Birth(Date):

    '''
    Sub-class of Date class\n
    
    This class is intended to store birth date and place given 
    by the user\n

    list of parameters to be provided to create object:\n
    + place : str (alphabet)\n
    + day   : int (numeric)\n
    + month : int (numeric)\n
    + year  : int (numeric)\n

    There isn't any usable method in this class\n

    Properties(read-only): birth
    '''

    def __init__(self,place:str,day:int,month:int,year:int,):
        super().__init__(day,month,year)
        self.__place = place
        self.__birth = self.__completeBirth()
           
    def __completeBirth(self):
        
        '''
        Encapsulated method\n

        Automatically provide complete birth because the user gives
        information about place, day, month, and year separately\n
        
        No argument is taken from the user\n
        return  -> Birth place and date (Ex: London, 1 January 2001)  
        '''

        return f"{self.__place}, {self.date}"
    
    @property
    def birth(self):
        return self.__birth