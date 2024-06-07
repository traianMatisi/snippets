package p1;
public enum Estado {
	
    GAME_OVER(0), PAUSADO(1), ATIVO(2);
	
	private static int valorEstado;

	private Estado(int valorEstado) {
		setEstado(valorEstado);
	}
	
	public static void setEstado(int valorEstado) {
		Estado.valorEstado = valorEstado;
	}
	
	public static int getEstado() {
		return Estado.valorEstado;
	}
}
