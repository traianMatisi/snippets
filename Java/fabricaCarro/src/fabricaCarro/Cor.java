package fabricaCarro;

public enum Cor {
	VERMELHO(0),
	VERDE(1),
	AZUL(2),
	AMARELO(3);
	
	private int cor;
	
	Cor(int cor_) {
		this.cor = cor_;
	}
	
	public int getCor() {
		return this.cor;
	}
}
