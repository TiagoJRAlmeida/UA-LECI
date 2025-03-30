import java.util.HashMap;

import startypes.*;

public class StarPool {
    private static HashMap<Character, StarType> starTypes = new HashMap<>();

    public static StarType getStarType(char type, int x, int y) {
        if(starTypes.get(type) == null) {
            switch (type) {
                case 'O':
                    starTypes.put(type, new OStar(x, y));
                    break;
                case 'B':
                    starTypes.put(type, new BStar(x, y));
                    break;
                case 'A':
                    starTypes.put(type, new AStar(x, y));
                    break;
                case 'F':
                    starTypes.put(type, new FStar(x, y));
                    break;
                case 'G':
                    starTypes.put(type, new GStar(x, y));
                    break;
                case 'K':
                    starTypes.put(type, new KStar(x, y));
                    break;
                case 'M':
                    starTypes.put(type, new MStar(x, y));
                    break;
            }
        }
        
        return starTypes.get(type);
    }
}
