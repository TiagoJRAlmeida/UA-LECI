package lab11.Ex01;

import java.time.Duration;
import java.time.Instant;
import java.util.ArrayList;

public class InsertionSort implements SortStrategy {

    @Override
    public void sort(ArrayList<Telemovel> telemoveis, String atributo) {
        Instant timeStart = Instant.now();

        for (int i = 1; i < telemoveis.size(); i++) {
            Telemovel key = telemoveis.get(i);
            int j = i - 1;
            while ((j > -1) && (telemoveis.get(j).getAtributo(atributo).compareTo(key.getAtributo(atributo)) > 0)) {
                telemoveis.set(j + 1, telemoveis.get(j));
                j--;
            }
        }

        Instant timeEnd = Instant.now();
        Duration duration = Duration.between(timeStart, timeEnd);
        long seconds = duration.getSeconds();
        System.out.printf("\t\tProcess time: %d ms\n", seconds);
    }
}
