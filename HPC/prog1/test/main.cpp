//
//  main.cpp
//  test
//
//  Created by Parry on 2/5/15.
//  Copyright (c) 2015 Parry. All rights reserved.
//

#include <iostream>


int setBits(int value){
    int dist = 0;
    while (value != 0) {
        dist++;
        value &= value - 1;
    }
    return dist;
}
int hamming(int x,int y) {
    int val = x^y;
    return setBits(val);
}

int  n_bit_position(int number,int position){
    int result = (number>>(position));
    return result;
}

int  find_next(int number,int position)
{
    int result=  n_bit_position(number,position);
    
    while (result!=0){
        int newnumber = (1<<position) - 1;
        position=position-1;
        number =number & newnumber;
        result=n_bit_position(number ,position);
    }
    
    int setter = 1<<position;
    number = setter  | number;
    return number;
}


int main(int argc, const char * argv[]) {
    // insert code here...
    int bits =5;
    int l = bits-1;
    int number = 0;
    int d = 3;
    int end = (1<<d)-1;
    
    while(number!=end){
        int result = n_bit_position(number,l);
        if (result == 0){
            int setter = 1<<l;
            number = setter  | number;
        }
        else{
            number = find_next(number,l);
        }
       
       if(setBits(number)<=d){
           std::cout <<number;
           std::cout <<"\n";
       }
   }
    
    return 0;
}
