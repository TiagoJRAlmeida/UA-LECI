import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Random;

public class WordPlacer {
    private static DirectionHelper dh = new DirectionHelper();
    private static WordSoupFiller wsf = new WordSoupFiller();

    public int[] GenerateStartPosition(WordSoup soup,String word){
        Random random = new Random();
        int x;
        int y;
        
        char[][] ws = soup.getWS();
        do{
            x = random.nextInt(15);
            y = random.nextInt(15);
        } while(Character.isLetter(ws[x][y]) && ws[x][y] != word.charAt(0));

        int[] coordinates = {x,y};

        return coordinates;
    }


    public boolean CheckValidWordPosition(WordSoup soup, String word, int[] coordinates, Direction direction){
        int dx = dh.GetDirectionX(direction);
        int dy = dh.GetDirectionY(direction);
        char[][] wsoup = soup.getWS();
        
        for (int i = 0; i < word.length(); i++) {
            int x = coordinates[0] + i * dx;
            int y = coordinates[1] + i * dy;

            if (Character.isLetter(wsoup[x][y]) && wsoup[x][y] != word.charAt(i)) {
                return false;
            }
        }
        return true;
    }


    public Direction GenerateValidDirection(WordSoup soup, String word, int[] coordinates) {
        Random random = new Random();
        int wordSize = word.length() - 1;

        List<Direction> directions = Arrays.asList(
            Direction.UP, Direction.UPRIGHT, Direction.RIGHT, Direction.DOWNRIGHT, 
            Direction.DOWN, Direction.DOWNLEFT, Direction.LEFT, Direction.UPLEFT
        );

        Collections.shuffle(directions, random);

        for (Direction direction : directions) {
            if (dh.IsWithinBounds(direction, coordinates, wordSize) &&
                CheckValidWordPosition(soup, word, coordinates, direction)) {
                return direction;
            }
        }

        return null;
    }


    public WordSoup InsertWord(WordSoup soup, WordLocation solution) {
        int x = solution.getColumn();
        int y = solution.getRow();
        int dx = dh.GetDirectionX(solution.getDirection());
        int dy = dh.GetDirectionY(solution.getDirection());

        for (int j = 0; j < solution.getWord().length(); j++) {
            wsf.AddCharacterToWS(soup, x + j * dx, y + j * dy, solution.getWord().charAt(j));
        }

        return soup;
    }
}
