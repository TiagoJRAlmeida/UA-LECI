package lab07.Ex03;

public class Conserva extends Produto {

    public Conserva(String nome, double peso) {
        super(nome, peso);
    }

    @Override
    public void draw() {
        System.out.println(indent.toString() + " Conserva '" + this.getName() + "' " + " - Weight : " + this.getWeight() + " ");
    }
}
