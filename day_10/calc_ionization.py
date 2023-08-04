
import numpy as np

def calc_ionization(alts):
    
    nAlts = len(alts)

    tau = np.zeros(nAlts) + 50.0
    peak_alt = 120.0
    tau[alts < peak_alt] = 10.0
    ionization = 1.3e-8 * np.exp(-np.abs(alts-peak_alt)/tau)

    return ionization
