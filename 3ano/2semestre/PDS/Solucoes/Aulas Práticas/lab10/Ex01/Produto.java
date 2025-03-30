package lab10.Ex01;

import java.util.ArrayList;
import java.util.List;

public class Produto {
    private List<Observer> observers = new ArrayList<Observer>();
    private static int idCount = 0;
    private int id;
    private String descricao;
    private double precoInicial;
    private double preco;
    private Estado estado;
    private double tempoLeilao = 0;

    public Produto(String descricao, double precoInicial) {
        this.id = ++idCount;
        this.descricao = descricao;
        this.precoInicial = precoInicial;
        this.preco = precoInicial;
        this.estado = Estado.STOCK;
    }

    public void attach(Observer observer) {
        observers.add(observer);
    }

    public void setEstado(Estado estado) {
        this.estado = estado;
        if (this.estado == Estado.LEILAO) {
            this.tempoLeilao = System.nanoTime();
        } else {
            this.tempoLeilao = System.nanoTime() - this.tempoLeilao;
            System.out.printf("O produto esteve em leilão %f ns", this.tempoLeilao);
            if (estado == Estado.STOCK) {
                this.preco = this.precoInicial;
            }
        }
        notifyObservers(false);
    }

    public Estado getEstado() {
        return this.estado;
    }

    public void setPreco(double preco) {
        this.preco = preco;
        notifyObservers(true);
    }

    public double getPreco() {
        return this.preco;
    }

    private void notifyObservers(boolean novaOferta) {
        for (Observer observer : observers) {
            observer.update(this, novaOferta);
        }
    }

    @Override
    public String toString() {
        return String.format("Produto %d: %s, %.2f", this.id, this.descricao, this.preco);
    }
}
