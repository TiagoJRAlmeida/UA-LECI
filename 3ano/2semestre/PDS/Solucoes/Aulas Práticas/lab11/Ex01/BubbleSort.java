package lab11.Ex01;

import java.time.Duration;
import java.time.Instant;
import java.util.ArrayList;

public class BubbleSort implements SortStrategy {

    @Override
    public void sort(ArrayList<Telemovel> telemoveis, String atributo) {
        Instant timeStart = Instant.now();

        boolean changed = false;
        do {
            changed = false;
            for (int i = 0; i < telemoveis.size() - 1; i++) {
                String atributo1 = telemoveis.get(i).getAtributo(atributo);
                String atributo2 = telemoveis.get(i+1).getAtributo(atributo);
                if (atributo1.compareTo(atributo2) > 0) {
                    Telemovel tmp = telemoveis.get(i);
                    telemoveis.set(i, telemoveis.get(i + 1));
                    telemoveis.set(i + 1, tmp);
                    changed = true;
                }
            }
        } while (changed);

        Instant timeEnd = Instant.now();
        Duration duration = Duration.between(timeStart, timeEnd);
        long seconds = duration.getSeconds();
        System.out.printf("\t\tProcess time: %d ms\n", seconds);
    }
}
