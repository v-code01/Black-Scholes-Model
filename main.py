from math import exp, log, sqrt
from scipy.stats import norm

def black_scholes_call(S, K, T, r, sigma):
    """
    Calculate the Black-Scholes call option price.

    Parameters:
    - S: Current stock price
    - K: Option strike price
    - T: Time to expiration (in years)
    - r: Risk-free interest rate
    - sigma: Volatility

    Returns:
    - call_price: Call option price
    """
    d1 = (log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)
    call_price = S * norm.cdf(d1) - K * exp(-r * T) * norm.cdf(d2)
    return call_price

def black_scholes_put(S, K, T, r, sigma):
    """
    Calculate the Black-Scholes put option price.

    Parameters:
    - S: Current stock price
    - K: Option strike price
    - T: Time to expiration (in years)
    - r: Risk-free interest rate
    - sigma: Volatility

    Returns:
    - put_price: Put option price
    """
    d1 = (log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)
    put_price = K * exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return put_price

def black_scholes_greeks(S, K, T, r, sigma):
    """
    Calculate the Greeks (Delta, Gamma, Theta, Vega, Rho) for a Black-Scholes option.

    Parameters:
    - S: Current stock price
    - K: Option strike price
    - T: Time to expiration (in years)
    - r: Risk-free interest rate
    - sigma: Volatility

    Returns:
    - delta: Option Delta
    - gamma: Option Gamma
    - theta: Option Theta
    - vega: Option Vega
    - rho: Option Rho
    """
    d1 = (log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)

    # Delta for both call and put
    delta_call = norm.cdf(d1)
    delta_put = norm.cdf(d1) - 1

    # Gamma for both call and put
    gamma = norm.pdf(d1) / (S * sigma * sqrt(T))

    # Theta for both call and put
    theta_call = -(S * norm.pdf(d1) * sigma) / (2 * sqrt(T)) - r * K * exp(-r * T) * norm.cdf(d2)
    theta_put = -(S * norm.pdf(d1) * sigma) / (2 * sqrt(T)) + r * K * exp(-r * T) * norm.cdf(-d2)

    # Vega for both call and put
    vega = S * norm.pdf(d1) * sqrt(T)

    # Rho for both call and put
    rho_call = K * T * exp(-r * T) * norm.cdf(d2)
    rho_put = -K * T * exp(-r * T) * norm.cdf(-d2)

    return delta_call, gamma, theta_call, vega, rho_call

# Example usage:
S = 100   # Current stock price
K = 100   # Option strike price
T = 1     # Time to expiration (in years)
r = 0.05  # Risk-free interest rate
sigma = 0.2  # Volatility

call_price = black_scholes_call(S, K, T, r, sigma)
put_price = black_scholes_put(S, K, T, r, sigma)
delta, gamma, theta, vega, rho = black_scholes_greeks(S, K, T, r, sigma)

print("Call Option Price:", call_price)
print("Put Option Price:", put_price)
print("Delta:", delta)
print("Gamma:", gamma)
print("Theta:", theta)
print("Vega:", vega)
print("Rho:", rho)
