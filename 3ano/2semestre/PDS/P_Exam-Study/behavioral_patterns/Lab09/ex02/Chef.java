public abstract class Chef {
    private Chef nextChef = null;
    
    public void parse(String mealName){
        if (nextChef != null){
            nextChef.parse(mealName);
        }
        else{
            System.err.println("We're sorry but that request can't be satisfied by our service!");
        }
    }

    public boolean canCook(String mealName){
        return mealName == null;
    }

    public void setNextChef(Chef chef){
        this.nextChef = chef;
    }
}

class SushiChef extends Chef {
    @Override
    public void parse(String mealName){
        if(canCook(mealName)){
            System.out.println("SushiChef: Starting to cook " + mealName + ". Out in 14 minutes!");
        }
        else{
            System.out.println("SushiChef: I can't cook that.");
            super.parse(mealName);
        }
    }

    @Override
    public boolean canCook(String mealName){
        return mealName.equals("sushi nigiri and sashimi");
    }
}

class PastaChef extends Chef {
    @Override
    public void parse(String mealName){
        if(canCook(mealName)){
            System.out.println("PastaChef: Starting to cook " + mealName + ". Out in 14 minutes!");
        }
        else{
            System.out.println("PastaChef: I can't cook that.");
            super.parse(mealName);
        }
    }

    @Override
    public boolean canCook(String mealName){
        return mealName.equals("Pasta Carbonara");
    }
}

class BurgerChef extends Chef {
    @Override
    public void parse(String mealName){
        if(canCook(mealName)){
            System.out.println("BurgerChef: Starting to cook " + mealName + ". Out in 19 minutes!");
        }
        else{
            System.out.println("BurgerChef: I can't cook that.");
            super.parse(mealName);
        }
    }

    @Override
    public boolean canCook(String mealName){
        return mealName.equals("veggie burger");
    }
}

class PizzaChef extends Chef {
    @Override
    public void parse(String mealName){
        if(canCook(mealName)){
            System.out.println("PizzaChef: Starting to cook" +  mealName + ". Out in 7 minutes!");
        }
        else{
            System.out.println("PizzaChef: I can't cook that.");
            super.parse(mealName);
        }
    }

    @Override
    public boolean canCook(String mealName){
        return mealName.equals("PLAIN pizza, no toppings!");
    }
}

class DessertChef extends Chef {
    @Override
    public void parse(String mealName){
        if(canCook(mealName)){
            System.out.println("DessertChef: Starting to cook " + mealName + ". Out in 17 \n" + //
                                "minutes! ");
        }
        else{
            System.out.println("DessertChef: I can't cook that.");
            super.parse(mealName);
        }
    }

    @Override
    public boolean canCook(String mealName){
        return mealName.equals("strawberry ice cream and waffles dessert");
    }
}
