/* Problem Title :Kangaroo
   Problem Statement:https://www.hackerrank.com/challenges/counting-valleys/problem
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

    // Complete the countingValleys function below.
    static int countingValleys(int n, String s) {

        /* Thoughts:
        We need to Iterate over the ups and downs keeping track of 
        the distance from sea level and whenever the transition is made 
        update the tracks correspondingly.Here we used valleycount,sealevel,upcount and downcount as tracker variables

        */
        
        int valleycount=0;
        int sealevel=0;
        int upcount = 0;
        int downcount=0;
        if(s.length()==n)
        {
for( int i=0; i<s.length(); i++ ) {
    if( s.charAt(i) == 'U' && sealevel==0 ){
        upcount++;
        sealevel++;
    } 
    else if(s.charAt(i)=='D' && sealevel==0){
        downcount++; 
        sealevel--;
        valleycount++;
    }
    else if(s.charAt(i)=='U' && sealevel<0)
    {
        upcount++;
        sealevel++;
        
    }
    else if(s.charAt(i)=='D' && sealevel<0)
    {
        downcount++; 
        sealevel--;
        
    }
    else if(s.charAt(i)=='U' && sealevel>0)
    {
        upcount++;
        sealevel++;
    }
    else if(s.charAt(i)=='D' && sealevel>0)
    {
        downcount++;
        sealevel--;
        
    }
}
        }
        
        
        
return valleycount;
        

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));
        int strconstrain=0;
        int stepconstrain=0;
        
        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        String s = scanner.nextLine();
        
        for( int i=0; i<s.length(); i++ ) {
    if( s.charAt(i) == 'U'|| s.charAt(i) == 'D' ){
       strconstrain=1;
    } 
        }
        if((n>=2) && (n<=1000000)){stepconstrain=1;}
        
        
        
if(strconstrain==1 && stepconstrain==1)
{
        int result = countingValleys(n, s);


        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();

}
       
}
    
}
