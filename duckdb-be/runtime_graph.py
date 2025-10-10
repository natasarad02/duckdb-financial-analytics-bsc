import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv("optimization.csv")


x = np.arange(len(df["query"]))  
width = 0.35  

# Before ms, after ms
plt.figure(figsize=(10, 6))
plt.bar(x - width/2, df["before_ms"], width, label="before", color='purple')
plt.bar(x + width/2, df["after_ms"], width, label="after", color='skyblue')

plt.xlabel("Query")
plt.ylabel("Time (ms)")
plt.title("Before Optimization vs Adter Optimization - Execution Time per Query")
plt.xticks(x, df["query"])
plt.legend()
plt.tight_layout()
plt.savefig("time_comparison.png", dpi=300)
plt.grid(True, which="both", linestyle="--", alpha=0.6)

plt.show()
