package ex01;

public class demo {
    public static void main(String[] args) {
        Date now = new Date(11, 05, 2004);

        Worker emp = new Employee("Alice");
        emp = new TeamMember(emp);
        emp = new TeamLeader(emp);  // emp é agora TeamLeader e TeamMember
        emp = new Manager(emp);     // emp tem agora todas as responsabilidades

        emp.start(now);
        emp.work();
        emp.terminate(now);

        System.out.println("\n----------------------------------");

        Worker emp1 = new Employee("Lucas");
        emp1 = new TeamMember(emp1);
    
        emp1.start(now);
        emp1.work();
        emp1.terminate(now);
    }
    
}
