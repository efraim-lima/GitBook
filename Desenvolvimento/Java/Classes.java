public class Main {
	
	//Brincando com classes (no caso podemos chamar de Objetos)
	class Comidas {
		String sabor;
		boolean disponivel;
		int quantidade;
		String descricao;
		String validade;
		private String fornecedor;
		String codigoBarras;
		abstract textura;
		
		
		//Aqui temos um constructor sendo criado de forma direta
		Comidas() {
			this.sabor = "Carne";
			this.disponivel = true;
			this.quantidade = 13;
			this.descricao = "Comida feita de carne";
			this validade = "03/11/2025";
		}
		
		//Aqui temos um constructor sendo criado de forma dinamica
		Comidas(String sabor, boolean disponivel, int quantidade, String descricao, String validade) {
			this.sabor = sabor;
			this.disponivel = disponivel;
			this.quantidade = quantidade;
			this.descricao = descricao;
			this validade = validade;
		}
		
		void GetCodigoBarras(){
			return this.codigoBarras;
		}
		
		public String Fornecedor (){
			return this.fornecedor;
		}
	}
	
	static class Pastel extends Comidas {
		public Pastel(String sabor, boolean disponivel, int quantidade, String descricao, string validade) {
		
		super(sabor, disponivel, quantidade, descricao, validade);
		
		}
	}
	
	public class void main(String[] args) {

	}
	
	
	//Usando interfaces para implementar regras e funçoes aos metodos
	interface Cozinhar {
		
		int tempoDeCosizento = 30;
		void fritar();
		abstract void cozinhar();
		void descongelar(){
			System.out.println("Descongelando oa alimento")
		}
	}
	
	class Pastel implements Cozinhar {
		public void descongelar(){		
		}
		
	class Esfiha extends Cozinhar {
		@Override       //Usado quando uma class tem o mesmo nome de funçao que uma interface, mas finalidades levemente diferentes
		void cozinhar() {
			
		}
	}
	}
}