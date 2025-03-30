package lab09.Ex02;

public class PizzaChef extends Chef{

    @Override
    public Handler setNext(Handler next) {
        this.next = next;
        return this;
    }

    @Override
    public void handle(String request) {
        if (request.toLowerCase().contains("pizza")) {
            this.cook(request);
        }
        else {
            System.out.println(getClass().getSimpleName() + ": I can't cook that.");
            super.handle(request);
        }
    }
}
