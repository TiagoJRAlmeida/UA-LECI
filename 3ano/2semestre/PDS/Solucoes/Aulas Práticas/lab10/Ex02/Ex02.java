package lab10.Ex02;

public class Ex02 {
    public static void main(String[] args) {

		Employee emp = EmployeeFactory.getEmployee("Mac");
		Employee emp2 = EmployeeFactory.getEmployee("Janela");
		Employee emp3 = EmployeeFactory.getEmployee("Linux");
		Employee emp4 = EmployeeFactory.getEmployee("Mack");

		System.out.println(emp.getName());
		System.out.println(emp2.getName());
		System.out.println(emp3.getName());
		System.out.println(emp4.getName());
	}
}
