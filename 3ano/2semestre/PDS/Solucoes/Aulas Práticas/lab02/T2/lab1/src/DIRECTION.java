public enum DIRECTION{
    Up,
    Down,
    Left,
    Right,
    UpLeft,
    UpRight,
    DownLeft,
    DownRight,
    None;

    public int[] toVec(){
        int[] r = new int[]{0,0};
        switch(this){
            case Up:
                return new int[]{0,-1};
            
            case Down:
                return new int[]{0,1};

            case Left:
                return new int[]{-1,0};

            case Right:
                return new int[]{1,0};
                
            case UpLeft:
                return new int[]{-1,-1};

            case UpRight:
                return new int[]{1,-1};

            case DownLeft:
                return new int[]{-1,1};

            case DownRight:
                return new int[]{1,1};

            default:
                break;
        }
        return r;
    }

    public static DIRECTION getRandom(){
        return DIRECTION.values()[(int)(Math.random()*8)];
    }
}