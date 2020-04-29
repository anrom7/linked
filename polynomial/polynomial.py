# Implementation of the Polynomial ADT using a sorted linked list.

class Polynomial :
    # Create a new polynomial object.
    def __init__(self, degree = None, coefficient = None):
        if degree is None :
            self._polyHead = None
        else :
            self._polyHead = _PolyTermNode(degree, coefficient)
        self._polyTail = self._polyHead

    # Return the degree of the polynomial.
    def degree(self):
        if self._polyHead is None :
            return -1
        else :
            return self._polyHead.degree

    # Return the coefficient for the term of the given degree.
    def __getitem__(self, degree):
        assert self.degree() >= 0, "Operation not permitted on an empty polynomial."
        curNode = self._polyHead
        while curNode is not None and curNode.degree >= degree :
            curNode = curNode.next

        if curNode is None or curNode.degree != degree :
            return 0.0
        else :
            return curNode.coefficient

    # Evaluate the polynomial at the given scalar value.
    def evaluate(self, scalar):
        assert self.degree() >= 0, "Only non -empty polynomials can be evaluated."
        result = 0.0
        curNode = self._polyHead
        while curNode is not None :
            result += curNode.coefficient * (scalar ** curNode.degree)
            curNode = curNode.next
        return result

    # Polynomial addition: newPoly = self + rhsPoly.
    def __add__(self, rhsPoly):
    #    pass

    # Polynomial subtraction: newPoly = self - rhsPoly.
    def __sub__(self, rhsPoly):
        pass

    # Polynomial multiplication: newPoly = self * rhsPoly.
    #def __mul__(self, rhsPoly):
    #    pass

    def simple_add(self, rhsPoly):
        newPoly = Polynomial()
        if self.degree() > rhsPoly.degree():
            maxDegree = self.degree()
        else:
            maxDegree = rhsPoly.degree()

        i = maxDegree
        while i >= 0:
            value = self[i] + rhsPoly[i]
            newPoly._appendTerm(i, value)
            i += 1
        return newPoly



    def __str__(self):
        pass

# Class for creating polynomial term nodes used with the linked list.
class _PolyTermNode(object):
    def __init__(self, degree, coefficient):
        self.degree = degree
        self.coefficient = coefficient
        self.next = None

    def __str__(self):
        """
        Prints the value stored in self.
        __str__: Node -> Str
        """
        return str(self.coefficient) + "x" + str(self.degree)
