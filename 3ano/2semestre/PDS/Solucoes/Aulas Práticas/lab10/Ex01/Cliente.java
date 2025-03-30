package lab10.Ex01;

import java.util.ArrayList;

public class Cliente extends Observer {

    public Cliente(String nome) {
        this.nome = nome;
        this.produtosLeilao = new ArrayList<Produto>();
    }

    public void bid(Produto produto, double quantiaOferta) {
        if (!this.produtosLeilao.contains(produto)) {
            if (produto.getEstado() == Estado.LEILAO) {
                produto.attach(this);
                this.produtosLeilao.add(produto);
            } else {
                System.out.println("Este produto não está em leilão de momento!");
                return;
            }
        }

        if (produto.getPreco() > quantiaOferta) {
            System.out.println("Oferta demasiado baixa! Deve ser de pelo menos " + produto.getPreco());
            return;
        }
        produto.setPreco(quantiaOferta);
    }

    @Override
    public void update(Produto produto, boolean novaOferta) {
        if (novaOferta == true) {
            System.out.printf("Anúncio para o cliente %s --> Produto %s tem uma nova oferta --> %f\n", this.nome,produto.toString(), produto.getPreco());
        } else {
            if (produto.getEstado() == Estado.VENDAS) {
                System.out.printf("Anúncio para o cliente %s --> Produto %s foi vendido --> %f\n", this.nome,
                produto.toString(), produto.getPreco());
            } else if (produto.getEstado() == Estado.STOCK) {
                System.out.printf("Anúncio para o cliente %s --> Produto %s parou de estar em leilão", this.nome,
                produto.toString());
            }
        }
    }
}
