package secretSanta;

import java.util.LinkedList;

public class secretList extends LinkedList<sexaiis> {

	
	
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	

	@Override
	public boolean add(sexaiis e) {
		/*need to generate random integer and then add sexaii at that point*/
		int randInt;
		
		this.add(randInt, e);
		return true; 
	}


	

	@Override
	public sexaiis get(int inde) {
		/*we will return the index +1 will will be the next sexaii in line*/
		return super.get(inde+1);
	}



	public String getSecret(sexaiis guy)
	{
		int index = this.indexOf(guy);
		sexaiis giftGuy = this.get(index);
		String nameOfSexaii = giftGuy.getName();
		
		
		return nameOfSexaii;
	}




	public static void main(String[] args) {
		// TODO Auto-generated method stub

		System.out.println( "Time to see what to do:");
		
	}

}
