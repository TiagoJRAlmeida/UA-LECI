public class WordLocation {
    private String word;
    private Integer row, column;
    private Direction direction;


    public WordLocation(String word, Integer row, Integer column, Direction direction) {
        this.word = word;
        this.row = row;
        this.column = column;
        this.direction = direction;
    }


    public WordLocation(String word) {
        this(word, null, null, null);
    }


    public String getWord() {
        return this.word;
    }


    public Integer getRow() {
        return this.row;
    }


    public Integer getColumn() {
        return this.column;
    }


    public Direction getDirection() {
        return this.direction;
    }


    public void setWord(String word) {
        this.word = word;
    }


    public void setRow(Integer row) {
        this.row = row;
    }


    public void setColumn(Integer column) {
        this.column = column;
    }


    public void setDirection(Direction direction) {
        this.direction = direction;
    }
    

    @Override
    public String toString() {
        return String.format("%-12s %-6d %-8s %-8s",
            this.word,
            this.word.length(),
            (this.row != null ? (this.row + 1) : "N/A") + "," + 
            (this.column != null ? (this.column + 1) : "N/A"),
            (this.direction != null ? this.direction : "N/A"));
    }

}
