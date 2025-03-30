package lab10.Ex01;

import java.util.ArrayList;

public abstract class Observer {
    protected String nome;
    protected ArrayList<Produto> produtosLeilao;
    
    public abstract void update(Produto produto, boolean novaOferta);
}
