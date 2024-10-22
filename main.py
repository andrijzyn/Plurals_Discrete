A = ['к', 'в', 'а', 'н', 'т']
B = ['л', 'ю', 'т', 'и', 'й']
C = ['м', 'а', 'й', 'к', 'а']
D = ['р', 'и', 'с', 'а', 'к']
E = ['с', 'к', 'у', 'л', 'а']


class ArrayOperations:
    def __init__(self, array):
        self.array = array

    def intersection(self, other):
        return list(set(self.array) & set(other))

    def unification(self, other):
        return list(set(self.array) | set(other))

    def difference(self, other):
        return list(set(self.array) - set(other))


a = ArrayOperations(A)
b = ArrayOperations(B)
c = ArrayOperations(C)
d = ArrayOperations(D)
e = ArrayOperations(E)

# Пересечение и объединение A, B, C, D, E
print("1) A ∩ B =", a.intersection(B))
print("2) A ∪ B =", a.unification(B))
print("3) A ∩ C =", a.intersection(C))
print("4) A ∪ C =", a.unification(C))
print("5) A ∩ D =", a.intersection(D))
print("6) A ∪ D =", a.unification(D))
print("7) A ∩ E =", a.intersection(E))
print("8) A ∪ E =", a.unification(E))

print("9) B ∩ C =", b.intersection(C))
print("10) B ∪ C =", b.unification(C))
print("11) B ∩ D =", b.intersection(D))
print("12) B ∪ D =", b.unification(D))
print("13) B ∩ E =", b.intersection(E))
print("14) B ∪ E =", b.unification(E))

print("15) C ∩ D =", c.intersection(D))
print("16) C ∪ D =", c.unification(D))
print("17) C ∩ E =", c.intersection(E))
print("18) C ∪ E =", c.unification(E))

print("19) D ∩ E =", d.intersection(E))
print("20) D ∪ E =", d.unification(E))

print("21) A \\ B =", a.difference(B))
print("22) A \\ C =", a.difference(C))
print("23) A \\ D =", a.difference(D))
print("24) A \\ E =", a.difference(E))

print("25) B \\ A =", b.difference(A))
print("26) B \\ C =", b.difference(C))
print("27) B \\ D =", b.difference(D))
print("28) B \\ E =", b.difference(E))

print("29) C \\ A =", c.difference(A))
print("30) C \\ B =", c.difference(B))
print("31) C \\ D =", c.difference(D))
print("32) C \\ E =", c.difference(E))

print("33) D \\ A =", d.difference(A))
print("34) D \\ B =", d.difference(B))
print("35) D \\ C =", d.difference(C))
print("36) D \\ E =", d.difference(E))

print("37) E \\ A =", e.difference(A))
print("38) E \\ B =", e.difference(B))
print("39) E \\ C =", e.difference(C))
print("40) E \\ D =", e.difference(D))

# a) (A∪B)∩(B∪C)∩(C∪D)∩(D∪A)
result_a = ArrayOperations(a.unification(B)).intersection(ArrayOperations(b.unification(C)).array)
result_a = ArrayOperations(result_a).intersection(ArrayOperations(c.unification(D)).array)
result_a = ArrayOperations(result_a).intersection(ArrayOperations(d.unification(A)).array)
print("a) (A∪B)∩(B∪C)∩(C∪D)∩(D∪A) =", result_a)

# b) (A\B)∪(B\C)∪(C\D)∪(D\A)
result_b = ArrayOperations(a.difference(B)).unification(ArrayOperations(b.difference(C)).array)
result_b = ArrayOperations(result_b).unification(ArrayOperations(c.difference(D)).array)
result_b = ArrayOperations(result_b).unification(ArrayOperations(d.difference(A)).array)
print("b) (A\\B)∪(B\\C)∪(C\\D)∪(D\\A) =", result_b)

# c) (A\B)∩(A\C)∩(A\D)∩(A\E)
result_c = ArrayOperations(a.difference(B)).intersection(ArrayOperations(a.difference(C)).array)
result_c = ArrayOperations(result_c).intersection(ArrayOperations(a.difference(D)).array)
result_c = ArrayOperations(result_c).intersection(ArrayOperations(a.difference(E)).array)
print("c) (A\\B)∩(A\\C)∩(A\\D)∩(A\\E) =", result_c)

# d) ((A∪B)\C)∩((A∪B)\D)
result_d = ArrayOperations(a.unification(B)).difference(C)
result_d = ArrayOperations(result_d).intersection(ArrayOperations(a.unification(B)).difference(D))
print("d) ((A∪B)\\C)∩((A∪B)\\D) =", result_d)

# e) ((A\B)∪C)∩((B\A)∪D)
result_e = ArrayOperations(a.difference(B)).unification(C)
result_e = ArrayOperations(result_e).intersection(ArrayOperations(b.difference(A)).unification(D))
print("e) ((A\\B)∪C)∩((B\\A)∪D) =", result_e)
