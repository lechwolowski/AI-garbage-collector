from sklearn import tree


def make_tree(maps, actions):
    # clf = tree.DecisionTreeClassifier(criterion = "entropy", max_depth = 6)
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(maps, actions)
    return clf
