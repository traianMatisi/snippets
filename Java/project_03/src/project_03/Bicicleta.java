package project_03;

public class Bicicleta {
	
	public int velocidade;
	public int marcha;
	
	public void mudarMarcha(int marcha) {
		this.marcha = marcha;
	}
	
	public void acelerar(int acelerar) {
		velocidade += acelerar;
	}
	
	public void freiar(int freiar) {
		velocidade -= freiar;
	}
	
	public void printStatus() {
		System.out.println("Velocidade; "+this.velocidade);
		System.out.println("Marcha: "+this.marcha);
	}
	
}
