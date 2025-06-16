import pandas as pd
from utils import clean_text
import random

df = pd.read_csv("data/twcs.csv")

df["cleaned_text"] = df['text'].astype(str).apply(clean_text)

df = df[df["cleaned_text"].str.strip() != ""]

sample_df = df.sample(n=200, random_state=42).copy()

sample_df["label"] = ""

final_df = sample_df[["cleaned_text", "label"]]
final_df.columns = ["text", "label"]

final_df.to_csv("labels/clean_sample_for_labeling.csv", index=False, encoding="utf-8-sig")
print("DONE")