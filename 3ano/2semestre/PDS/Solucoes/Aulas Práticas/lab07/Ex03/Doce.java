package lab07.Ex03;

public class Doce extends Produto {

    public Doce(String nome, double peso) {
        super(nome, peso);
    }

    @Override
    public void draw() {
        System.out.println(indent.toString() + " Doce '" + this.getName() + "' " + " - Weight : " + this.getWeight() + " ");
    }
}
