class Condicionais {
	public static void main(String[] args) {
		
	}
	
	static int Comparando() {
		int valorAlvo = 30;
		int valor = 14;
		
		if (valor > valorAlvo) {
			System.out.println("Seu valor e maior que o objetivo");
		} else if (valor == valorAlvo) {
			System.out.println("Cara, foi no alvo!!");
		} else {
			System.out.println("Cara, ta quase...mais uma vez");
		}
	}
	
	static void Acesso(){
		boolean acesso = true;
		boolean admin= false;
		
		if (acesso && admin) {
			System.out.println("Sucesso, pode acessar o sistema como administrador!");
		} else if (admin && !acesso) {
			System.out.println("Preciso que providencie suas credenciais novamente");
		} else if (acesso && !admin) {
			System.out.println("Pode acessar, mas sem privil´egios");
		} else {
			System.out.println("Acesso negado");
		}
	}
	
	static void Switches(){
		char letra = "A";
		
		switch (letra){
			case "E";
			case "I":
				System.out.println("N~ao ´e a letra");
				break;
			case "A":
				System.out.println("Ta a´i a letra");
				break;
			default:
				System.out.println("Acho que deu ruim rsrs");
		}
	}
}