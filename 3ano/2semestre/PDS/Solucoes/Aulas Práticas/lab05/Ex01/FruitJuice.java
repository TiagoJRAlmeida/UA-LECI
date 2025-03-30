package lab05.Ex01;

public class FruitJuice extends PortionFactory {
    // Atributos
    private String sabor;

    // Construtor
    protected FruitJuice(String sabor) {
        super();
        this.setTemperature(Temperature.COLD);
        this.setState(State.Liquid);
        this.sabor = sabor;
    }

    @Override
    // Método toString
    public String toString() {
        return "FruitJuice: " + this.sabor + ", Temperature " + this.getTemperature() + ", State " + this.getState();
    }
}
