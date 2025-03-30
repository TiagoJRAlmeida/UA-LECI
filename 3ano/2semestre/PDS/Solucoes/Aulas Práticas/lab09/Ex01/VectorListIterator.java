package lab09.Ex01;

import java.util.ListIterator;
import java.util.NoSuchElementException;

public class VectorListIterator<T> implements ListIterator<T> {
    private VectorGeneric<T> vector;
    private int index;

    public VectorListIterator(VectorGeneric<T> vector, int index) {
        this.vector = vector;
        this.index = index;
    }

    @Override
    public boolean hasNext() {
        if (this.index < vector.totalElem()) {
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

    @Override
    public boolean hasPrevious() {
        if (this.index > 0) {
            return true;
        } else {
            return false;
        }
    }

    @Override
    public T previous() {
        if (hasPrevious()) {
            return vector.getElem(--index);
        } else {
            throw new NoSuchElementException("Operation not supported");
        }
    }

    @Override
    public int nextIndex() {
        return this.index + 1;
    }

    @Override
    public int previousIndex() {
        return this.index - 1;
    }

    @Override
    public void remove() {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'remove'");
    }

    @Override
    public void set(T e) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'set'");
    }

    @Override
    public void add(T e) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'add'");
    }
}
