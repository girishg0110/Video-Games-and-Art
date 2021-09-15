import java.awt.*;

public class Paddle {
	private int x;
	private int y;
	private Color color;
	private int score = 0;
	private int length, width = 20;
	
	public Paddle(int x, int y, Color color) {
		this.x = x;
		this.y = y;
		this.color = color;
		length = 50;
	}
	
	public Paddle(int x, int y, Color color, int length) {
		this(x, y, color);
		this.length = length;
	}
	
	public void update(int y, int height) {
		if (y - length/2 >= 0 || y + length/2 <= height) this.y = y;
	}
	
	public void pointScored() { score++; }
	public int getScore() { return score; }
	
	public int getX() { return x; }
	public int getY() { return y; }
	
	public void display(Graphics g) {
		g.setColor(color);
		g.fillRect(x - width/2, y - length/2, width, length*2);
	}
}