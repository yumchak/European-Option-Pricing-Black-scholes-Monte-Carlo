import numpy as np
from scipy.stats import norm 

def black_scholes_call(S, K, r, sigma, T):
    d1 = (np.log(S/K) + (r + 1/2 * sigma **2)* T) / sigma * np.sqrt(T)
    d2 = d1 - sigma* np.sqrt(T)
    C = S * norm.cdf(d1) - K * np.exp( -r * T) * norm.cdf(d2)
    return C