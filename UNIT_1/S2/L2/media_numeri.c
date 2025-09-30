#include <stdio.h>

/*
    media tra due numeri
*/

int main () {
    float num1, num2, i = 0;
    float somma = 0, media;

    printf("Inserisci il primo numero: ");
    scanf("%f", &num1);

    printf("Inserisci il secondo numero: ");
    scanf("%f", &num2);

    while(i < 2) {
        if(i == 0) {
            somma = somma + num1;
        }
        else {
            somma = somma + num2;
        }
        i++;
    }
   
    media = somma / 2;
    printf("La media tra %.3f e %.3f è %.3f\n", num1, num2, media);

    return 0;

}