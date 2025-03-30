package lab08.Ex02;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Company {

	public static User user;
	private List<Employee> emps = new ArrayList<>();
	private Insurance insurance = new Insurance();
	private SocialSecurity socialSecurity = new SocialSecurity();
	private Parking parking = new Parking();

	public void admitEmployee(Person person, double salary) {
		Employee e = new Employee(person, salary);
		emps.add(e);
		socialSecurity.regist(e);
		insurance.regist(e);
		EmployeeCard c = new EmployeeCard(e);
		e.giveCard(c);
		if (salary > this.averageSalary()) {
			parking.allow(e);
		}
	}

	//getters
	public Insurance getInsurance() {
		return insurance;
	}

	public SocialSecurity getSocialSecurity() {
		return socialSecurity;
	}

	public Parking getParking() {
		return parking;
	}
	
	public void paySalaries(int month) {
		for (Employee e : emps) {
			e.paySalary(e.getSalary());
		}
	}
	
	public List<Employee> employees() {
		return Collections.unmodifiableList(emps);
	}

	public double averageSalary() {
		double sum = 0;
		for (Employee e : emps) {
			sum += e.getSalary();
		}
		return sum / emps.size();
	}
}