import java.awt.Color;
import java.awt.Graphics;

public class Ball {
	private int x;
	private int y;
	private int speedX = (int)(Math.random()*10) + 50;
	private int speedY = (int)(Math.random()*10) + 70;
	
	public Ball(int x, int y) {
		this.x = x;
		this.y = y;
	}
	
	public void update(Paddle a, Paddle b, int height) {
		x += speedX;
		y += speedY;
		if (y + 20 > height || y - 20 < 0) speedY *= -1;
		if ((a.getX() + 10 >= x - 20 && a.getY() - 40 <= y && a.getY() + 40 >= y)|| (b.getX() - 10 <= x + 20 && b.getY() - 40 <= y && b.getY() + 40 >= y)) speedX *= -1;		
	}
	
	public void reset(int x, int y) { 
		this.x = x;
		this.y = y;
	}
	
	public int getY() { return y; }
	
	private Color randColor() {
		switch((int)(Math.random()*5)) {
			case 0:
				return Color.MAGENTA;
			case 1:
				return Color.BLUE;
			case 2:
				return Color.ORANGE;
			case 3:
				return Color.GREEN;
			case 4:
				return Color.YELLOW;
		}
		
		return Color.PINK;
	}
	
	public boolean point(Paddle a, int width) {
		if (a.getX() > width/2 && x > width + 20) { return true; }
		if (a.getX() < width/2 && x < -20) { return true; }
		return false;
	}
	
	public void display(Graphics g) {
		g.setColor(randColor());
		g.fillOval(x - 20, y - 20, 40, 40);
	}
}