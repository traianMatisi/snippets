package p1;
public abstract class Item {

	public final String nome;
	public int forca;
	public int inteligencia;
	public int vida;

	Item(String nome, int forca, int inteligencia, int vida) {
		this.nome = nome;
		this.forca = forca;
		this.inteligencia = inteligencia;
		this.vida = vida;
	}	
}
