interface EstadoProduto {
    void handle(Produto produto);
    String getNomeEstado();
}

class EstadoStock implements EstadoProduto {
    public void handle(Produto produto) {
        // Não faz nada, produto está em stock
    }
    public String getNomeEstado() { return "STOCK"; }
}

class EstadoLeilao implements EstadoProduto {
    private long tempoFinal;
    
    public EstadoLeilao(int segundos) {
        this.tempoFinal = System.currentTimeMillis() + segundos * 1000;
    }
    
    public void handle(Produto produto) {
        if (System.currentTimeMillis() >= tempoFinal) {
            if (produto.getUltimaLicitacao() != null) {
                produto.setEstado(new EstadoVendido());
            } else {
                produto.setEstado(new EstadoStock());
            }
        }
    }
    
    public String getNomeEstado() { return "LEILAO"; }
}

class EstadoVendido implements EstadoProduto {
    public void handle(Produto produto) {
        // Produto vendido, não faz mais nada
    }
    public String getNomeEstado() { return "VENDIDO"; }
}