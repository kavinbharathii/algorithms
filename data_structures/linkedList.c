
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int key;
    struct Node *next;
} Node;

Node* newNode(int val) {
    Node* temp = (Node*)malloc(sizeof(Node));
    temp->key = val;
    temp->next = NULL;

    return temp;
    
}

Node* linkedList(int array[], int length) {
    Node * head;
    Node * temp;

    for (int i = 0; i < length; i++) {
        Node * node = (Node*)malloc(sizeof(Node));
        node = newNode(array[i]);

        if (i == 0) {
            head = node;
            temp = node;
        } else {
            temp->next = node;
        }
        temp = node;
    }
    return head;
}


void main() {
    int arr[] = {2, 3, 6, 7, 10, 13, 53, 98, 22};
    int len = sizeof(arr) / sizeof(int);
    Node * head = linkedList(arr, len);
    
    while (1) {
        printf("%d\n", head->key);
        head = head->next;

        if (head == NULL) {
            break;
        }
    }
}
