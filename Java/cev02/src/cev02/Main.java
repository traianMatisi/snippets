package cev02;
public class Main {
	public static void main(String[] args) {
		Caneta le_bic = new Caneta("Compactor", true);
		System.out.println(le_bic.modelo);
		System.out.println("Tampada? "+le_bic.tampa);
		le_bic.modelo = "Bic";
		le_bic.des_tampar();
		System.out.println(le_bic.modelo);
		System.out.println("Tampada? "+le_bic.tampa);
		le_bic.des_tampar();
		System.out.println(le_bic.modelo);
		System.out.println("Tampada? "+le_bic.tampa);
	}

}