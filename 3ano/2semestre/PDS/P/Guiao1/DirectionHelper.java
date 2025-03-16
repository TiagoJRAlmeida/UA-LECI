public class DirectionHelper {
    public int GetDirectionX(Direction direction) {
        switch (direction) {
            case LEFT: case UPLEFT: case DOWNLEFT: return -1;
            case RIGHT: case UPRIGHT: case DOWNRIGHT: return 1;
            default: return 0;
        }
    }
    

    public int GetDirectionY(Direction direction) {
        switch (direction) {
            case UP: case UPLEFT: case UPRIGHT: return -1;
            case DOWN: case DOWNLEFT: case DOWNRIGHT: return 1;
            default: return 0;
        }
    }


    public boolean IsWithinBounds(Direction direction, int[] coordinates, int wordSize) {
        int x = coordinates[0];
        int y = coordinates[1];

        switch (direction) {
            case UP: return y - wordSize >= 0;
            case UPRIGHT: return x + wordSize < 15 && y - wordSize >= 0;
            case RIGHT: return x + wordSize < 15;
            case DOWNRIGHT: return x + wordSize < 15 && y + wordSize < 15;
            case DOWN: return y + wordSize < 15;
            case DOWNLEFT: return x - wordSize >= 0 && y + wordSize < 15;
            case LEFT: return x - wordSize >= 0;
            case UPLEFT: return x - wordSize >= 0 && y - wordSize >= 0;
            default: return false;
        }
    }
}
