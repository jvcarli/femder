import numpy as np

# This is the original fd.SPL (it has the conversion to np.real)
# def p2SPL(p):
#     SPL = 10 * np.log10(0.5 * p * np.conj(p) / (2e-5) ** 2)
#     return np.real(SPL)


def p2SPL(p):
    SPL = 10 * np.log10(0.5 * p * np.conj(p) / (2e-5) ** 2)
    return SPL
