/* Problem Title :Climbing the leaderboard
   Problem Statement:https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem 
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

    /*
      Thoughts:
         Here we can convert the scores array into the array with same score repeated only once and then use binary search to find the rank of alice scores in that score repeated once array 
         Always remember to consider the performance (complexity) in case of larger input sets 
    */

   
    static int[] climbingLeaderboard(int[] scores, int[] alice) {

                int SROA_SIZE=0;
                int SROA_INDEX=0;

        for(int i=0;i<scores.length;i++) {
            if (i==scores.length-1)
            {
                SROA_SIZE++;

            }
            else 
            {

            if(scores[i]>scores[i+1])
            {
                SROA_SIZE++;
            }
            else continue;

            }

       }

 int scorerepeatedoncearray_SROA[]=new int[SROA_SIZE];
       int alicescoreranks[]=new int[alice.length];

       for(int i=0;i<scores.length;i++)
       {
           if (i==scores.length-1)
            {
             scorerepeatedoncearray_SROA[SROA_INDEX]=scores[i];

            }
            else
            {

             if(scores[i]>scores[i+1])
            {
                scorerepeatedoncearray_SROA[SROA_INDEX]=scores[i];SROA_INDEX++;
            } 
            else continue; 

            }
          
       }



for(int j=0;j<alicescoreranks.length;j++)
{
    int score=alice[j];
    alicescoreranks[j]=BSearchedRank(scorerepeatedoncearray_SROA,score);
}


return alicescoreranks;


    }



public static int BSearchedRank(int[] SROA ,int score){
    int left_index=0;
    int right_index=SROA.length-1;
    int mid_index=0;
    while(left_index <= right_index){
        mid_index=left_index+((right_index-left_index)/2);
        
        if(SROA[mid_index]==score){
            return mid_index+1;
        }

        else if(score<SROA[mid_index]){
            
            left_index=mid_index+1;
        
        }
        else if(score>SROA[mid_index]){
           
          
            right_index=mid_index-1;
    }
    else return 0;

   




   
    }



    return left_index+1;

}








    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int scoresCount = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] scores = new int[scoresCount];

        String[] scoresItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < scoresCount; i++) {
            int scoresItem = Integer.parseInt(scoresItems[i]);
            scores[i] = scoresItem;
        }

        int aliceCount = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] alice = new int[aliceCount];

        String[] aliceItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < aliceCount; i++) {
            int aliceItem = Integer.parseInt(aliceItems[i]);
            alice[i] = aliceItem;
        }

        int[] result = climbingLeaderboard(scores, alice);

        for (int i = 0; i < result.length; i++) {
            bufferedWriter.write(String.valueOf(result[i]));

            if (i != result.length - 1) {
                bufferedWriter.write("\n");
            }
        }

        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}