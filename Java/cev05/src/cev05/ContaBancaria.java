package cev05;

public class ContaBancaria {
	
	//###### ATRIBUTES ######//
	public int numConta;
	protected char tipo;
	private String titular;
	private float saldo;
	private boolean status;
	
	//###### CONSTRUCT ######//
	public ContaBancaria(int numConta, char tipo, String titular) {
		super();
		this.numConta = numConta;
		this.tipo = tipo;
		this.titular = titular;
		this.saldo = 0.0f;
		this.status = false;
	}
	
	//###### GETTERS AND SETTERS ######//
	public int getNumConta() {
		return numConta;
	}

	public void setNumConta(int numConta) {
		this.numConta = numConta;
	}

	public char getTipo() {
		return tipo;
	}

	public void setTipo(char tipo) {
		this.tipo = tipo;
	}

	public String getTitular() {
		return titular;
	}

	public void setTitular(String titular) {
		this.titular = titular;
	}

	public float getSaldo() {
		return saldo;
	}

	public void setSaldo(float saldo) {
		this.saldo = saldo;
	}

	public boolean isStatus() {
		return status;
	}

	public void setStatus(boolean status) {
		this.status = status;
	}
	
	
}
