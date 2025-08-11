import java.util.List;

public class SharkCompany2 {
	public static void main(String[] args) {
        Person[] persons = {
            new Person("Maria Silva"),
            new Person("Manuel Pereira"),
            new Person("Aurora Machado"),
            new Person("Augusto Lima")
        };

        CompanyFacade shark = new CompanyFacade(new Company());
        Company.user = User.COMPANY;

        shark.admitEmployee(persons[0], 1000);
        System.out.println("");
        shark.admitEmployee(persons[1], 900);
        System.out.println("");
        shark.admitEmployee(persons[2], 1200);
        System.out.println("");
        shark.admitEmployee(persons[3], 1100);
        System.out.println("");

        List<Employee> emps = shark.employees();
        for (Employee e : emps) {
            System.out.println(e.getSalary());
        }

        shark.paySalaries(1);
    }
}