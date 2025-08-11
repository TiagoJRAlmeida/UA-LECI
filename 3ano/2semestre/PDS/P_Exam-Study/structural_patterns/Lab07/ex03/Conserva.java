package ex03;

public class Conserva implements Produto {
    private String name;
    private double peso;

    public Conserva(String name, int peso) {
        this.name = name;
        this.peso = (double)peso;
    }

    @Override
    public double getTotalWeight() {
        return peso;
    }

    @Override
    public void draw(String prefix) {
        System.out.println(prefix + "Conserva '" + name + "' - Weight : " + peso);
    }
}