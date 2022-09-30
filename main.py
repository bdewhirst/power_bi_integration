import pandas as pd
import sklearn

# import numpy as np
# import matplotlib


class Example:
    # examples to test Power BI integration
    def __init__(self):
        data = [["Alex", 10], ["Bob", 12], ["Clarke", 13]]
        self.df = pd.DataFrame(data, columns=["Name", "Age"], dtype=float)

        from sklearn.datasets import load_iris

        data = load_iris()
        self.df2 = pd.DataFrame(data=data.data, columns=data.feature_names)

    def trivial_example(self):
        print(self.df)

    def second_example(self):
        print(self.df2)

    def kmeans_example(self):
        from sklearn.cluster import KMeans

        dataset = self.df2.copy()

        kmeans = KMeans(
            n_clusters=4,
            init="k-means++",
            n_init=1,
            random_state=42,
        )
        kmeans_fit = kmeans.fit(dataset)
        labels = kmeans_fit.labels_
        dataset["Cluster"] = labels
        return labels


if __name__ == "__main__":
    e = Example()
    e.trivial_example()
    e.second_example()
    labels = e.kmeans_example()
    print("done")
