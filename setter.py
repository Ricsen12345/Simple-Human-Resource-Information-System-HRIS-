from birth_date import Birth
from creator import Creator

class Setter:
    
    '''
    This class is intended to set some of the information (instance attribute) 
    of the employee\n

    __init__ (constructor) is not available\n

    Static methods:\n
    setName(), setNIK(), setGender(), setPassword(), setBirth(), setAddress()
    '''
    
    @staticmethod
    def setName():
        newName = '#'
        while newName.replace(' ','').isalpha() == False:
            newName = input('Full Name : ').title()
        return newName

    @staticmethod
    def setNIK():
        newNIK = ' '
        while newNIK.isnumeric()==False:
            newNIK = input('NIK       : ')
        return newNIK
    
    @staticmethod
    def setGender():
        choose = ' '
        while choose not in ['M','F']:
            choose = input('Gender    : ')
        newGender = 'Male' if choose=='M' else 'Female'
        return newGender

    @staticmethod
    def setPassword():
        newPassword = ' '
        while len(newPassword)<8:
            newPassword = input('Password  : ')
        return newPassword

    @staticmethod
    def setBirth():
        Creator.createBirth()
    
    @staticmethod
    def setAddress():
        Creator.createAddress()