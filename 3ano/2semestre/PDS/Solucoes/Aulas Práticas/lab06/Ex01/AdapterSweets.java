package lab06.Ex01;

public class AdapterSweets implements Adapter {
    // Database
    private Database database;

    // Constructor
    public AdapterSweets(Database database) {
        this.database = database;
    }

    @Override
    // Adiciona um emplyee atrvés de um empregado
    public void addEmpregado(Empregado empregado) {
        Employee emp = new Employee(empregado.nome() + " " + empregado.apelido(), (long) empregado.codigo(), empregado.salario());

        database.addEmployee(emp);
    }

    @Override
    // Remove um employee atrvés de um código
    public void removeEmpregado(int codigo) {
        database.deleteEmployee(codigo);
    }

    @Override
    // Verifica se existe um employee com o código passado
    public boolean isEmpregado(int codigo) {
        return database.isEmployee(codigo);
    }

    @Override
    // Lista todos os employees
    public void listaEmpregados() {
        // Cria um array de employees
        Employee[] employees = database.getAllEmployees();

        // Percorre o array e imprime cada employee
        for (int i = 0; i < employees.length; i++) {
            System.out.println(employees[i]);
        }
    }
}
