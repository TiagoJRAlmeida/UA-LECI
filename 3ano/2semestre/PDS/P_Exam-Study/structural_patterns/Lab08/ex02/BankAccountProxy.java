public class BankAccountProxy implements BankAccount {
    private BankAccount bankAccount;
    private User user;  
    
    public BankAccountProxy(BankAccount bankAccount){
        this.bankAccount = bankAccount;
    }
    public void deposit(double amount){
        bankAccount.deposit(amount);
    }
	
    public boolean withdraw(double amount){
        if(user == User.OWNER) { 
            return bankAccount.withdraw(amount); 
        }
        else { 
            System.err.println("ERRO: Não tens acesso a esta conta!!!");
            return false;
        }
    }
	
    public double balance(){
        return bankAccount.balance();
    }
}
