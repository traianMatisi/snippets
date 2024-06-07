package p1;
public class Mago extends Personagem {

    private int mana;

    Mago(String nome, Genero genero) {
        super(nome, genero);
        this.mana = 50;
    }
    
    public static Personagem criarMago(String nome, Genero genero) {
    	Personagem mago = new Mago(nome, genero);
    	return mago;
    }

    public int lancarMagia() {
		return this.mana * this.inteligencia;
	}    
}
