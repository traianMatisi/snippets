package project_03;

public class Demonstracao {

	public static void main(String[] args) {
		
		Bicicleta bike01 = new Bicicleta();
		bike01.velocidade = 0;
		bike01.marcha = 1;
		
		bike01.printStatus();
		bike01.mudarMarcha(3);
		bike01.acelerar(10);
		bike01.printStatus();
	}

}
