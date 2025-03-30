package lab09.Ex01;

public interface Vector<T> {
    public java.util.Iterator<T> Iterator();
    public java.util.ListIterator<T> listIterator();
    public java.util.ListIterator<T> listIterator(int index);
}
