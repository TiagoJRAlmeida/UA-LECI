public class JogoGalo implements JGaloInterface {
	
	private char jogador1, jogador2;
	private char[][] table;
	private int nJogadas;
	
	public JogoGalo() {
		this.jogador1 = 'X';
		this.jogador2 = 'O';
		this.nJogadas = 0;
		this.table = new char[3][3];
	}

	public JogoGalo(String jogador) {
		this.jogador1 = jogador.toUpperCase().charAt(0);
		if (this.jogador1 == 'X' || this.jogador1 == 'x') {
			this.jogador2 = 'O';
		} else if (this.jogador1 == 'O' || this.jogador1 == 'o') {
			this.jogador2 = 'X';
		} else {
			System.err.println("When choosing the player please select 'X' or 'O'");
			System.exit(1);
		}
		this.nJogadas = 0;
		this.table = new char[3][3];
	}
	
	
	@Override
	public char getActualPlayer() {
		if (nJogadas%2 == 0) {
			return jogador1;             // Por omissao, comeca por X
		}
		return jogador2;
	}
	
	@Override
	public boolean setJogada(int lin, int col) {  // matriz 3x3 -> cada linha e cada coluna vao de 1 ate 3
		lin--;
		col--;
		char jogador = getActualPlayer();
		if (lin >= 0 || lin < 3 || col >= 0 || col < 3 || this.table[lin][col] != '\0') {
			this.table[lin][col] = jogador;
			this.nJogadas++;
			return true;
		}
		else {
			return false;
		}
	}
	
	@Override
	public boolean isFinished() {
		if (checkResult() != ' ' || this.nJogadas == 9 ) {
			return true;
		}
		return false;
		
	}

	@Override
	public char checkResult() {

        

		// Check Diagonals
		if ((this.table[0][0] != '\0') && (this.table[0][0]==this.table[1][1]) && (this.table[0][0]==this.table[2][2])) {
			return this.table[0][0];
		}
		if ((this.table[2][0] != '\0') && (this.table[2][0]==this.table[1][1]) && (this.table[2][0]==this.table[0][2])) {
			return this.table[2][0];
		}

		// Check Rows
		for (int i=0; i<3; i++) {
			if ((this.table[i][0] != '\0') && (this.table[i][0]==this.table[i][1]) && (this.table[i][0]==this.table[i][2])) {
				return this.table[i][0];
				
			}
		}
		
		// Check Columns
		for (int j=0; j<3; j++) {
			if ((this.table[0][j] != '\0') && (this.table[0][j]==this.table[1][j]) && (this.table[0][j]==this.table[2][j])) {
				return this.table[0][j];
			}
		}
		
       

        return ' ';
	}

}