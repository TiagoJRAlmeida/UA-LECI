package lab07.Ex01;

import java.util.Date;

public class TeamMember extends Decorator {

    public TeamMember(EmployeeInterface employee) {
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

    public void colaborate() {
        System.out.println(super.getName() + " is colaborating");
    }
}
