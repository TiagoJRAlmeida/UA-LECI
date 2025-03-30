package lab09.Ex03;

import java.util.Collection;

public class AddCommand<E> implements Command {
    private Collection<E> collection;
    private E element;

    public AddCommand(Collection<E> collection, E element) {
        this.collection = collection;
        this.element = element;
    }
    
    @Override
    public void execute() {
        this.collection.add(this.element);
    }

    @Override
    public void undo() {
        this.collection.remove(this.element);
    }
    
}
