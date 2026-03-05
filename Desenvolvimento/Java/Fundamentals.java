class WelcomeToJava {
	public static void main(String[] args){
		//Brincando com strings
		String nome = "Efraim";
		int nomeLength = nome.length();
		String nomeUpper = nome.toUpperCase();
		String nomeLower = nome.toLowerCase();
		
		System.out.println("Java".contains("av"))
		System.out.println("Java".charAt(1))
		System.out.println("Java".substring(0,3))
		
		String word = "Java";
		System.out.println(word.equals("Java")) //Comparando strings
		System.out.println(word == "Java") //Pode ocorrer um erro, pois o calculo e feito em nivel de bytes
		
		//Brincando com valores numericos
		String numeroUmStr = "1";
		int numeroUm = 1;
		int numeroDois = 2;
		int soma = numeroUm + numeroUmInt;
		
		System.out.println(soma)
		
		//Brincando com arrays
		int[] arrayDeNumeros;
		arrayDeNumeros = {1,2,3,4,5,6};
		
		int primeiroElemento = arrayDeNumeros[0];    //Acessando a primeira posiçao do array
		int segundoElemento = arrayDeNumeros[1];   //Acessando a segunda posiçao do array
		
		arrayDeNumeros[5] =  10; //Alterando um valor dentro do array
		int tamanhoDoArray = arayDeNumeros.length;
		
		//Brincando com operaçao entre numeros
		numeroDois++;  //Incrementando em 1
		numeroDois--; //Decrementando em 1
		multiplicando = numeroUm * numeroDois;
		

		}
}