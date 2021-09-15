import java.awt.*;

public class Board {
	private Piece[][][] pieces;
	public Board() {
		pieces = new Piece[4][4][4]; // all null right now
	}
	
	public boolean add(int level, int row, int column, char turn) {
		if (level < 0 || row < 0 || column < 0) return false;
		if (pieces[level][row][column] == null) {
			pieces[level][row][column] = new Piece(turn);
			return true;
		}
		return false;
	}
	
	public int[] findPiece(int x, int y) {
		int[] location = {-1, -1, -1};
		for (int l = 0; l < 4; l++) {
			for (int r = 0; r < 4; r++) {
				for (int c = 0; c < 4; c++) {
					if (x > 340 - 30*r + 60*c && y > 50 + 150 * l + 30*r && x < 350 - 30*r - 10 + 60*c + 60 && y < 80 + 150 * l + 30*r) {
						location[0] = l;
						location[1] = r;
						location[2] = c;
						return location;
					}	
				}
			}
		}
		return location;
	}
	
	private void displayRow(int x, int y, int level, int row, Graphics g) {
		g.setFont(new Font("Consolas", Font.BOLD, 50));
		g.setColor(Color.GREEN);
		for (int c = 0; c < 4; c++) {
			//g.drawRect(x - 10 + 60*c, y-30, 60, 30);
			if (row == 0) g.drawLine(x + 60*c, y-30, x - 120 + 60*c, y + 90);
			g.drawLine(x + 60*c, y-30, x + 60+ 60*c, y -30); 
			if (pieces[level][row][c] == null)	g.drawString(" ", x + c*60, y-2);
			else g.drawString(pieces[level][row][c].getSymbol()+"", x + c*60, y-2);
		}
	}
	
	private void displayLevel(int x, int y, int level, Graphics g) {
		g.setColor(Color.GREEN);
		for (int r = 0; r < 4; r++) {
			displayRow(x - 30*r, y + 30*r, level, r, g);
			g.drawLine(x + 60*4, y-30, x - 120 + 60*4, y + 90);
			g.drawLine(x - 120 + 60*r, y + 90, x - 60 + 60*r, y + 90); 
		} 
	}

	public void display(Graphics g) {
		g.setColor(Color.GREEN);
		for (int l = 0; l < 4; l++) {
			displayLevel(350, 80 + 150 * l, l, g);
		}
	}
	
