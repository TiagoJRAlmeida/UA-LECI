package lab05.Ex01;

public class PlasticBag extends Container {
    // Construtor
    protected PlasticBag(Portion portion) {
        super(portion);
    }

    @Override
    // Método toString
    public String toString() {
        return "PlasticBag with portion = " + getPortion().toString();
    }

}
