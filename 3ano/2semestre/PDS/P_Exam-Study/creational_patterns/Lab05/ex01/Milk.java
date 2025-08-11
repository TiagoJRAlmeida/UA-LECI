public class Milk implements Portion { 
    public Temperature getTemperature(){
        return Temperature.WARM;
    } 

    public State getState(){
        return State.Liquid;
    }

    public String toString(){
        return "Milk: Temperature WARM, State Liquid";
    }
}
