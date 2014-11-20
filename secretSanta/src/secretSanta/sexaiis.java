package secretSanta;

public class sexaiis {

	/*will have a name and a check off system*/
	
	public String name;
	
	public boolean hasBeenPicked;

	
	/*simple constructor*/
	public sexaiis(String nam) {
		this.name = nam;
		this.hasBeenPicked = false;
		
	}

	public void isPicked()
	{
		this.hasBeenPicked = true;
	}
	/*gets name only if the person hasnt been picked previously*/
	public String getName()
	{
		if ( this.hasBeenPicked)
			return this.name;
		else
			return null;
	}

}
