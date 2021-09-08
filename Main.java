package com.company;
import java.util.*;

public class Main {

    public static void main(String[] args) {

        Scanner hand1 = new Scanner(System.in);
        System.out.println("Input the first card of the first hand: ");
        String hand1card1 = hand1.nextLine();
        Scanner hand1nextcard = new Scanner(System.in);
        System.out.println("Input the second card of the first hand: ");
        String hand1card2 = hand1nextcard.nextLine();

        Scanner hand2 = new Scanner(System.in);
        System.out.println("Input the first card of the first hand: ");
        String hand2card1 = hand2.nextLine();
        Scanner hand2nextcard = new Scanner(System.in);
        System.out.println("Input the second card of the first hand: ");
        String hand2card2 = hand2nextcard.nextLine();


    }
}

class Cards {
    public String AceOfSpades = "As";
    public String AceOfClubs = "Ac";
    public String AceOfDiamonds = "Ad";
    public String AceOfHearts = "Ah";
    public String KingOfSpades = "Ks";
    public String KingOfClubs = "Kc";
    public String KingOfDiamonds = "Kd";
    public String KingOfHearts = "Kh";
    public String QueenOfSpades = "Qs";
    public String QueenOfClubs = "Qc";
    public String QueenOfDiamonds = "Qd";
    public String QueenOfHearts = "Qh";
    public String JackOfSpades = "Js";
    public String JackOfClubs = "Jc";
    public String JackOfDiamonds = "Jd";
    public String JackOfHearts = "Jh";
    public String TenofSpades = "Ts";
    public String TenofClubs = "Tc";
    public String TenOfDiamonds = "Td";
    public String TenOfHearts = "Th";
    public String NineOfSpades = "9s";
    public String NineOfClubs = "9c";
    public String NineOfDiamonds = "9d";
    public String NineOfHearts = "9h";
    public String EightOfSpades = "8s";
    public String EightOfClubs = "8c";
    public String EightOfDiamonds = "8d";
    public String EightOfHearts = "8h";
    public String SevenOfSpades = "7s";
    public String SevenOfClubs = "7c";
    public String SevenOfDiamonds = "7d";
    public String SevenOfHearts = "7h";
    public String SixOfSpades = "6s";
    public String SixOfClubs = "6c";
    public String SixOfDiamonds = "6d";
    public String SixOfHearts = "6h";
    public String FiveOfSpades = "5s";
    public String FiveOfClubs = "5c";
    public String FiveOfDiamonds = "5d";
    public String FiveOfHearts = "5h";
    public String FourOfSpades = "4s";
    public String FourOfClubs = "4c";
    public String FourOfDiamonds = "4d";
    public String FourOfHearts = "4h";
    public String ThreeOfSpades = "3s";
    public String ThreeOfClubs = "3c";
    public String ThreeOfDiamonds = "3d";
    public String ThreeOfHearts = "3h";
    public String TwoOfSpades = "2s";
    public String TwoOfClubs = "2c";
    public String TwoOfDiamonds = "2d";
    public String TwoOfHearts = "2h";
}
