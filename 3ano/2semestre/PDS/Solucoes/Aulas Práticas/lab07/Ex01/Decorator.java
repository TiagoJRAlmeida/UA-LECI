package lab07.Ex01;

import java.util.Date;

public class Decorator implements EmployeeInterface {
    private EmployeeInterface employee;

    public Decorator(EmployeeInterface employee) {
        this.employee = employee;
    }

    @Override
    public void start(Date date) {
        this.employee.start(date);
    }

    @Override
    public void terminate(Date date) {
        this.employee.terminate(date);
    }

    @Override
    public void work() {
        this.employee.work();
    }

    @Override
    public String getName() {
        return this.employee.getName();
    }
}
