public class demo {
    public static void main(String[] args) {
        Chef sushi = new SushiChef();
        Chef pasta = new PastaChef();
        Chef burger = new BurgerChef();
        Chef pizza = new PizzaChef();
        Chef dessert = new DessertChef();

        sushi.setNextChef(pasta);
        pasta.setNextChef(burger);
        burger.setNextChef(pizza);
        pizza.setNextChef(dessert);

        System.out.println("\nCan I please get a veggie burger?");
        sushi.parse("veggie burger");

        System.out.println("\nCan I please get a Pasta Carbonara?");
        sushi.parse("Pasta Carbonara");

        System.out.println("\nCan I please get a PLAIN pizza, no toppings!?");
        sushi.parse("PLAIN pizza, no toppings!");

        System.out.println("\nCan I please get a sushi nigiri and sashimi?");
        sushi.parse("sushi nigiri and sashimi");

        System.out.println("\nCan I please get a salad with tuna?");
        sushi.parse("salad with tuna");

        System.out.println("\nCan I please get a strawberry ice cream and waffles dessert?");
        sushi.parse("strawberry ice cream and waffles dessert");
    }   
}
