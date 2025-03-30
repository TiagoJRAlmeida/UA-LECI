import java.util.Vector;

public class Database {  // Data elements 
    private Vector<Employee> employees; // Stores the employees 

    
    public Database() { 
        employees = new Vector<>(); 
    } 
    
    
    public boolean addEmployee(Employee employee) { 
        // Code to add employee
        if (employee == null || employees.contains(employee)) return false;
        employees.add(employee);
        return true;
    } 
    
    
    public void deleteEmployee(long emp_num) { 
        // Code to delete employee
        for(Employee employee : employees){
            if(employee.getEmpNum() == emp_num){
                employees.remove(employee);
                return;
            }
        } 
    } 
    
    
    public Employee[] getAllEmployees() { 
        // Code to retrieve collection
        return employees.toArray(new Employee[0]);
    } 
} 