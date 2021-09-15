import java.awt.Graphics;
import java.awt.Color;
import java.applet.Applet;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;

public class TicTacToe extends Applet implements MouseListener{
	int mouseX, mouseY;
	Board board = new Board();
	// end = 1 is player win,  end = 0 is tie
	boolean outline = false;
	int end = 2;
	int player = (int)(Math.random()*2);
	char turn;
	int spots = 0;
	
	public void init() {
		if (player == 0) turn = 'X';
		else turn = 'O';
		setBackground(Color.BLACK);
		addMouseListener(this);
		try {
			Thread.sleep(20);
		} catch (Exception e) {
			
		}
		setSize(1050, 700);
	}
	
	public void paint(Graphics g) {
		g.setColor(Color.GREEN);
		board.display(g);
		g.setColor(Color.CYAN);
		if (end == 0) {
			g.drawString("It's a tie...", 600, 400);
			board.reset();
			end = 2;
		}
		if (end == 1) {
			g.drawString("Player " + board.checkWin() + " wins!!!", 600, 400);
			board.reset();
			end = 2;
		}
		//g.drawString("(" + mouseX + ", " + mouseY + ")", mouseX , mouseY);
		//if (outline) {
		//	g.setColor(Color.YELLOW);
		//	g.drawRect(mouseX, mouseY, 60, 30);
		//	g.setColor(Color.GREEN);
		//}
		//if (mouseX != -1 && mouseY != -1) System.out.println(mouseX + ", " + mouseY);
	}
	
	public void mouseClicked(MouseEvent e) {
		mouseX = e.getX();
		mouseY = e.getY();
		int[] coordinates = board.findPiece(mouseX, mouseY);
		if (board.add(coordinates[0], coordinates[1], coordinates[2], turn)) {
			if (turn == 'X') turn = 'O';
			else turn = 'X';
			spots++;
		}
		if (board.checkWin() != ' ') end = 1;
		if (board.checkWin() == ' ' && spots == 64) end = 0;
		repaint();
	}
	public void mousePressed(MouseEvent e) {}
	public void mouseReleased(MouseEvent e) {}
	public void mouseEntered(MouseEvent e) {
		//mouseX = e.getX();
		//mouseY = e.getY();
		//if (board.findPiece(mouseX, mouseY)[0] != -1 && board.findPiece(mouseX, mouseY)[1] != -1 && board.findPiece(mouseX, mouseY)[2] != -1) {
		//	outline = true;
		//}
	}
	public void mouseExited(MouseEvent e) {}
}



