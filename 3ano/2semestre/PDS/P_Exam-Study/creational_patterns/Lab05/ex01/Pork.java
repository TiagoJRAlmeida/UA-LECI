public class Pork implements Portion{
    public Temperature getTemperature(){
        return Temperature.WARM;
    } 

    public State getState(){
        return State.Solid;
    }

    public String toString(){
        return "Pork: Temperature WARM, State Solid";
    }
}
