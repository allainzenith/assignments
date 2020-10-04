import java.util.*;

   public class Salary{
      public static void main(String[] args){
         Scanner in = new Scanner(System.in);
         
         System.out.print("Please input the employee's gross monthly salary: ");
         double monthlySalary = in.nextDouble();
         
         System.out.println("\n"+"Output:"+"\n");
         System.out.println("Taxable Monthly Salary is:" +String.format("%.2f", taxableSalary(monthlySalary,totalDeductions(monthlySalary))));
         System.out.println("Total deduction is:" +String.format("%.2f",totalDeductions(monthlySalary)));
         System.out.println("Withholding tax is:" +String.format("%.2f",withholdingTax(taxableSalary(monthlySalary,totalDeductions(monthlySalary)))));
         double withholdTax = withholdingTax(taxableSalary(monthlySalary,totalDeductions(monthlySalary)));
         System.out.println("Net income is:" +String.format("%.2f",netIncome(taxableSalary(monthlySalary,totalDeductions(monthlySalary)),withholdTax)));      
     }
     
  public static double totalDeductions(double monthlySalary){
      double philHealth; 
      //for sss
      double sss = (monthlySalary>=16000?581.30:monthlySalary*0.0363);
            
      //for philhealth computation
      if (monthlySalary<=10000){
         philHealth = 137.50;
      }
      else if (monthlySalary<=39999.99){
         philHealth = (monthlySalary * 0.0275)/2;
      }
      else{
         philHealth = 550;
      }
      
      //for pag-ibig
      double pagIbig = (monthlySalary>=5000?100:monthlySalary*0.02) ;

      return sss + philHealth + pagIbig;
  }
  
  public static double taxableSalary(double monthlySalary,double totalDeductions){
      double deductedSalary = monthlySalary - totalDeductions;
      double taxableSalary= (monthlySalary>90000?deductedSalary+((monthlySalary-90000)/12):deductedSalary);
      return taxableSalary;
  }
  
  public static double withholdingTax(double taxableSalary){
      double withholdingTax;
      if (taxableSalary>666677){ //taxable is above 666667 <column 6>
         withholdingTax = ((taxableSalary - 666666.67) *0.35) + 200833.33;
;
      }
      else if (taxableSalary>166667){ //taxable exceeds 16,667 <column 5>
         withholdingTax = ((taxableSalary - 166666.67) * 0.32) + 40833.33;
      }
      else if (taxableSalary>66667){ //taxable exceeds 66,667 <column 3>
         withholdingTax = ((taxableSalary - 66666.67) * 0.30) + 10833.33;
      }
      else if (taxableSalary>33333){ //taxable exceeds 33,333 <column 4>
         withholdingTax = ((taxableSalary - 33333.33) * 0.25) + 2500; 
      }
      else if (taxableSalary>20833){ //taxable exceeds 20,833 <column 5>
         withholdingTax = ((taxableSalary - 20833.33) * 0.2);
       } 
      else{ //taxable is less than 20,833 <column 1>
         withholdingTax = 0;
      }    
      return withholdingTax;
  }
  
  public static double netIncome(double taxableSalary, double withholdingTax){
      return taxableSalary - withholdingTax;
  }
 
  }