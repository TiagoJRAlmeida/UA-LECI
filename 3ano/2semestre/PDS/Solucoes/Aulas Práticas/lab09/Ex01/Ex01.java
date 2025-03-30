package lab09.Ex01;

import java.util.Iterator;
import java.util.ListIterator;

public class Ex01 {
    public static <T> void main(String[] args) {
        VectorGeneric<String> vector = new VectorGeneric<>();
        
        // Adicionar elementos ao vetor
        vector.addElem("A");
        vector.addElem("B");
        vector.addElem("C");
        vector.addElem("D");
        vector.addElem("E");

        Vector<String> v = vector;
        Iterator<String> iterator;
        ListIterator<String> listIterator;
        // Testar o método Iterator()
        iterator = v.Iterator();
        System.out.println("Iterating with Iterator:");
        while (iterator.hasNext()) {
            String element = iterator.next();
            System.out.println(element);
        }
        System.out.println();

        // Testar o método listIterator()
        listIterator = v.listIterator();
        System.out.println("Iterating with ListIterator (starting at index 0):");
        while (listIterator.hasNext()) {
            String element = listIterator.next();
            System.out.println(element);
        }
        System.out.println();

        // Testar o método listIterator(int index)
        listIterator = v.listIterator(2);
        System.out.println("Iterating with ListIterator (starting at index 2):");
        while (listIterator.hasNext()) {
            String element = listIterator.next();
            System.out.println(element);
        }
        System.out.println();
    }
}
