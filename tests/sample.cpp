#include <stdio.h>
#include <exception>


#define BAD_MAX(a, b) ((a > b)? a: b)


// Main function: entry point for execution
int widget() {
    int a = 0;
    int b = 1;

    printf("Hello World");

    if (a == b) {
        return 1;
    }
    if (a > b) {
        return 2;
    }

    return 0;
}

namespace bar {

class Baz {
protected:


};

double sqrt(float x) {
    if (x < 0.0) {
        throw std::exception();
    } else {
        return x/2;
    }
}

};

class Foo {
    private:
    int a;
    public:
    void method(int b) { 
        if (a > b) {
            printf("something");
        }
    };

};
