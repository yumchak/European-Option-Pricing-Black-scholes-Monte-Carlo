# European Option Pricing and Risk Sensitivity Analysis

## Overview
This project studies the pricing of European call options using both analytical and simulation-based approaches. The Black–Scholes model is implemented to compute the theoretical option price, while Monte Carlo simulation is used to estimate the option value numerically.

The project also investigates how option prices respond to changes in key parameters such as volatility and time to maturity, providing insights into option risk sensitivities.

The stock price dynamics are assumed to follow Geometric Brownian Motion (GBM), which is commonly used in quantitative finance to model asset price evolution.

## Mathematical Framework

### Stock Price Model

Under the Black–Scholes framework, the underlying asset price follows Geometric Brownian Motion:
$$d S_t = \mu S_t dt + \sigma S_t d W_t$$

which has the solution
$$S_T = S_0  \exp \left((\mu - \frac{1}{2} \sigma ^2)T + \sigma W_T\right)$$

### Black–Scholes Call Option Price
The Black–Scholes formula for a European call option is
$$ C = S_0 N(d_1) - K e^{(-rT)} N(d_2)$$

where
$$d_1 = \frac {\ln (\frac{S_0}{K}) + (r + \frac {1}{2} \sigma^2)  T}{\sigma \sqrt{T}}$$
$$d_2 = d_1 - \sigma \sqrt{T}$$

### Monte Carlo Pricing
Monte Carlo simulation estimates the option price by simulating many possible stock price paths and computing the discounted expected payoff:
$$
\hat{C} = e^{-rT} (\frac{1}{N}) \sum \max (S_T ^i - K, 0)
$$

As the number of simulations increases, the Monte Carlo estimate converges to the theoretical Black–Scholes price.

## Project structure
#### Section 1. Implemention of pricing models
- Implement the Black-Scholes formula for European call options
- Simulate stock price paths using Geometric Brownian Motion
- Estimate option prices using Monte Carlo simulation
#### Section 2. Price Behaviour Analysis
- Analyse how option prices change with respect to underlying stock price
- Compare theoretical prices with Monte Carlo estimates
#### Section 3. Risk Sensitivity Analysis
- Investigate the Greeks (Vega, Theta)
- Analyse how different parameters affect option price and risk exposure

## Conclusion
This project demonstrates how analytical models and simulation techniques can be used together to study derivative pricing. The Monte Carlo method provides numerical estimates that converge to the theoretical Black–Scholes price as the number of simulations increases. Sensitivity analysis further illustrates how volatility and time to maturity influence option values.
