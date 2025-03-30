package lab10.Ex03;

public class Jet implements Aircraft {
    private AirTrafficControlMediator mediator;
    private String name;

    public Jet(AirTrafficControlMediator mediator, String name) {
        this.mediator = mediator;
        this.name = name;
    }

    public String getName() {
        return name;
    }

    @Override
    public void send(String message) {
        mediator.sendMessage(message, this);
    }

    @Override
    public void receive(String message) {
        System.out.println(this.getName() + " received: " + message);
    }
}
