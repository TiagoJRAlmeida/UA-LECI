package lab11.Ex01;

import java.util.ArrayList;

public class Revista {
    private SortStrategy sortStrategy;
    private ArrayList<Telemovel> telemoveis;

    public Revista(SortStrategy sortStrategy, ArrayList<Telemovel> telemoveis) {
        this.sortStrategy = sortStrategy;
        this.telemoveis = telemoveis;
    }

    public ArrayList<Telemovel> getTelemoveis() {
        return telemoveis;
    }

    public void setTelemoveis(ArrayList<Telemovel> telemoveis) {
        this.telemoveis = telemoveis;
    }

    public SortStrategy getSortStrategy() {
        return sortStrategy;
    }
    
    public void setSortStrategy(SortStrategy sortStrategy) {
        this.sortStrategy = sortStrategy;
    }

    public void sort(String atributo) {
        this.sortStrategy.sort(this.telemoveis, atributo);
    }

    public void print() {
        for (Telemovel telemovel : this.telemoveis) {
            System.out.println(telemovel);
        }
    }
}
