package lab07.Ex03;

public abstract class Produto {
    protected double peso;
    private String nome;
    protected static StringBuffer indent = new StringBuffer();

    public Produto(String nome, double peso) {
        this.nome = nome;
        this.peso = peso;
    }

    public String getName() {
        return this.nome;
    }

    public double getWeight() {
        return this.peso;
    }

    public abstract void draw();
}
