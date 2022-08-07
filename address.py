class Address:
    
    '''
    This class is intended to store address given by the user\n
    
    list of parameters to be provided to create object:\n
    + street  : str (alphabet & numeric)\n
    + city    : str (alphabet)\n
    + state   : str (alphabet)\n
    + country : str (alphabet)\n

    There isn't any usable method in this class\n

    Properties(read-only): address
    '''

    def __init__(self,street:str,city:str,state:str,country:str):
        self.__street = street
        self.__city = city
        self.__state = state
        self.__country = country
        self.__address = self.__completeAdress()

    def __completeAdress(self):
        
        '''
        Encapsulated Method\n

        Automatically provide complete address because the user gives
        information about street, city, state, and country separately\n

        No argument is taken from the user\n
        return  -> Employee's complete address\n
        (Ex: Jln. Cibarusa No.3, Bogor, Jawa Barat, Indonesia)
        '''

        return f"{self.__street}, {self.__city}, {self.__state}, {self.__country}"
        
    @property
    def address(self):
        return self.__address