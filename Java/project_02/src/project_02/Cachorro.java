package project_02;

public class Cachorro {
	
	public String nome;
	
	public void late(String name) {
		System.out.println(nome+": Woof");
	}
	

	public static void main(String[] args) {
		
		Cachorro cachorro01 = new Cachorro();
		cachorro01.nome = "Bingo";
		cachorro01.late(cachorro01.nome);
		
		Cachorro cachorro02 = new Cachorro();
		cachorro02.nome = "Rex";
		cachorro02.late(cachorro02.nome);
	}
	
}
