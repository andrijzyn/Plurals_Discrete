import termcolor

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


def print_colored_intersection(label, array1, array2):
    intersection = set(array1) & set(array2)
    colored_array1 = [termcolor.colored(x, 'green') if x in intersection else x for x in array1]
    colored_array2 = [termcolor.colored(x, 'green') if x in intersection else x for x in array2]
    print(f"{label} {intersection} - A = {''.join(colored_array1)}, B = {''.join(colored_array2)}")


# Пересечение и объединение A, B, C, D, E
print_colored_intersection("1) A ∩ B =", A, B)
print(f"2) A ∪ B = {a.unification(B)}")
print_colored_intersection("3) A ∩ C =", A, C)
print(f"4) A ∪ C = {a.unification(C)}")
print_colored_intersection("5) A ∩ D =", A, D)
print(f"6) A ∪ D = {a.unification(D)}")
print_colored_intersection("7) A ∩ E =", A, E)
print(f"8) A ∪ E = {a.unification(E)}")

print_colored_intersection("9) B ∩ C =", B, C)
print(f"10) B ∪ C = {b.unification(C)}")
print_colored_intersection("11) B ∩ D =", B, D)
print(f"12) B ∪ D = {b.unification(D)}")
print_colored_intersection("13) B ∩ E =", B, E)
print(f"14) B ∪ E = {b.unification(E)}")

print_colored_intersection("15) C ∩ D =", C, D)
print(f"16) C ∪ D = {c.unification(D)}")
print_colored_intersection("17) C ∩ E =", C, E)
print(f"18) C ∪ E = {c.unification(E)}")

print_colored_intersection("19) D ∩ E =", D, E)
print(f"20) D ∪ E = {d.unification(E)}")

print(f"21) A \\ B = {a.difference(B)}")
print(f"22) A \\ C = {a.difference(C)}")
print(f"23) A \\ D = {a.difference(D)}")
print(f"24) A \\ E = {a.difference(E)}")

print(f"25) B \\ A = {b.difference(A)}")
print(f"26) B \\ C = {b.difference(C)}")
print(f"27) B \\ D = {b.difference(D)}")
print(f"28) B \\ E = {b.difference(E)}")

print(f"29) C \\ A = {c.difference(A)}")
print(f"30) C \\ B = {c.difference(B)}")
print(f"31) C \\ D = {c.difference(D)}")
print(f"32) C \\ E = {c.difference(E)}")

print(f"33) D \\ A = {d.difference(A)}")
print(f"34) D \\ B = {d.difference(B)}")
print(f"35) D \\ C = {d.difference(C)}")
print(f"36) D \\ E = {d.difference(E)}")

print(f"37) E \\ A = {e.difference(A)}")
print(f"38) E \\ B = {e.difference(B)}")
print(f"39) E \\ C = {e.difference(C)}")
print(f"40) E \\ D = {e.difference(D)}")

# a) (A∪B)∩(B∪C)∩(C∪D)∩(D∪A)
step1_a = a.unification(B)
step2_a = b.unification(C)
step3_a = c.unification(D)
step4_a = d.unification(A)
step5_a = ArrayOperations(step1_a).intersection(step2_a)
step6_a = ArrayOperations(step5_a).intersection(step3_a)
result_a = ArrayOperations(step6_a).intersection(step4_a)
print(f"a) (A∪B) = {step1_a}, (B∪C) = {step2_a}, (C∪D) = {step3_a}, (D∪A) = {step4_a}")
print(f"a) (A∪B)∩(B∪C) = {step5_a}, (A∪B)∩(B∪C)∩(C∪D) = {step6_a}, (A∪B)∩(B∪C)∩(C∪D)∩(D∪A) = {result_a}")

# b) (A\B)∪(B\C)∪(C\D)∪(D\A)
step1_b = a.difference(B)
step2_b = b.difference(C)
step3_b = c.difference(D)
step4_b = d.difference(A)
step5_b = ArrayOperations(step1_b).unification(step2_b)
step6_b = ArrayOperations(step5_b).unification(step3_b)
result_b = ArrayOperations(step6_b).unification(step4_b)
print(f"b) (A\\B) = {step1_b}, (B\\C) = {step2_b}, (C\\D) = {step3_b}, (D\\A) = {step4_b}")
print(f"b) (A\\B)∪(B\\C) = {step5_b}, (A\\B)∪(B\\C)∪(C\\D) = {step6_b}, (A\\B)∪(B\\C)∪(C\\D)∪(D\\A) = {result_b}")

# c) (A\B)∩(A\C)∩(A\D)∩(A\E)
step1_c = a.difference(B)
step2_c = a.difference(C)
step3_c = a.difference(D)
step4_c = a.difference(E)
step5_c = ArrayOperations(step1_c).intersection(step2_c)
step6_c = ArrayOperations(step5_c).intersection(step3_c)
result_c = ArrayOperations(step6_c).intersection(step4_c)
print(f"c) (A\\B) = {step1_c}, (A\\C) = {step2_c}, (A\\D) = {step3_c}, (A\\E) = {step4_c}")
print(f"c) (A\\B)∩(A\\C) = {step5_c}, (A\\B)∩(A\\C)∩(A\\D) = {step6_c}, (A\\B)∩(A\\C)∩(A\\D)∩(A\\E) = {result_c}")

# d) ((A∪B)\C)∩((A∪B)\D)
step1_d = a.unification(B)
step2_d = ArrayOperations(step1_d).difference(C)
step3_d = ArrayOperations(step1_d).difference(D)
result_d = ArrayOperations(step2_d).intersection(step3_d)
print(f"d) (A∪B) = {step1_d}, ((A∪B)\\C) = {step2_d}, ((A∪B)\\D) = {step3_d}")
print(f"d) ((A∪B)\\C)∩((A∪B)\\D) = {result_d}")

# e) ((A\B)∪C)∩((B\A)∪D)
step1_e = a.difference(B)
step2_e = b.difference(A)
step3_e = ArrayOperations(step1_e).unification(C)
step4_e = ArrayOperations(step2_e).unification(D)
result_e = ArrayOperations(step3_e).intersection(step4_e)
print(f"e) (A\\B) = {step1_e}, (B\\A) = {step2_e}, ((A\\B)∪C) = {step3_e}, ((B\\A)∪D) = {step4_e}")
print(f"e) ((A\\B)∪C)∩((B\\A)∪D) = {result_e}")
