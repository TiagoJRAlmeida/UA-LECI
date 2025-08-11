public class CakeMaster {
    protected CakeBuilder cakeBuilder;
    protected Cake newCake;

    public void setCakeBuilder(CakeBuilder cb){
        this.cakeBuilder = cb;
    } 

    public void createCake(String Message){
        cakeBuilder.createCake();
        cakeBuilder.addCakeLayer();
        cakeBuilder.addCreamLayer();
        cakeBuilder.addTopLayer(); 
        cakeBuilder.addTopping(); 
        cakeBuilder.addMessage(Message); 
    }

    public void createCake(int numLayers, String Message){
        cakeBuilder.createCake();
        cakeBuilder.addCakeLayer();
        cakeBuilder.addCreamLayer();
        cakeBuilder.addTopLayer(); 
        cakeBuilder.addTopping(); 
        cakeBuilder.addMessage(Message); 
    }

    public void createCake(Shape shape, int numLayers, String Message){
        cakeBuilder.createCake();
        cakeBuilder.addCakeLayer();
        cakeBuilder.addCreamLayer();
        cakeBuilder.addTopLayer(); 
        cakeBuilder.addTopping(); 
        cakeBuilder.addMessage(Message); 
    }

    public Cake getCake(){
        return cakeBuilder.getCake();
    } 
}