package lab07.Ex02;

public class VowelFilter extends Decorator {
    
        public VowelFilter(ReaderInterface reader) {
            super(reader);
        }
        
        @Override
        public String next() {
            String word = super.next();
            String newWord = "";
            for (int i = 0; i < word.length(); i++) {
                if (word.charAt(i) != 'a' && word.charAt(i) != 'e' && word.charAt(i) != 'i' && word.charAt(i) != 'o' && word.charAt(i) != 'u') {
                    newWord += word.charAt(i);
                }
            }
            return newWord;
        }
}
