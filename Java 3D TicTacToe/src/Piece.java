
public class Piece {
	private char symbol;
	
	public Piece(char symbol) {
		this.symbol = symbol;
	}
		
	public char getSymbol() {
		return symbol;
	}
	
	public boolean isX() {
		if (symbol == 'x') return true;
		return false;
	}

	public boolean isO() {
		if (symbol == 'o') return true;
		return false;
	}
}
