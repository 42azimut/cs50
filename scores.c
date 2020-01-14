#include <cs50.h>
#include <stdlib.h>


int main()
{
    int n = get_int("Number of scores: ");
    
    int scores[n];
    for (int i = 0; i < n; i++)
    {
        scores[i] = get_int("Score: ");
    }


    //printf("Average: %i\n", (scores[0]+scores[1]+scores[2]) / N);

}

