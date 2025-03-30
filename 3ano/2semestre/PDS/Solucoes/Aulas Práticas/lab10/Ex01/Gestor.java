package lab10.Ex01;

import java.util.ArrayList;

public class Gestor extends Observer {
    protected ArrayList<Produto> produtosStock;
    protected ArrayList<Produto> produtosVendas;

    public Gestor(String nome) {
        this.nome = nome;
        this.produtosLeilao = new ArrayList<Produto>();
        this.produtosStock = new ArrayList<Produto>();
        this.produtosVendas = new ArrayList<Produto>();
    }

    public void registarProduto(Produto produto) {
        if (produto.getEstado() == Estado.LEILAO) {
            this.produtosLeilao.add(produto);
        } else if (produto.getEstado() == Estado.STOCK) {
            this.produtosStock.add(produto);
        } else if (produto.getEstado() == Estado.VENDAS) {
            this.produtosVendas.add(produto);
        }

        produto.attach(this);
    }

    @Override
    public void update(Produto produto, boolean novaOferta) {
        if (novaOferta == true) {
            System.out.printf("Anúncio para o gestor %s --> Produto %s tem uma nova oferta --> %f\n", this.nome, produto.toString(), produto.getPreco());
        } else {
            if (produto.getEstado() == Estado.LEILAO) {
                this.produtosLeilao.add(produto);
                this.produtosStock.remove(produto);
            } else if (produto.getEstado() == Estado.STOCK) {
                this.produtosStock.add(produto);
                this.produtosLeilao.remove(produto);
            } else if (produto.getEstado() == Estado.VENDAS) {
                this.produtosVendas.add(produto);
                this.produtosLeilao.remove(produto);
                System.out.printf("Anúncio para o gestor %s --> Produto %s foi vendido --> %f\n", this.nome, produto.toString(), produto.getPreco());
            }
        }
    }
}
