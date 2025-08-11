enum Shape { Circle, Square, Rectangle }
enum Cream { Whipped_Cream, Red_Berries, Vanilla }
enum Topping { Fruit, Chocolate }

public class Cake {
    private Shape shape = Shape.Circle; 
    private String cakeLayer; 
    private int numCakeLayers = 1; 
    private Cream midLayerCream; 
    private Cream topLayerCream; 
    private Topping topping; 
    private String message;

    public void setShape(Shape shape) {
        this.shape = shape;
    }

    public void setCakeLayer(String cakeLayer) {
        this.cakeLayer = cakeLayer;
    }

    public void setNumCakeLayers(int numCakeLayers) {
        this.numCakeLayers = numCakeLayers;
    }

    public void setMidLayerCream(Cream midLayerCream) {
        this.midLayerCream = midLayerCream;
    }

    public void setTopLayerCream(Cream topLayerCream) {
        this.topLayerCream = topLayerCream;
    }

    public void setTopping(Topping topping) {
        this.topping = topping;
    }

    public void setMessage(String message) {
        this.message = message;
    } 

    public int getNumCakeLayers() {
        return numCakeLayers;
    }

    public String toString(){
        StringBuilder cakeInfo = new StringBuilder();
        cakeInfo.append(this.cakeLayer + " cake ");
        cakeInfo.append(String.format("with %d layers", this.numCakeLayers));
        if (this.midLayerCream != null){
            cakeInfo.append(" and ").append(this.midLayerCream).append(" cream");
        } 
        cakeInfo.append(", topped with ");
        if (this.topLayerCream != null){
            cakeInfo.append(this.topLayerCream).append(" cream and ");
        }
        cakeInfo.append(this.topping);
        cakeInfo.append(". Message says: \"" + this.message + "\".");
        return cakeInfo.toString();
    }
}
