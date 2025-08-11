import java.util.List;

public class CompanyFacade{
    private Company company;

    public CompanyFacade(Company company){
        this.company = company;
    }

    public void admitEmployee(Person person , double salary) {
        SocialSecurity.regist(person);
        Insurance.regist(person);
        Parking.allow(person);
        company.admitEmployee(person, salary);
	}


    public void paySalaries(int month) {
        company.paySalaries(month);
    }

    public List<Employee> employees(){
        return company.employees();
    }
}
