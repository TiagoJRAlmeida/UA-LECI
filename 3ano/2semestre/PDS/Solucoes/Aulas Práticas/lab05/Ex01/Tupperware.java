package lab05.Ex01;

public class Tupperware extends Container{
    // Construtor
    protected Tupperware(Portion portion){
        super(portion);
    }

    @Override
    // Método toString
    public String toString(){
        return "Tupperware with portion = " + getPortion().toString();
    }
}
