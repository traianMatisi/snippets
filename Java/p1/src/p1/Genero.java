package p1;
public enum Genero {
	
	FEMININO(0), MASCULINO(1);
	
	private int valorGenero;

	private Genero(int genero) {
		this.valorGenero = genero;
	}
	
	public int getGenero() {
		return this.valorGenero;
	}
}
