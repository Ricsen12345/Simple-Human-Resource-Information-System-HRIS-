from department import *

class Relocate:
    
    def __init__(self, emp):
        self.__emp = emp

    def nameVar(self):
        name = self.__emp.name.replace(' ','')
        return name

    def relocate(self):
        choose = None
        while choose not in ['1','2','3','4','5','6','7']:
            l0 = '\nRelocate to what department?\n'
            l1 = '(Choose the same department to cancel)\n'
            l2 = '1) HRD\n'
            l3 = '2) Accounting\n'
            l4 = '3) Production\n'
            l5 = '4) Data Analyst\n'
            l6 = '5) Marketing\n'
            l7 = '6) Purchasing\n'
            l8 = '7) Maintenance'
            print(l0+l1+l2+l3+l4+l5+l6+l7+l8)
                
            choose = input('Answer: ')
        
        gender = 'M' if self.__emp.gender=='M' else 'F'

        if choose=='1' and isinstance(self.__emp, HRD)==False:
            globals()[self.nameVar()] = HRD(self.__emp.name, self.__emp.NIK, gender, 
                                            self.__emp.password)
        
        elif choose=='2' and isinstance(self.__emp, Accounting)==False:
            globals()[self.nameVar()] = Accounting(self.__emp.name, self.__emp.NIK, gender, 
                                                   self.__emp.password)
        
        elif choose=='3' and isinstance(self.__emp, Production)==False:
            globals()[self.nameVar()] = Production(self.__emp.name, self.__emp.NIK, gender, 
                                                   self.__emp.password)
        
        elif choose=='4' and isinstance(self.__emp, DataAnalyst)==False:
            globals()[self.nameVar()] = DataAnalyst(self.__emp.name, self.__emp.NIK, gender, 
                                                    self.__emp.password)

        elif choose=='5' and isinstance(self.__emp, Marketing)==False:
            globals()[self.nameVar()] = Marketing(self.__emp.name, self.__emp.NIK, gender, 
                                                  self.__emp.password)
        
        elif choose=='6' and isinstance(self.__emp, Purchasing)==False:
            globals()[self.nameVar()] = Production(self.__emp.name, self.__emp.NIK, gender, 
                                                   self.__emp.password)
        
        elif choose=='7' and isinstance(self.__emp, Maintenance)==False:
            globals()[self.nameVar()] = Maintenance(self.__emp.name, self.__emp.NIK, gender, 
                                                    self.__emp.password)