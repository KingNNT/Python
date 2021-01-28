import numpy as np
import pandas as pd
eps = np.finfo(float).eps
from numpy import log2 as log
import pprint

def find_entropy(df):
    Class = df.keys()[-1]
    entropy = 0
    values = df[Class].unique()
    for value in values:
        fraction = df[Class].value_counts()[value]/len(df[Class])
        entropy += -fraction*np.log2(fraction)
    return entropy

def find_entropy_attribute(df, attribute):
    Class = df.keys()[-1]
    target_variables = df[Class].unique()
    variables = df[attribute].unique()
    entropy2 = 0
    for variable in variables:
        entropy = 0
        for target_variable in target_variables:
            num = len(df[attribute][df[attribute] == variable][df[Class] == target_variable])
            den = len(df[attribute][df[attribute] == variable])
            fraction = num/(den+eps)
            entropy += -fraction*log(fraction+eps)
        fraction2 = den/len(df)
        entropy2 += -fraction2*entropy
    return abs(entropy2)

def find_winner(df):
    Entropy_att = []
    IG = []
    for key in df.keys()[:-1]:
        Entropy_att.append(find_entropy_attribute(df,key))
        IG.append(find_entropy(df)-find_entropy_attribute(df, key))
    return df.keys()[:-1][np.argmax(IG)]

def getSubtable(df, node, value):
    return df[df[node] == value].reset_index(drop=True)

def buildTree(df, tree=None):
    Class = df.keys()[-1]
    node = find_winner(df)
    attValue = np.unique(df[node])

    if tree is None:
        tree = {}
        tree[node] = {}

    for value in attValue:
        subtable = getSubtable(df, node, value)
        clValue, counts = np.unique(subtable['condition'], return_counts=True)
        if len(counts) == 1:
            tree[node][value] = clValue[0]
        else:
            tree[node][value] = buildTree(subtable)
    return tree

def main():
    df = pd.read_csv('/mnt/LearningAndWorking/Develop/Python/Learning/Excercise/DecisionTree/ID3/family.csv')
    pprint.pprint(df)
    for index, row in df.iterrows():
        if row['tax'] < 0:
            row['tax'] = 0
        if row['tax'] >= 0 and row['tax'] < 50:
            row['tax'] = 50
        if row['tax'] >= 50 and row['tax'] < 100:
            row['tax'] = 100
        if row['tax'] >= 100 and row['tax'] < 150:
            row['tax'] = 150
    pprint.pprint(df)
    t = buildTree(df)
    pprint.pprint(t)

if __name__ == "__main__":
    main()