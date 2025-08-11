public class FruitJuice implements Portion{
    public String fruitName = "Orange";

    public Temperature getTemperature(){
        return Temperature.COLD;
    } 

    public State getState(){
        return State.Liquid;
    }

    public String toString(){
        return "FruitJuice: " + fruitName + ", Temperature COLD, State Liquid";
    }
}
