#include <iostream>

void memoryLeakExample() {
    int* ptr = new int(5);  // Memory leak, no delete
    std::cout << "Value: " << *ptr << std::endl;
}

int main() {
    memoryLeakExample();
    return 0;
}
