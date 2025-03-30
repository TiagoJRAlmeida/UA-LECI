package lab07.Ex02;

public class CapitalizationFilter extends Decorator {
    
    public CapitalizationFilter(ReaderInterface reader) {
        super(reader);
    }
    
    @Override
    public String next() {
        String word = super.next();
        if (word.length() > 1) {
            return Character.toUpperCase(word.charAt(0)) + word.substring(1, word.length()-1).toLowerCase() + Character.toUpperCase(word.charAt(word.length()-1));
        } else if (word.length() == 1) {
            return String.valueOf(Character.toUpperCase(word.charAt(0)));
        } else {
            return word;
        }
    }
}
