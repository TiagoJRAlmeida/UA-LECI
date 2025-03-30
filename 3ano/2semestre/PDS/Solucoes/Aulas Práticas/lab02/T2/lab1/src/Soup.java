import java.lang.Math;
public class Soup {
    private String[] puzzle;
    private int FirstFree;
    private int n;
    private static String chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    public Soup(int n) {
        //Create Solved Soup
        if(n>40){
            System.err.println("Invalid Size- too big");
            System.exit(-1);
        }
        this.puzzle=new String[n];
        this.n=n;
        this.FirstFree=0;
    }

    public int getN(){
        return this.n;
    }

    public boolean isCorrectSize(){
        return this.n == this.FirstFree;
    }
     
    /**
     * try to put word in puzzle 
     * if it can do it, it does and returns true
     * if it cant do it returns false
     */
    public boolean setword(Word wclass) {
        String word=wclass.getUpper();
        int size=word.length();

        //Direction to vector
        int[] vec = wclass.getDir().toVec();

        //Support Variables
        int px,py,n;

        for(n= 0 ; n < size ; n++){
            px = n*vec[0]+wclass.getCoords()[1]-1;
            py = n*vec[1]+wclass.getCoords()[0]-1;

            //invalid position
            if( !(px > -1 && px < this.n && py > -1 && py < this.n) || 
                // check if valid write
                !(this.puzzle[py].charAt(px) =='.' || this.puzzle[py].charAt(px)==word.charAt(n))){
                    return false;
            }
  
        }

        for (n = 0; n < size; n++) {
            px = n * vec[0] + wclass.getCoords()[1] - 1;
            py = n * vec[1] + wclass.getCoords()[0] - 1;
            this.puzzle[py] = this.puzzle[py].substring(0, px) + word.charAt(n) + this.puzzle[py].substring(px + 1);
        }
        
        return true;
    }
    
    public void fillEmpty(){
        String s = "";
        for(int n=0;n<this.n;n++){
            s+=".";
        }
        for(int n=0;n<this.n;n++){
            this.puzzle[n]=s;
        }
    }

    public void filler(){
        char []temp;
        for(int i=0;i<this.n;i++){
            temp=this.puzzle[i].toCharArray();
            for(int u=0;u<this.n;u++)
                if(temp[u]=='.')
                    temp[u]=Soup.chars.charAt((int)(Math.random()*26));   
            this.puzzle[i]=new String(temp);
        }
    }

    public int add(String str){
        //Invalid Size 
        if(this.FirstFree>=this.n){
            System.err.println("Invalid Size- non-square");
            System.exit(-1);
        }
        //Has non lower case
        if(str.matches("[a-z]")){
            System.err.println("Non Lower case letter found in line "+FirstFree);
            System.exit(-1);
        }

        //Add line to puzzle
        this.puzzle[this.FirstFree++] = String.valueOf(str);
        
        return FirstFree;
    }

    public String toString(){
        String s = "";
        int j;
        for(j = 0 ; j < this.n-1 ; j++){
            s+=puzzle[j]+"\n";
        }
        s += puzzle[j];
        return s;
    }
 
}
