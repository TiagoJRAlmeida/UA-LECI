interface CakeBuilder { 
    public void setCakeShape(Shape shape); 
    public void addCakeLayer(); 
    public void addCreamLayer(); 
    public void addTopLayer(); 
    public void addTopping(); 
    public void addMessage(String m); 
    public void createCake(); 
    public Cake getCake(); 
}


class ChocolateCakeBuilder implements CakeBuilder {
    protected Cake chocolateCake = new Cake();

    public void setCakeShape(Shape shape){} 

    public void addCakeLayer(){
        chocolateCake.setCakeLayer("Soft chocolate");
    } 

    public void addCreamLayer(){} 
    
    public void addTopLayer(){
        chocolateCake.setTopLayerCream(Cream.Whipped_Cream);
    } 

    public void addTopping(){
        chocolateCake.setTopping(Topping.Fruit);
    } 
    
    public void addMessage(String m){
        chocolateCake.setMessage(m);
    } 

    public void createCake(){
        chocolateCake = new Cake();
        // chocolateCake.setCakeLayer("Soft chocolate");
        // addTopLayer();
        // addTopping();
        // addMessage("Congratulations");
    }

    public Cake getCake(){
        return chocolateCake;
    } 
}


class SpongeCakeBuilder implements CakeBuilder {
    protected Cake SpongeCake;

    public void setCakeShape(Shape shape){} 

    public void addCakeLayer(){
        SpongeCake.setCakeLayer("Sponge");
        SpongeCake.setNumCakeLayers(2);
    } 

    public void addCreamLayer(){
        SpongeCake.setMidLayerCream(Cream.Red_Berries);
    } 
    
    public void addTopLayer(){
        SpongeCake.setTopLayerCream(Cream.Whipped_Cream);
    } 

    public void addTopping(){
        SpongeCake.setTopping(Topping.Fruit);
    } 
    
    public void addMessage(String m){
        SpongeCake.setMessage(m);
    } 

    public void createCake(){
        SpongeCake = new Cake();
        // SpongeCake.setCakeLayer("Sponge");
        // addCakeLayer();
        // addCreamLayer();
        // addTopLayer();
        // addTopping();
        // addMessage("Well done");
    }

    public Cake getCake(){
        return SpongeCake;
    } 
}


class YogurtCakeBuilder implements CakeBuilder {
    protected Cake YogurtCake;
    
    public void setCakeShape(Shape shape){} 

    public void addCakeLayer(){
        YogurtCake.setCakeLayer("Yogurt");
        YogurtCake.setNumCakeLayers(3);
    } 

    public void addCreamLayer(){
        YogurtCake.setMidLayerCream(Cream.Vanilla);
    } 
    
    public void addTopLayer(){
        YogurtCake.setTopLayerCream(Cream.Red_Berries);
    } 

    public void addTopping(){
        YogurtCake.setTopping(Topping.Chocolate);
    } 
    
    public void addMessage(String m){
        YogurtCake.setMessage(m);
    } 

    public void createCake(){
        YogurtCake = new Cake();
    }

    public Cake getCake(){
        return YogurtCake;
    } 
}