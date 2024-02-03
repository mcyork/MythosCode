#include <iostream>

class Daedalus {
public:
    void createWings() { std::cout << "Daedalus creates wings to escape." << std::endl; }
};

class Icarus : public Daedalus {
public:
    void flyTooHigh() { std::cout << "Icarus flies too close to the sun, and his wings melt." << std::endl; }
};

int main() {
    Icarus icarus;
    icarus.createWings();
    icarus.flyTooHigh();
    return 0;
}
