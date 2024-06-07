package p1;
public enum NomeFases {
	
	PLANICIE(0), ILHA(1), PANTANO(2), MONTANHA(3), FLORESTA(4);
	
	static NomeFases[] fases = NomeFases.values();
	
	private int valorFases;
	
	private NomeFases(int valorFases) {
		setValor(valorFases);
	}
	
	public void setValor(int valorFases) {
		this.valorFases = valorFases;
	}
	
	public int getValor() {
		return this.valorFases;
	}	
}
