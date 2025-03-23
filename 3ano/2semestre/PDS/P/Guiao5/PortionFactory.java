public class PortionFactory {
    public static Portion create(String state, Temperature temp){
        if(state.equalsIgnoreCase("Beverage") && temp.equals(Temperature.WARM))
            return new Milk();
        if(state.equalsIgnoreCase("Beverage") && temp.equals(Temperature.COLD))
            return new FruiteJuice();
        if(state.equalsIgnoreCase("Meat") && temp.equals(Temperature.COLD))
            return new Tuna();
        if(state.equalsIgnoreCase("Meat") && temp.equals(Temperature.WARM))
            return new Pork();
        else
            throw new IllegalArgumentException("Porção não existente!");
    }
}
