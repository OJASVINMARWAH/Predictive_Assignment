import numpy as np
import pandas as pd

dat = pd.read_csv("data.csv", encoding="latin1", low_memory=False)

no2_col = None
for col in dat.columns:
    if "no2" in col.lower():
        no2_col = col
        break

x = pd.to_numeric(dat[no2_col], errors="coerce").dropna().values

r = 102316096

a_r = 0.05 * (r % 7)
b_r = 0.3 * ((r % 5) + 1)

z = x + a_r * np.sin(b_r * x)

mu = np.mean(z)

sigma_sq = np.mean((z - mu) ** 2)
lam = 1 / (2 * sigma_sq)

c = np.sqrt(lam / np.pi)

print(mu)
print(lam)
print(c)
