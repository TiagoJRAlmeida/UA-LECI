package lab05.Ex02;

public interface CakeBuilder {
    public void setCakeShape(Shape shape); // default circle

    public void addCakeLayer();

    public void addCreamLayer();

    public void addTopLayer();

    public void addTopping();

    public void addMessage(String m);

    public void CreateCake();

    public Cake getCake();
}
