package fabricaCarro;

public class Carro {
	private String modelo;
	private Cor cor;
	public final int chassi;
	
	Carro(String modelo_, Cor cor_, int chassi_) {
		this.modelo = modelo_;
		this.cor = cor_;
		this.chassi = chassi_;
	}
	public void specsCarro() {
		System.out.println("Modelo: " + this.modelo);
		System.out.println("Cor: " + this.cor);
		System.out.println("Serial: " + this.chassi);
		System.out.println("");
	}
}
