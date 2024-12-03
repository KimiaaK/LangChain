"""Given a dataset of test scores,
write pandas code to return the cumulative percentage
of students that received scores within the buckets of
<50, <75, <90, <100."""

import pandas as pd

data = {"scores": [45, 67, 88, 92, 49, 74, 89, 55, 90, 100, 72, 65, 87, 94, 56, 30]}
df = pd.DataFrame(data)

bins = [-float("inf"), 50, 75, 90, 100]
labels = ["<50", "<75", "<90", "<100"]
df["bucket"] = pd.cut(df["scores"], bins=bins, labels=labels, right=False)
cumulative_counts = df["bucket"].value_counts(sort=False).cumsum()
total = len(df)
cumulative_percentage = (cumulative_counts / total) * 100
result = cumulative_percentage.reset_index()
result.columns = ["Bucket", "Cumulative Percentage"]
