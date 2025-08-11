// PDS, lab03 
package aula03.ex1;

public interface JGaloInterface {
	public char currentPlayer(); 			// 'O' or 'X'
	public boolean play(int lin, int col);
	public boolean finished();   			// someone wons, or no empty positions
	public char result();					// who won?
}