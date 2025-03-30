package lab11.Ex01;

import java.time.Duration;
import java.time.Instant;
import java.util.ArrayList;
import java.util.Arrays;

public class QuickSort implements SortStrategy {

    @Override
    public void sort(ArrayList<Telemovel> telemoveis, String atributo) {
        Instant timeStart = Instant.now();
        Telemovel pivot = telemoveis.get(0);

        if (pivot == null) {
            return;
        }

        Telemovel[] antes = new Telemovel[telemoveis.size()];
        Telemovel[] pivotList = new Telemovel[telemoveis.size()];
        Telemovel[] depois = new Telemovel[telemoveis.size()];

        // Partição
        int indexAntes = 0;
        int indexPivot = 0;
        int indexDepois = 0;

        // Atributo a ordenar
        String atributoOrdenacao = pivot.getAtributo(atributo);

        for (Telemovel telemovel : telemoveis) {
            if (telemovel == null)
                return;
            String attr1 = telemovel.getAtributo(atributo);
            if (attr1.compareTo(atributoOrdenacao) < 0)
                antes[indexAntes++] = telemovel;
            else if (attr1.compareTo(atributoOrdenacao) > 0)
                depois[indexDepois++] = telemovel;
            else
                pivotList[indexPivot++] = telemovel;
        }


        // Ordenar partições
        this.sort(new ArrayList<>(Arrays.asList(antes)), atributo);
        this.sort(new ArrayList<>(Arrays.asList(depois)), atributo);

        // Juntar partições
        int index = 0;
        for (Telemovel telemovel : antes) {
            if (telemovel != null)
                telemoveis.set(index++, telemovel);
        }
        for (Telemovel telemovel : pivotList) {
            if (telemovel != null)
                telemoveis.set(index++, telemovel);
        }
        for (Telemovel telemovel : depois) {
            if (telemovel != null)
                telemoveis.set(index++, telemovel);
        }

        Instant timeEnd = Instant.now();
        Duration duration = Duration.between(timeStart, timeEnd);
        long seconds = duration.getSeconds();
        System.out.printf("\t\tProcess time: %d ms\n", seconds);
    }
}
