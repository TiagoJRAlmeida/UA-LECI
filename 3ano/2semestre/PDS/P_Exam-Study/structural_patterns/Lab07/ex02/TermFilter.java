package ex02;

public class TermFilter extends TextReaderDecorator {
    private TextReader tr;

    public TermFilter(TextReader tr){
        super(tr);
    }

    
}
