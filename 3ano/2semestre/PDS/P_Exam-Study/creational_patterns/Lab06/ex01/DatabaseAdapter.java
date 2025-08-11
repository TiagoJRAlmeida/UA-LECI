public class DatabaseAdapter implements PstAdapter{
    private Database employees;

    public DatabaseAdapter(Database db){
        this.employees = db;
    }

    public void addEmployee(Object e){
        if (e instanceof Employee) { 
            employees.addEmployee((Employee)e); 
        }        
    }

    public void removeEmployee(long code){
        employees.deleteEmployee(code);
    }

    public boolean isEmployee(long code){
        for(Employee e : employees.getAllEmployees()){
            if (e.getEmpNum() == code){
                return true;
            }
        }
        return false;
    }

    public void showEmployees(){
        for(Employee e : employees.getAllEmployees()){
            System.out.println(e);
        }
    }    
}
