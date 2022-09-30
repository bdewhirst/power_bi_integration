
# flat script 1
import pandas as pd

data = [["Alex", 10], ["Bob", 12], ["Clarke", 13]]
df = pd.DataFrame(data, columns=["Name", "Age"], dtype=float)
print(df)


# flat script 2
import pandas as pd
from sklearn.datasets import load_iris

data = load_iris()
df2 = pd.DataFrame(data=data.data, columns=data.feature_names)
print(df2)

# flat script 3 (apply as transform after loading in df2)
import pandas as pd
from sklearn.cluster import KMeans

dataset = pd.DataFrame(data=data.data, columns=data.feature_names)
kmeans = KMeans(
    n_clusters=4,
    init="k-means++",
    n_init=1,
    random_state=42,
)
kmeans_fit = kmeans.fit(dataset)
labels = kmeans_fit.labels_
dataset["Cluster"] = labels
