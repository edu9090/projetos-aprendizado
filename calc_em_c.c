/*codigo um dos primeiros codigos feitos com o intuito de treinar operadores logicos e matematicos*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
    float valor1, valor2, resultado, repet, expo, numero = 2, x1 ,x2 , x3 , delta;
    char op[10];
    int variavel = 1 ;
    while(variavel == 1){
    system ("clear");
    printf("digite uma das seguintes opções:\n mais\n menos\n vezes\n dividir\n bhaskara \n \n");
    scanf("%s", op);
    if(strcmp (op, "mais")== 0){
        printf("qual o valor 1 : ");
        scanf("%f", &valor1);
          printf("qual o valor 2 : ");
        scanf("%f", &valor2);
        resultado = valor1 + valor2;
        printf("o resultado é: %.2f \n", resultado);
    }
    if(strcmp(op, "menos")== 0){
         printf("qual o valor 1 : ");
        scanf("%f", &valor1);
          printf("qual o valor 2 : ");
        scanf("%f", &valor2);
        resultado = valor1 - valor2;
        printf("o resultado é: %.2f \n", resultado);
        
    }
    if(strcmp(op, "vezes")== 0){
         printf("qual o valor 1 : ");
        scanf("%f", &valor1);
          printf("qual o valor 2 : ");
        scanf("%f", &valor2);
        resultado = valor1 * valor2;
        printf("o resultado é: %.2f \n", resultado);
    }
    if(strcmp(op, "dividir")== 0){
         printf("qual o valor 1 : ");
        scanf("%f", &valor1);
          printf("qual o valor 2 : ");
        scanf("%f", &valor2);
        resultado = valor1 / valor2;
        printf("o resultado é: %.2f \n", resultado);
    }
    if(strcmp(op , "bhaskara" )==0) {
        printf("qual o primeiro icognito : ");
        scanf("%f" , & x1);
        printf("qual o segundo icognito : ");
        scanf ("%f" , & x2);
        printf ("qual o termo idependente : ");
        scanf ("%f" , &x3);
        delta = (x2 * x2 ) - 4 * x1 * x3;
        printf("o delta é : %.2f\n" , delta);
        printf("o x1linha é : %.2f\n", (-x2 + pow(delta , 1/2)) / 2*x1 );
        printf("o x2linha é : %.2f\n", (-x2 - pow(delta , 1/2)) / 2*x1 );
}
    printf("continuar = 1\n parar = 0\n -->");
    scanf("%d", &variavel);
        }
    
    return ("sucesso");
    }








