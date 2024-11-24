class ArrayMatrix:
    def __init__(self):
        self.array = []
        self.matrix = []

    # Array Operations
    def insert_to_array(self, index, value):
        self.array.insert(index, value)

    def delete_from_array(self, index):
        if 0 <= index < len(self.array):
            self.array.pop(index)
        else:
            raise IndexError("Index out of range.")

    def access_array(self, index):
        if 0 <= index < len(self.array):
            return self.array[index]
        else:
            raise IndexError("Index out of range.")

    # Matrix Operations
    def create_matrix(self, rows, cols):
        self.matrix = [[0] * cols for _ in range(rows)]

    def update_matrix(self, row, col, value):
        self.matrix[row][col] = value

    def access_matrix(self, row, col):
        return self.matrix[row][col]

    # Example Usage
    def array_example(self):
        print("Array Example:")
        self.insert_to_array(0, 10)
        self.insert_to_array(1, 20)
        print(f"Array after insertion: {self.array}")  # [10, 20]
        self.delete_from_array(0)
        print(f"Array after deletion: {self.array}")  # [20]
        print(f"Accessing first element: {self.access_array(0)}")  # 20

    def matrix_example(self):
        print("Matrix Example:")
        self.create_matrix(3, 3)
        self.update_matrix(1, 1, 5)
        print(f"Matrix element at (1, 1): {self.access_matrix(1, 1)}")  # 5
        print(f"Matrix: {self.matrix}")

data = ArrayMatrix()
data.array_example()
data.matrix_example()
