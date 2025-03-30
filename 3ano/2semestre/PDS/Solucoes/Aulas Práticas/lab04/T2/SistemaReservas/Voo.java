package lab03.SistemaReservas;

public class Voo {
    private String codigo;
    private Aviao aviao;
    private int lugaresTuristica;
    private int lugaresExecutiva;
    
    public Voo(String codigo, Aviao aviao){
        this.codigo = codigo;
        this.aviao = aviao;
    }


    public String getCodigo() {
        return codigo;
    }

    public Aviao getAviao() {
        return aviao;
    }

    public int getLugaresTuristica() {
        return lugaresTuristica;
    }

    public int getLugaresExecutiva() {
        return lugaresExecutiva;
    }

    @Override
    public String toString() {

        if (aviao.getLugaresExecutiva() != 0) {
            return "Código do voo: " + this.codigo + ". Lugares disponíveis: " + aviao.getLugaresExecutiva() + " em\nclasse Executiva; " + aviao.getLugaresTuristica() + " em classe Turística.";
        }
        else {
            return "Código do voo: " + this.codigo + ". Lugares disponíveis: " + aviao.getLugaresTuristica() + " lugares em\nclasse Turística.\nClasse executiva não disponível neste voo.";
        }
        
    }   
}