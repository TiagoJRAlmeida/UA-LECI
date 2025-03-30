package lab03.SistemaReservas;
import java.util.*;

public class Reservas {

    private String codigo = "RE";
    private static int numReserva = 0;
    private String classe;
    private int numPassageiros;
    private HashMap<String, ArrayList<Integer>> lugaresReservas = new HashMap<String, ArrayList<Integer>>();
    

    public Reservas(String flightCode, String classe, int numPassageiros) {
        numReserva += 1;
        this.codigo = flightCode + ":" + String.valueOf(numReserva);
        this.classe = classe;
        this.numPassageiros = numPassageiros;
    }

    public String getCodigo() {
        return codigo;
    }

    public int getNumReserva() {
        return numReserva;
    }

    public String getClasse() {
        return classe;
    }

    public int getNumPassageiro() {
        return numPassageiros;
    }
    
    public HashMap<String, ArrayList<Integer>> getLugaresReservas() {
        return lugaresReservas;
    }

    @Override
    public String toString() {
        return "Reserva [codigo=" + codigo + ", classe=" + classe + ", numPassageiros=" + numPassageiros + "]";
    }
}
