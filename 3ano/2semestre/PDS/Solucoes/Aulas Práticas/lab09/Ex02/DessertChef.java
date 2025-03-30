package lab09.Ex02;

public class DessertChef extends Chef {

    @Override
    public Handler setNext(Handler next) {
        this.next = next;
        return this;
    }

    @Override
    public void handle(String request) {
        if (request.toLowerCase().contains("dessert")) {
            this.cook(request);
        }
        else {
            System.out.println(getClass().getSimpleName() + ": I can't cook that.");
            super.handle(request);
        }
    }
}
