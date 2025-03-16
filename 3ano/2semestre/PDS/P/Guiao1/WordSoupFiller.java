import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.Random;

public class WordSoupFiller {
    private static DirectionHelper dh = new DirectionHelper();
    
    public void AddWordLettersToMap(WordLocation solution, Map<List<Integer>, Character> letterMap){
        int x = solution.getColumn();
        int y = solution.getRow();
        int dx = dh.GetDirectionX(solution.getDirection());
        int dy = dh.GetDirectionY(solution.getDirection());

        for(int i = 0; i < solution.getWord().length(); i++) {
            letterMap.put(Arrays.asList(x + i * dx, y + i * dy), Character.toUpperCase(solution.getWord().charAt(i)));
        }
    }


    public WordSoup FillWS(WordSoup soup){
        Random random = new Random();
        char[][] wsoup = soup.getWS();
        for(int i = 0; i < 15; i ++){
            for(int j = 0; j < 15; j ++){
                if(!Character.isLetter(wsoup[i][j])){
                    char c = (char)(random.nextInt(26) + 'a');
                    AddCharacterToWS(soup, i, j, c);
                }
            }
        }
        return soup;
    }

    
    public void AddCharacterToWS(WordSoup ws, int x, int y, char value) {
        char[][] wordSoup = ws.getWS();
        wordSoup[x][y] = value;
        ws.setWS(wordSoup);
    }
}
