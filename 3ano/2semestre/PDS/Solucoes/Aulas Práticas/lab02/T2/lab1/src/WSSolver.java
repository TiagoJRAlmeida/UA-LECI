import java.io.File;
import java.util.Scanner;
import java.io.FileNotFoundException;

public class WSSolver {

    public static void main(String[] args) throws Exception {
        try {
            File puzzle = new File(args[0]);
            Scanner reader = new Scanner(puzzle);
            String data = reader.nextLine();
            int n = data.length();
            int counter=0;
            Word[] words=new Word[10];

            Soup soup = new Soup(n);

            //put things in soup
            soup.add(data);
            while (reader.hasNextLine()) {
                data = reader.nextLine();
                int s = soup.add(data);
                if (s >= n) {
                    break;
                }
            }

            // Check if its square
            assert soup.isCorrectSize();

            // this soup is for printing
            Soup solved = new Soup(n);
            solved.fillEmpty();

            reader.useDelimiter("[,;\r\n ]");
            while (reader.hasNext()) {
                data = reader.next();
                Word w = new Word(data);
                // solve non null words 
                if (w.getWord()!=null) {
                    for(int i=0;i<counter;i++){
                        if(words[i].getWord().contains(w.getWord())){
                            break;
                        }
                        if(w.getWord().contains(words[i].getWord())){
                            words[i]=w;
                            break;
                        }
                    }
                    if(counter==words.length){
                        Word[]temp=new Word[words.length+10];
                        words=temp;
                    }
                    words[counter]=w;
                    counter++;
                }
            }
            for(int o=0;o<counter;o++){
                Word w=words[o];
                if(w.solve(soup)){
                    System.out.println(w.toString());
                    solved.setword(w);
                }
                
            }
            
            // print solved grid
            System.out.println("\n"+solved);
            reader.close();
        } catch (FileNotFoundException e) {
            System.out.println("Couldnt open file.");
            e.printStackTrace();
        }
    }

    
}
