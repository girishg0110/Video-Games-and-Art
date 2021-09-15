import java.awt.*;
import java.awt.event.*;
import java.applet.Applet;
import javax.swing.Timer;

@SuppressWarnings("serial")
public class Pong extends Applet implements ActionListener, MouseMotionListener, MouseListener{
	
	//int width, height;
	Timer pongTimer = new Timer(30, this);
	int mouseY;
	Paddle player, enemy;
	Ball ball;
	boolean game = false;
	int pt;
	public void init() {
		try { Thread.sleep(200); } catch(InterruptedException e) {}
		
		setSize(1450, 775);
		setBackground(Color.BLACK);
		pongTimer.start();
		
		player = new Paddle(getWidth() - 50, getHeight()/2,  Color.CYAN, 100);
		enemy = new Paddle(50, getHeight()/2, Color.RED);
		ball = new Ball(getWidth()/2, getHeight()/2);
		
		addMouseMotionListener(this);
		addMouseListener(this);
	}
	
	public void paint(Graphics g) {
		player.display(g);
		enemy.display(g);
		ball.display(g);
		
		if (!game) displayScore(g);
	}
	
	public void actionPerformed(ActionEvent e) {
		if (game) {
			ball.update(enemy, player, getHeight());
			enemy.update(ball.getY(), getHeight());
			//
			player.update(ball.getY(), getHeight());
			if (ball.point(player, getWidth())) {
				enemy.pointScored();
				ball.reset(getWidth()/2, getHeight()/2);
				game = false;
			}
			if (ball.point(enemy, getWidth())) {
				player.pointScored();
				ball.reset(getWidth()/2, getHeight()/2);
				game = false;
			}
		}
		repaint();
	} 
	
	public void displayScore(Graphics g) {
		Font t = new Font("Times New Roman", 100, 100);
		g.setFont(t);
		g.setColor(Color.WHITE);
		g.drawString(enemy.getScore() + " - " + player.getScore(), getWidth()/2 - 100, 100);
	}
	
	public void mouseMoved(MouseEvent e) {
		/*mouseY = e.getY();
		if (game) player.update(mouseY, getHeight());
		repaint();*/
	}
	
	public void mouseDragged(MouseEvent e) {}
	
	public void mouseClicked(MouseEvent e) {}
	public void mousePressed(MouseEvent e) {}
	public void mouseReleased(MouseEvent e) {
		game = !game;
		repaint();
	}
	public void mouseEntered(MouseEvent e) {}
	public void mouseExited(MouseEvent e) {}
}