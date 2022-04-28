#include <stdio.h>
#include <string.h>

void reverse(char arr[]) {
    int len = strlen(arr);
    for (int i = 0; i < len/2; i++) {
        char temp = arr[i];
        arr[i] = arr[len-1-i];
        arr[len-1-i] = temp;
    }
}

void add(char A[], char B[]) {
    int carry = 0;
    char result[10003] = {0};
    int max_len = 0;
    
    if (strlen(A) > strlen(B)) {
        max_len = strlen(A);
    }
    else {
        max_len = strlen(B);
    }
    
    for (int i = 0; i < max_len; i++) {
        int sum = A[i] - '0' + B[i] - '0' + carry;
        if (sum < 0) {
            sum += '0';
        }
        if (sum >= 10) {
            carry = 1;
            sum -= 10;
        }
        else {
            carry = 0;
        }
        result[i] = sum + '0';
    }
    
    if (carry == 1) {
        result[max_len] = '1';
    }
    
    reverse(result);
    printf("%s", result);
}

int main() {
    char A[10002] = {0};
    char B[10002] = {0};
    
    scanf("%s %s", A, B);
    
    reverse(A);
    reverse(B);
    
    add(A, B);
}
