package lab05.Ex02;

public class CarrotCakeBuilder implements CakeBuilder {
    // Atributos
    private Cake chocolateCake;

    // Getters e Setters
    public void setCakeShape(Shape shape) {
        chocolateCake.setShape(shape);
    }

    public void addCakeLayer() {
        chocolateCake.addLayer();
    }

    public void addCreamLayer() {
        chocolateCake.setMidLayerCream(Cream.NULL);
    }

    public void addTopLayer() {
        chocolateCake.setTopLayerCream(Cream.Chocolate);
    }

    public void addTopping() {
        chocolateCake.setTopping(Topping.NULL);
    }

    public void addMessage(String m) {
        chocolateCake.setMessage(m);
    }

    // Cria o bolo
    public void CreateCake() {
        chocolateCake = new Cake("Carrot and Chocolate");
        addTopping();
        addTopLayer();
        addCreamLayer();
    }

    // Retorna o bolo
    public Cake getCake() {
        return chocolateCake;
    }
}
