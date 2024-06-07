package p1;
public class Main {

	public static void main(String[] args) {
		
		Jogo jogo = new Jogo();
		
		jogo.personagens.add(0, Guerreiro.criarGuerreiro("Kamahl", Enum.valueOf(Genero.class, "MASCULINO")));
		jogo.personagens.add(1, Mago.criarMago("Phage", Enum.valueOf(Genero.class, "FEMININO")));
		
		for (int i = 0; i < NomeFases.fases.length; i++) {
			jogo.fases.add(i, Fase.criarFase(NomeFases.fases[i], jogo.personagens.size()));
		}
		
		jogo.gameRun();
		
	}
	
}
