package lab03.JogodoGalo;

public class GaloGame implements JGaloInterface {

    private char[][] grid;
    private char currentPlayer; 
    private int plays;
    
    
    public GaloGame(){               //construtor sem argumento
        this('X');                 
    }

    public GaloGame(char arg){               //construtor com argumento
        currentPlayer = arg;        
        grid = new char[3][3];   //matriz 3x3 com valor default nulo (0)
        plays = 0;                  
    }
    public char getActualPlayer() {
        return this.currentPlayer;
    }
    

    public boolean setJogada(int lin, int col) {
        boolean control = true;
        
        grid[lin-1][col-1] = currentPlayer;
        this.plays++;
        return control;
    }

    public boolean isFinished() {
        
         if (this.plays == 9 || checkResult() != ' ') {  //verifica se foram executadas 9 jogadas ou se algum jogador ganhou
            return true;
        } else {
            this.currentPlayer = this.getActualPlayer() == 'X' ? 'O' : 'X'; //ainda nÃ£o acabou o jogo, trocar de jogador
            return false;
        }        
    }


    public char checkResult() {
        
        char result = ' ';   //empate (valor default)
        
        //Verificar linhas completas
        for (int l = 0; l < 3; l++) {
            if (this.grid[l][0] == this.grid[l][1] && this.grid[l][1] == this.grid[l][2] && this.grid[l][0] != 0) {
                result = this.grid[l][0];
            }
        }

        //Verificar colunas completas
        for (int c = 0; c < 3; c++) {
            if (this.grid[0][c] == this.grid[1][c] && this.grid[1][c] == this.grid[2][c] && this.grid[0][c] != 0) {
                result = this.grid[0][c];
            }
        }

        //Verificar diagonais completas
        if (this.grid[0][0] == this.grid[1][1] && this.grid[1][1] == this.grid[2][2] && this.grid[0][0] != 0) {
            result = this.grid[0][0];
        } else if (this.grid[2][0] == this.grid[1][1] && this.grid[1][1] == this.grid[0][2] && this.grid[2][0] != 0) {
            result = this.grid[2][0];
        }
        return result;
    }
}