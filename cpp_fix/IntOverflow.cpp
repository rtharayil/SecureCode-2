/* #include <iostream>
#include <limits>

int add(int a, int b) {
    return a + b;
}

int main() {
    int x = 2000000000;
    int y = 1500000000;
    int result = add(x, y);  // Overflow occurs here
    std::cout << "Result: " << result << std::endl;
    return 0;
}
*/

/*
Instructions:

Enter %x %x %x as input to read memory content.
Secure the function by specifying a format string.

*/

#include <iostream>
#include <cstdio>

void vulnerableFunction(const char* userInput) {
    printf(userInput);  // Vulnerable to format string attack
}

int main() {
    char input[100];
    std::cout << "Enter a string: ";
    std::cin >> input;
    vulnerableFunction(input);
    return 0;
}
