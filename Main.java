package com.company;
import java.util.*;

public class Main {


    public static void main(String[] args) {
         final int[][] fullDeck = new int[][]{{2,1},{3,1},{4,1},{5,1},{6,1},{7,1},{8,1},{9,1},{10,1},{11,1},{12,1},{13,1},{14,1},{2,2},{3,2},{4,2},{5,2},{6,2},{7,2},{8,2},{9,2},{10,2},{11,2},{12,2},{13,2},{14,2},{2,3},{3,3},{4,3},{5,3},{6,3},{7,3},{8,3},{9,3},{10,3},{11,3},{12,3},{13,3},{14,3},{2,4},{3,4},{4,4},{5,4},{6,4},{7,4},{8,4},{9,4},{10,4},{11,4},{12,4},{13,4},{14,4}};
         int[][] tempDeck = fullDeck;
         //System.out.println(Arrays.deepToString(fullDeck));
         ArrayList<String> deckOfCards = new ArrayList<String>(); // something about this having to be a list and not array
         //String deck[] = new String [52]

        Object[][] hand1 = new Object[2][2];
        Object[][] hand2 = new Object[2][2];
        int[][] hand1i = new int[2][2];
        int[][] hand2i = new int[2][2];

        Scanner scan = new Scanner(System.in);

        System.out.println("Input the first card of the first hand: ");
            hand1[0] = scan.nextLine().split(" ");

         System.out.println("Input the second card of the first hand: ");
            hand1[1] = scan.nextLine().split(" ");

         System.out.println("Input the first card of the second hand: ");
             hand2[0] = scan.nextLine().split(" ");

         System.out.println("Input the second card of the second hand: ");
             hand2[1] = scan.nextLine().split(" ");

         if(hand1[0][0] == "2" || hand1[0][0] == "3" || hand1[0][0] == "4" || hand1[0][0] == "5" || hand1[0][0] == "6" || hand1[0][0] == "7" || hand1[0][0] == "8" || hand1[0][0] == "9" || hand1[0][0] == "10")  {
            hand1i[0][0] = (int) hand1[0][0];
            if(hand1[0][1] == "Spade")  {
                hand1i[0][1] = 1;
            }   else if(hand1[0][1] == "Club")    {
                hand1i[0][1] = 2;
            }   else if(hand1[0][1] == "Heart")    {
                hand1i[0][1] = 3;
            }   else if(hand1[0][1] == "Diamond")    {
                hand1i[0][1] = 4;
            }
         }
         else if(hand1[0][0] == "Jack") {
             hand1i[0][0] = 11;
             if(hand1[0][1] == "Spade")  {
                 hand1i[0][1] = 1;
             }   else if(hand1[0][1] == "Club")    {
                 hand1i[0][1] = 2;
             }   else if(hand1[0][1] == "Heart")    {
                 hand1i[0][1] = 3;
             }   else if(hand1[0][1] == "Diamond")    {
                 hand1i[0][1] = 4;
             }
         }
         else if(hand1[0][0] == "Queen") {
             hand1i[0][0] = 12;
             if(hand1[0][1] == "Spade")  {
                 hand1i[0][1] = 1;
             }   else if(hand1[0][1] == "Club")    {
                 hand1i[0][1] = 2;
             }   else if(hand1[0][1] == "Heart")    {
                 hand1i[0][1] = 3;
             }   else if(hand1[0][1] == "Diamond")    {
                 hand1i[0][1] = 4;
             }
         }
         else if(hand1[0][0] == "King") {
             hand1i[0][0] = 13;
             if(hand1[0][1] == "Spade")  {
                 hand1i[0][1] = 1;
             }   else if(hand1[0][1] == "Club")    {
                 hand1i[0][1] = 2;
             }   else if(hand1[0][1] == "Heart")    {
                 hand1i[0][1] = 3;
             }   else if(hand1[0][1] == "Diamond")    {
                 hand1i[0][1] = 4;
             }
         }
         else if(hand1[0][0] == "Ace") {
             hand1i[0][0] = 1;
             if(hand1[0][1] == "Spade")  {
                 hand1i[0][1] = 1;
             }   else if(hand1[0][1] == "Club")    {
                 hand1i[0][1] = 2;
             }   else if(hand1[0][1] == "Heart")    {
                 hand1i[0][1] = 3;
             }   else if(hand1[0][1] == "Diamond")    {
                 hand1i[0][1] = 4;
             }
         }

        if(hand1[1][0] == "2" || hand1[1][0] == "3" || hand1[1][0] == "4" || hand1[1][0] == "5" || hand1[1][0] == "6" || hand1[1][0] == "7" || hand1[1][0] == "8" || hand1[1][0] == "9" || hand1[1][0] == "10")  {
            hand1i[1][0] = (int) hand1[1][0];
            if(hand1[1][1] == "Spade")  {
                hand1i[1][1] = 1;
            }   else if(hand1[1][1] == "Club")    {
                hand1i[1][1] = 2;
            }   else if(hand1[1][1] == "Heart")    {
                hand1i[1][1] = 3;
            }   else if(hand1[1][1] == "Diamond")    {
                hand1i[1][1] = 4;
            }
        }
        else if(hand1[0][0] == "Jack")   {
            hand1i[1][0] = 11;
            if(hand1[1][1] == "Spade")  {
                hand1i[1][1] = 1;
            }   else if(hand1[1][1] == "Club")    {
                hand1i[1][1] = 2;
            }   else if(hand1[1][1] == "Heart")    {
                hand1i[1][1] = 3;
            }   else if(hand1[1][1] == "Diamond")    {
                hand1i[1][1] = 4;
            }
        }
        else if(hand1[0][0] == "Queen")   {
            hand1i[1][0] = 12;
            if(hand1[1][1] == "Spade")  {
                hand1i[1][1] = 1;
            }   else if(hand1[1][1] == "Club")    {
                hand1i[1][1] = 2;
            }   else if(hand1[1][1] == "Heart")    {
                hand1i[1][1] = 3;
            }   else if(hand1[1][1] == "Diamond")    {
                hand1i[1][1] = 4;
            }
        }
        else if(hand1[0][0] == "King")   {
            hand1i[1][0] = 13;
            if(hand1[1][1] == "Spade")  {
                hand1i[1][1] = 1;
            }   else if(hand1[1][1] == "Club")    {
                hand1i[1][1] = 2;
            }   else if(hand1[1][1] == "Heart")    {
                hand1i[1][1] = 3;
            }   else if(hand1[1][1] == "Diamond")    {
                hand1i[1][1] = 4;
            }
        }
        else if(hand1[0][0] == "Ace")   {
            hand1i[1][0] = 1;
            if(hand1[1][1] == "Spade")  {
                hand1i[1][1] = 1;
            }   else if(hand1[1][1] == "Club")    {
                hand1i[1][1] = 2;
            }   else if(hand1[1][1] == "Heart")    {
                hand1i[1][1] = 3;
            }   else if(hand1[1][1] == "Diamond")    {
                hand1i[1][1] = 4;
            }
        }

        if(hand2[0][0] == "2" || hand2[0][0] == "3" || hand2[0][0] == "4" || hand2[0][0] == "5" || hand2[0][0] == "6" || hand2[0][0] == "7" || hand2[0][0] == "8" || hand2[0][0] == "9" || hand2[0][0] == "10")  {
            hand2i[0][0] = (int) hand2[0][0];
            if(hand2[0][1] == "Spade")  {
                hand2i[0][1] = 1;
            }   else if(hand2[0][1] == "Club")    {
                hand2i[0][1] = 2;
            }   else if(hand2[0][1] == "Heart")    {
                hand2i[0][1] = 3;
            }   else if(hand2[0][1] == "Diamond")    {
                hand2i[0][1] = 4;
            }
        }
        else if(hand2[0][0] == "Jack")   {
            hand2i[0][0] = 11;
            if(hand2[0][1] == "Spade")  {
                hand2i[0][1] = 1;
            }   else if(hand2[0][1] == "Club")    {
                hand2i[0][1] = 2;
            }   else if(hand2[0][1] == "Heart")    {
                hand2i[0][1] = 3;
            }   else if(hand2[0][1] == "Diamond")    {
                hand2i[0][1] = 4;
            }
        }
        else if(hand2[0][0] == "Queen")   {
            hand2i[0][0] = 12;
            if(hand2[0][1] == "Spade")  {
                hand2i[0][1] = 1;
            }   else if(hand2[0][1] == "Club")    {
                hand2i[0][1] = 2;
            }   else if(hand2[0][1] == "Heart")    {
                hand2i[0][1] = 3;
            }   else if(hand2[0][1] == "Diamond")    {
                hand2i[0][1] = 4;
            }
        }
        else if(hand2[0][0] == "King")   {
            hand2i[0][0] = 13;
            if(hand2[0][1] == "Spade")  {
                hand2i[0][1] = 1;
            }   else if(hand2[0][1] == "Club")    {
                hand2i[0][1] = 2;
            }   else if(hand2[0][1] == "Heart")    {
                hand2i[0][1] = 3;
            }   else if(hand2[0][1] == "Diamond")    {
                hand2i[0][1] = 4;
            }
        }
        else if(hand2[0][0] == "Ace")   {
            hand2i[0][0] = 1;
            if(hand2[0][1] == "Spade")  {
                hand2i[0][1] = 1;
            }   else if(hand2[0][1] == "Club")    {
                hand2i[0][1] = 2;
            }   else if(hand2[0][1] == "Heart")    {
                hand2i[0][1] = 3;
            }   else if(hand2[0][1] == "Diamond")    {
                hand2i[0][1] = 4;
            }
        }

        if(hand2[1][0] == "2" || hand2[1][0] == "3" || hand2[1][0] == "4" || hand2[1][0] == "5" || hand2[1][0] == "6" || hand2[1][0] == "7" || hand2[1][0] == "8" || hand2[1][0] == "9" || hand2[1][0] == "10")  {
            hand2i[1][0] = (int) hand2[1][0];
            if(hand2[1][1] == "Spade")  {
                hand2i[1][1] = 1;
            }   else if(hand2[1][1] == "Club")    {
                hand2i[1][1] = 2;
            }   else if(hand2[1][1] == "Heart")    {
                hand2i[1][1] = 3;
            }   else if(hand2[1][1] == "Diamond")    {
                hand2i[1][1] = 4;
            }
        }
        else if(hand2[0][0] == "Jack")   {
            hand2i[1][0] = 11;
            if(hand2[1][1] == "Spade")  {
                hand2i[1][1] = 1;
            }   else if(hand2[1][1] == "Club")    {
                hand2i[1][1] = 2;
            }   else if(hand2[1][1] == "Heart")    {
                hand2i[1][1] = 3;
            }   else if(hand2[1][1] == "Diamond")    {
                hand2i[1][1] = 4;
            }
        }
        else if(hand2[0][0] == "Queen")   {
            hand2i[1][0] = 12;
            if(hand2[1][1] == "Spade")  {
                hand2i[1][1] = 1;
            }   else if(hand2[1][1] == "Club")    {
                hand2i[1][1] = 2;
            }   else if(hand2[1][1] == "Heart")    {
                hand2i[1][1] = 3;
            }   else if(hand2[1][1] == "Diamond")    {
                hand2i[1][1] = 4;
            }
        }
        else if(hand2[0][0] == "King")   {
            hand2i[1][0] = 13;
            if(hand2[1][1] == "Spade")  {
                hand2i[1][1] = 1;
            }   else if(hand2[1][1] == "Club")    {
                hand2i[1][1] = 2;
            }   else if(hand2[1][1] == "Heart")    {
                hand2i[1][1] = 3;
            }   else if(hand2[1][1] == "Diamond")    {
                hand2i[1][1] = 4;
            }
        }
        else if(hand2[0][0] == "Ace")   {
            hand2i[1][0] = 1;
            if(hand2[1][1] == "Spade")  {
                hand2i[1][1] = 1;
            }   else if(hand2[1][1] == "Club")    {
                hand2i[1][1] = 2;
            }   else if(hand2[1][1] == "Heart")    {
                hand2i[1][1] = 3;
            }   else if(hand2[1][1] == "Diamond")    {
                hand2i[1][1] = 4;
            }
        }

         // removing the cards that are in the hand from the deck
/*
        int counter = 0;
        Object[] deck = deckOfCards.toArray();
        int n = deck.length;
        int combos = 5;
        String data[] = new String[combos];
        printCombination(deck, n, combos);
*/





    }



}









