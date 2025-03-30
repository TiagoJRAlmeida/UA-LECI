package lab07.Ex03;

public class Bebida extends Produto {

    public Bebida(String nome, double peso) {
        super(nome, peso);
    }

    @Override
    public void draw() {
        System.out.println(indent.toString() + " Bebida '" + this.getName() + "' " + " - Weight : " + this.getWeight() + " ");
    }
}