	public char checkWin() {
		/* 2D */
		// Horizontal
		for (int l = 0; l < 4; l++) {
			for (int r = 0; r < 4; r++) {
				if (pieces[l][r][0] != null && pieces[l][r][1] != null && pieces[l][r][2] != null && pieces[l][r][3] != null) {
					if (pieces[l][r][0].getSymbol() == pieces[l][r][1].getSymbol() && pieces[l][r][1].getSymbol() == pieces[l][r][2].getSymbol() && pieces[l][r][2].getSymbol() == pieces[l][r][3].getSymbol() && pieces[l][r][3].getSymbol() != ' ') return pieces[l][r][0].getSymbol();
				}
			}
		}
		
		// Vertical
		for (int l = 0; l < 4; l++) {
			for (int c = 0; c < 4; c++) {
				if (pieces[l][0][c] != null && pieces[l][1][c] != null && pieces[l][2][c] != null && pieces[l][3][c] != null) {
					if (pieces[l][0][c].getSymbol() == pieces[l][1][c].getSymbol() && pieces[l][1][c].getSymbol() == pieces[l][2][c].getSymbol() && pieces[l][2][c].getSymbol() == pieces[l][3][c].getSymbol() && pieces[l][3][c].getSymbol() != ' ') return pieces[l][3][c].getSymbol();
				}
			}
		}
		
		// Diagonal -> x = y
		for (int l = 0; l < 4; l++) {
			if (pieces[l][0][3] != null && pieces[l][1][2] != null && pieces[l][2][1] != null && pieces[l][3][0] != null) {
				if (pieces[l][0][3].getSymbol() == pieces[l][1][2].getSymbol() && pieces[l][1][2].getSymbol() == pieces[l][2][1].getSymbol() && pieces[l][2][1].getSymbol() == pieces[l][3][0].getSymbol() && pieces[l][3][0].getSymbol() != ' ') return pieces[l][3][0].getSymbol();
			}
		}
		
		// Diagonal -> x = -y
		for (int l = 0; l < 4; l++) {
			if (pieces[l][0][0] != null && pieces[l][1][1] != null && pieces[l][2][2] != null && pieces[l][3][3] != null) {
				if (pieces[l][0][0].getSymbol() == pieces[l][1][1].getSymbol() && pieces[l][1][1].getSymbol() == pieces[l][2][2].getSymbol() && pieces[l][1][1].getSymbol() == pieces[l][3][3].getSymbol() && pieces[l][3][3].getSymbol() != ' ') return pieces[l][1][1].getSymbol();
			}
		}
		
		/* 3D */
		// Vertical
		for (int c = 0; c < 4; c++) {
			for (int r = 0; r < 4; r++) {
				if (pieces[0][r][c] != null && pieces[1][r][c] != null && pieces[2][r][c] != null && pieces[3][r][c] != null) {
					if (pieces[0][r][c].getSymbol() == pieces[1][r][c].getSymbol() && pieces[1][r][c].getSymbol() == pieces[2][r][c].getSymbol() && pieces[2][r][c].getSymbol() == pieces[3][r][c].getSymbol() && pieces[2][r][c].getSymbol() != ' ') return pieces[3][r][c].getSymbol();
				}
			}
		}
		
		// Horizontal - TL to BoR
		for (int r = 0; r < 4; r++) {
			if (pieces[0][r][0] != null && pieces[1][r][1] != null && pieces[2][r][2] != null && pieces[3][r][3] != null) {
				if (pieces[0][r][0].getSymbol() == pieces[1][r][1].getSymbol() && pieces[1][r][1].getSymbol() == pieces[2][r][2].getSymbol() && pieces[2][r][2].getSymbol() == pieces[3][r][3].getSymbol() && pieces[2][r][2].getSymbol() != ' ') return pieces[3][r][3].getSymbol();
			}
		}
		
		// Horizontal - TR to BoL
		for (int r = 0; r < 4; r++) {
			if (pieces[0][r][3] != null && pieces[1][r][2] != null && pieces[2][r][1] != null && pieces[3][r][0] != null) {
				if (pieces[0][r][3].getSymbol() == pieces[1][r][2].getSymbol() && pieces[1][r][2].getSymbol() == pieces[2][r][1].getSymbol() && pieces[2][r][1].getSymbol() == pieces[3][r][0].getSymbol() && pieces[3][r][0].getSymbol() != ' ') return pieces[3][r][0].getSymbol();
			}
		}
		
		// Horizontal - TF to BoBa
		for (int c = 0; c < 4; c++) {
			if (pieces[0][3][c] != null && pieces[1][2][c] != null && pieces[2][1][c] != null && pieces[3][0][c] != null) {
				if (pieces[0][3][c].getSymbol() == pieces[1][2][c].getSymbol() && pieces[1][2][c].getSymbol() == pieces[2][1][c].getSymbol() && pieces[2][1][c].getSymbol() == pieces[3][0][c].getSymbol() && pieces[3][0][c].getSymbol() != ' ') return pieces[3][0][c].getSymbol();
			}
		}
		
		// Horizontal - TBa to BoF
		for (int c = 0; c < 4; c++) {
			if (pieces[0][0][c] != null && pieces[1][1][c] != null && pieces[2][2][c] != null && pieces[3][3][c] != null) {
				if (pieces[0][0][c].getSymbol() == pieces[1][1][c].getSymbol() && pieces[1][1][c].getSymbol() == pieces[2][2][c].getSymbol() && pieces[2][2][c].getSymbol() == pieces[3][3][c].getSymbol() && pieces[2][2][c].getSymbol() != ' ') return pieces[2][2][c].getSymbol();
			}
		}
		
		// Diagonal - TL to BoR
		if (pieces[0][0][0] != null && pieces[1][1][1] != null && pieces[2][2][2] != null && pieces[3][3][3] != null) {
			if (pieces[0][0][0].getSymbol() == pieces[1][1][1].getSymbol() && pieces[1][1][1].getSymbol() == pieces[2][2][2].getSymbol() && pieces[2][2][2].getSymbol() == pieces[3][3][3].getSymbol() && pieces[2][2][2].getSymbol() != ' ') return pieces[3][3][3].getSymbol();
		}
		// Diagonal - TR to BoL
		if (pieces[0][0][3] != null && pieces[1][1][2] != null && pieces[2][2][1] != null && pieces[3][3][0] != null) {
			if (pieces[0][0][3].getSymbol() == pieces[1][1][2].getSymbol() && pieces[1][1][2].getSymbol() == pieces[2][2][1].getSymbol() && pieces[2][2][1].getSymbol() == pieces[3][3][0].getSymbol() && pieces[2][2][1].getSymbol() != ' ') return pieces[3][3][0].getSymbol();
		}
		// Diagonal - BoR to TL
		if (pieces[0][3][3] != null && pieces[1][2][2] != null && pieces[2][1][1] != null && pieces[3][0][0] != null) {
			if (pieces[0][3][3].getSymbol() == pieces[1][2][2].getSymbol() && pieces[1][2][2].getSymbol() == pieces[2][1][1].getSymbol() && pieces[2][1][1].getSymbol() == pieces[3][0][0].getSymbol() && pieces[3][0][0].getSymbol() != ' ') return pieces[3][0][0].getSymbol();
		}
		// Diagonal - BoL to TR
		if (pieces[0][3][0] != null && pieces[1][2][1] != null && pieces[2][1][2] != null && pieces[3][0][3] != null) {
			if (pieces[0][3][0].getSymbol() == pieces[1][2][1].getSymbol() && pieces[1][2][1].getSymbol() == pieces[2][1][2].getSymbol() && pieces[2][1][2].getSymbol() == pieces[3][0][3].getSymbol() && pieces[3][0][3].getSymbol() != ' ') return pieces[3][0][3].getSymbol();
		}
		return ' ';
	}
	
	public void reset() {
		for (int l = 0; l < 4; l++) {
			for (int r = 0; r < 4; r++) {
				for (int c = 0; c < 4; c++) {
					pieces[l][r][c] = null;
				}
			}
		}
	}
	
}
