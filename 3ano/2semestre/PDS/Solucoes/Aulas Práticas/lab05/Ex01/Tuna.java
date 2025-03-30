package lab05.Ex01;

public class Tuna extends PortionFactory {
    // Construtor
    protected Tuna() {
        super();
        this.setTemperature(Temperature.COLD);
        this.setState(State.Solid);
    }

    @Override
    // Método toString
    public String toString() {
        return "Tuna: " + "Temperature " + this.getTemperature() + ", State " + this.getState() ;
    }
}
