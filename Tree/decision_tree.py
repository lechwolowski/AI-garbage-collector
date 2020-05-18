from sklearn import tree


def make_tree(maps, actions):
    clf = tree.DecisionTreeClassifier(criterion="entropy")
    clf = clf.fit(maps, actions)
    return clf
