package lab11.Ex01;

public class Telemovel {
    private String nome;
    private String processador;
    private double preco;
    private int memoria;
    private int camera;

    public Telemovel(String nome, String processador, double preco, int memoria, int camera) {
        this.nome = nome;
        this.processador = processador;
        this.preco = preco;
        this.memoria = memoria;
        this.camera = camera;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getProcessador() {
        return processador;
    }

    public void setProcessador(String processador) {
        this.processador = processador;
    }

    public double getPreco() {
        return preco;
    }

    public void setPreco(float preco) {
        this.preco = preco;
    }

    public int getMemoria() {
        return memoria;
    }

    public void setMemoria(int memoria) {
        this.memoria = memoria;
    }

    public int getCamera() {
        return camera;
    }

    public void setCamera(int camera) {
        this.camera = camera;
    }

    public String getAtributo(String atributo) {
        switch (atributo) {
            case "nome":
                return this.nome;
            case "processador":
                return this.processador;
            case "preco":
                return String.valueOf(this.preco);
            case "memoria":
                return String.valueOf(this.memoria);
            case "camera":
                return String.valueOf(this.camera);
            default:
                return null;
        }
    }

    @Override
    public String toString() {
        return "Telemovel{" +
                "nome='" + nome + '\'' +
                ", processador='" + processador + '\'' +
                ", preco=" + preco +
                ", memoria=" + memoria +
                ", camera=" + camera +
                '}';
    }
}
