#include <stdio.h>
#include <stdlib.h>

float read_temperature() {
    return 22.5 + (rand() % 100) / 10.0;
}

int main() {
    printf("Current temperature: %.2f°C\n", read_temperature());
    return 0;
}
