#include <iostream>

using namespace std;

int findMaxUnique(int* row, int size) {
    int maxUnique = -1;
    bool hasUnique = false;
    
    for (int i = 0; i < size; i++) {
        int count = 0;
        for (int j = 0; j < size; j++) {
            if (row[i] == row[j]) {
                count++;
            }
        }
        if (count == 1) {
            hasUnique = true;
            if (row[i] > maxUnique) {
                maxUnique = row[i];
            }
        }
    }
    
    return hasUnique ? maxUnique : -1;
}

void sortMatrix(int** matrix, int* sizes, int rows) {
    int* keys = new int[rows];
    int* indices = new int[rows];
    
    for (int i = 0; i < rows; i++) {
        keys[i] = findMaxUnique(matrix[i], sizes[i]);
        indices[i] = i;
    }
    
    for (int i = 0; i < rows - 1; i++) {
        for (int j = 0; j < rows - i - 1; j++) {
            bool swapNeeded = false;
            
            if (keys[j] == -1 && keys[j + 1] != -1) {
                swapNeeded = false;
            } else if (keys[j] != -1 && keys[j + 1] == -1) {
                swapNeeded = true;
            } else if (keys[j] != -1 && keys[j + 1] != -1) {
                if (keys[j] > keys[j + 1]) {
                    swapNeeded = true;
                }
            }
            
            if (swapNeeded) {
                int tempKey = keys[j];
                keys[j] = keys[j + 1];
                keys[j + 1] = tempKey;
                
                int tempIndex = indices[j];
                indices[j] = indices[j + 1];
                indices[j + 1] = tempIndex;
            }
        }
    }
    
    int** sortedMatrix = new int*[rows];
    int* sortedSizes = new int[rows];
    
    for (int i = 0; i < rows; i++) {
        sortedMatrix[i] = matrix[indices[i]];
        sortedSizes[i] = sizes[indices[i]];
    }
    
    for (int i = 0; i < rows; i++) {
        matrix[i] = sortedMatrix[i];
        sizes[i] = sortedSizes[i];
    }
    
    delete[] keys;
    delete[] indices;
    delete[] sortedMatrix;
    delete[] sortedSizes;
}

void printMatrix(int** matrix, int* sizes, int rows, const char* title) {
    cout << "\n" << title << ":\n";
    for (int i = 0; i < rows; i++) {
        cout << "  Строка " << i + 1 << ": [";
        for (int j = 0; j < sizes[i]; j++) {
            cout << matrix[i][j];
            if (j < sizes[i] - 1) cout << ", ";
        }
        cout << "]";
        
        int maxUnique = findMaxUnique(matrix[i], sizes[i]);
        if (maxUnique != -1) {
            cout << " -> макс. неповторяющийся: " << maxUnique;
        } else {
            cout << " -> нет неповторяющихся элементов";
        }
        cout << "\n";
    }
}

int main() {
    int rows = 6;
    int** matrix = new int*[rows];
    int* sizes = new int[rows];
    
    sizes[0] = 6;
    matrix[0] = new int[sizes[0]]{3, 1, 4, 1, 5, 2};
    
    sizes[1] = 4;
    matrix[1] = new int[sizes[1]]{2, 2, 2, 2};
    
    sizes[2] = 7;
    matrix[2] = new int[sizes[2]]{7, 8, 9, 7, 8, 10, 9};
    
    sizes[3] = 5;
    matrix[3] = new int[sizes[3]]{1, 2, 3, 4, 5};
    
    sizes[4] = 8;
    matrix[4] = new int[sizes[4]]{6, 6, 6, 7, 7, 7, 8, 8};
    
    sizes[5] = 6;
    matrix[5] = new int[sizes[5]]{0, 1, 0, 2, 3, 2};
    
    cout << "Исходная матрица:";
    for (int i = 0; i < rows; i++) {
        cout << "\n  Строка " << i + 1 << ": [";
        for (int j = 0; j < sizes[i]; j++) {
            cout << matrix[i][j];
            if (j < sizes[i] - 1) cout << ", ";
        }
        cout << "]";
    }
    
    sortMatrix(matrix, sizes, rows);
    
    printMatrix(matrix, sizes, rows, "Отсортированная матрица");
    
    cout << "\nПорядок сортировки (по возрастанию наибольшего неповторяющегося элемента):\n";
    for (int i = 0; i < rows; i++) {
        int maxUnique = findMaxUnique(matrix[i], sizes[i]);
        cout << "  " << i + 1 << ". [";
        for (int j = 0; j < sizes[i]; j++) {
            cout << matrix[i][j];
            if (j < sizes[i] - 1) cout << ", ";
        }
        cout << "]";
        if (maxUnique != -1) {
            cout << " -> " << maxUnique;
        } else {
            cout << " -> нет уникальных элементов";
        }
        cout << "\n";
    }
    
    for (int i = 0; i < rows; i++) {
        delete[] matrix[i];
    }
    delete[] matrix;
    delete[] sizes;
    
    return 0;
}