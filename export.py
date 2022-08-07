import pandas as pd
from datetime import date

class Export:
    
    '''
    This class is intended to convert python DataFrame which contains all
    employee's data to .csv (Comma Separated Value) or .xlsx (Excel) format\n
    
    list of parameters to be provided to create object:\n
    + listname          : list of str (alphabet)\n
    + listid            : list of str (numerical)\n
    + listNIK           : list of str (numerical)\n
    + listgender        : list of str (alphabet)\n
    + listemail         : list of str\n
    + listbirth         : list of object\n
    + listage           : list of int\n
    + listdepartment    : list of str (alphabet)\n
    + listaddress       : list of str (alphabet and numerical)\n
    + listposition      : list of str (alphabet)\n
    + listactiveness    : list of str (alphabet)\n
    + liststartingDay   : list of object\n
    + listworkingYears  : list of int\n

    Each element of list with the same index should has correlation\n
    (Ex: listname[1] correlated with listid[1], listNIK[1], ...)\n

    Instance method:\n
    + export_csv\n
    + export_excel 
    '''

    def __init__(self,listname, listid, listNIK, listgender, listemail, listbirth, listage, 
                 listdepartment, listaddress, listposition, listactiveness, 
                 liststartingDay, listworkingYears):

        self.__listname = listname
        self.__listid = listid
        self.__listNIK = listNIK
        self.__listgender = listgender
        self.__listemail = listemail
        self.__listbirth = listbirth
        self.__listage = listage
        self.__listdepartment = listdepartment
        self.__listaddress = listaddress
        self.__listposition = listposition
        self.__listactiveness = listactiveness
        self.__liststartingDay = liststartingDay
        self.__listworkingYears = listworkingYears

        self.__dataframe = self.__createDataFrame()


    def __createDataFrame(self):
        
        data_employee = {
            'Name': self.__listname,
            'ID': self.__listid,
            'NIK': self.__listNIK,
            'Gender': self.__listgender,
            'Email': self.__listemail,
            'Birth': self.__listbirth,
            'Age': self.__listage,
            'Department': self.__listdepartment,
            'Address': self.__listaddress,
            'Position': self.__listposition,
            'Activeness': self.__listactiveness,
            'Starting Day': self.__liststartingDay,
            'Working Years': self.__listworkingYears
        }
        
        df = pd.DataFrame(data_employee)
        
        return df


    def export_csv(self):
        
        '''
        Useable Method\n
        Automatically convert the python file to CSV format.
        There's no argument that taken from the user.
        No return value
        '''
        
        self.__dataframe.to_csv(f'Employees data ({date.today()}).csv')
    

    def export_excel(self):
        
        '''
        Useable Method\n
        Automatically convert the python file to Excel format.
        There's no argument that taken from the user.
        No return value
        '''
        
        self.__dataframe.to_excel(f'Employees data ({date.today()}).xlsx')