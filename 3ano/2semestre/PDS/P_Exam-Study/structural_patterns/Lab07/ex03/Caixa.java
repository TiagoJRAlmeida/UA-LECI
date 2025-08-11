package ex03;

import java.util.ArrayList;

public class Caixa implements Produto{
    private String name;
    private double peso;
    protected ArrayList<Produto> produtos = new ArrayList<>();

    public Caixa(String name, int peso) {
        this.name = name;
        this.peso = (double)peso;
    }

    public void add(Produto produto){
        produtos.add(produto);
    }

    public double getTotalWeight(){
        double pesoTotal = this.peso;
        
        for(Produto produto : produtos){
            pesoTotal += produto.getTotalWeight();
        }

        return pesoTotal;
    }

    public void draw(String prefix){
        System.out.println(prefix + "* " + this.toString());
        
        for(Produto produto : produtos){
            produto.draw(prefix + "\t");
        }
    }

    public void draw(){
        draw("");
    }

    public String toString(){
        return String.format("Caixa '%s' [ Weight: %.1f ; Total: %.1f]", this.name, (double)this.peso, (double)this.getTotalWeight());
    }
}
