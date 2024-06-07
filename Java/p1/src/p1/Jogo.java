package p1;
import java.util.ArrayList;
public class Jogo {
	
	public ArrayList<Fase> fases = new ArrayList<>();
	public ArrayList<Personagem> personagens = new ArrayList<>();
	
	private Estado estado;
	
	Jogo() {
		this.estado = Estado.ATIVO;
	}
	
	public void setEstado(Estado estado) {
		if (this.estado.equals(Estado.ATIVO)) {
			this.estado = Estado.PAUSADO;
		}
		else {
			this.estado = Estado.ATIVO;
		}
	}
	
	public void gameRun() {
		System.out.println("Estado do jogo: " + this.getEstado());
		
		System.out.println("Fase 1: " + this.fases.get(0).getNome());
		System.out.println("Fase 2: " + this.fases.get(1).getNome());
		System.out.println("Fase 3: " + this.fases.get(2).getNome());
		System.out.println("Fase 4: " + this.fases.get(3).getNome());
		System.out.println("Fase 5: " + this.fases.get(4).getNome());
		
		System.out.println("Player 1: " + this.personagens.get(0).getNome());
		System.out.println("Player 2: " + this.personagens.get(1).getNome());
	}
	
	public Estado getEstado() {
		return this.estado;
	}
}
