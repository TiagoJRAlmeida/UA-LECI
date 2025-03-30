package lab05.Ex03;

public class Person {
    // Atributos
    private final String name;

    // Construtor
    public Person(String name) {
        this.name = name;
    }

    // Getters
    public String getName() {
        return name;
    }

    @Override
    // Método toString
    public String toString() {
        return name;
    }
}
