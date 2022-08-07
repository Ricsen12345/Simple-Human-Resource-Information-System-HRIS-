# Python built-in libraries
from abc import ABC, abstractmethod
from datetime import date

# Imported from other classes
from birth_date import *
from creator import Creator
from export import Export
from setter import Setter
from relocate import Relocate


class Employee(ABC):

    '''
    Parent class (abstract)\n
    
    This class store all employees' data given by employee when
    he/she enters the company (account creation)\n

    list of parameters to be provided to create object:
    + Full name     : str (alphabet)
    + NIK           : str (numeric)
    + Gender        : str (value either 'M' or 'F')
    + Department    : str (alpabet)
    + Password      : str (any)\n

    Instance methods:\n
    promoted(), demoted(), login(), accessProfile(), relocate()\n 
    
    Class methods:\n
    updateData(), exportData(), setSalPercentage(), setMaxSalary()\n

    Properties (read-only):\n
    name, id, NIK, email, birth, age, department, position, address,
    activeness, startingDay, workingYears
    '''

    # Class Attributes (Encapsulated)
    __salaryPercentage = {
        'Staff'           : 0.4,
        'Executive'       : 0.6,
        'Section head'    : 0.8,
        'Department head' : 1
    }
    __listPosition = ['Staff', 'Executive', 'Section head', 'Department head']
    __listEmployees = []

    @abstractmethod
    def __init__(self, name:str, NIK:str, gender:str, department:str, password:str):
        
        # Ignore lowercase by convert it to uppercase
        gender = gender.upper()
        
        # Ask for inputs if doesn't meet criteria made
        # I think I should have put name at main file
        while True:
            if name.replace(' ','').isalpha() == False:
                name  = input('\nOnly alphabet allowed\nName: ')
            elif NIK.isdigit()==False:
                NIK = input('\nOnly number allowed\nNIK: ')
            elif gender not in ['M','F']:
                gender = input('\nOnly M or F allowed\nGender: ')
            elif len(password)<8:
                password = input('\nShould contain at least 8 characters\nPassword: ')
            else:
                break
        
        # Convert into formal format (Capital in front of each word)
        name = name.title()

        # Add this employee to list (class attribute)
        self.__listEmployees.append(self)

        # Arguments taken from the user (outside class)
        self.__name = name
        self.__NIK = NIK
        self.__gender = 'Male' if gender=='M' else 'Female'
        self.__department = department
        self.__password = password

        # Arguments taken from the user (inside class)
        self.__birth = Creator.createBirth()
        self.__address = Creator.createAddress()

        # Default attributes after object creation
        self.__position = 'Staff'
        self.__activeness = 'Active'

        # Auto generated attributes
        self.__startingDay = Date(date.today().day, date.today().month, date.today().year)
        self.__workingYears = self.__calculateYear(self.__startingDay)
        self.__age = self.__calculateYear(self.__birth)
        self.__email = self.__generateEmail()
        self.__id = self.__generateId()
    

    ################################################ 
    # ---- Auto generated instance attributes ---- #
    ################################################

    def __generateId(self):
        
        '''
        Encapsulated method\n

        Automatically generates employee's id when the employee
        enter the company (create account) or when the employee
        got relocated to other department\n

        id = (department id)(starting year)(nth employee in company)\n

        No argument is taken from the user\n
        return -> employee's id
        '''

        return f'{self.clsid}{self.__startingDay.year}{str(len(self.__listEmployees)).zfill(5)}'


    def __generateEmail(self):
        
        '''
        Encapsulated method\n

        Automatically generates employee's company email, this method
        can only be used once (during object creation)\n

        No argument is taken from the user\n
        return -> employee's company email
        '''
        
        modifyName = self.__name.lower().split(' ')
        
        while len(modifyName)>2:
            modifyName.pop()
        emailName = '.'.join(modifyName)
        
        return f'{emailName}@employee.mekarmukti.ac.id'


    def __calculateYear(self, case):
        
        '''
        Encapsulated method\n

        Automatically calculates the total year of a certain time
        to date, this method can only be used during object creation 
        and data updating\n

        Argument taken  -> case:object\n
        Return          -> total years
        '''

        today = date.today()
        yrs = today.year - case.year - ((today.month, today.day) < (case.month, case.day))
        return yrs


    ############################################## 
    # ---- Employee's Position Manipulation ---- #
    ##############################################
    
    def promoted(self):
        
        '''
        Host's method\n

        Automatically promotes each employee to one position above
        their initial position\n

        If the employee already occupies the highest position, then 
        he/she won't get any promotion and his/her position is still 
        as 'Department head'\n

        No argument is taken from the user\n
        No returned value
        '''
        
        idx = self.__listPosition.index(self.__position)
        if (idx != len(self.__listPosition)-1) and (self.__activeness == 'Active'):
            self.__position = self.__listPosition[idx+1]
    
    
    def demoted(self):
        
        '''
        Host's method\n

        Automatically demotes each employee to one position below
        their initial position\n

        If the employee already occupies the lowest position, then 
        he/she will be fired from the company and he/she will become 
        in-active (self.__activeness = 'in-active')\n

        No argument is taken from the user\n
        No returned value
        '''

        idx = self.__listPosition.index(self.__position)
        if idx > 0:
            self.__position = self.__listPosition[idx-1]
        elif (idx==0) and (self.__activeness == 'Active'):
            self.__inActive()
    

    def __inActive(self):
        
        '''
        Encapsulated method\n

        Automatically non-activate an employee when he/she
        got demoted even though he/she already at the lowest
        position in the company (fired)\n

        No argument is taken from the user\n
        No returned value
        '''
        
        self.__position = None
        self.__activeness = 'Non-active'


    ################################################## 
    # ---- Data Accessing & Manipulation (User) ---- #
    ##################################################

    def login(self):
        
        '''
        Employee's method\n

        Automatically asks the user what information he/she wants 
        to set, can only set his/her own information by validating 
        it using password created during object creation\n

        Information that can be set:\n
        name, NIK, gender, password, birth, address

        No argument is taken from the user
        No returned value
        '''

        input_pw = input('Enter Password : ')

        if self.__password == input_pw:
            # l -> line
            l0 = '\nComplete Profile\n'
            l1  = f'Name          : {self.__name}\n'
            l2  = f'NIK           : {self.__NIK}\n'
            l3  = f'Id            : {self.__id}\n'
            l4  = f'Email         : {self.__email}\n'
            l5  = f'Gender        : {self.__gender}\n'
            l6  = f'Age           : {self.__age}\n'
            l7  = f'Birth         : {self.__birth.birth}\n'
            l8  = f'Address       : {self.__address}\n'
            l9  = f'Department    : {self.__department}\n'
            l10 = f'Position      : {self.__position}\n'
            l11 = f'Activeness    : {self.__activeness}\n'
            l12 = f'Starting Day  : {self.__startingDay.date}\n'
            l13 = f'Working Years : {self.__workingYears}\n'
            
            percentage = self.__salaryPercentage[self.__position]
            maxsal = self.clsMaxSalary
            salary = percentage*maxsal
            l14 = f'Salary/month  : Rp {int(salary)}'
            
            line = l0+l1+l2+l3+l4+l5+l6+l7+l8+l9+l10+l11+l12+l13+l14
            print(line)

            val = None
            while val not in ['y','n']:
                val = input("\nDo you want to set something (y/n)? ")
            
            if val=='y':
                while True:
                    setwhat = -1
                    while setwhat not in ['1','2','3','4','5','6','7']:
                        # l -> line
                        l0 = '\nWhat do you want to set?\n'
                        l1 = '1) Name\n'
                        l2 = '2) NIK\n'
                        l3 = '3) Gender\n'
                        l4 = '4) Password\n'
                        l5 = '5) Birth\n'
                        l6 = '6) Address\n'
                        l7 = '7) None'
                        print(l0+l1+l2+l3+l4+l5+l6+l7)

                        setwhat = input('Answer: ')
                    
                    # if setwhat = 7 (the program won't do anything)
                    if setwhat == '1':
                        self.__name = Setter().setName()
                    elif setwhat == '2':
                        self.__NIK = Setter().setNIK()
                    elif setwhat == '3':
                        self.__gender = Setter().setGender()
                    elif setwhat == '4':
                        self.__password = Setter().setPassword()
                    elif setwhat == '5':
                        self.__birth = Setter().setBirth()
                    elif setwhat == '6':
                        self.__address = Setter().setAddress()
                    else:
                        break            
        
        else:
            print("Wrong Password")

    
    def accessProfile(self):
        
        '''
        Employee's method\n

        See other employee's profile (information) to some extent\n

        No argument is taken from the user\n

        returned information:\n
        name, id, email, department, position, activeness
        '''

        # l -> line
        l0 = f"\n{self.__name}'s profile\n"
        l1 = f'Id         : {self.__id}\n'
        l2 = f'Email      : {self.__email}\n'
        l3 = f'Department : {self.__department}\n'
        l4 = f'Position   : {self.__position}\n'
        l5 = f'Activeness : {self.__activeness}'
        return l0+l1+l2+l3+l4+l5
    

    def relocateEmployee(self):
        ans = None
        while ans not in ['y','n']:
            ans = input('Are you sure you want to relocate this employee (y/n)? ')
        
        if ans=='y':
            Relocate(self).relocate()


    ###################################################
    # ---- Data Manipulation & Extraction (Host) ---- #
    ###################################################

    @classmethod
    def updateData(cls):

        '''
        Host's method\n

        Automatically update every employee's data\n

        Updated information:\n
        + age           -> recalculated using __calculateYear() method\n
        + workingYears  -> recalculated using __calculateYear() method\n

        If employee's age exceed 60 years after updating the data, he/she
        will have to retire from this company
        
        No argument is taken from the user\n
        No returned value
        '''
        
        for obj in cls.__listEmployees:
            obj.age = cls.__calculateYear(obj, obj.birth)
            obj.workingYears = cls.__calculateYear(obj, obj.startingDay)

            if obj.age > 60:
                cls.__inActive(obj)

    
    @classmethod
    def exportData(cls):

        '''
        Host's method\n

        Export data related to all employees' information
        (except employee's password)\n

        No argument is taken from the user\n
        No returned value
        '''

        # Lists to store employee's information
        listname = []
        listid = []
        listNIK = []
        listgender = []
        listemail = []
        listbirth = []
        listage = []
        listdepartment = []
        listaddress = []
        listposition = []
        listactiveness = []
        liststartingDay = []
        listworkingYears = []

        for obj in cls.__listEmployees:
            listname.append(obj.name)
            listid.append(obj.id)
            listNIK.append(obj.NIK)
            listgender.append(obj.gender)
            listemail.append(obj.email)
            listbirth.append(obj.birth.birth)
            listage.append(obj.age)
            listdepartment.append(obj.department)
            listaddress.append(obj.address)
            listposition.append(obj.position)
            listactiveness.append(obj.activeness)
            liststartingDay.append(obj.startingDay.date)
            listworkingYears.append(obj.workingYears)

        expData = Export(listname, listid, listNIK, listgender, listemail, listbirth, listage, 
                         listdepartment, listaddress, listposition, listactiveness, 
                         liststartingDay, listworkingYears)
        
        ans = None
        while ans not in ['1','2','3']:
            l0 = '\nPick the format\n'
            l1 = '1) Excel\n'
            l2 = '2) CSV (Comma Separated Value)\n'
            l3 = '3) Cancel'
            print(l0+l1+l2+l3)

            ans = input('Answer: ')
        
        if ans=='1':
            expData.export_excel()
        elif ans=='2':
            expData.export_csv()
    
    
    ###########################################
    # ---- Class Attribute Setter (Host) ---- #
    ###########################################

    @classmethod
    def setSalPercentage(cls):
        
        '''
        Host's method\n

        Manipulate salary percentage for each positions (class attribute),
        the host must reset every percentage in dictionary\n

        No argument is taken from the host\n
        No returned value
        '''
        
        print('Previous Salary Percentage')
        for key in cls.__salaryPercentage:
            print(f'{key}: {cls.__salaryPercentage[key]}')

        print('\nSet your new Salary Percentage')
        for key in cls.__salaryPercentage:
            newValue = input(f'{key}: ')
            cls.__salaryPercentage[key] = newValue
    

    @staticmethod
    def setMaxSalary(cls, newMaxSalary):
        
        '''
        Host's method\n

        Manipulate maximum salary of the respective department (sub-class)\n

        Argument taken  -> new maximum salary\n
        No returned value
        '''
        
        # I think setter is needed in each department classes
        cls.clsMaxSalary = newMaxSalary


    #################################### 
    # ---- Properties (read-only) ---- #
    ####################################
    
    @property
    def name(self):
        return self.__name
    
    @property
    def id(self):
        return self.__id
    
    @property
    def NIK(self):
        return self.__NIK
    
    @property
    def gender(self):
        return self.__gender
    
    @property
    def email(self):
        return self.__email
    
    @property
    def birth(self):
        return self.__birth
    
    @property
    def age(self):
        return self.__age
    
    @property
    def department(self):
        return self.__department
    
    @property
    def position(self):
        return self.__position
    
    @property
    def address(self):
        return self.__address
    
    @property
    def activeness(self):
        return self.__activeness
    
    @property
    def startingDay(self):
        return self.__startingDay
    
    @property
    def workingYears(self):
        return self.__workingYears

    @age.setter
    def age(self, newAge):
        self.__age = newAge
    
    @workingYears.setter
    def workingYears(self, newworkingYears):
        self.__workingYears = newworkingYears