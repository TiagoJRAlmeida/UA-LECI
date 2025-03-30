package lab09.Ex01;

import java.util.Iterator;
import java.util.NoSuchElementException;

public class VectorIterator<T> implements Iterator<T> {
    private VectorGeneric<T> vector;
    private int index;

    public VectorIterator(VectorGeneric<T> vector) {
        this.vector = vector;
        this.index = 0;
    }

    @Override
    public boolean hasNext() {
        if (this.index < vector.totalElem())
        {
            return true;
        } else {
            return false;
        }
    }

    @Override
    public T next() {
        if (hasNext()) {
            return vector.getElem(index++);
        } else {
            throw new NoSuchElementException("Operation not supported");
        }
    }
}
