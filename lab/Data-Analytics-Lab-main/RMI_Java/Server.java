//SERVER
import java.rmi.*;

public class Server
{
  public static void main (String[] argv) 
  {
    try 
    {
      CalculatorImp remoteObj = new CalculatorImp();
      Naming.rebind("myCalci", remoteObj);
      System.out.println ("Calculator Server is ready.");
    } 
    catch (Exception e) 
    {
      System.out.println ("Calculator Server failed: " + e);
    }
  }
}

