import java.util.ArrayList;

public class WordFinder {
    private static DirectionHelper dh = new DirectionHelper();

    private boolean MatchesFirstCharacter(char[][] ws, String word, int row, int column, Direction direction) {
        int dx = dh.GetDirectionX(direction);
        int dy = dh.GetDirectionY(direction);
        return ws[column + dx][row + dy] == word.charAt(1);
    }


    private boolean WordFits(char[][] ws, String word, int row, int column, Direction direction) {
        int dx = dh.GetDirectionX(direction);
        int dy = dh.GetDirectionY(direction);
    
        for (int i = 0; i < word.length(); i++) {
            if (ws[column][row] != Character.toLowerCase(word.charAt(i))) {
                return false;
            }
            column += dx;
            row += dy;
        }
        return true;
    }


    public void FindWord(WordLocation solution, char[][] ws){
        for(Integer row = 0; row < 15; row++){
            for(Integer column = 0; column < 15; column++){
                if(ws[column][row] == Character.toLowerCase(solution.getWord().charAt(0))){
                    Direction direction = FindDirection(ws, solution.getWord(), row, column); 
                    if(direction != null) {
                        solution.setRow(row);
                        solution.setColumn(column);;
                        solution.setDirection(direction);;
                        return;
                    }
                }
            }
        }
    }


    public Direction FindDirection(char[][] ws, String word, int row, int column) {
        ArrayList<Direction> possibleDirections = new ArrayList<>();
        int word_length = word.length() - 1;
        int[] coordinates = {column, row};
    
        for (Direction direction : Direction.values()) {
            if (dh.IsWithinBounds(direction, coordinates, word_length)) {
                possibleDirections.add(direction);
            }
        }
    
        possibleDirections.removeIf(direction -> !MatchesFirstCharacter(ws, word, row, column, direction));
    
        if (possibleDirections.isEmpty()) return null;
    
        for (Direction direction : possibleDirections) {
            if (WordFits(ws, word, row, column, direction)) {
                return direction;
            }
        }
    
        return null;
    }
}
