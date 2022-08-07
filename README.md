Simple Human Resource Information System HRIS
=============================================

<p>
  This project aims to keep track of employees data within a company. This project is an Object-Oriented program made in Python. This project doesn't have any connection to database and doesn't have any UI design. This project also consists of lots of exception handling, so you'll hardly find any error when running the program.
</p>
**Contributors**: Ricsen, Muh. Raihan Arrasyid, Tony Hendra Wijaya.


<br/>
<h2>Stored Information</h2>
<p>
  HRIS in this program is created to store information about each employee who works in the company. Some information is entered by the employees themselves, such as their name, NIK or ID number, gender, account password, department, main address, place of birth, and date of birth. Other information is generated automatically by the system, such as employee ID, company email, age, position, status of the employee (active/inactive), starting day, total years of working at the company, and monthly salary.
</p>
<p>  
  Employee ID consists of 12 digits and cannot be changed unless the employee is transferred to another department. The first 3 digits represent the department ID (appendix A), the next 4 digits represent the year the employee entered the company, and the last 5 digits represent the number of employees in the company at the time the employee entered the company.
</p>
<p>
  The employee's age is calculated automatically by the system using information regarding the current date and date of birth of the employee. The position of the employee when entering the company is staff by default. The status of the employee when entering the company is active by default. The employee's monthly salary is calculated according their department and position in the company using the following equation:
</p>
<h5>
  S=%S*clsmax_S
</h5>
<p>
  where S is the employee’s monthly salary, %S is the salary percentage based on employee’s position (appendix B), clsmax_S is the maximum salary based on the employee's department (appendix C).
</p>


<br/>
<h2>Employee's Accessibility</h2>
<p>
  Employees can access other employee’s profile to some extent (read only). Displayed information are name, employee id, email address, department, position, and status of the employee. Employees can also log into their account by validating it using the password they have created at the time of account creation. Once logged in, employees can view their detailed information and manipulate their own information. Information that can be changed is only name, NIK, birth, gender, address and password.
</p>


<br/>
<h2>System Administrator's Accessibility</h2>
<p>
  The system administrator is prompted to create a password for the system when the program is just starting. System administrator can promote employees to higher positions, demote employees to lower positions, move employees to other departments, update employee data, export all data to csv (comma separated values) or xlsx (Excel) files, set salary percentage based on employee’s position and maximum salary based on the employee's department. Updating employee data means recalculate employee’s age and total years of working at the company. These features can only be used by the system administrator after he/she has entered the correct system password. System administrator can also stop this program by entering the correct password.
</p>


<br/>
<h2>Class Diagram and Its Description</h2>

![HRIS Class Diagram](https://user-images.githubusercontent.com/105400052/183294528-660bcbdf-2945-4e40-b22d-2db7d60a13ae.png)

<p>
  Employee class is the class that plays the biggest role in this program. This is the class that stores employee’s information and most of the main features of the program are located in this class. Employee class is associated with other classes such as Setter class, Creator class, Date class, and Department class. Setter class is used to set employee information when the employee him/herself logs into his/her account. Creator class is used to connect Employee class and Setter class to Birth class and Address class.
</p>
<p>
  Date class is used to neatly store information about starting day and birth date which consist of information about the day, month, and year. Date class also acts as a “parent” of Birth class. Address class is used to neatly store information about main address which consist of information about the street, city, state, and country. Department class is used to store information about the employee's department, department ID (Appendix A), and the maximum salary of each department (Appendix C). Employees can be transferred to another department using one of the methods in the Department class. Export class is used to convert data previously stored in pandas dataframe to csv or xlsx file.
</p>

<br/>
<h2>Further Details</h2>
<p>
  It's available in every python file in this repository, so if you want to know more about these classes, it's better to take a look at them than this readme file because this file is only meant as an introduction to the system. If you want to know what it looks like at run time, you might want to copy (clone) it to your device and run it using your interpreter. Type this command in your terminal:
<h5>git clone 
