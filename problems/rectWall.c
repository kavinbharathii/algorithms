#include <stdio.h>
#include <stdlib.h>

// QUESTION: given an array of numbers representing the height of vertical 
// slabs of stone, find the largest rectangular area that can be formed
// from the slabs, assuming the slabs are of unit width.

// find the largest integer in a given array 
int findMaxInArray(int arr[], int len) {
    int highest = 0;

    for (int i = 0; i < len; i++) {
        if (arr[i] > highest) {
            highest = arr[i];
        }
    }

    return highest;
}

// find the largest rectangular area from a 
// given array of vertical stone slabs 
int findLargestArea(int arr[], int len) {
    
    // array for storing the largest area that can
    // be calculated from each slab in the array 
    int *areas = (int*)malloc(sizeof(int) * len);

    for (int i = 0; i < len; i++) {
        int height = arr[i];

        // rectMap stored the number of adjacent slabs 
        // at various levels of height, ranging from 0..to the height of the slab 
        int *rectMap = (int*)malloc(sizeof(int) * height);

        while (height > 0) {
            int slabsOfSameHeight = 1;

            // checking slabs to the left
            int j = i - 1;
            while (j > -1) {
                if (arr[j] >= height) {
                    slabsOfSameHeight ++;
                } else {
                    break;
                }
                j--;
            }

            // checking slabs to the right
            j = i + 1;
            while (j < len) {
                if (arr[j] >= height) {
                    slabsOfSameHeight ++;
                } else {
                    break;
                }
                j ++;
            }

            height --;
            rectMap[height] = slabsOfSameHeight;
        }

        int maximumAreaFromSlab = 0;
        for (int h = 0; h < arr[i]; h++) {
            // essentially we are multiplying the height 
            // with the number of adjacent slabs near the current
            // slab that are atleast as tall as h(the current height)
            // which will give us the area of the rectangle
            // formed from this slab 
            int areaFromSlabHeight = rectMap[h] * (h + 1);

            if (areaFromSlabHeight > maximumAreaFromSlab) {
                maximumAreaFromSlab = areaFromSlabHeight;
            }
        }
        // storing the largest possible area for the slab
        areas[i] = maximumAreaFromSlab;
    }

    int largestArea = findMaxInArray(areas, len);
    return largestArea;
}

void main() {
    int arr[8] = {4, 1, 5, 3, 3, 2, 4, 1};
    int len = sizeof(arr) / sizeof(int);
    int area = findLargestArea(arr, len);
    printf("Largest available area is: %d", area); 
}
