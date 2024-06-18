package p1;
public class Fase {

	private final NomeFases nome;
	private int numPersonagens = 0;
	private int dificuldade = 1;
	
	Fase(NomeFases nomeFases, int numPersonagens) {
		this.nome = nomeFases;
		this.numPersonagens = numPersonagens;
		this.dificuldade += this.numPersonagens;
		if (this.dificuldade > 5)
			this.dificuldade = 5;
	}

	public static Fase criarFase(NomeFases nomeFases, int numPersonagens) {
		Fase fase = new Fase(nomeFases, numPersonagens);
		return fase;
	}

	public NomeFases getNome() {
		return this.nome;
	}
}
//amo voce bons estudos dorme direto bebe agua um abra;o
