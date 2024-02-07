# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import pandas as pd
import seaborn as sns

df = sns.load_dataset("penguins")

# %%
# Anzahl nach Gattung
df.species.value_counts()

# %%
# Anzahl nach Geschlecht
df.sex.value_counts(dropna=False) # / len(penguins)

# %%
# Anzahl nach Gattung pro Insel
df[["island", "species"]].value_counts()

# %%
# durchschnittliches Gewicht pro Spezies
df.groupby("species").body_mass_g.mean()
df.groupby("species")["body_mass_g"].agg(["mean"])
df.groupby("species").agg({"body_mass_g": "mean"})

# %%
# Pinguine über 6kg Gewicht
df[df.body_mass_g > 6000]

# %%
# Anzahl Pinguine nach verschiedenen Unterscheidungskriterien
df.groupby([df.body_mass_g > 4000, df.bill_depth_mm > 20]).size()

# %%
df.describe()

# %%
df.groupby("species").describe()
