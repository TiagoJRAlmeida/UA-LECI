abstract class Container {
    protected Portion p;

    public Container(Portion portion){
        this.p = portion;
    }

    public static Container create(Portion p){
        State state = p.getState();
        Temperature temp = p.getTemperature();

        if(state == State.Liquid){
            if(temp == Temperature.COLD) { return new PlasticBottle(p); }
            else { return new TermicBottle(p); }
        }
        else{
            if(temp == Temperature.COLD) { return new PlasticBag(p); }
            else { return new Tupperware(p); }
        }
    }

    public abstract String toString();
}
