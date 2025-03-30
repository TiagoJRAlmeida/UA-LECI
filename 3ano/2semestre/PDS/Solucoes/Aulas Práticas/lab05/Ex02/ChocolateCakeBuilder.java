package lab05.Ex02;

public class ChocolateCakeBuilder implements CakeBuilder {
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
        chocolateCake.setTopLayerCream(Cream.Whipped_Cream);
    }

    public void addTopping() {
        chocolateCake.setTopping(Topping.Fruit);
    }

    public void addMessage(String m) {
        chocolateCake.setMessage(m);
    }

    // Cria o bolo
    public void CreateCake() {
        chocolateCake = new Cake("Soft chocolate");
        addTopping();
        addTopLayer();
        addCreamLayer();
    }

    // Retorna o bolo
    public Cake getCake() {
        return chocolateCake;
    }
}
