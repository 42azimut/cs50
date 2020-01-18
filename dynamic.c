#include <stdio.h>
#include <stdlib.h>

int main()
{
    char* pc = NULL;
    int i = 0;
    pc = (char*)malloc(100 * sizeof(char));  //초기화
    if (pc == NULL){
        printf("dynamic memory aloc failed.\n");
        exit(1);
    }
    for (i = 0; i < 26; i++){
        *(pc + i) = 65 + i; // 대문자 아스키 코드 방식
        //*(p + i ) = 'a' = i  // 소문자 출력 
    }
    *(pc + i) = 0;

    printf("%s\n", pc);
    free(pc);
    return 0;
}

