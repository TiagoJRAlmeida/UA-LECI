import java.util.Iterator;

public class demo {
    public static void main(String[] args) {
        VectorGeneric<String> vg = new VectorGeneric<>();

        vg.addElem("one");
        vg.addElem("two");
        vg.addElem("three");

        System.out.println("Usando Iterator:");
        Iterator<String> it = vg.iterator();
        while (it.hasNext()) {
            System.out.println(it.next());
        }

        // System.out.println("\nUsando ListIterator (forward):");
        // ListIterator<String> lit = vg.listIterator();
        // while (lit.hasNext()) {
        //     System.out.println(lit.next());
        // }

        // System.out.println("\nUsando ListIterator (backward):");
        // while (lit.hasPrevious()) {
        //     System.out.println(lit.previous());
        // }

        // System.out.println("\nUsar dois iteradores em simultâneo:");
        // Iterator<String> it1 = vg.iterator();
        // Iterator<String> it2 = vg.iterator();
        // System.out.println("it1: " + it1.next());
        // System.out.println("it2: " + it2.next());
        // System.out.println("it1: " + it1.next());
    }
}
