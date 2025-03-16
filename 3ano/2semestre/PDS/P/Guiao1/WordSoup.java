import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class WordSoup {
    private char[][] WS;
    private ArrayList<WordLocation> solutions;

    public WordSoup() {
        this.WS = new char[15][15];
        this.solutions = null;
    }


    public void loadWS(String path){
        char[][] word_soup = new char[15][15];
        int line_counter = 0;
        
        try (BufferedReader br = new BufferedReader(new FileReader(path))) {
            String line;
            while ((line = br.readLine()) != null) {
                for(int i = 0; i < 15; i++ ){
                    try{
                        word_soup[i][line_counter] = Character.toLowerCase(line.charAt(i));
                    } catch(Exception e) {
                        System.out.println("Erro ao ler a sopa de letras: " + e.getMessage());
                        System.exit(1);
                    }
                }
                if(line_counter == 14) {
                    this.WS = word_soup;
                    return;
                } 
                line_counter += 1;
            }
            
            System.out.println("Numero insuficiente de linhas");    
            System.exit(1);
        } catch (IOException e) {
            System.out.println("Erro ao ler o ficheiro: " + e.getMessage());
            System.exit(1);
        }
    }


    public void loadSolutions(String path) {
        ArrayList<String> wordList = new ArrayList<>();
        String regex = "[,; ]+";
    
        try (BufferedReader br = new BufferedReader(new FileReader(path))) {
            String line;
            while ((line = br.readLine()) != null) { 
                String[] new_solutions = line.split(regex);
                for (String word : new_solutions) {
                    if (word.length() >= 3 && Character.isUpperCase(word.charAt(0)) && word.matches("[a-zA-Z]+")) {
                        wordList.add(word.toLowerCase());
                    }
                }
            }
        } catch (IOException e) {
            System.out.println("Erro ao ler o ficheiro: " + e.getMessage());
            System.exit(1);
        }
    
        // Ordenar por tamanho decrescente para garantir que a maior palavra aparece primeiro
        wordList.sort((a, b) -> Integer.compare(b.length(), a.length()));
    
        ArrayList<WordLocation> solutions = new ArrayList<>();
    
        for (String word : wordList) {
            boolean isSubstring = false;
    
            // Verificar se a palavra já está contida numa palavra maior
            for (WordLocation existing : solutions) {
                if (existing.getWord().contains(word)) {
                    isSubstring = true;
                    break;
                }
            }
    
            if (!isSubstring) {
                solutions.add(new WordLocation(word));
            }
        }
    
        this.solutions = solutions;
    }
    


    public char[][] getWS(){
        return this.WS;
    }


    public ArrayList<WordLocation> getSolutions(){
        return this.solutions;
    }


    public void setWS(char[][] wS) {
        WS = wS;
    }


    public void setSolutions(ArrayList<WordLocation> solutions) {
        this.solutions = solutions;
    }


    public String toString() {
        StringBuilder sb = new StringBuilder();
    
        for (char[] row : this.WS) {
            sb.append(row).append("\n");
        }
    
        for (WordLocation s : this.solutions) {
            String word = s.getWord();
            String formattedWord = word.substring(0, 1).toUpperCase() + word.substring(1).toLowerCase();
            sb.append(formattedWord).append("\n");
        }
    
        return sb.toString();
    }
}
