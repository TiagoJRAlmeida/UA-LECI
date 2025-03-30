package lab07.Ex02;

import java.text.Normalizer;

public class NormalizationFilter extends Decorator {

    public NormalizationFilter(ReaderInterface reader) {
        super(reader);
    }
    
    @Override
    public String next() {
        return Normalizer.normalize(super.next(), Normalizer.Form.NFD).replaceAll("[^\\p{ASCII}]", "").replaceAll("\\p{Punct}", "");
    }
}
