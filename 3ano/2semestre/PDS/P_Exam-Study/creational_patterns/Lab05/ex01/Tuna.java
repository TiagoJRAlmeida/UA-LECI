public class Tuna implements Portion{
    public Temperature getTemperature(){
        return Temperature.COLD;
    } 

    public State getState(){
        return State.Solid;
    }

    public String toString(){
        return "Tuna: Temperature COLD, State Solid";
    }
}
