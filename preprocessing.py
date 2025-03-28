def clear_titanicset(dataset):
    dataset.drop(["Name", "PassengerId", "Cabin"], axis=1, inplace=True)
    dataset.fillna({"Age": dataset["Age"].median()}, inplace=True)
    dataset.dropna(inplace=True)
    return dataset

def