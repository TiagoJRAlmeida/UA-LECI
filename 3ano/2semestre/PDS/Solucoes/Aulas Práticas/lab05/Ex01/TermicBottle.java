package lab05.Ex01;

public class TermicBottle extends Container{
    // Construtor
    protected TermicBottle(Portion portion){
        super(portion);
    }

    @Override
    // Método toString
    public String toString(){
        return "TermicBottle with portion = " + getPortion().toString();
    }
}
