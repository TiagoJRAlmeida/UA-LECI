package lab05.Ex02;

public class Cake {
    // Atributos
    private Shape shape = Shape.Circle; // default shape
    private String cakeLayer;
    private int numCakeLayers = 1;
    private Cream midLayerCream = Cream.NULL;
    private Cream topLayerCream = Cream.NULL;
    private Topping topping = Topping.NULL;
    private String message = "";

    // Construtor
    public Cake(String cakeLayer) {
        this.cakeLayer = cakeLayer;
    }

    // Getters e Setters
    public void addLayer() {
        this.numCakeLayers++;
    }

    public void setTopping(Topping topping) {
        this.topping = topping;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public void setCakeLayer(String cakeLayer) {
        this.cakeLayer = cakeLayer;
    }

    public void setShape(Shape shape) {
        this.shape = shape;
    }

    public void setMidLayerCream(Cream midLayerCream) {
        this.midLayerCream = midLayerCream;
    }

    public void setTopLayerCream(Cream topLayerCream) {
        this.topLayerCream = topLayerCream;
    }

    @Override
    // Método toString
    public String toString() {
        if (numCakeLayers == 1 || this.midLayerCream == Cream.NULL)
            if (this.topping == Topping.NULL)
                return this.cakeLayer + " cake with " + this.numCakeLayers + " layers, topped with " + this.topLayerCream
                        + " cream. Message says: \"" + this.message + "\".";
            else
                return this.cakeLayer + " cake with " + this.numCakeLayers + " layers, topped with " + this.topLayerCream
                        + " cream and " + this.topping + ". Message says: \"" + this.message + "\".";
        
        if (this.topping == Topping.NULL)
            return this.cakeLayer + " cake with " + this.numCakeLayers + " layers and " + this.midLayerCream
                    + " cream, topped with "
                    + this.topLayerCream + " cream. Message says: \"" + this.message + "\".";
        else
            return this.cakeLayer + " cake with " + this.numCakeLayers + " layers and " + this.midLayerCream
                    + " cream, topped with "
                    + this.topLayerCream + " cream and " + this.topping + ". Message says: \"" + this.message + "\".";
    }

}
