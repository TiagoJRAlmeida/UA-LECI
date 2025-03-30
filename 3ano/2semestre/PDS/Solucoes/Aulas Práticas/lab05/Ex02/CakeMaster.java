package lab05.Ex02;

public class CakeMaster {
    // Atributos
    private CakeBuilder cakeBuilder;

    // Construtor
    public void setCakeBuilder(CakeBuilder cakeBuilder) {
        this.cakeBuilder = cakeBuilder;
    }

    // createCake se o bolo apenas tiver mensagem
    public void createCake(String message) {
        cakeBuilder.CreateCake();
        cakeBuilder.setCakeShape(Shape.Circle);
        cakeBuilder.addTopLayer();
        cakeBuilder.addTopping();
        cakeBuilder.addMessage(message);
    }

    // createCake se o bolo tiver forma, número de camadas e mensagem
    public void createCake(Shape shape, int numLayers, String message) {
        cakeBuilder.CreateCake();
        cakeBuilder.setCakeShape(shape);
        for (int i = 1; i < numLayers; i++) {
            cakeBuilder.addCakeLayer();
        }
        if (numLayers > 1) {
            cakeBuilder.addCreamLayer();
        }
        cakeBuilder.addTopLayer();
        cakeBuilder.addTopping();
        cakeBuilder.addMessage(message);
    }

    // createCake se o bolo tiver número de camadas, cobertura e mensagem
    public void createCake(int numLayers, String message) {
        cakeBuilder.CreateCake();
        cakeBuilder.setCakeShape(Shape.Circle);
        for (int i = 1; i < numLayers; i++) {
            cakeBuilder.addCakeLayer();
        }
        if (numLayers > 1) {
            cakeBuilder.addCreamLayer();
        }
        cakeBuilder.addTopLayer();
        cakeBuilder.addTopping();
        cakeBuilder.addMessage(message);
    }

    // Retorna o bolo
    public Cake getCake() {
        return cakeBuilder.getCake();
    }
}
