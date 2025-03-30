package lab03.SistemaReservas;

public class Aviao {
    
    private int numLugFilaTuristica;                //numero de lugares por fila turistica
    private int numLugFilaExecutiva;                //numero de lugares por fila executiva
    
    private int numFilasTuristica;              //numero de filas turistica
    private int numFilasExecutiva;              //numero de filas executiva

    public Aviao(int numLugFilaTuristica, int numLugFilaExecutiva, int numFilasTuristica, int numFilasExecutiva) {      //construtor com argumentos de todas as classes
        this.numLugFilaTuristica = numLugFilaTuristica;
        this.numLugFilaExecutiva = numLugFilaExecutiva;
        this.numFilasTuristica = numFilasTuristica;
        this.numFilasExecutiva = numFilasExecutiva;
    }

    public int getNumLugFilaTuristica() {       //retorna o numero de lugares por fila da classe turistica
        return this.numLugFilaTuristica;
    }

    public int getNumLugFilaExecutiva() {       //retorna o numero de lugares por fila da classe executiva
        return this.numLugFilaExecutiva;
    }

    public int getNumFilasTuristica() {     //retorna o numero de filas da classe turistica
        return this.numFilasTuristica;
    }

    public int getNumFilasExecutiva() {     //retorna o numero de filas da classe executiva
        return this.numFilasExecutiva;
    }

    public int getLugaresExecutiva() {     //retorna o numero de lugares da classe executiva
        return this.numFilasExecutiva * this.numLugFilaExecutiva;
    }

    public int getLugaresTuristica() {     //retorna o numero de lugares da classe executiva
        return this.numFilasTuristica * this.numLugFilaTuristica;
    }

    public int[][] getMapaExecutiva() {      //retorna o mapa da classe executiva
        int[][] mapa = new int[this.numFilasExecutiva][this.numLugFilaExecutiva];
        for (int i = 0; i < this.numFilasExecutiva; i++) {
            for (int j = 0; j < this.numLugFilaExecutiva; j++) {
                mapa[i][j] = 0;
            }
        }
        return mapa;
    }

    public int[][] getMapaTouristica() {      //retorna o mapa da classe executiva
        int[][] mapa = new int[this.numFilasTuristica][this.numLugFilaTuristica];
        for (int i = 0; i < this.numFilasTuristica; i++) {
            for (int j = 0; j < this.numLugFilaTuristica; j++) {
                mapa[i][j] = 0;
            }
        }
        return mapa;
    }

    @Override
    public String toString() {
        return "Aviao [lugTuristica=" + this.getLugaresTuristica() + ", lugExecutiva=" + this.getLugaresExecutiva() + ", numFilasTuristica="
                + numFilasTuristica + ", numFilasExecutiva=" + numFilasExecutiva + "]";
    }
}