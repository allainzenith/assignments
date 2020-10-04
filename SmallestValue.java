import java.util.*;

   public class SmallestValue{
   
      public static void main(String[] args){
         Scanner num=new Scanner(System.in);//This is used to accept inputs and allocate the value needed for each variable.
         
         /*The try and catch method is used in this program to display an error message should there be any wrong inputs entered 
         while executing the program. Otherwise, the code inside the try statement is executed.(e.g.The error message will display
         if the user inputs a letter.)*/
         
         try {
         /*This is the section of the code where the variables (num1,num2 and num3) are being declared and prompts the user to input three numbers.*/
         System.out.print("Enter first number:");
         int num1=num.nextInt();
         System.out.print("Enter second number:");
         int num2=num.nextInt();
         System.out.print("Enter third number:");
         int num3=num.nextInt();
         
         /*This is the section of the code where the values allocated inside the variables are being compared
         in order to display the smallest value.*/
         if (num1<num2){
            if(num1<num3){
               System.out.println("Output: "+num1);
            }
            else{
               System.out.println("Output: "+num3);
            }
         }
        
         else if (num2<num3){
              System.out.println("Output: "+num2);
         }
         
         else{
              System.out.println("Output: "+num3);
         } 
         } catch (Exception e) {
               System.out.println("Output: Error! Please input an integer!"); /*This is the error message that will display if 
                                                                               there are wrong inputs entered by the user.*/
         }
         
   }
} 
        

        
         
