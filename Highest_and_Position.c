#include <stdio.h>

int main(){
    int num, max, position;

    for(int i=1; i<=100; i++) {
        scanf("%d", &num);

        if(i == 1) {
            max = num;
            position = i;
        } else if(num > max) {
            max = num;
            position = i;
        }
    }
    printf("%d\n", max);
    printf("%d\n", position);
    return 0;
}