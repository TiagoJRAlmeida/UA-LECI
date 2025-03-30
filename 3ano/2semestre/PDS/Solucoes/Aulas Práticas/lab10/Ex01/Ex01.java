package lab10.Ex01;

public class Ex01 {
    public static void main(String[] args) {

        Produto p1 = new Produto("Coiso e tal", 500.0);
        Produto p2 = new Produto("Cena fixe", 30000.0);
        Produto p3 = new Produto("bola", 10.0);
        Produto p4 = new Produto("livro", 3500.0);

        Cliente c1 = new Cliente("carlos");
        Cliente c2 = new Cliente("manel");
        Cliente c3 = new Cliente("andre ricardo");

        Gestor mg = new Gestor("Chefe de hogwards");
        mg.registarProduto(p1);
        mg.registarProduto(p2);
        mg.registarProduto(p3);
        mg.registarProduto(p4);

        p1.setEstado(Estado.LEILAO);
        p3.setEstado(Estado.LEILAO);

        c1.bid(p1, 500.4);
        System.out.println("");
        c1.bid(p3, 20);
        System.out.println("");

        p4.setEstado(Estado.LEILAO);

        c2.bid(p1, 520.6);
        System.out.println("");

        c1.bid(p1, 600);
        System.out.println("");

        c3.bid(p4, 4242.42);
        System.out.println("");

        p1.setEstado(Estado.VENDAS);
        c2.bid(p1, 10);

    }
}
