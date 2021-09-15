
import java.util.*;

public class Main {


    public static void main(String[] args) {
    	
    	//fullDeck is all 52 cards in a standard deck
        final int[][] fullDeck = new int[][]{{2,1},{3,1},{4,1},{5,1},{6,1},{7,1},{8,1},{9,1},{10,1},{11,1},{12,1},{13,1},{14,1},{2,2},{3,2},{4,2},{5,2},{6,2},{7,2},{8,2},{9,2},{10,2},{11,2},{12,2},{13,2},{14,2},{2,3},{3,3},{4,3},{5,3},{6,3},{7,3},{8,3},{9,3},{10,3},{11,3},{12,3},{13,3},{14,3},{2,4},{3,4},{4,4},{5,4},{6,4},{7,4},{8,4},{9,4},{10,4},{11,4},{12,4},{13,4},{14,4}};
        
        //
        int[][] tempDeck = fullDeck;
        
        //first taking input of two cards and putting them into two String arrays respectively
        Object[][] hand1s = new Object[2][2];
        Object[][] hand2s = new Object[2][2];
        //will all be converted into integer arrays after receiving input and converting it all into integers
        int[][] hand1i = new int[2][2];
        int[][] hand2i = new int[2][2];

        Scanner scan = new Scanner(System.in);
        //taking input of the two hands
        System.out.println("Input the first card of the first hand: ");
            hand1s[0] = scan.nextLine().split(" ");

        System.out.println("Input the second card of the first hand: ");
            hand1s[1] = scan.nextLine().split(" ");

        System.out.println("Input the first card of the second hand: ");
            hand2s[0] = scan.nextLine().split(" ");

        System.out.println("Input the second card of the second hand: ");
            hand2s[1] = scan.nextLine().split(" ");

        //converting first hand's card values 2 through 10 to integers
        if(hand1s[0][0] == "2" || hand1s[0][0] == "3" || hand1s[0][0] == "4" || hand1s[0][0] == "5" || hand1s[0][0] == "6" || hand1s[0][0] == "7" || hand1s[0][0] == "8" || hand1s[0][0] == "9" || hand1s[0][0] == "10")  {
        	hand1i[0][0] = (int) hand1s[0][0];
        	//converting card suit into integer representation with 1 = spade, 2 = club, 3 = heart, 4 = diamond
            if(hand1s[0][1] == "Spade")  {
                hand1i[0][1] = 1;
            }   else if(hand1s[0][1] == "Club")    {
                hand1i[0][1] = 2;
            }   else if(hand1s[0][1] == "Heart")    {
                hand1i[0][1] = 3;
            }   else if(hand1s[0][1] == "Diamond")    {
                hand1i[0][1] = 4;
            }
         }
         //converting Jack into integer value 11
         else if(hand1s[0][0] == "Jack") {
             hand1i[0][0] = 11;
             if(hand1s[0][1] == "Spade")  {
                 hand1i[0][1] = 1;
             }   else if(hand1s[0][1] == "Club")    {
                 hand1i[0][1] = 2;
             }   else if(hand1s[0][1] == "Heart")    {
                 hand1i[0][1] = 3;
             }   else if(hand1s[0][1] == "Diamond")    {
                 hand1i[0][1] = 4;
             }
         }
         //converting Queen into integer value 12
         else if(hand1s[0][0] == "Queen") {
             hand1i[0][0] = 12;
             if(hand1s[0][1] == "Spade")  {
                 hand1i[0][1] = 1;
             }   else if(hand1s[0][1] == "Club")    {
                 hand1i[0][1] = 2;
             }   else if(hand1s[0][1] == "Heart")    {
                 hand1i[0][1] = 3;
             }   else if(hand1s[0][1] == "Diamond")    {
                 hand1i[0][1] = 4;
             }
         }
         //converting King into integer value 13
         else if(hand1s[0][0] == "King") {
             hand1i[0][0] = 13;
             if(hand1s[0][1] == "Spade")  {
                 hand1i[0][1] = 1;
             }   else if(hand1s[0][1] == "Club")    {
                 hand1i[0][1] = 2;
             }   else if(hand1s[0][1] == "Heart")    {
                 hand1i[0][1] = 3;
             }   else if(hand1s[0][1] == "Diamond")    {
                 hand1i[0][1] = 4;
             }
         }
         //converting Ace into integer value 14
         else if(hand1s[0][0] == "Ace") {
             hand1i[0][0] = 1;
             if(hand1s[0][1] == "Spade")  {
                 hand1i[0][1] = 1;
             }   else if(hand1s[0][1] == "Club")    {
                 hand1i[0][1] = 2;
             }   else if(hand1s[0][1] == "Heart")    {
                 hand1i[0][1] = 3;
             }   else if(hand1s[0][1] == "Diamond")    {
                 hand1i[0][1] = 4;
             }
         }
        //same with second card of first hand
        if(hand1s[1][0] == "2" || hand1s[1][0] == "3" || hand1s[1][0] == "4" || hand1s[1][0] == "5" || hand1s[1][0] == "6" || hand1s[1][0] == "7" || hand1s[1][0] == "8" || hand1s[1][0] == "9" || hand1s[1][0] == "10")  {
            hand1i[1][0] = (int) hand1s[1][0];
            if(hand1s[1][1] == "Spade")  {
                hand1i[1][1] = 1;
            }   else if(hand1s[1][1] == "Club")    {
                hand1i[1][1] = 2;
            }   else if(hand1s[1][1] == "Heart")    {
                hand1i[1][1] = 3;
            }   else if(hand1s[1][1] == "Diamond")    {
                hand1i[1][1] = 4;
            }
        }
        else if(hand1s[0][0] == "Jack")   {
            hand1i[1][0] = 11;
            if(hand1s[1][1] == "Spade")  {
                hand1i[1][1] = 1;
            }   else if(hand1s[1][1] == "Club")    {
                hand1i[1][1] = 2;
            }   else if(hand1s[1][1] == "Heart")    {
                hand1i[1][1] = 3;
            }   else if(hand1s[1][1] == "Diamond")    {
                hand1i[1][1] = 4;
            }
        }
        else if(hand1s[0][0] == "Queen")   {
            hand1i[1][0] = 12;
            if(hand1s[1][1] == "Spade")  {
                hand1i[1][1] = 1;
            }   else if(hand1s[1][1] == "Club")    {
                hand1i[1][1] = 2;
            }   else if(hand1s[1][1] == "Heart")    {
                hand1i[1][1] = 3;
            }   else if(hand1s[1][1] == "Diamond")    {
                hand1i[1][1] = 4;
            }
        }
        else if(hand1s[0][0] == "King")   {
            hand1i[1][0] = 13;
            if(hand1s[1][1] == "Spade")  {
                hand1i[1][1] = 1;
            }   else if(hand1s[1][1] == "Club")    {
                hand1i[1][1] = 2;
            }   else if(hand1s[1][1] == "Heart")    {
                hand1i[1][1] = 3;
            }   else if(hand1s[1][1] == "Diamond")    {
                hand1i[1][1] = 4;
            }
        }
        else if(hand1s[0][0] == "Ace")   {
            hand1i[1][0] = 1;
            if(hand1s[1][1] == "Spade")  {
                hand1i[1][1] = 1;
            }   else if(hand1s[1][1] == "Club")    {
                hand1i[1][1] = 2;
            }   else if(hand1s[1][1] == "Heart")    {
                hand1i[1][1] = 3;
            }   else if(hand1s[1][1] == "Diamond")    {
                hand1i[1][1] = 4;
            }
        }
        //same with first card of second hand
        if(hand2s[0][0] == "2" || hand2s[0][0] == "3" || hand2s[0][0] == "4" || hand2s[0][0] == "5" || hand2s[0][0] == "6" || hand2s[0][0] == "7" || hand2s[0][0] == "8" || hand2s[0][0] == "9" || hand2s[0][0] == "10")  {
            hand2i[0][0] = (int) hand2s[0][0];
            if(hand2s[0][1] == "Spade")  {
                hand2i[0][1] = 1;
            }   else if(hand2s[0][1] == "Club")    {
                hand2i[0][1] = 2;
            }   else if(hand2s[0][1] == "Heart")    {
                hand2i[0][1] = 3;
            }   else if(hand2s[0][1] == "Diamond")    {
                hand2i[0][1] = 4;
            }
        }
        else if(hand2s[0][0] == "Jack")   {
            hand2i[0][0] = 11;
            if(hand2s[0][1] == "Spade")  {
                hand2i[0][1] = 1;
            }   else if(hand2s[0][1] == "Club")    {
                hand2i[0][1] = 2;
            }   else if(hand2s[0][1] == "Heart")    {
                hand2i[0][1] = 3;
            }   else if(hand2s[0][1] == "Diamond")    {
                hand2i[0][1] = 4;
            }
        }
        else if(hand2s[0][0] == "Queen")   {
            hand2i[0][0] = 12;
            if(hand2s[0][1] == "Spade")  {
                hand2i[0][1] = 1;
            }   else if(hand2s[0][1] == "Club")    {
                hand2i[0][1] = 2;
            }   else if(hand2s[0][1] == "Heart")    {
                hand2i[0][1] = 3;
            }   else if(hand2s[0][1] == "Diamond")    {
                hand2i[0][1] = 4;
            }
        }
        else if(hand2s[0][0] == "King")   {
            hand2i[0][0] = 13;
            if(hand2s[0][1] == "Spade")  {
                hand2i[0][1] = 1;
            }   else if(hand2s[0][1] == "Club")    {
                hand2i[0][1] = 2;
            }   else if(hand2s[0][1] == "Heart")    {
                hand2i[0][1] = 3;
            }   else if(hand2s[0][1] == "Diamond")    {
                hand2i[0][1] = 4;
            }
        }
        else if(hand2s[0][0] == "Ace")   {
            hand2i[0][0] = 1;
            if(hand2s[0][1] == "Spade")  {
                hand2i[0][1] = 1;
            }   else if(hand2s[0][1] == "Club")    {
                hand2i[0][1] = 2;
            }   else if(hand2s[0][1] == "Heart")    {
                hand2i[0][1] = 3;
            }   else if(hand2s[0][1] == "Diamond")    {
                hand2i[0][1] = 4;
            }
        }
        //same with second card of second hand
        if(hand2s[1][0] == "2" || hand2s[1][0] == "3" || hand2s[1][0] == "4" || hand2s[1][0] == "5" || hand2s[1][0] == "6" || hand2s[1][0] == "7" || hand2s[1][0] == "8" || hand2s[1][0] == "9" || hand2s[1][0] == "10")  {
            hand2i[1][0] = (int) hand2s[1][0];
            if(hand2s[1][1] == "Spade")  {
                hand2i[1][1] = 1;
            }   else if(hand2s[1][1] == "Club")    {
                hand2i[1][1] = 2;
            }   else if(hand2s[1][1] == "Heart")    {
                hand2i[1][1] = 3;
            }   else if(hand2s[1][1] == "Diamond")    {
                hand2i[1][1] = 4;
            }
        }
        else if(hand2s[0][0] == "Jack")   {
            hand2i[1][0] = 11;
            if(hand2s[1][1] == "Spade")  {
                hand2i[1][1] = 1;
            }   else if(hand2s[1][1] == "Club")    {
                hand2i[1][1] = 2;
            }   else if(hand2s[1][1] == "Heart")    {
                hand2i[1][1] = 3;
            }   else if(hand2s[1][1] == "Diamond")    {
                hand2i[1][1] = 4;
            }
        }
        else if(hand2s[0][0] == "Queen")   {
            hand2i[1][0] = 12;
            if(hand2s[1][1] == "Spade")  {
                hand2i[1][1] = 1;
            }   else if(hand2s[1][1] == "Club")    {
                hand2i[1][1] = 2;
            }   else if(hand2s[1][1] == "Heart")    {
                hand2i[1][1] = 3;
            }   else if(hand2s[1][1] == "Diamond")    {
                hand2i[1][1] = 4;
            }
        }
        else if(hand2s[0][0] == "King")   {
            hand2i[1][0] = 13;
            if(hand2s[1][1] == "Spade")  {
                hand2i[1][1] = 1;
            }   else if(hand2s[1][1] == "Club")    {
                hand2i[1][1] = 2;
            }   else if(hand2s[1][1] == "Heart")    {
                hand2i[1][1] = 3;
            }   else if(hand2s[1][1] == "Diamond")    {
                hand2i[1][1] = 4;
            }
        }
        else if(hand2s[0][0] == "Ace")   {
            hand2i[1][0] = 1;
            if(hand2s[1][1] == "Spade")  {
                hand2i[1][1] = 1;
            }   else if(hand2s[1][1] == "Club")    {
                hand2i[1][1] = 2;
            }   else if(hand2s[1][1] == "Heart")    {
                hand2i[1][1] = 3;
            }   else if(hand2s[1][1] == "Diamond")    {
                hand2i[1][1] = 4;
            }
        }






    }



}









