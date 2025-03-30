package lab06.Ex01;

import java.util.Vector;

public class Database { // Data elements
    private Vector<Employee> employees; // Stores the employees

    public Database() { 
        employees = new Vector<Employee>();
    }

    public boolean addEmployee(Employee employee) {
        // Code to add employee
        if (!isEmployee(employee.getEmp_num())) {
            employees.add(employee);
            return true;
        }
        return false;
    }

    public void deleteEmployee(long emp_num) {
        // Code to delete employee
        for (int i=0; i<employees.size(); i++) {
            if (employees.get(i).getEmp_num() == emp_num) {
                employees.remove(i);
            }
        }
    }

    public boolean isEmployee(long emp_num) {
        // Code to find employee
        for (int i=0; i<employees.size(); i++) {
            if (employees.get(i).getEmp_num() == emp_num) {
                return true;
            }
        }
        return false;
    }

    public Employee[] getAllEmployees() {
        // Code to retrieve collection
        Employee[] employeesArray = new Employee[employees.size()];
        for (int i=0; i<employees.size(); i++) {
            employeesArray[i] = employees.get(i);
        }
        return employeesArray;
    }

    @Override
    public String toString() {
        return "Database: " + employees;
    }
}
