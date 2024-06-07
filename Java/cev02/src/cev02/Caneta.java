package cev02;
public class Caneta {
	String modelo;
	boolean tampa;
	public Caneta(String x, boolean y) {
		this.modelo = x;
		this.tampa = y;
	}
	public void des_tampar() {
			this.tampa = !(this.tampa);
	}
	public String getModelo() {
		return modelo;
	}
	public void setModelo(String modelo) {
		this.modelo = modelo;
	}
	public boolean isTampa() {
		return tampa;
	}
	public void setTampa(boolean tampa) {
		this.tampa = tampa;
	}
}