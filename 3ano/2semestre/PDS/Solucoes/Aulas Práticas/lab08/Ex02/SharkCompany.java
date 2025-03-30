package lab08.Ex02;

import java.util.List;

public class SharkCompany {
	public static void main(String[] args) {
		Person[] persons = { new Person("Maria Silva"),
					new Person("Manuel Pereira"),
					new Person("Aurora Machado"),
					new Person("Augusto Lima") };
		Company shark = new Company();
		Company.user = User.COMPANY;
		shark.admitEmployee(persons[0], 1000);
		shark.admitEmployee(persons[1], 900);
		shark.admitEmployee(persons[2], 1200);
		shark.admitEmployee(persons[3], 1100);
		List<Employee> sharkEmps = shark.employees();
		for (Employee e : sharkEmps)
			System.out.println(e.getSalary());
		shark.paySalaries(1);

		for (Person p : persons) {
			assert shark.getSocialSecurity().getAderentes().contains(p);
			assert shark.getInsurance().getAderentes().contains(p);
		}

		for (int i = 0; i < persons.length; i++) {
			assert persons[i].equals(sharkEmps.get(i).getCard().getEmployee());
		}
		
		System.out.println("\nSalário médio: " + shark.averageSalary());
		System.out.println("Permitido: " + shark.getParking().getPermitidos().contains(persons[0]) + "\tSalário: " + sharkEmps.get(0).getSalary());
		System.out.println("Permitido: " + shark.getParking().getPermitidos().contains(persons[1]) + "\tSalário: " + sharkEmps.get(1).getSalary());
		System.out.println("Permitido: " + shark.getParking().getPermitidos().contains(persons[2]) + "\t\tSalário: " + sharkEmps.get(2).getSalary());
		System.out.println("Permitido: " + shark.getParking().getPermitidos().contains(persons[3]) + "\t\tSalário: " + sharkEmps.get(3).getSalary());
	}
}
