package lab06.Ex01;

public class Empregado {
    // Atributos
    private String nome;
    private String apelido;
    private int codigo;
    private double salario;

    // Construtor
    public Empregado(String nome, String apelido, int codigo, double salario) {
        this.nome = nome;
        this.apelido = apelido;
        this.codigo = codigo;
        this.salario = salario;
    }

    // Getters e Setters
    public String apelido() {
        return apelido;
    }

    public String nome() {
        return nome;
    }

    public int codigo() {
        return codigo;
    }

    public double salario() {
        return salario;
    }

    @Override
    // Transforma o objeto em string
    public String toString() {
        return "Empregado " + nome + " " + apelido + "(" + codigo + ") " + salario + "€";
    }
}
