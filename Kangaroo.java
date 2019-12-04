/* Problem Title :Kangaroo
   Problem Statement:https://www.hackerrank.com/challenges/kangaroo/problem 
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

    // Complete the kangaroo function below.
    static String kangaroo(int x1, int v1, int x2, int v2) {
        
     /*  --STATEGY--
     Suppose they must make the same number of jumps 'n'. Representing in algebraic form
               
                   v1*n+x1=v2*n+x2....................(i)
                   n=(x2-x1)/(v1-v2)
             where n integer value
     */

if(v1>v2)
{
    if(((x2-x1)%(v2-v1))==0)
    { return "YES";}
    else return "NO";
}
        else return "NO";
        
        
        
        
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] x1V1X2V2 = scanner.nextLine().split(" ");

        int x1 = Integer.parseInt(x1V1X2V2[0]);

        int v1 = Integer.parseInt(x1V1X2V2[1]);

        int x2 = Integer.parseInt(x1V1X2V2[2]);

        int v2 = Integer.parseInt(x1V1X2V2[3]);
        
    if(((x1>=0) && (x1<=10000)) && ((x2>=0) && (x2<=10000)) &&(x2>x1) &&((v1>=1) && (v1<=10000)) && ((v2>=1) && (v2<=10000)) ) 
    {
        String result = kangaroo(x1, v1, x2, v2);
        bufferedWriter.write(result);
        bufferedWriter.newLine();
        bufferedWriter.close();
      
        
        
        scanner.close();
    }
        
    }
}