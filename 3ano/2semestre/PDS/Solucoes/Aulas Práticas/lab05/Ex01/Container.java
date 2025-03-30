package lab05.Ex01;

public abstract class Container {
    // Atributos
    private Portion portion;

    // Construtor
    public Container(Portion portion) {
        this.portion = portion;
    }

    // Getters
    public Portion getPortion() {
        return portion;
    }

    // Factory method
    public static Container create(Portion menu) {
        // Verifica o estado do menu
        switch (menu.getState()) {
            // Verifica se o estado é líquido
            case Liquid:
                // Verifica se a temperatura é fria
                if (menu.getTemperature()== Temperature.COLD) {
                        // Coloca pedido em PlasticBottle
                        return new PlasticBottle(menu);
                }
                // Coloca pedido em TermicBottle
                return new TermicBottle(menu);
            // Verifica se o estado é sólido
            case Solid:
                // Verifica se a temperatura é fria
                if (menu.getTemperature() == Temperature.COLD) {
                    // Coloca pedido em PlasticBag  
                        return new PlasticBag(menu);
                }
                // Coloca pedido em Tupperware
                return new Tupperware(menu);
            // Caso o estado não seja válido
            default:
                System.out.println("Error! Unknown State enum declared!");
                System.exit(1);
        }
        return null;
    }
}