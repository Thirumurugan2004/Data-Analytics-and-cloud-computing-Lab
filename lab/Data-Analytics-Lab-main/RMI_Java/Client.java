//CLIENT
import java.rmi.*;
import java.util.Scanner;

public class Client
{
  public static void main (String[] argv) 
  {
    try {
      int res=0;
      Scanner scan = new Scanner(System.in);
      System.out.print("Enter Operation +,-,*,/ : ");
      char op = scan.next().charAt(0);

      System.out.print("Enter First Number : ");
      int x = scan.nextInt();
      System.out.print("Enter Second Number : ");
      int y = scan.nextInt();
      Calculator calci = (Calculator) Naming.lookup("//localhost/myCalci");
      if(op=='+'){
        res = calci.add(x,y);
      }
      else if(op=='-'){
        res = calci.sub(x,y);
      }
      else if(op=='*'){
        res = calci.mul(x,y);
      }
      else if(op=='/'){
        res = calci.div(x,y);
      }
      System.out.println("Result from remote Object = " + res);
      scan.close();
    }
    
    catch (Exception e) {
      System.out.println ("CalculatorClient exception: " + e);
    }
  }
}

