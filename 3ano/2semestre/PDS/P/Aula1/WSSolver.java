import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


public class WSSolver {

    public static void main(String[] args){
        if(args.length != 1){
            System.out.println("Error: Number of arguments passed is wrong.");
            return;
        }

        WordFinder wf = new WordFinder();
        WordSoupFiller wsf = new WordSoupFiller();

        String path = args[0];
        WordSoup ws = new WordSoup();
        ws.loadWS(path);
        ws.loadSolutions(path);

        char[][] word_soup = ws.getWS();
        if(word_soup == null) return;

        ArrayList<WordLocation> solutions = ws.getSolutions();
        
        // Mapa que vai conter as letras associadas a cada coordenada
        Map<List<Integer>, Character> lettersPosition = new HashMap<>();

        for (WordLocation solution : solutions) {
            
            // Atualizar a solução atual com as informções sobre as suas coordenadas e direção 
            wf.FindWord(solution, word_soup);

            // Atualizar o mapa
            wsf.AddWordLettersToMap(solution, lettersPosition);

            System.out.println(solution);
        }

        StringBuilder sb = new StringBuilder();
        for (Integer i = 0; i < 15; i++) {
            sb.append("\n");
            for (Integer j = 0; j < 15; j++) {
                if (lettersPosition.containsKey(Arrays.asList(j, i))) sb.append(lettersPosition.get(Arrays.asList(j, i)));
                else sb.append("_");
            }
        }
        System.out.println(sb);

    }

}
