package lab05.Ex02;

public class SpongeCakeBuilder implements CakeBuilder {
    // Atributos
    private Cake spongeCake;

    // Getters e Setters
    public void setCakeShape(Shape shape) {
        spongeCake.setShape(shape);
    }

    public void addCakeLayer() {
        spongeCake.addLayer();
    }

    public void addCreamLayer() {
        spongeCake.setMidLayerCream(Cream.Red_Berries);
    }

    public void addTopLayer() {
        spongeCake.setTopLayerCream(Cream.Whipped_Cream);
    }

    public void addTopping() {
        spongeCake.setTopping(Topping.Fruit);
    }

    public void addMessage(String m) {
        spongeCake.setMessage(m);
    }

    // Cria o bolo
    public void CreateCake() {
        spongeCake = new Cake("Sponge");
        addTopping();
        addTopLayer();
        addCreamLayer();
    }

    // Retorna o bolo
    public Cake getCake() {
        return spongeCake;
    }
}
