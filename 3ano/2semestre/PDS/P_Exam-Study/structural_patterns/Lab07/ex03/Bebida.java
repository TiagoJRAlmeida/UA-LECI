package ex03;

public class Bebida implements Produto {
    private String name;
    private double peso;

    public Bebida(String name, int peso) {
        this.name = name;
        this.peso = (double)peso;
    }

    @Override
    public double getTotalWeight() {
        return peso;
    }

    @Override
    public void draw(String prefix) {
        System.out.println(prefix + "Bebida '" + name + "' - Weight : " + peso);
    }
}