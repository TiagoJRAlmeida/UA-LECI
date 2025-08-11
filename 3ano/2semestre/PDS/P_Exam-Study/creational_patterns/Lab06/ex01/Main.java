public class Main {
    public static void main(String[] args){
        // Test Sweets factory
        Employee e1 = new Employee("John", 10000, 1000.0);
        Employee e2 = new Employee("James", 10001, 2000.0);
        Employee e3 = new Employee("Peter", 10002, 3000.0);

        Database SweetsDb = new Database();
        
        SweetsDb.addEmployee(e1);
        SweetsDb.addEmployee(e2);
        SweetsDb.addEmployee(e3);
        
        System.out.println("All current employees in Sweets inc.:");
        for (Employee emp : SweetsDb.getAllEmployees()){
            System.out.println(emp);
        }

        System.out.println("\nDeleting James...");
        SweetsDb.deleteEmployee(10001);

        System.out.println("\nAll current employees in Sweets inc.:");
        for (Employee emp : SweetsDb.getAllEmployees()){
            System.out.println(emp);
        }


        /////////////////////////////////////////////////
        // Test Petiscos factory
        Empregado emp1 = new Empregado("Carlos", "Silva", 10, 1100); 
        Empregado emp2 = new Empregado("Diana", "Costa", 11, 1150);
        
        Registos PetiscosReg = new Registos();

        PetiscosReg.insere(emp1);
        PetiscosReg.insere(emp2);

        System.out.println("\n\nAll current employees in Petiscos inc.:");
        for (Empregado e : PetiscosReg.listaDeEmpregados()) {
            System.out.println(e);
        }
        
        System.out.println("\nDeleting Carlos...");
        PetiscosReg.remove(10);

        System.out.println("\nAll current employees in Petiscos inc.:");
        for (Empregado e : PetiscosReg.listaDeEmpregados()) {
            System.out.println(e);
        }
    }
}
