"""
This script implements a multi-model classifier using different ml classifiers
"""
import numpy as np
import pandas as pd
from joblib import dump
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, ExtraTreesClassifier
from sklearn.tree import DecisionTreeClassifier, ExtraTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB, BernoulliNB
from sklearn.neighbors import KNeighborsClassifier
from constants import PandasDataFrame, dataset_path
from preprocess import preprocess_raw_data, create_numerical_presentation_mapper


def get_feature_ranking_importance(data: PandasDataFrame) -> None:
    """
    Requirements:This function requires mapped numerical presentation of feature 'create_numerical_presentation_mapper'
    function
    Description: Get the feature ranking importance using random forest.
    Feature importances  are computed as the mean and standard deviation of accumulation of the impurity decrease within
    each tree.
    Random Forest's ensemble approach averages individual trees' information, reducing overfitting and improving
    generalization.
    """
    # Convert categorical features into binary dummy variables 'one hot encoding'
    new_data = pd.get_dummies(data)
    # Set prediction target as parent school satisfaction as fixed-length string of size 6 characters for data type
    # The target shape is [number_of_all_parent_school_satisfaction_rows]
    y = np.asarray(new_data['parent_school_satisfaction'], dtype="|S6")
    new_data = new_data.drop(['parent_school_satisfaction'], axis=1)
    # Drop target from the dataframe to use the rest as input
    # The input shape is [number_of_rows, number_of_features]
    X = new_data.values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
    print("The data shape for input is ", X_train.shape)
    print("The data shape for target is ", y.shape)
    random_forest = RandomForestClassifier()
    random_forest.fit(X_train, y_train)
    # Sort importance in ascending order (reverse order)
    indices = np.argsort(random_forest.feature_importances_)[::-1]
    print("Feature ranking:")
    for feature in range(new_data.shape[1]):
        print("{index}: feature {feature_ranking} {feature_name} {feature_importance}".format(
            index=feature + 1,
            feature_ranking=indices[feature],
            feature_name=new_data.columns[indices[feature]],
            feature_importance=random_forest.feature_importances_[indices[feature]]))


# data = create_numerical_presentation_mapper(preprocess_raw_data(dataset_path))
# get_feature_ranking_importance(data)

def build_model_classifiers(data: PandasDataFrame) -> list[tuple[str, float]]:
    """
    Requirements:This function requires mapped numerical presentation of feature 'create_numerical_presentation_mapper'
    function
    Description: Build the ml model using random forest, ada boost, extra trees, k-nearest neighbors, decision trees,
    gaussian naive bayes, and bernoulli naive bays classifies
    :param data:
    :return all classifiers' scores:
    """
    # Define multi-model classifiers
    classifiers = [
        ('RandomForestClassifierG', RandomForestClassifier(n_jobs=-1, criterion='gini')),
        ('RandomForestClassifierE', RandomForestClassifier(n_jobs=-1, criterion='entropy')),
        ('AdaBoostClassifier', AdaBoostClassifier()),
        ('ExtraTreesClassifier', ExtraTreesClassifier(n_jobs=-1)),
        ('KNeighborsClassifier', KNeighborsClassifier(n_jobs=-1)),
        ('DecisionTreeClassifier', DecisionTreeClassifier()),
        ('ExtraTreeClassifier', ExtraTreeClassifier()),
        ('LogisticRegression', LogisticRegression()),
        ('GaussianNB', GaussianNB()),
        ('BernoulliNB', BernoulliNB())
    ]
    all_scores = []
    # Drop target from the dataframe to use the rest as input
    # The input shape is [number_of_rows, number_of_features]
    X = data.drop('parent_school_satisfaction', axis=1)
    print("The input data shape for input is: ", X.shape)
    # Set prediction target as parent school satisfaction as fixed-length string of size 6 characters for data type
    # The target shape is [number_of_all_parent_school_satisfaction_rows]
    y = np.asarray(data['parent_school_satisfaction'], dtype="|S6")
    print("The target data shape for target is: ", y.shape)
    for name, classifier in classifiers:
        scores = []
        # Fit classifiers
        classifier.fit(X, y)
        # Perform cross validation for 20 iterations (19 train iteration and 1 validation iteration)
        for i in range(20):
            # Use area under ROC as a validation metric
            roc = cross_val_score(classifier, X, y)
            scores.extend(list(roc))
        scores = np.array(scores)
        print(name, scores.mean())
        dump(classifier, f"classifiers/{name}.joblib")
        # Add a tuple for the name of the classifier and its score
        new_data = [(name, score) for score in scores]
        all_scores.extend(new_data)
    return all_scores


# data = create_numerical_presentation_mapper(preprocess_raw_data(dataset_path))
# build_model_classifiers(data)
