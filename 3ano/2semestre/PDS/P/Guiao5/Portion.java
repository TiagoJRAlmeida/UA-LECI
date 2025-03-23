public interface Portion { 
    public Temperature getTemperature(); 
    public State getState(); 
}


class Milk implements Portion {
    public Temperature getTemperature(){ return Temperature.WARM; }
    public State getState(){ return State.Liquid; }
    public String toString() { return "Milk: Temperature WARM, State Liquid"; }
}


class FruiteJuice implements Portion {
    String fruit;
    public FruiteJuice(String fruit){
        this.fruit = fruit;
    }

    public FruiteJuice(){
        this.fruit = "Orange";
    }

    public Temperature getTemperature(){ return Temperature.COLD; }
    public State getState(){ return State.Liquid; }
    public String getFruit() { return this.fruit; }
    public void setFruit(String newFruit) { this.fruit = newFruit; }
    public String toString() { return String.format("FruiteJuice: %s, Temperature COLD, State Liquid", this.getFruit()); }
}


class Tuna implements Portion {
    public Temperature getTemperature(){ return Temperature.COLD; }
    public State getState(){ return State.Solid; }
    public String toString() { return "Tuna: Temperature COLD, State Solid"; }
}


class Pork implements Portion {
    public Temperature getTemperature(){ return Temperature.WARM; }
    public State getState(){ return State.Solid; }
    public String toString() { return "Pork: Temperature WARM, State Solid"; }
}