#include <iostream>
#include <string>
#include <map>

class KoscheiBessmertnyi { // Class names can be transliterated to maintain the code's readability.
private:
    bool zhivoy;
    std::map<std::string, std::string> mestoSkrytiya;

public:
    KoscheiBessmertnyi() {
        zhivoy = true;
        mestoSkrytiya["okean"] = "ostrov";
        mestoSkrytiya["ostrov"] = "zelenyDub";
        mestoSkrytiya["zelenyDub"] = "zheleznySunduk";
        mestoSkrytiya["zheleznySunduk"] = "zayats";
        mestoSkrytiya["zayats"] = "utka";
        mestoSkrytiya["utka"] = "yaytso";
        mestoSkrytiya["yaytso"] = "igla";
    }

    void naytiIUbitDushu(std::string nachalo) {
        std::string tekushcheye = nachalo;
        while (mestoSkrytiya.find(tekushcheye) != mestoSkrytiya.end()) {
            tekushcheye = mestoSkrytiya[tekushcheye];
        }

        if (tekushcheye == "igla") {
            zhivoy = false;
            std::cout << "Душа Кощея уничтожена. Он побежден." << std::endl;
        } else {
            std::cout << "Поиск продолжается. Кощей остается в живых." << std::endl;
        }
    }
};

int main() {
    KoscheiBessmertnyi koschei;
    koschei.naytiIUbitDushu("okean");
    return 0;
}
