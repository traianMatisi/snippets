package fabricaCarro;

public class Main {

	public static void main(String[] args) {
		Carro carro1 = FabricaCarro.makeCarro("Camaro", Enum.valueOf(Cor.class, "AMARELO"), FabricaCarro.contadorChassi);
		Carro carro2 = FabricaCarro.makeCarro("Ferrari", Enum.valueOf(Cor.class, "VERMELHO"), FabricaCarro.contadorChassi);
		Carro carro3 = FabricaCarro.makeCarro("Mustang", Enum.valueOf(Cor.class, "AZUL"), FabricaCarro.contadorChassi);
		Carro carro4 = FabricaCarro.makeCarro("Celta", Enum.valueOf(Cor.class, "VERDE"), FabricaCarro.contadorChassi);
		carro1.specsCarro();
		carro2.specsCarro();
		carro3.specsCarro();
		carro4.specsCarro();
	}

}
