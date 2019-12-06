/* Problem Title :Forming a magic square
   Problem Statement:https://www.hackerrank.com/challenges/magic-square-forming/problem
   Coding language : Java8
*/

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    /* -Thoughts-:
      A magic square is said to be an n*n  matrix of distinct positive integers from 1 to n^2 where the sum of any row, column, or diagonal (i.e., of length n) is always equal to the same number (i.e., the magic constant).
      The magic constant of a normal magic square depends only on n and has the following value:
      M = n(n^2+1)/2.........(i)
      ie for n=3 M=15

      Here there are 8 possible combinations(can be found by brute force approach) for n=3 to form magic square (below p->0 to p->7)
    Now just take the input matrix ,check the difference between the numbers in the given input and the 8 possible solutions and then take the smallest of those.(i.e.,with low cost)

    */
    static int formingMagicSquare(int[][] s) {
        
         int[][][] possiblePermutations = {
            {{8, 1, 6}, {3, 5, 7}, {4, 9, 2}},//p->0

            {{6, 1, 8}, {7, 5, 3}, {2, 9, 4}},//p->1
             

            {{4, 9, 2}, {3, 5, 7}, {8, 1, 6}},//p->2

            {{2, 9, 4}, {7, 5, 3}, {6, 1, 8}},//p->3

            {{8, 3, 4}, {1, 5, 9}, {6, 7, 2}},//p->4

            {{4, 3, 8}, {9, 5, 1}, {2, 7, 6}},//p->5

            {{6, 7, 2}, {1, 5, 9}, {8, 3, 4}},//p->6

            {{2, 7, 6}, {9, 5, 1}, {4, 3, 8}},//p->7
        };

        int minCost = Integer.MAX_VALUE;
        for (int p = 0; p < 8; p++) 
        {
            int permutationCost = 0;
            for (int i = 0; i < 3; i++) 
            {
                for (int j = 0; j < 3; j++)
                    permutationCost += Math.abs(s[i][j] - possiblePermutations[p][i][j]);
            }
            minCost = Math.min(minCost, permutationCost);
        }
        
        return minCost;
        

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int[][] s = new int[3][3];

        for (int i = 0; i < 3; i++) {
            String[] sRowItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int j = 0; j < 3; j++) {
                int sItem = Integer.parseInt(sRowItems[j]);
                s[i][j] = sItem;
            }
        }

        int result = formingMagicSquare(s);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
