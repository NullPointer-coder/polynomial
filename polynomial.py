class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

class Int:
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return str(self.i)

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, (Mul, Div)):
            p1_repr = "( " + repr(self.p1) + " )"
        else:
            p1_repr = repr(self.p1)

        if isinstance(self.p2, (Mul, Div)):
            p2_repr = "( " + repr(self.p2) + " )"
        else:
            p2_repr = repr(self.p2)

        return p1_repr + " - " + p2_repr

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, Add):
            if isinstance(self.p2, Add):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, Add):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)

class Div:
  def __init__(self, p1, p2):
      self.p1 = p1
      self.p2 = p2

  def __repr__(self):
      if isinstance(self.p1, (Add, Sub, Mul)):
          p1_repr = "( " + repr(self.p1) + " )"
      else:
          p1_repr = repr(self.p1)

      if isinstance(self.p2, (Add, Sub, Mul)):
          p2_repr = "( " + repr(self.p2) + " )"
      else:
          p2_repr = repr(self.p2)

      return p1_repr + " / " + p2_repr



poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly)

test_poly = Div(Sub(X(), Int(2)), Mul(Int(3), X())) #Output: 4 + 3 + X + 1 * ( X * X + 1 )
print(test_poly)  # Output: ((X - 2) / (3 * X))
