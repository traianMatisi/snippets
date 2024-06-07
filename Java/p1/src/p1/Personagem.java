package p1;
import java.util.ArrayList;

public abstract class Personagem {
	
	protected final String nome;
	protected int pontuacao;
	protected int forca;
	protected int inteligencia;
	protected int vida;
	protected final Genero genero;
	
	protected ArrayList<Item> itens = new ArrayList<>();
	
	Personagem(String nome, Genero genero) {
		this.nome = nome;
		this.pontuacao = 0;
		this.vida = 100;
		this.genero = genero;
		switch (genero) {		
			case MASCULINO:
				this.forca = 10;
				this.inteligencia = 5;
				break;
				
			case FEMININO:
				this.forca = 5;
				this.inteligencia = 10;
				break;
		}
	}
	
	public String getNome() {
		return this.nome;
	}
}
