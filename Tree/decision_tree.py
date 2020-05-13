from sklearn import tree


def make_tree(maps, actions):
    clf = tree.DecisionTreeClassifier(criterion="entropy")
    print("przed fit")
    print("maps:", maps)
    print("actions:", actions)
    clf = clf.fit(maps, actions)
    print("po fit")
    return clf
