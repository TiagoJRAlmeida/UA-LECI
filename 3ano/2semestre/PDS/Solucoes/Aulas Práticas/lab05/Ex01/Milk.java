package lab05.Ex01;

public class Milk extends PortionFactory {
    // Construtor
    protected Milk() {
        super();
        this.setTemperature(Temperature.WARM);
        this.setState(State.Liquid);
    }

    // Método toString
    @Override
    public String toString() {
        return "Milk: " + "Temperature " + this.getTemperature() + ", State " + this.getState() ;
    }
    

}
