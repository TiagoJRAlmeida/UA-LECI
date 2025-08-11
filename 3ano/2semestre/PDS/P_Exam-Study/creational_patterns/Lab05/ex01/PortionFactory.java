public class PortionFactory {
    
    public static Portion create(String type, Temperature temp){
        if(type.equals("Beverage") && temp == Temperature.COLD){
            return new FruitJuice();
        }

        if(type.equals("Beverage") && temp == Temperature.WARM){
            return new Milk();
        }

        if(type.equals("Meat") && temp == Temperature.COLD){
            return new Tuna();
        }

        if(type.equals("Meat") && temp == Temperature.WARM){
            return new Pork();
        }

        return null;
    }
}
