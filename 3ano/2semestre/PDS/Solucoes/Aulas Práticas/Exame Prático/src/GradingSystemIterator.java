import java.util.Iterator;

public class GradingSystemIterator implements Iterator<StudentAdm> {
    private Iterator<StudentAdm> iterator;

    public GradingSystemIterator(GradingSystem gs) {
        this.iterator = gs.studentsAdm.iterator();
    }

    public boolean hasNext() {
        return iterator.hasNext();
    }

    public StudentAdm next() {
        return iterator.next();
    }

    public void remove() {
        iterator.remove();
    }
}
