
# Human Resource Information System (HRIS)

Python Object-oriented programming based project to manage employee data in an organization. This is not a form of API and the data is not stored in a database.


## Features

- Store employee's basic information
- Calculate employee's salary based on department and position
- Relocate employee from one department to another department
- Promote/demote employee from their initial position
- Export all employees information in the form of Excel/CSV
- Accessibility based on user metrics (administrator / employee)


## Run Locally

Clone the project

```bash
  git clone https://github.com/Ricsen12345/Simple-Human-Resource-Information-System-HRIS-.git
```

Go to the project directory

```bash
  cd Simple-Human-Resource-Information-System-HRIS-
```

Install dependencies

```bash
  pip install -r requirement.txt
```

Run the program

```bash
  python main.py
```


## Acknowledgements

Special thanks to [Mr.Iksan Bukhori](https://github.com/iksanb) as a lecturer in Object-Oriented Programming subject at President University who has taught and helped the authors in developing this project.


## Authors

- [@ricsen12345](https://github.com/Ricsen12345)
- [Muhammad Raihan Arrasyid](https://www.linkedin.com/in/muhammad-raihan-arrasyid-1b4005180/)
- [Tony Hendra Wijaya](https://www.linkedin.com/in/tony-hendra-wijaya-376252215/)


## Appendix A - Department ID

Department   | ID
------------ | -------------
HRD          | 001
Accounting   | 002
Production   | 003
Data Analyst | 004
Marketing    | 005
Purchasing   | 006
Maintenance  | 007


## Appendix B - Maximum Salary Default

Department   | Maximum Salary
------------ | ----------------
HRD          | IDR 17,500,000
Accounting   | IDR 19,000,000
Production   | IDR 21,000,000
Data Analyst | IDR 25,000,000
Marketing    | IDR 15,000,000
Purchasing   | IDR 16,500,000
Maintenance  | IDR 20,000,000


## Appendix C - Salary Percentage Default

Position        | Percentage
--------------- | -------------
Staff           | 40%
Executive       | 60%
Section Head    | 80%
Department Head | 100%
