package lab11.Ex03;

public interface State {
    public boolean regista(Livro livro);
    public boolean requisita(Livro livro);
    public boolean reserva(Livro livro);
    public boolean cancelaReserva(Livro livro);
    public boolean devolve(Livro livro);
}
