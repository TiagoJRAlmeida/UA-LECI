import java.util.ArrayList;

public class Reserva {
    int totalQueues = 0;
    int maxSeats = 0;
    public Reserva (String code, ArrayList<String> listOfFlights, ArrayList<ArrayList<String>> listOfArrangements) {
        int index = listOfFlights.indexOf(code);
        this.totalQueues = Integer.parseInt(String.valueOf(listOfFlights.get(index+1))) + Integer.parseInt(String.valueOf(listOfFlights.get(index+3)));
        this.maxSeats = Math.max(Integer.parseInt(String.valueOf(listOfFlights.get(index+2))), Integer.parseInt(String.valueOf(listOfFlights.get(index+4))));
        ArrayList<String> thisArrangement = new ArrayList<>();
        initArrangement(thisArrangement, index, listOfFlights, this.totalQueues, this.maxSeats, listOfArrangements, code);
    }
    public void initArrangement ( ArrayList<String> thisArrangement, int index, ArrayList<String> listOfFlights, int totalQueues, int maxSeats, ArrayList<ArrayList<String>> listOfArrangements, String code) {
        thisArrangement.add(code);
        for (int i=0; i < totalQueues; i++) {
            for (int j=0; j < maxSeats; j++) {
                if ((i < Integer.parseInt(String.valueOf(listOfFlights.get(index+3)))) && (j < Integer.parseInt(String.valueOf(listOfFlights.get(index+4))))) {
                    thisArrangement.add("0");
                } else if ((i >= Integer.parseInt(String.valueOf(listOfFlights.get(index+3)))) && (j < Integer.parseInt(String.valueOf(listOfFlights.get(index+2))))) {
                    thisArrangement.add("0");
                } else {
                    thisArrangement.add(" ");
                }
            }
        }
        listOfArrangements.add(thisArrangement);
    }
    public int getTotalQueues() {
        return totalQueues;
    }
    public int getMaxSeats() { return maxSeats; }
}