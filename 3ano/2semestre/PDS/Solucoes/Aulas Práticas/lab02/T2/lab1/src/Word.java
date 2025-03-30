public class Word {
    private int siz;
    private DIRECTION dir;
    private int[] coords;
    private String word;
    private String upper;

    public Word(DIRECTION dir, int[] coords, String word) {
        this.siz = word.length();
        this.dir = dir;
        this.coords = coords;
        this.word = word;
        this.upper = word.toUpperCase();
    }

    public Word(String word){
        if(!word.matches("[a-zA-Z]+")||word.length()<3)
            return;
        this.word = word;
        this.upper = word.toUpperCase();
        this.siz = word.length();
        this.dir = DIRECTION.None;
        this.coords = new int[]{-1,-1};
    }

    public DIRECTION getDir() {
        return this.dir;
    }

    public int[] getCoords() {
        return this.coords;
    }

    public String getWord() {
        return this.word;
    }

    public String getUpper() {
        return this.upper;
    }

    public void setDir(DIRECTION dir){
        this.dir=dir;
    }

    public void setCoords(int[] coords){
        this.coords=coords;
    }

    public boolean solve(Soup s){
        for(int x = 1 ; x <= s.getN() ; x++)
            for(int y = 1 ; y <= s.getN() ; y++)
                for(DIRECTION dir : DIRECTION.values())
                    if(s.setword( new Word(dir,new int[]{y,x},this.word)) ){
                        this.coords=new int[]{y,x};
                        this.dir=dir;
                        return true;
                    }

        return false;
    }

    @Override
    public String toString(){
        return String.format("%-15s %5d %5d,%-5d %10s",this.word,this.siz,this.coords[0],this.coords[1],this.dir.toString());
    }
}
