package ex02;

public class TextReaderDecorator implements TextReader {
    private TextReader wrapper;

    public TextReaderDecorator(TextReader wrapper){
        this.wrapper = wrapper;
    }

    public boolean hasNext(){ return wrapper.hasNext(); }
    
    public String Next() {return wrapper.Next(); } 
    
}
