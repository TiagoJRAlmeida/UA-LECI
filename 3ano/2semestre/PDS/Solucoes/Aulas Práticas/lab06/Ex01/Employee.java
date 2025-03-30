package lab06.Ex01;

public class Employee {
    // Atributes
    private String name;
    private long emp_num;
    private double salary;

    // Constructor
    public Employee(String name, long emp_num, double salary) {
        this.name = name;
        this.emp_num = emp_num;
        this.salary = salary;
    }

    // Getters e Setters
    public String getName() {
        return name;
    }

    public long getEmp_num() {
        return emp_num;
    }

    public double getSalary() {
        return salary;
    }

    @Override
    // Transforma o objeto em string
    public String toString() {
        return "Employee " + name + "(" + emp_num + ") " + salary + "€";
    }
}
