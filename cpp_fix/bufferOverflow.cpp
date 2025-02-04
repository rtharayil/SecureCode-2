/*
#include <iostream>
#include <cstring>

void vulnerableFunction(const char* input) {
    char buffer[10];
    strcpy(buffer, input);  // No boundary check
    std::cout << "Buffer content: " << buffer << std::endl;
}

int main() {
    char input[100];
    std::cout << "Enter input: ";
    std::cin >> input;
    vulnerableFunction(input);
    return 0;
}

*/

/*
Input a string longer than 10 characters and observe the crash.
Apply boundary checks using strncpy
*/

#include <iostream>
#include <cstring>

void secureFunction(const char* input) {
    char buffer[10];
    strncpy(buffer, input, sizeof(buffer) - 1);
    buffer[sizeof(buffer) - 1] = '\0';  // Ensure null-termination
    std::cout << "Buffer content: " << buffer << std::endl;
}

int main() {
    char input[100];
    std::cout << "Enter input: ";
    std::cin >> input;
    secureFunction(input);
    return 0;
}
