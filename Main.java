package com.company;
import java.util.*;

public class Main {

    static void combinationUtil(Object deck[], Object data[], int start, int end, int index, int r){
        if (index == r) {
            for (int j = 0; j < r; j++) {
                System.out.print(data[j]+" ");
            }
            System.out.println("");

            return;
        }
        for (int i = start; i <= end && end - i + 1 >= r - index; i++) {
            data[index] = deck[i];
            combinationUtil(deck, data, i + 1, end, index + 1, r);
        }

    }

    static void printCombination(Object deck[], int n, int r) {
        Object data[] = new Object[r];
        combinationUtil(deck, data, 0, n-1, 0, r);
    }


    public static void main(String[] args) {

         ArrayList<String> deckOfCards = new ArrayList<String>(); // something about this having to be a list and not array
         //String deck[] = new String [52]


         String AceOfSpades = "As";
         String AceOfClubs = "Ac";
         String AceOfDiamonds = "Ad";
         String AceOfHearts = "Ah";
         String KingOfSpades = "Ks";
         String KingOfClubs = "Kc";
         String KingOfDiamonds = "Kd";
         String KingOfHearts = "Kh";
         String QueenOfSpades = "Qs";
         String QueenOfClubs = "Qc";
         String QueenOfDiamonds = "Qd";
         String QueenOfHearts = "Qh";
         String JackOfSpades = "Js";
         String JackOfClubs = "Jc";
         String JackOfDiamonds = "Jd";
         String JackOfHearts = "Jh";
         String TenofSpades = "Ts";
         String TenofClubs = "Tc";
         String TenOfDiamonds = "Td";
         String TenOfHearts = "Th";
         String NineOfSpades = "9s";
         String NineOfClubs = "9c";
         String NineOfDiamonds = "9d";
         String NineOfHearts = "9h";
         String EightOfSpades = "8s";
         String EightOfClubs = "8c";
         String EightOfDiamonds = "8d";
         String EightOfHearts = "8h";
         String SevenOfSpades = "7s";
         String SevenOfClubs = "7c";
         String SevenOfDiamonds = "7d";
         String SevenOfHearts = "7h";
         String SixOfSpades = "6s";
         String SixOfClubs = "6c";
         String SixOfDiamonds = "6d";
         String SixOfHearts = "6h";
         String FiveOfSpades = "5s";
         String FiveOfClubs = "5c";
         String FiveOfDiamonds = "5d";
         String FiveOfHearts = "5h";
         String FourOfSpades = "4s";
         String FourOfClubs = "4c";
         String FourOfDiamonds = "4d";
         String FourOfHearts = "4h";
         String ThreeOfSpades = "3s";
         String ThreeOfClubs = "3c";
         String ThreeOfDiamonds = "3d";
         String ThreeOfHearts = "3h";
         String TwoOfSpades = "2s";
         String TwoOfClubs = "2c";
         String TwoOfDiamonds = "2d";
         String TwoOfHearts = "2h";


         deckOfCards.add(AceOfSpades);
         deckOfCards.add(AceOfClubs);
         deckOfCards.add(AceOfDiamonds);
         deckOfCards.add(AceOfHearts);
         deckOfCards.add(KingOfClubs);
         deckOfCards.add(KingOfDiamonds);
         deckOfCards.add(KingOfHearts);
         deckOfCards.add(KingOfSpades);
         deckOfCards.add(QueenOfClubs);
         deckOfCards.add(QueenOfDiamonds);
         deckOfCards.add(QueenOfHearts);
         deckOfCards.add(QueenOfSpades);
         deckOfCards.add(JackOfClubs);
         deckOfCards.add(JackOfDiamonds);
         deckOfCards.add(JackOfHearts);
         deckOfCards.add(JackOfSpades);
         deckOfCards.add(TenofClubs);
         deckOfCards.add(TenOfDiamonds);
         deckOfCards.add(TenOfHearts);
         deckOfCards.add(TenofSpades);
         deckOfCards.add(NineOfClubs);
         deckOfCards.add(NineOfDiamonds);
         deckOfCards.add(NineOfHearts);
         deckOfCards.add(NineOfSpades);
         deckOfCards.add(EightOfClubs);
         deckOfCards.add(EightOfDiamonds);
         deckOfCards.add(EightOfHearts);
         deckOfCards.add(EightOfSpades);
         deckOfCards.add(SevenOfClubs);
         deckOfCards.add(SevenOfDiamonds);
         deckOfCards.add(SevenOfHearts);
         deckOfCards.add(SevenOfSpades);
         deckOfCards.add(SixOfClubs);
         deckOfCards.add(SixOfDiamonds);
         deckOfCards.add(SixOfHearts);
         deckOfCards.add(SixOfSpades);
         deckOfCards.add(FiveOfClubs);
         deckOfCards.add(FiveOfDiamonds);
         deckOfCards.add(FiveOfHearts);
         deckOfCards.add(FiveOfSpades);
         deckOfCards.add(FourOfClubs);
         deckOfCards.add(FourOfDiamonds);
         deckOfCards.add(FourOfHearts);
         deckOfCards.add(FourOfSpades);
         deckOfCards.add(ThreeOfClubs);
         deckOfCards.add(ThreeOfDiamonds);
         deckOfCards.add(ThreeOfHearts);
         deckOfCards.add(ThreeOfSpades);
         deckOfCards.add(TwoOfClubs);
         deckOfCards.add(TwoOfDiamonds);
         deckOfCards.add(TwoOfHearts);
         deckOfCards.add(TwoOfSpades);

         Scanner hand1 = new Scanner(System.in);
         System.out.println("Input the first card of the first hand: ");
         String hand1card1 = hand1.nextLine();

         Scanner hand1nextcard = new Scanner(System.in);
         System.out.println("Input the second card of the first hand: ");
         String hand1card2 = hand1nextcard.nextLine();

         Scanner hand2 = new Scanner(System.in);
         System.out.println("Input the first card of the second hand: ");
         String hand2card1 = hand2.nextLine();

         Scanner hand2nextcard = new Scanner(System.in);
         System.out.println("Input the second card of the second hand: ");
         String hand2card2 = hand2nextcard.nextLine();

         for (int i = 0; i < deckOfCards.size(); i++) {
             if (hand1card1.equals(deckOfCards.get(i))) {
                 deckOfCards.remove(deckOfCards.get(i));
             }
             if (hand1card2.equals(deckOfCards.get(i))) {
                 deckOfCards.remove(deckOfCards.get(i));
             }
             if (hand2card1.equals(deckOfCards.get(i))) {
                 deckOfCards.remove(deckOfCards.get(i));
             }
             if (hand2card2.equals(deckOfCards.get(i))) {
                 deckOfCards.remove(deckOfCards.get(i));
             }

         }
         // removing the cards that are in the hand from the deck


        Object[] deck = deckOfCards.toArray();
        int n = deck.length;
        int combos = 5;
        String data[] = new String[combos];
        printCombination(deck, n, combos);






    }



}









