#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_WORD_LENGTH 30
#define MAX_LINE_LENGTH 100

typedef struct Node { // Define a structure for a node in the binary search tree
    char word[MAX_WORD_LENGTH + 1];
    int count;
    struct Node *left, *right;
} Node;

Node* insert(Node *node, char *word) { // Insert a word into the binary search tree
    if (node == NULL) {
        Node *newNode = (Node *)malloc(sizeof(Node));
        if (newNode == NULL) {
            fprintf(stderr, "Memory allocation error\n");
            exit(EXIT_FAILURE);
        }
        strcpy(newNode->word, word);
        newNode->count = 1;
        newNode->left = newNode->right = NULL;
        return newNode;
    }

    int cmp = strcmp(word, node->word); // Compare the word with the word in the current node
    if (cmp < 0) {
        node->left = insert(node->left, word);
    } else if (cmp > 0) {
        node->right = insert(node->right, word);
    } else {
        node->count++;
    }

    return node;
}

Node* search(Node *node, char *word) {
    if (node == NULL) {
        return NULL;
    }

    int cmp = strcmp(word, node->word);
    if (cmp < 0) {
        return search(node->left, word);
    } else if (cmp > 0) {
        return search(node->right, word);
    } else {
        return node;
    }
}

void cleanseWord(char *word) {     // Cleanse a word by removing non-alphabetic characters and converting it to lowercase
    char cleansed[MAX_WORD_LENGTH + 1];
    int j = 0;
    for (int i = 0; word[i] != '\0' && j < MAX_WORD_LENGTH; ++i) {
        if (isalpha(word[i])) {
            cleansed[j++] = tolower(word[i]);
        }
    }
    cleansed[j] = '\0';
    strcpy(word, cleansed);
}

void freeTree(Node *node) { // Free the memory allocated for the binary search tree
    if (node == NULL) {
        return;
    }
    freeTree(node->left);
    freeTree(node->right);
    free(node);
}

int main() {
    char searchWord[MAX_WORD_LENGTH + 1], originalSearchWord[MAX_WORD_LENGTH + 1], line[MAX_LINE_LENGTH + 1];
    scanf("%s%*c", searchWord);
    strcpy(originalSearchWord, searchWord); // Store the original search word
    cleanseWord(searchWord); // cleanse the search word for comparison

    Node *root = NULL;
    while (fgets(line, sizeof(line), stdin)) {
        char *token = strtok(line, " ,.\n");
        while (token != NULL) {
            cleanseWord(token);
            if (strlen(token) > 0) {
                root = insert(root, token);
            }
            token = strtok(NULL, " ,.\n");
        }
    }

    Node *found = search(root, searchWord);
    if (found) {
        printf("%s => %d\n", originalSearchWord, found->count);
    } else {
        printf("** \"%s\" not found **\n", originalSearchWord); 
    }

    freeTree(root);
    return 0;
}

