#include <stdio.h>
#include <stdlib.h>

void update(int *a,int *b) {
    int a_new, b_new; 
    a_new = *a + *b;          // *a represents value stored at memory a 
    b_new = abs(*a - *b);
    *a = a_new;               // replace old memory content with new value
    *b = b_new;    
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}