#include <iostream>
#include <cmath>

using namespace std;

const double EPS = 1e-9;
const int MAX_ITER = 10000;

double norm(double* v, int n) {
    double sum = 0;
    for (int i = 0; i < n; i++) {
        sum += v[i] * v[i];
    }
    return sqrt(sum);
}

void normalize(double* v, int n) {
    double nrm = norm(v, n);
    if (nrm > EPS) {
        for (int i = 0; i < n; i++) {
            v[i] /= nrm;
        }
    }
}

void multiply(double** A, double* v, double* result, int n) {
    for (int i = 0; i < n; i++) {
        result[i] = 0;
        for (int j = 0; j < n; j++) {
            result[i] += A[i][j] * v[j];
        }
    }
}

double dot(double* a, double* b, int n) {
    double sum = 0;
    for (int i = 0; i < n; i++) {
        sum += a[i] * b[i];
    }
    return sum;
}

void powerMethod(double** A, int n, double& eigenvalue, double* eigenvector) {
    double* v = new double[n];
    double* Av = new double[n];
    
    for (int i = 0; i < n; i++) {
        v[i] = 1.0;
    }
    
    normalize(v, n);
    
    double lambda_old = 0;
    double lambda_new = 0;
    
    for (int iter = 0; iter < MAX_ITER; iter++) {
        multiply(A, v, Av, n);
        
        lambda_new = dot(Av, v, n);
        
        normalize(Av, n);
        
        for (int i = 0; i < n; i++) {
            v[i] = Av[i];
        }
        
        if (fabs(lambda_new - lambda_old) < EPS) {
            break;
        }
        
        lambda_old = lambda_new;
    }
    
    eigenvalue = lambda_new;
    for (int i = 0; i < n; i++) {
        eigenvector[i] = v[i];
    }
    
    delete[] v;
    delete[] Av;
}

void printMatrix(double** A, int n) {
    for (int i = 0; i < n; i++) {
        cout << "  ";
        for (int j = 0; j < n; j++) {
            cout << A[i][j];
            if (j < n - 1) cout << "\t";
        }
        cout << endl;
    }
}

void printVector(double* v, int n, const char* name) {
    cout << name << " = [";
    for (int i = 0; i < n; i++) {
        cout << v[i];
        if (i < n - 1) cout << ", ";
    }
    cout << "]" << endl;
}

int main() {
    int n;
    
    cout << "Введите размер матрицы: ";
    cin >> n;
    
    double** A = new double*[n];
    for (int i = 0; i < n; i++) {
        A[i] = new double[n];
    }
    
    cout << "Введите элементы матрицы:" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> A[i][j];
        }
    }
    
    cout << "\nМатрица A:" << endl;
    printMatrix(A, n);
    
    double eigenvalue;
    double* eigenvector = new double[n];
    
    powerMethod(A, n, eigenvalue, eigenvector);
    
    cout << "\nРезультаты:" << endl;
    cout << "Наибольшее по модулю собственное значение: " << eigenvalue << endl;
    cout << "Соответствующий собственный вектор: ";
    printVector(eigenvector, n, "v");
    
    
    for (int i = 0; i < n; i++) {
        delete[] A[i];
    }
    delete[] A;
    delete[] eigenvector;
    
    
    return 0;
}