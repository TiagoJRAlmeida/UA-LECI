package lab07.Ex03;

import java.util.ArrayList;

public class Caixa extends Produto {
    private double pesoTotal;
    private ArrayList<Produto> produtos = new ArrayList<>();

    public Caixa(String nome, double peso) {
        super(nome, peso);
    }

    public double getTotalWeight() {
        return this.pesoTotal;
    }

    public void add(Produto produto) {
        produtos.add(produto);
        this.pesoTotal += produto.getWeight();
    }

    public double PesoTotalCaixas() {
        this.pesoTotal = this.getWeight();
        for (Produto i : this.produtos) {
            if (i instanceof Caixa) {
                this.pesoTotal += ((Caixa) i).PesoTotalCaixas();
            } else {
                this.pesoTotal += i.getWeight();
            }
        }
        return this.pesoTotal;
    }

    @Override
    public void draw() {
        System.out.println(indent + "* Caixa '" + this.getName() + "' [ Weight : " + this.getWeight() + "; Total : " + this.PesoTotalCaixas() + "]");
        
        indent.append(" ");
        
        for (Produto produto : produtos) {
            produto.draw();
        }

        indent.deleteCharAt(indent.length() - 1);
    }

}
