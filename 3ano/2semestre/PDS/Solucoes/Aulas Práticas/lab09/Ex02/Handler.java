package lab09.Ex02;

public interface Handler {
    public Handler setNext(Handler handler);
    public void handle(String request);
}
