package p1;
public class Guerreiro extends Personagem {

	private int estamina;
	
	Guerreiro(String nome, Genero genero) {
		super(nome, genero);
		this.estamina = 50;
	}
	
	public static Personagem criarGuerreiro(String nome, Genero genero) {
		Guerreiro guerreiro = new Guerreiro(nome, genero);
		return guerreiro;
	}

	public int ataquePoderoso() {
		return this.estamina * this.forca;
	}
	
	public String getNome() {
		return this.nome;
	}
}
