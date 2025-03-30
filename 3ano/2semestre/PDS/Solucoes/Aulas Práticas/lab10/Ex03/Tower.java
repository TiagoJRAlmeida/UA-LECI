package lab10.Ex03;

public class Tower implements AirTrafficControlMediator {
    private Aircraft aircraft;

    public void setAircraft(Aircraft aircraft) {
        this.aircraft = aircraft;
    }

    @Override
    public void sendMessage(String message, Aircraft aircraft) {
        if (this.aircraft != aircraft) {
            this.aircraft.receive(message);
        }
    }
}
