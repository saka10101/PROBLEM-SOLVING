/* Problem Title :Time conversion
   Problem Statement:https://www.hackerrank.com/challenges/time-conversion/problem 
   Coding language : C++
*/


#include <bits/stdc++.h>
#include <iostream>
#include <sstream>
#include <iomanip>
using namespace std;

int main(){

     /*
        Since  Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock. using this fact we can convert into military time 
     */
    int h, m, s;
    char ch, ampm;
    
    cin >> h >> ch >> m >> ch >> s >> ampm >> ch;
    h = (ampm== 'A') ? (h==12 ? 0 : h) : (h==12 ? 12 : h+12);
        
    cout << setw(2) << setfill('0') << h << ":" 
         << setw(2) << setfill('0') << m << ":" 
         << setw(2) << setfill('0') << s << endl;
    
    return 0;
}