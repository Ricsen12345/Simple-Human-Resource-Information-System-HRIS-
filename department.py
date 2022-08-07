from employee import Employee

class HRD(Employee):
    clsid = '001'
    clsMaxSalary = 17500000

    def __init__(self, name:str, NIK:str, gender:str, password:str):
        super().__init__(name, NIK, gender, 'HRD', password)


class Accounting(Employee):
    clsid = '002'
    clsMaxSalary = 19000000
    
    def __init__(self, name:str, NIK:str, gender:str, password:str):
        super().__init__(name, NIK, gender, 'Accounting', password)


class Production(Employee):
    clsid = '003'
    clsMaxSalary = 21000000
    
    def __init__(self, name:str, NIK:str, gender:str, password:str):
        super().__init__(name, NIK, gender, 'Production', password)


class DataAnalyst(Employee):
    clsid = '004'
    clsMaxSalary = 25000000
    
    def __init__(self, name:str, NIK:str, gender:str, password:str):
        super().__init__(name, NIK, gender, 'Data Analyst', password)


class Marketing(Employee):
    clsid = '005'
    clsMaxSalary = 15000000
    
    def __init__(self, name:str, NIK:str, gender:str, password:str):
        super().__init__(name, NIK, gender, 'Marketing', password)


class Purchasing(Employee):
    clsid = '006'
    clsMaxSalary = 16500000
    
    def __init__(self, name:str, NIK:str, gender:str, password:str):
        super().__init__(name, NIK, gender, 'Purchasing', password)


class Maintenance(Employee):
    clsid = '007'
    clsMaxSalary = 20000000
    
    def __init__(self, name:str, NIK:str, gender:str, password:str):
        super().__init__(name, NIK, gender, 'Maintenance', password)