package lab07.Ex01;

import java.util.Date;

public class Manager extends Decorator {

    public Manager(EmployeeInterface employee) {
        super(employee);
    }

    @Override
    public void start(Date date) {
        super.start(date);
    }

    @Override
    public void terminate(Date date) {
        super.terminate(date);
    }
    
    @Override
    public void work() {
        super.work();
    }

    public void manage() {
        System.out.println(super.getName() + " is managing");
    }

}
