# Black-Scholes Option Pricing Model

## Overview

This Python repository implements the Black-Scholes option pricing model, providing a tool for calculating option prices and Greeks (Delta, Gamma, Theta, Vega, Rho) for both call and put options.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Installation

To use this Black-Scholes option pricing model, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/black-scholes-option-pricing.git
    ```

2. Install required dependencies:

    ```bash
    pip install scipy
    ```

## Usage

The main functionality is provided by the `black_scholes.py` file, which includes functions for calculating option prices and Greeks.

### Option Pricing

```python
from black_scholes import black_scholes_call, black_scholes_put

# Define option parameters
S = 100   # Current stock price
K = 100   # Option strike price
T = 1     # Time to expiration (in years)
r = 0.05  # Risk-free interest rate
sigma = 0.2  # Volatility

# Calculate option prices
call_price = black_scholes_call(S, K, T, r, sigma)
put_price = black_scholes_put(S, K, T, r, sigma)
