package lab07.Ex01;

import java.util.Date;

public class Employee implements EmployeeInterface {
    private String name;
    private Date startDate;
    private Date endDate;

    public Employee(String name) {
        this.name = name;
    }

    public String getName() {
        return this.name;
    }

    @Override
    public void start(Date date) {
        this.startDate = date;
        System.out.println(this.name + ": I'm starting on " + this.startDate.toString());
    }

    @Override
    public void terminate(Date date) {
        this.endDate = date;
        System.out.println(this.name + ": I'm terminating on " + this.endDate.toString());
    }

    @Override
    public void work() {
        System.out.println(this.name + " is working");
    }
    
}
