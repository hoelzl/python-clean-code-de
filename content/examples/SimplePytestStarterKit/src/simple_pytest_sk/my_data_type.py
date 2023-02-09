class MyDataType:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def compute_result(self):
        """Compute an important result."""
        return self.a + self.b * 2

    def compute_another_result(self):
        """Compute another important result."""
        return 2 * self.a + self.b

    def print_results(self):
        """Print both results."""
        print(
            f"The results are: "
            f"{self.compute_result()}, "
            f"{self.compute_another_result()}."
        )
