package lab05.Ex01;

public class PlasticBottle extends Container{
    // Construtor
    protected PlasticBottle(Portion portion){
        super(portion);
    }

    @Override
    // Método toString
    public String toString(){
        return "PlasticBottle with portion = " + getPortion().toString();
    }
}
