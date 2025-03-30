package lab05.Ex01;

public abstract class PortionFactory implements Portion {
    // Atributos
    private State estado;
    private Temperature temperatura;

    // Getters e Setters
    public State getState() {
        return estado;
    }

    public Temperature getTemperature() {
        return temperatura;
    }

    public void setState(State estado) {
        this.estado = estado;
    }

    public void setTemperature(Temperature temperatura) {
        this.temperatura = temperatura;
    }

    // Métodos
    public static Portion create(String nome, Temperature temperatura) {
        Portion pedido = null;

        // Verifica se o nome é válido
        try {
            // Verifica se o nome é Beverage
            if (nome.equalsIgnoreCase("Beverage")) {
                // Verifica se a temperatura é fria
                if (temperatura == Temperature.COLD) {
                    // Cria um pedido de FruitJuice
                    pedido = new FruitJuice("Orange");
                // Verifica se a temperatura é quente
                } else if (temperatura == Temperature.WARM) {
                    // Cria um pedido de Milk
                    pedido = new Milk();
                }
            // Verifica se o nome é Meat
            } else if (nome.equalsIgnoreCase("Meat")) {
                // Verifica se a temperatura é fria
                if (temperatura == Temperature.COLD) {
                    // Cria um pedido de Tuna
                    pedido = new Tuna();
                // Verifica se a temperatura é quente
                } else if (temperatura == Temperature.WARM) {
                    // Cria um pedido de Pork
                    pedido = new Pork();
                }
            }
        // Caso o nome não seja válido
        } catch (Exception e) {
            throw new IllegalArgumentException(nome + " não existente!");
        }

        return pedido;
    }
}
