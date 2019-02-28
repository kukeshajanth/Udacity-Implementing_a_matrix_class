import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I
def dot_product(vectorA, vectorB):
        """
        Creates dot product
        """
        result = 0
    
        for i in range(len(vectorA)):
            result += vectorA[i] * vectorB[i]
        
        return result


class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        if self.h == 1 :
            return self.g[0][0]
        if self.h == 2:
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            det = (a*d) - (b*c)
            return det
        return None

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")
        
        result = 0.0

        for i in range(self.h):
            result += self[i][i]
        return result

       

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        
        inverse = []
        
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
        if self.h == 1:
            inverse.append([1 / self.g[0][0]])
        if self.h ==2:
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            det = (a*d) - (b*c)
            if (a*d) == (b*c):
                raise ValueError('The matrix is not invertible.')
            else:
                 factor = 1 / det
            
                 inverse = [[d, -b],[-c, a]]
            
                 for i in range(len(inverse)):
                     for j in range(len(inverse[0])):
                        inverse[i][j] = factor * inverse[i][j]
    
        return Matrix(inverse)
            
            

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        matrix_transpose = []
        for i in range(self.w):
            row = []
            for j in range(self.h):
                 row.append(self.g[j][i])
            matrix_transpose.append(row)
    
    
            
    
        return Matrix(matrix_transpose)

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        add = []
        
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self.g[i][j] + other.g[i][j])
            add.append(row)
            
            
            
        return Matrix(add)
                
                

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        neg = []
        
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self.g[i][j] * -1.0)
            neg.append(row)
            
            
        return Matrix(neg)
    
    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        sub = []
        
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self.g[i][j] - other.g[i][j])
            sub.append(row)
            
            
            
        return Matrix(sub)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        product = []
        
        otherT = other.T()
        
        
        
        for i in range(self.h):
            row = []
            for j in range(otherT.h):
                row.append(dot_product(self.g[i],otherT.g[j]))
            product.append(row)
                    
                
            
        return Matrix(product)
                

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            mul = []
            for i in range(self.h):
                row = []
                for j in range(self.w):
                    row.append(self.g[i][j]*other)
                mul.append(row)
            return Matrix(mul)
            
            