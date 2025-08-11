public class MainPst {
    public static void main(String[] args) {
        // Sweets
        Database db = new Database();
        PstAdapter sweets = new DatabaseAdapter(db);
        sweets.addEmployee(new Employee("Ana", 101, 2000));
        sweets.addEmployee(new Employee("Bruno", 102, 2100));

        // Petiscos
        Registos reg = new Registos();
        PstAdapter petiscos = new RegistosAdapter(reg);
        petiscos.addEmployee(new Empregado("Clara", "Silva", 201, 1800));
        petiscos.addEmployee(new Empregado("Duarte", "Oliveira", 202, 1900));

        // Testes
        sweets.showEmployees();
        petiscos.showEmployees();

        System.out.println("Bruno existe? " + sweets.isEmployee(102));
        System.out.println("Clara existe? " + petiscos.isEmployee(201));

        sweets.removeEmployee(101);
        petiscos.removeEmployee(202);

        System.out.println("Após remoção:");
        sweets.showEmployees();
        petiscos.showEmployees();
    }
}
