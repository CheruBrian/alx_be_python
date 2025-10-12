class Calculator:
    """A simple calculator demonstrating class and static methods."""

    # Class attribute accessible via cls in a class method
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method that returns the sum of two numbers.
        Does not access class or instance data.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method that prints the class attribute
        and returns the product of two numbers.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
