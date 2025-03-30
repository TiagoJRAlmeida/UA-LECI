package lab10.Ex02;

public class Programmer extends Employee {
    public Programmer(String name) {
		this.name = name;
	}

	@Override
	public String getName() {
		return name;
	}
}
