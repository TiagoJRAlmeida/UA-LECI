import java.util.ArrayList;
import java.util.Iterator;

public class Manager {
    // Função que vai encontrar as palavras
    public WordLocation find_word(char[][] ws, String word){
        for(int row = 0; row < 15; row++){
            for(int column = 0; column < 15; column++){
                if(ws[column][row] == Character.toLowerCase(word.charAt(0))){
                    Direction direction = find_direction(ws, word, row, column); 
                    if(direction != null) return new WordLocation(row, column, direction);
                }
            }
        }

        // Se não encontrar a palavra, retornar null
        return null;
    }


    public Direction find_direction(char[][] ws, String word, int row, int column) {
        ArrayList<Direction> possible_directions = new ArrayList<>();
        int word_length = word.length() - 1;

        if (row - word_length >= 0) possible_directions.add(Direction.UP);
        if (row - word_length >= 0 && column + word_length <= 14) possible_directions.add(Direction.UPRIGHT);
        if (column + word_length <= 14) possible_directions.add(Direction.RIGHT);
        if (row + word_length <= 14 && column + word_length <= 14) possible_directions.add(Direction.DOWNRIGHT);
        if (row + word_length <= 14) possible_directions.add(Direction.DOWN);
        if (row + word_length <= 14 && column - word_length >= 0) possible_directions.add(Direction.DOWNLEFT);
        if (column - word_length >= 0) possible_directions.add(Direction.LEFT);
        if (row - word_length >= 0 && column - word_length >= 0) possible_directions.add(Direction.UPLEFT);

        Iterator<Direction> iterator = possible_directions.iterator();
        while (iterator.hasNext()) {
            Direction direction = iterator.next();
            switch (direction) {
                case UP:
                    if (ws[column][row - 1] != word.charAt(1)) iterator.remove();
                    break;
                case UPRIGHT:
                    if (ws[column + 1][row - 1] != word.charAt(1)) iterator.remove();
                    break;
                case RIGHT:
                    if (ws[column + 1][row] != word.charAt(1)) iterator.remove();
                    break;
                case DOWNRIGHT:
                    if (ws[column + 1][row + 1] != word.charAt(1)) iterator.remove();
                    break;
                case DOWN:
                    if (ws[column][row + 1] != word.charAt(1)) iterator.remove();
                    break;
                case DOWNLEFT:
                    if (ws[column - 1][row + 1] != word.charAt(1)) iterator.remove();
                    break;        // Check valid directions

                case LEFT:
                    if (ws[column - 1][row] != word.charAt(1)) iterator.remove();
                    break;
                case UPLEFT:
                    if (ws[column - 1][row - 1] != word.charAt(1)) iterator.remove();
                    break;
            }
        }

        if (possible_directions.isEmpty()) return null;

        for (Direction direction : possible_directions) {
            int aux_row = row, aux_column = column, count = 0;

            switch (direction) {
                case UP:
                    while (count < word.length() - 1 && ws[aux_column][aux_row] == Character.toLowerCase(word.charAt(count))) {
                        count++;
                        aux_row--;
                    }
                    if (count == word.length() - 1) return Direction.UP;
                    break;

                case UPRIGHT:
                    while (count < word.length() - 1 && ws[aux_column][aux_row] == Character.toLowerCase(word.charAt(count))) {
                        count++;
                        aux_row--;
                        aux_column++;
                    }
                    if (count == word.length() - 1) return Direction.UPRIGHT;
                    break;

                case RIGHT:
                    while (count < word.length() - 1 && ws[aux_column][aux_row] == Character.toLowerCase(word.charAt(count))) {
                        count++;
                        aux_column++;
                    }
                    if (count == word.length() - 1) return Direction.RIGHT;
                    break;

                case DOWNRIGHT:
                    while (count < word.length() - 1 && ws[aux_column][aux_row] == Character.toLowerCase(word.charAt(count))) {
                        count++;
                        aux_row++;
                        aux_column++;
                    }
                    if (count == word.length() - 1) return Direction.DOWNRIGHT;
                    break;

                case DOWN:
                    while (count < word.length() - 1 && ws[aux_column][aux_row] == Character.toLowerCase(word.charAt(count))) {
                        count++;
                        aux_row++;
                    }
                    if (count == word.length() - 1) return Direction.DOWN;
                    break;

                case DOWNLEFT:
                    while (count < word.length() - 1 && ws[aux_column][aux_row] == Character.toLowerCase(word.charAt(count))) {
                        count++;
                        aux_row++;
                        aux_column--;
                    }
                    if (count == word.length() - 1) return Direction.DOWNLEFT;
                    break;

                case LEFT:
                    while (count < word.length() - 1 && ws[aux_column][aux_row] == Character.toLowerCase(word.charAt(count))) {
                        count++;
                        aux_column--;
                    }
                    if (count == word.length() - 1) return Direction.LEFT;
                    break;

                case UPLEFT:
                    while (count < word.length() - 1 && ws[aux_column][aux_row] == Character.toLowerCase(word.charAt(count))) {
                        count++;
                        aux_row--;
                        aux_column--;
                    }
                    if (count == word.length() - 1) return Direction.UPLEFT;
                    break;
            }
        }

        return null;
    }
}
