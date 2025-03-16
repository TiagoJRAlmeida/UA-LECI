import java.util.Arrays;

public class JGaloLogic implements JGaloInterface{
    static char currentPlay = 'O';
    static char[][] JGaloBoard = new char[3][3];

    public char currentPlayer(){
        return currentPlay;
    }


    public boolean play(int lin, int col){
        if(JGaloBoard[lin-1][col-1] == '\0'){
            JGaloBoard[lin-1][col-1] = currentPlay;
            if(currentPlay == 'X') currentPlay = 'O';
            else currentPlay = 'X';
            return true;
        }
        return false;
    }

    
    public boolean JGaloBoardFull(char[][] JGaloBoard){
        for(int i = 0; i < 3; i++){
            for(int j = 0; j < 3; j++){
                if(JGaloBoard[j][i] == '\0') return false;
            }
        }

        return true;
    }


    public boolean CheckXPlayerWon(char[][] JGaloBoard){
        // Verificar se Ganhou pela horizontal
        for(int i = 0; i < 3; i++){
            if(Arrays.equals(JGaloBoard[i], new char[]{'X', 'X', 'X'})){
                return true;
            }
        }
        
        // Verificar se Ganhou pela vertical
        for(int i = 0; i < 3; i++){
            char[] column = new char[3];
            for(int j = 0; j < 3; j++){
                column[j] = JGaloBoard[j][i];
            }
            if(Arrays.equals(column, new char[]{'X', 'X', 'X'})){
                return true;
            }
        }

        // Verificar se Ganhou pela diagonal
        if(JGaloBoard[1][1] != 'X') return false;
        char[] diagonal1 = {JGaloBoard[0][0], JGaloBoard[1][1], JGaloBoard[2][2]}; 
        char[] diagonal2 = {JGaloBoard[0][2], JGaloBoard[1][1], JGaloBoard[2][0]};
        if(Arrays.equals(diagonal1, new char[]{'X', 'X', 'X'}) || Arrays.equals(diagonal2, new char[]{'X', 'X', 'X'}))
            return true;
        
        return false;
    }


    public boolean CheckOPlayerWon(char[][] JGaloBoard){
        // Verificar se Ganhou pela horizontal
        for(int i = 0; i < 3; i++){
            if(Arrays.equals(JGaloBoard[i], new char[]{'O', 'O', 'O'})){
                return true;
            }
        }
        
        // Verificar se Ganhou pela vertical
        for(int i = 0; i < 3; i++){
            char[] column = new char[3];
            for(int j = 0; j < 3; j++){
                column[j] = JGaloBoard[j][i];
            }
            if(Arrays.equals(column, new char[]{'O', 'O', 'O'})){
                return true;
            }
        }

        // Verificar se Ganhou pela diagonal
        if(JGaloBoard[1][1] != 'O') return false;
        char[] diagonal1 = {JGaloBoard[0][0], JGaloBoard[1][1], JGaloBoard[2][2]}; 
        char[] diagonal2 = {JGaloBoard[0][2], JGaloBoard[1][1], JGaloBoard[2][0]};
        if(Arrays.equals(diagonal1, new char[]{'O', 'O', 'O'}) || Arrays.equals(diagonal2, new char[]{'O', 'O', 'O'}))
            return true;
        
        return false;
    }


    public boolean finished(){
        return (JGaloBoardFull(JGaloBoard) || CheckXPlayerWon(JGaloBoard) || CheckOPlayerWon(JGaloBoard));
    }


    public char result(){
        if(CheckXPlayerWon(JGaloBoard)) return 'X';
        else if(CheckOPlayerWon(JGaloBoard)) return 'O';
        else return ' ';
    }
}
