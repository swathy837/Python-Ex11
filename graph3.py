import numpy as np
import matplotlib.pyplot as plt
np.random.seed(10)
daily_returns = np.random.normal(0.001, 0.02, 252)
initial_price = 100
stock_prices = initial_price * np.cumprod(1 + daily_returns)
cumulative_returns = (stock_prices / initial_price) - 1
average_return = np.mean(daily_returns)
volatility = np.std(daily_returns)
final_return = cumulative_returns[-1]
print("Average Daily Return =", average_return)
print("Volatility (Std Dev) =", volatility)
print("Final Cumulative Return =", final_return)
plt.plot(stock_prices)
plt.xlabel("Trading Days")
plt.ylabel("Stock Price")
plt.title("Simulated Stock Price Movement")
plt.grid(True)
plt.show()
plt.plot(cumulative_returns)
plt.xlabel("Trading Days")
plt.ylabel("Cumulative Return")
plt.title("Cumulative Returns Over Time")
plt.grid(True)
plt.show()
