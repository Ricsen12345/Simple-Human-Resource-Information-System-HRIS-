from department import *
from employee import Employee

def nameinp():
    name = input('Full Name      : ')
    name = name.title().replace(' ','')
    return name

def runProgram():
    print('System start operating...\n')

    # Ask for password of the host (for host settings & stop the program)
    print('Please insert new password for this system')
    PWchar = input('Password: ')
    while len(PWchar)<8:
        PWchar = input('Password: ')

    # Looping until the program stopped (all data lost)
    while True:
        do = None
        while do not in ['1','2','3','4','5']:
            l0 = '\nWhat do you want to do?\n'
            l1 = '1) Create account\n'
            l2 = '2) Access profile\n'
            l3 = '3) Login\n'
            l4 = '4) Host settings\n'
            l5 = '5) Stop this program'
            print(l0+l1+l2+l3+l4+l5)
            
            do = input('Answer: ')

        ############################   
        # ---- Create Account ---- #
        ############################
        
        if do=='1':
            # Ask the user until he/she insert between 1-7
            dept = None
            while dept not in ['1','2','3','4','5','6','7']:
                l0 = '\nWhich department are you in?\n'
                l1 = '1) HRD\n'
                l2 = '2) Accounting\n'
                l3 = '3) Production\n'
                l4 = '4) Data Analyst\n'
                l5 = '5) Marketing\n'
                l6 = '6) Purchasing\n'
                l7 = '7) Maintenance'
                print(l0+l1+l2+l3+l4+l5+l6+l7)
                
                dept = input('Answer: ')
            
            print('\nInsert your personal Information')
            name     = input('Full Name : ')
            nik      = input('NIK       : ')
            gender   = input('Gender    : ')
            password = input('Password  : ')

            name1 = name.title().replace(" ", '')
            
            if dept=='1':
                globals()[name1] = HRD(name,nik,gender,password)
           
            elif dept=='2':
                globals()[name1] = Accounting(name,nik,gender,password)

            elif dept=='3':
                globals()[name1] = Production(name,nik,gender,password)
            
            elif dept=='4':
                globals()[name1] = DataAnalyst(name,nik,gender,password)

            elif dept=='5':
                globals()[name1] = DataAnalyst(name,nik,gender,password)

            elif dept=='6':
                globals()[name1] = Purchasing(name,nik,gender,password)
            
            elif dept=='7':
                globals()[name1] = Maintenance(name,nik,gender,password)

        ############################
        # ---- Access Profile ---- #
        ############################

        elif do=='2':
            try:
                print()
                print(globals()[nameinp()].accessProfile())
            except:
                print('There is no employee with that name')

        ###################
        # ---- Login ---- #
        ###################

        elif do=='3':
            try:
                print()
                globals()[nameinp()].login()
            except:
                print('There is no employee with that name')

        ###########################
        # ---- Host Settings ---- #
        ###########################

        elif do=='4':
            print("\nPlease input host's password")
            password = input('Password: ')
            
            if password == PWchar:
                
                while True:
                    ans = None
                    while ans not in ['1','2','3','4','5','6','7','8']:
                        l0 = '\nWhat do you want to do?\n'
                        l1 = '1) Promote Employee\n'
                        l2 = '2) Demote Employee\n'
                        l3 = '3) Relocate Employee\n'
                        l4 = '4) Update Data\n'
                        l5 = '5) Export Data\n'
                        l6 = '6) Set Salary Percetage\n'
                        l7 = '7) Set Maximum Salary\n'
                        l8 = '8) Back'
                        print(l0+l1+l2+l3+l4+l5+l6+l7+l8)

                        ans = input('Answer: ')

                    if ans=='1':
                        try:
                            print()
                            globals()[nameinp()].promoted()
                        except:
                            print('There is no employee with that name')

                    elif ans=='2':
                        try:
                            print()
                            globals()[nameinp()].demoted()
                        except:
                            print('There is no employee with that name')

                    elif ans=='3':
                        print()
                        globals()[nameinp()].relocateEmployee()

                    elif ans=='4':
                        Employee.updateData()

                    elif ans=='5':
                        Employee.exportData()

                    elif ans=='6':
                        print()
                        Employee.setSalPercentage()

                    elif ans=='7':
                        
                        choose_cls = None
                        while choose_cls not in ['1','2','3','4','5','6','7','8']:
                            
                            l0 = '\nChoose the department\n'
                            l1 = '1) HRD\n'
                            l2 = '2) Accounting\n'
                            l3 = '3) Production\n'
                            l4 = '4) Data Analyst\n'
                            l5 = '5) Marketing\n'
                            l6 = '6) Purchasing\n'
                            l7 = '7) Maintenance\n'
                            l8 = '8) Back'
                            print(l0+l1+l2+l3+l4+l5+l6+l7+l8)

                            choose_cls = input('Answer: ')
                        
                        if choose_cls=='1':
                            newMaxSalary = int(input('New Max Salary: '))
                            Employee.setMaxSalary(HRD, newMaxSalary)
                        
                        elif choose_cls=='2':
                            newMaxSalary = int(input('New Max Salary: '))
                            Employee.setMaxSalary(Accounting, newMaxSalary)
                        
                        elif choose_cls=='3':
                            newMaxSalary = int(input('New Max Salary: '))
                            Employee.setMaxSalary(Production, newMaxSalary)
                        
                        elif choose_cls=='4':
                            newMaxSalary = int(input('New Max Salary: '))
                            Employee.setMaxSalary(DataAnalyst, newMaxSalary)
                        
                        elif choose_cls=='5':
                            newMaxSalary = int(input('New Max Salary: '))
                            Employee.setMaxSalary(Marketing, newMaxSalary)
                        
                        elif choose_cls=='6':
                            newMaxSalary = int(input('New Max Salary: '))
                            Employee.setMaxSalary(Purchasing, newMaxSalary)
                        
                        elif choose_cls=='7':
                            newMaxSalary = int(input('New Max Salary: '))
                            Employee.setMaxSalary(Maintenance, newMaxSalary)

                    elif ans=='8':
                        break

            else:
                print('Wrong Password')


        elif do=='5':
            print("\nPlease enter the Password!")
            password = input('Password: ')
            if password == PWchar:
                yesno = input('Are you sure you want to shut down the system (y/n)? ')
                if yesno == 'y':
                    break
                       
runProgram()