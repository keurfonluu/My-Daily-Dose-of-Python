#%% [markdown]
# You are given an array. Each element represents the price of a stock on that particular day.
# Calculate and return the maximum profit you can make from buying and selling that stock only once.
#
# Example
# ```
# Input: [9, 11, 8, 5, 7, 10]
# Output: 5
# ```

#%%
def buy_and_sell(arr):
    profit = arr[1] - arr[0]
    for i, buy in enumerate(arr[:-1]):
        for sell in arr[i:]:
            profit = max(profit, sell - buy)
    return profit
  
print(buy_and_sell([9, 11, 8, 5, 7, 10]))