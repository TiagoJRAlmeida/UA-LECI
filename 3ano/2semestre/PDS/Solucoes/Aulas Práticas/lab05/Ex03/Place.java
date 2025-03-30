package lab05.Ex03;

public class Place {
    // Atributos
    private final String name;

    // Construtor
    public Place(String name) {
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
