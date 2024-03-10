"""
This script evaluates the classifiers using dummy data
"""

import pandas as pd
from joblib import load
from constants import test_data, consistent_column_names_dict
from preprocess import create_numerical_presentation_mapper


def evaluate_classifier(classifier_name: str) -> None:
    """
    Requirements: Preprocess dummy test data and pass the classifier name
    Description: Evaluates the classifiers using dummy test data
    :param classifier_name:
    :return:
    """
    # Load the model based on the classifier name
    loaded_model = load("classifiers/{classifier_name}.joblib".format(classifier_name=classifier_name))
    print("Prediction using {classifier_name}".format(classifier_name=classifier_name))
    # Create a new dataframe from the test data
    new_dataframe = pd.DataFrame(test_data)
    # Rename column names in the dataframe to ensure consistency
    renamed_data = new_dataframe.rename(columns=consistent_column_names_dict)
    # Create a numerical presentation mapper for non-numerical values in the dataframe
    numerical_data = create_numerical_presentation_mapper(renamed_data)
    # Drop the prediction target
    prediction_data = numerical_data.drop('parent_school_satisfaction', axis=1)
    # Make the prediction of parent satisfaction of the student school
    prediction = loaded_model.predict(prediction_data)
    print(prediction)


"""
The critical features which affect the prediction are the student behavioural features (raised_hands, visited_resources,
announcement_views, discussion)
"""
evaluate_classifier("GaussianNB")
