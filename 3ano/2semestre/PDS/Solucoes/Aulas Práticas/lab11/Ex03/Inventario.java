package lab11.Ex03;

public class Inventario implements State {

    @Override
    public boolean regista(Livro livro) {
        return true;
    }

    @Override
    public boolean requisita(Livro livro) {
        return false;
    }

    @Override
    public boolean reserva(Livro livro) {
        return false;
    }

    @Override
    public boolean cancelaReserva(Livro livro) {
        return false;
    }

    @Override
    public boolean devolve(Livro livro) {
        return false;
    }
    
    @Override
    public String toString() {
        return "[Inventário]";
    }
}
