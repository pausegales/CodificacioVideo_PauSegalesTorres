import os
import numpy as np
# ---- 6 ----
#DCT implementation

import numpy as np

class DCTConverter:
    def __init__(self):
        pass

    def forward_dct(self, input_matrix):
        """
        Perform forward Discrete Cosine Transform (DCT) on an input matrix.

        Args:
            input_matrix (numpy.ndarray): The input matrix to be transformed.

        Returns:
            numpy.ndarray: The DCT-transformed matrix.
        """
        M, N = input_matrix.shape
        dct_matrix = np.zeros((M, N))

        for u in range(M):
            for v in range(N):
                sum_dct = 0
                for x in range(M):
                    for y in range(N):
                        sum_dct += input_matrix[x, y] * np.cos((2 * x + 1) * u * np.pi / (2 * M)) * np.cos((2 * y + 1) * v * np.pi / (2 * N))
                alpha_u = 1 if u == 0 else np.sqrt(2)
                alpha_v = 1 if v == 0 else np.sqrt(2)
                dct_matrix[u, v] = (alpha_u * alpha_v / 4) * sum_dct

        return dct_matrix

    def inverse_dct(self, dct_matrix):
        """
        Perform inverse Discrete Cosine Transform (IDCT) on a DCT-transformed matrix.

        Args:
            dct_matrix (numpy.ndarray): The DCT-transformed matrix.

        Returns:
            numpy.ndarray: The original matrix after applying IDCT.
        """
        M, N = dct_matrix.shape
        idct_matrix = np.zeros((M, N))

        for x in range(M):
            for y in range(N):
                sum_idct = 0
                for u in range(M):
                    for v in range(N):
                        alpha_u = 1 if u == 0 else np.sqrt(2)
                        alpha_v = 1 if v == 0 else np.sqrt(2)
                        sum_idct += alpha_u * alpha_v * dct_matrix[u, v] * np.cos((2 * x + 1) * u * np.pi / (2 * M)) * np.cos((2 * y + 1) * v * np.pi / (2 * N))
                idct_matrix[x, y] = sum_idct / 4

        return idct_matrix

# Example usage:
if __name__ == "__main__":
    # Create an instance of the DCTConverter
    dct_converter = DCTConverter()

    # Create a sample input matrix (you can use your own data)
    input_matrix = np.array([[1, 2, 3, 4],
                             [5, 6, 7, 8],
                             [9, 10, 11, 12],
                             [13, 14, 15, 16]])

    # Perform forward DCT
    dct_transformed_matrix = dct_converter.forward_dct(input_matrix)
    print("DCT-transformed matrix:")
    print(dct_transformed_matrix)

    # Perform inverse DCT to get back the original matrix
    original_matrix = dct_converter.inverse_dct(dct_transformed_matrix)
    print("\nOriginal matrix after inverse DCT:")
    print(original_matrix)
