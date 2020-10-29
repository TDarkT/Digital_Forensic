#include <iostream>

class test {
    
    public:
        test();
        static int num_package;
        
};
int test::num_package = 0;
test::test() {
    test::num_package++;
    std::cout << num_package;
}

int main() {
    test test1;
    test test2;
    test test3;
    return 1;
}