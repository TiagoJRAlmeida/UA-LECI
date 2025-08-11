class Person {
	private String name;
	private BankAccount bankAccount;

	public Person(String n) {
		name = n;
		BankAccount realBankAccount = new BankAccountImpl("PeDeMeia", 0);
		bankAccount = new BankAccountProxy(realBankAccount);
	}

	public String getName() {
		return name;
	}
	
	public BankAccount getBankAccount() {
		return bankAccount;
	}
}