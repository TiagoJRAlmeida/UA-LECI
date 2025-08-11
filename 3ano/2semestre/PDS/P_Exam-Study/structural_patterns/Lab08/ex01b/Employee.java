class Employee {
	private double salary;
	private BankAccount bankAccount;

	public Employee(Person person, double s) {
		this.salary = s;
		BankAccount real = new BankAccountImpl("PeDeMeia", 0);
        this.bankAccount = new BankAccountProxy(real);  // proteger acesso
	}

	public void paySalary() {
        bankAccount.deposit(salary);
    }

	public void spend(double amount) {
        Company.user = User.OWNER;  // simula o dono a gastar
        bankAccount.withdraw(amount);
    }

	public double getSalary() {
		return salary;
	}
}