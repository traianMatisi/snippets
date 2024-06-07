package rascunho;

public enum Numeros {
	ZERO(0), UM(1), DOIS(2);
	
	int valor;
	
	private Numeros(int valor) {
		this.setValor(valor);
	}
	
	public void setValor(int valor) {
		this.valor = valor;
	}
	
	public int getValor() {
		return this.valor;
	}
}
