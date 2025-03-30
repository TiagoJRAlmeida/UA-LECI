package lab10.Ex03;

public class Ex03 {
    public static void main(String[] args) {
        Tower airTrafficControlTower = new Tower();

        Aircraft airplane = new Airplane(airTrafficControlTower, "AIRPLANE");
        Aircraft jet = new Jet (airTrafficControlTower, "JET");

        airTrafficControlTower.setAircraft(jet);
        airplane.send("Hello from " + airplane.getName() + "!");

        airTrafficControlTower.setAircraft(airplane);
        jet.send("Hello from " + jet.getName() + "!");
    }
}
