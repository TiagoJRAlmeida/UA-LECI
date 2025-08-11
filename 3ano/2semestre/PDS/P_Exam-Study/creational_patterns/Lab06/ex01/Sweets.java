import java.util.Vector;

class Employee { 
    private String name; 
    private long emp_num; 
    private double salary; 
    
    public Employee(String name, long emp_num, double salary) { 
        this.name = name; 
        this.emp_num = emp_num; 
        this.salary = salary; 
    } 
    public String getName() { 
        return name; 
    } 
    public long getEmpNum() { 
        return emp_num; 
    } 
    public double getSalary() { 
        return salary; 
    }
    
    public String toString(){
        return String.format("Employee %s --> Number: %d; Salary: %.2f", this.name, this.emp_num, this.salary);
    }
} 
    
class Database {  // Data elements 
    private Vector<Employee> employees; // Stores the employees 

    public Database() { 
        employees = new Vector<>(); 
    }

    public boolean addEmployee(Employee employee) { 
        // Code to add employee
        if (!employees.contains(employee)){
            employees.add(employee);
            return true;
        } 
        else {
            return false;
        }
    }

    public void deleteEmployee(long emp_num) { 
        // Code to delete employee
        for (Employee emp : employees){
            if (emp.getEmpNum() == emp_num){
                employees.remove(emp);
            }
        } 
    }

    public Employee[] getAllEmployees() { 
        // Code to retrieve collection 
        Employee[] employeesArray = new Employee[employees.size()];
        int index = 0;
        for (Employee emp : employees){
            employeesArray[index] = emp;
            index++;
        }
        return employeesArray;
    } 
}