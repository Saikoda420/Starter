#include <stdio.h>
int alu(int sf[5]);
int main() {
    int sc[5]={1,2,3,4,5};
    alu(sc);
}
int alu(int sf[5]){
    printf("%i",sf[0]);
    printf("%i",sf[1]);
    printf("%i",sf[2]);
    printf("%i",sf[3]);
    printf("%i",sf[4]);
}