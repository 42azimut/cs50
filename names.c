#include <stdio.h>
#include <string.h>

int main()
{
    char names[4];
    names[0] = "Emma";
    names[1] = "Rodrigo";
    names[2] = "Brain";
    names[3] = "David";

    printf("%s\n", names[0]);
    printf("%c%c%c%c\n", names[0][0], names[0][1], names[0][2], names[0][3]);
    return 0;
}

