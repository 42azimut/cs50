#include <stdio.h>

int main()

{
    int a[5];
    int i;
    int sum = 0;

    for (i = 0; i < 5; i++)
    {
        a[i] = i + 1;
        printf("a[%d] = %d\n", i, a[i]);
        sum += a[i];
    }
        printf("모든 배열의 합은 %d\n", sum);

    return 0;
}

