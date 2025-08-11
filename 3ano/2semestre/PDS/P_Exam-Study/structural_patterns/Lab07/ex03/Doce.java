package ex03;

public class Doce implements Produto {
    private String name;
    private double peso;

    public Doce(String name, int peso) {
        this.name = name;
        this.peso = (double)peso;
    }

    @Override
    public double getTotalWeight() {
        return peso;
    }

    @Override
    public void draw(String prefix) {
        System.out.println(prefix + "Doce '" + name + "' - Weight : " + peso);
    }
}