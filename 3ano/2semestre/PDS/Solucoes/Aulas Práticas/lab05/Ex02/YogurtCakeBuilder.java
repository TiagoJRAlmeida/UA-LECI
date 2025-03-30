package lab05.Ex02;

public class YogurtCakeBuilder implements CakeBuilder {
    // Atributos
    private Cake yogurtCake;

    // Getters e Setters
    public void setCakeShape(Shape shape) {
        yogurtCake.setShape(shape);
    }

    public void addCakeLayer() {
        yogurtCake.addLayer();
    }

    public void addCreamLayer() {
        yogurtCake.setMidLayerCream(Cream.Vanilla);
    }

    public void addTopLayer() {
        yogurtCake.setTopLayerCream(Cream.Red_Berries);
    }

    public void addTopping() {
        yogurtCake.setTopping(Topping.Chocolate);
    }

    public void addMessage(String m) {
        yogurtCake.setMessage(m);
    }

    // Cria o bolo
    public void CreateCake() {
        yogurtCake = new Cake("Yogurt");
        addTopping();
        addTopLayer();
        addCreamLayer();
    }

    // Retorna o bolo
    public Cake getCake() {
        return yogurtCake;
    }
}
