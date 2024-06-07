package fabricaCarro;
public abstract class FabricaCarro {
	public static int contadorChassi = 0;
	
	public static Carro makeCarro(String modelo_, Cor cor_, int chassi_) {
		Carro carro = new Carro(modelo_, cor_, chassi_);
		FabricaCarro.contadorChassi++;
		return carro;
	}
}
