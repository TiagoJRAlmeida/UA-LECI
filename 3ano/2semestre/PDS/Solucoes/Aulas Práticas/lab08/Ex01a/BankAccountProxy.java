package lab08.Ex01a;

public class BankAccountProxy implements BankAccount {
    private BankAccountImpl realBank;

    public BankAccountProxy(String bank, double initialDeposit) {
        this.realBank = new BankAccountImpl(bank, initialDeposit);
    }

    public boolean checkAccess() {
        if (Company.user == User.OWNER) {
            return true;
        } else {
            System.out.println("Utilizador não autorizado!");
            return false;
        }
    }

    @Override
	public void deposit(double amount) {
		this.realBank.deposit(amount);
	}

    @Override
	public boolean withdraw(double amount) {
		if (checkAccess()) {
            return this.realBank.withdraw(amount);
        }
		return false;
	}

	@Override
	public double balance() {
		if (checkAccess()) {
            return this.realBank.balance();
        }
		return Double.NaN;
	}
}
