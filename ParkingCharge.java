import java.util.*;

   public class ParkingCharge{
   
      public static void main(String[] args){
         Scanner input=new Scanner(System.in);//This is used to accept inputs and allocate the value needed for each variable.
         
         /*This is a message that shows the three vehicle types along with its rate per hour. The character 'c' is for car, 'b' is for bus
         and 't' is for truck. These three choices are the only acceptable inputs.*/
         System.out.println("c-car- PHP20.00 per hour");
         System.out.println("b-bus- PHP35.00 per hour");
         System.out.println("t-truck- PHP50.00 per hour");
         System.out.println("");
         
         /*The try and catch method is used in this program to display an error message should there be any wrong inputs entered 
         while executing the program. Otherwise, the code inside the try statement is executed. (e.g.The error message will display
         if the user inputs a number or symbol as the vehicle type.)*/

         try{
            /*This is the section of the code where the variables (vehicle and parkDuration) are being declared and prompts the user to input the vehicle
            type (vehicle) and the number of parking hours. (parkDuration)*/
            System.out.print("Enter vehicle type(c/b/t): ");
            char vehicle=input.next().toUpperCase().charAt(0);
            
            if (vehicle=='C'||vehicle=='B'||vehicle=='T'){  //If the condition is true, the program will ask for the parking hours and  display the output.
            System.out.print("Parking duration(hrs): ");               
            double parkDuration=input.nextDouble();
            
            /*The switch statement is used to perform different executions depending on the input provided. With this regard,
            the parking charge will depend on the vehicle type and parking hours inputted by the user.*/
         
            switch (vehicle){
               case 'C':
                  System.out.println("Total parking charge: PHP"+String.format("%.2f",parkDuration*20));
                  break;//The purpose of break is to terminate the flow of the switch statement once the case asked for is found.
               case 'B':
                  System.out.println("Total parking charge: PHP"+String.format("%.2f",parkDuration*35));//"%.2f" is used to limit the final answer up to 2 decimal places.
                  break;
               case 'T':
                  System.out.println("Total parking charge: PHP"+String.format("%.2f",parkDuration*50));
                  break;
               default:
                  System.out.println("Error. Please input a letter that corresponds to the choices.");/*Once the inputted value is not found on the cases given above, 
                                                                                                      the program will resort to default and perform its executions.*/
            }
          }
          else{  //If condition is false, the program will execute this statement and display the message.
            System.out.println("Error. Please input a letter that corresponds to the choices.");
          }
         } catch (Exception e){
            System.out.println("Error! Invalid input.");/*This is the error message that will display if 
                                                         here are wrong inputs entered by the user.*/
         }
         
    }
}
