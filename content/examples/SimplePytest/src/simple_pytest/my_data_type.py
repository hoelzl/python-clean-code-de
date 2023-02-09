class MyDataType:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def compute_result(self):
        """Compute an important result.

        >>> MyDataType(2, 3).compute_result()
        8
        """
        return self.a + self.b * 2

    def compute_another_result(self):
        """Compute another important result.

        >>> MyDataType(2, 3).compute_another_result()
        7
        """
        return 2 * self.a + self.b

    def print_results(self):
        """Print both results.

        >>> MyDataType(2, 3).print_results()
        The results are: 8, 7.
        """
        print(
            f"The results are: "
            f"{self.compute_result()}, "
            f"{self.compute_another_result()}."
        )
