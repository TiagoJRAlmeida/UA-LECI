package lab05.Ex01;

public class Pork extends PortionFactory {
    // Construtor
    protected Pork() {
        super();
        this.setTemperature(Temperature.WARM);
        this.setState(State.Solid);
    }

    @Override
    // Método toString
    public String toString() {
        return "Pork: " + "Temperature " + this.getTemperature() + ", State " + this.getState() ;
    }
}
