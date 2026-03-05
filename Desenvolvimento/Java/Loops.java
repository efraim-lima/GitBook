import java.util.Arraylist;
import java.util.Arrays;
import java.util.List;

class Loops {
	public static void main(String[] args) {
		for (int i=0; i<5; i++) {
			
			System.out.println("Agora o iterador esta em: " + i)
			
			//As maiores causas de quebras em loopings for vem devido a:
			// - nao existencia de update do interator (i)
			// - condiçao de parada errada
			// Isso pode fazer com que hajam falhas e quebras inesperadas na apicaçao
			
			if (i ==4) {
				//O uso do break deve ser comedido, para alguns casos pode ser melhor usar os laços while
				break;
			}
		}
		

		
		String[] pasteis = {"carne", "frango", "queijo", "palmito"};
		
		for (String pastel: pasteis) {          //leia-se: para cada pastel em pastel faça algo
			System.out.println(pastel);
			
			//Este loop ´e o tipo foreach, util para:
			// - iterar sobre listas ou arrays
			// - quando nao sabemos quantos elementos existem em nossa amostragem
			// - quando nao precisamos saber a posiçao dos elementos no laço (loop)
		}
		
		List<String> arrayPasteis = new ArrayList<>(Arrays.asList(pasteis));
		String[] pasteisReserva = {"batata", "4 queijos", "3 queijos", "calabreza", "chocolate"};
		
		int contador = 1;
		
		while (arrayPasteis.size() < 8) {
			arrayPasteis.add(pasteisReserva[contador]);
			System.out.println(arrayPasteis);
			System.out.println(arrayPasteis.size());
			contador = contador += 1;
		}
	}
}