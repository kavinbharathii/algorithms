#include <stdio.h>
#include <stdlib.h>


// given an array of numbers representing the height of towers,
// find the maximum volume of water that can be contained between the towers.

// find the maximum element in a given array
int findHighest(int arr[], int len) {
    if (len <= 0) {
        return 0;
    } else {
        int highest = arr[0];

        for (int i = 0; i < len; i++) {
            if (arr[i] > highest) {
                highest = arr[i];
            }
        }

        return highest;
    }
}

// fundtion that prints the tower[kinda] with "  " and "██" characters
void printArray(int arr[], int len) {
    for (int i = 0; i < len; i++) {
        switch (arr[i]) {
            case 0:
                printf("  ");
                break;

            case 1:
                // 219 is the ascii character code for "█" [block character]
                printf("%c%c", 219, 219);
                break;
        }
    }
}

int findWaterLevel(int arr[], int len) {
    int highest = findHighest(arr, len);
    int totalVolume = 0;

    while (highest > 0) {
        int* topLayer = (int*)(malloc(sizeof(int) * len));
        int first = -1;
        int last;

        for (int i = 0; i < len; i++) {

            // make a layer of all the top blocks [blocks of the maximum height]
            if (arr[i] == highest) {
                topLayer[i] = 1;

                // note the first occurence of a 1
                if (first < 0) {
                    first = i;
                }

                // note the final occurence of a 1 
                last = i;
            } else {
                topLayer[i] = 0;
            }
            arr[i] = arr[i] == highest ? arr[i] - 1 : arr[i];
        }

        // count all the zeroes BETWEEN two 1's [between two blocks, since that is the only way to hold water]
        for (int i = first; i < last; i++) {
            if (topLayer[i] == 0) {
                totalVolume += 1;
            }
        }
        printArray(topLayer, 10);
        printf("\n");
        highest = findHighest(arr, len);
    }

    return totalVolume;
}

int main() {
    // int arr[12] = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
    // int arr[6] = {4, 2, 0, 3, 2, 5};
    int arr[10] = {5, 3, 7, 2, 6, 4, 5, 9, 1, 2};
    int len = 10;
    int ans = findWaterLevel(arr, len);
    printf("%d\n", ans);
}
