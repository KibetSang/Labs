class Calculator:
    """
    A simple Calculator class to perform basic arithmetic operations.

    This class is initialized with two numbers (num1 and num2),
    and provides methods to add, subtract, and multiply them.

    Attributes
    ----------
    num1 : int or float
        The first number.
    num2 : int or float
        The second number.
    """

    def __init__(self, num1, num2):
        """
        Initialize the Calculator with two numbers.

        Parameters
        ----------
        num1 : int or float
            The first number.
        num2 : int or float
            The second number.
        """
        self.num1 = num1
        self.num2 = num2

    def add(self):
        """
        Add the two initialized numbers.

        Returns
        -------
        int or float
            The sum of num1 and num2.
        """
        return self.num1 + self.num2

    def sub(self):
        """
        Subtract the second number from the first.

        Returns
        -------
        int or float
            The difference (num1 - num2).
        """
        return self.num1 - self.num2

    def mul(self):
        """
        Multiply the two initialized numbers.

        Returns
        -------
        int or float
            The product of num1 and num2.
        """
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2



# ------------------ Example Usage ------------------

# Create a Calculator object with numbers 2 and 4
kim = Calculator(2, 4)

# Perform operations
print("Addition:", kim.add())  # Output: 6
print("Subtraction:", kim.sub())  # Output: -2
print("Multiplication:", kim.mul())  # Output: 8
print("Division:", kim.divide())
print("The codes here testing")