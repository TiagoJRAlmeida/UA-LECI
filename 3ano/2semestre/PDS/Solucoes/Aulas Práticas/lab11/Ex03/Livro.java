package lab11.Ex03;

public class Livro {
    private String titulo;
    private int ISBN;
    private int ano;
    private String autor;
    private State estado;

    public Livro(String titulo, int ISBN, int ano, String autor, State estado) {
        this.titulo = titulo;
        this.ISBN = ISBN;
        this.ano = ano;
        this.autor = autor;
        this.estado = estado;
    }

    public void regista() {
        if (estado.regista(this)) {
            this.estado = new Disponivel();
        } else {
            System.out.println("Operação não disponível\n");
        }
    }

    public void requisita() {
        if (estado.requisita(this)) {
            this.estado = new Emprestado();
        } else {
            System.out.println("Operação não disponível\n");
        }
    }

    public void reserva() {
        if (estado.reserva(this)) {
            this.estado = new Reservado();
        } else {
            System.out.println("Operação não disponível\n");
        }
    }

    public void cancelaReserva() {
        if (estado.cancelaReserva(this)) {
            this.estado = new Disponivel();
        } else {
            System.out.println("Operação não disponível\n");
        }
    }

    public void devolve() {
        if (estado.devolve(this)) {
            this.estado = new Disponivel();
        } else {
            System.out.println("Operação não disponível\n");
        }
    }

    @Override
    public String toString() {
        return titulo + "\t" + autor + "\t" + estado.toString();
    }
}
