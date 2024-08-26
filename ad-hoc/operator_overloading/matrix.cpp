#include <assert.h>
#include <vector>


class Matrix {
public:
  Matrix(int rows, int columns): rows_(rows), columns_(columns), values_(rows*columns) {}
  int& operator()(int row, int column) {
    return values_[row*columns_ + column];
  }
  int operator()(int row, int column) const {
    return values_[row*columns_ + column];
  }
  Matrix operator+(Matrix m) {
    Matrix res(rows_, columns_);
    for (int i = 0; i < rows_; i++){
        for (int j = 0; j < columns_; j++) {
            res(i, j) = this->operator()(i, j) + m(i, j);
        }
    }
    return res;
  }

private:
  int rows_;
  int columns_;
  std::vector<int> values_;

};


int main() {
    Matrix matrix(2, 2);
    matrix(0, 0) = 4;
    assert(matrix(0, 0) == 4);
    Matrix mateix_sum = Matrix(2, 2) + matrix;
}