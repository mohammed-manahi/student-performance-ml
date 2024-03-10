"""
This script contains data visualization plots
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from constants import dataset_path, plots_path, PandasDataFrame
from preprocess import preprocess_raw_data, create_numerical_presentation_mapper
from multi_model_classifier import build_model_classifiers


def visualize_student_behaviour(data: PandasDataFrame) -> None:
    """
    Requirements: This function requires renamed columns 'preprocess_raw_data' function
    Description: Plot a heatmap of mean and standard deviation for the students' behaviour (raised_hands,
    visited_resources, announcement_views, discussion) based on their demographic data (gender, nationality,
    place_of_birth)
    :return:
    """
    # Create pivot table
    pivot_table = pd.pivot_table(
        data,
        values=["raised_hands", "visited_resources", "announcement_views", "discussion"],
        index=["gender", "nationality", "place_of_birth"],
        columns=["parent_school_satisfaction"],
        aggfunc=[np.mean, np.std],
        margins=True)
    # Define a color palette
    palette = sns.cubehelix_palette(start=1.5, rot=1.5, as_cmap=True)
    plt.subplots(figsize=(30, 20))
    sns.heatmap(pivot_table, linewidths=0.2, square=True, cmap=palette)
    plt.show()


# visualize_student_behaviour(preprocess_raw_data(dataset_path))


def visualize_behavioural_data_correlations(data: PandasDataFrame) -> None:
    """
    Requirements: This function requires renamed columns 'preprocess_raw_data' function
    Description: Plot a heatmap of the correlation between students' behaviour features (raised_hands, visited_resources
    , announcement_views, discussion)
    :param data:
    :return:
    """
    features = data[["raised_hands", "visited_resources", "announcement_views", "discussion"]]
    correlations = features.corr()
    sns.set_style("white")
    figure, axes = plt.subplots(figsize=(20, 20))
    # Initialize correlation matrix with zeros
    mask = np.zeros_like(correlations, dtype=bool)
    # Hide redundant correlations
    mask[np.triu_indices_from(mask)] = True
    cmap = sns.diverging_palette(h_neg=220, h_pos=10, as_cmap=True)
    sns.heatmap(correlations, mask=mask, cmap=cmap, ax=axes)
    plt.show()


# visualize_behavioural_data_correlations(preprocess_raw_data(dataset_path))


def visualize_pairplot(data: PandasDataFrame) -> None:
    """
    Requirements: This function requires renamed columns 'preprocess_raw_data' function
    Description: Visualize pairplot where each subplot in the matrix shows the relationship between two of the variables
    :param data:
    :return:
    """
    selections = ["nationality", "raised_hands", "visited_resources", "announcement_views", "discussion"]
    columns = data[selections]
    sns.pairplot(columns, hue="nationality")
    plt.show()


# visualize_pairplot(preprocess_raw_data(dataset_path))


def visualize_features_numerical_distribution(data: PandasDataFrame) -> None:
    """
    Requirements: This function requires mapped numerical presentation of feature 'create_numerical_presentation_mapper'
    function
    Description: Visualize numerical presentation distribution for dataframe features
    :param data:
    :return:
    """
    sns.set(style="white", palette="muted", color_codes=True)
    figure, axes = plt.subplots(4, 4, figsize=(20, 20))
    sns.despine(left=True)
    sns.distplot(data['nationality'], kde=False, color="b", ax=axes[0, 0])
    sns.distplot(data['place_of_birth'], kde=False, color="b", ax=axes[0, 1])
    sns.distplot(data['stage_id'], kde=False, color="b", ax=axes[0, 2])
    sns.distplot(data['grade_id'], kde=False, color="b", ax=axes[0, 3])
    sns.distplot(data['section_id'], kde=False, color="b", ax=axes[1, 0])
    sns.distplot(data['topic'], kde=False, color="b", ax=axes[1, 1])
    sns.distplot(data['semester'], kde=False, color="b", ax=axes[1, 2])
    sns.distplot(data['relation'], kde=False, color="b", ax=axes[1, 2])
    sns.distplot(data['raised_hands'], kde=False, color="b", ax=axes[1, 3])
    sns.distplot(data['visited_resources'], kde=False, color="b", ax=axes[2, 0])
    sns.distplot(data['announcement_views'], kde=False, color="b", ax=axes[2, 1])
    sns.distplot(data['discussion'], kde=False, color="b", ax=axes[2, 2])
    sns.distplot(data['parent_answering_survey'], kde=False, color="b", ax=axes[2, 3])
    sns.distplot(data['parent_school_satisfaction'], kde=False, color="b", ax=axes[3, 0])
    sns.distplot(data['student_absence_days'], kde=False, color="b", ax=axes[3, 1])
    sns.distplot(data['student_class'], kde=False, color="b", ax=axes[3, 2])
    plt.tight_layout()
    plt.show()


# data = create_numerical_presentation_mapper(preprocess_raw_data(dataset_path))
# visualize_features_numerical_distribution(data)


def visualize_numerical_data_correlations(data: PandasDataFrame) -> None:
    """
    Requirements: This function requires mapped numerical presentation of feature 'create_numerical_presentation_mapper'
    function
    Description: Plot a heatmap of the correlation between all features after the numerical mapping
    :param data:
    :return:
    """
    features = data
    correlations = features.corr()
    sns.set_style("white")
    figure, axes = plt.subplots(figsize=(20, 20))
    # Initialize correlation matrix with zeros
    mask = np.zeros_like(correlations, dtype=bool)
    # Hide redundant correlations
    mask[np.triu_indices_from(mask)] = True
    cmap = sns.diverging_palette(h_neg=220, h_pos=10, as_cmap=True)
    sns.heatmap(correlations, mask=mask, cmap=cmap, ax=axes)
    plt.show()


# data = create_numerical_presentation_mapper(preprocess_raw_data(dataset_path))
# visualize_numerical_data_correlations(data)


def visualize_multiple_model_classifiers(all_scores: list[tuple[str, float]]) -> None:
    """
    Requirements: This function requires mapped numerical presentation of feature 'create_numerical_presentation_mapper'
    function and classifier scores for different models after the training 'build_model_classifiers' function
    Description: Plot a categorical plot of classifier scores after the training
    :param all_scores:
    :return:
    """
    results = pd.DataFrame(all_scores, columns=['classifier', 'score'])
    sns.boxplot(
        x="classifier",
        y="score",
        showmeans=True,
        data=results
    )
    plt.xticks(rotation=45)
    plt.show()


# data = create_numerical_presentation_mapper(preprocess_raw_data(dataset_path))
# all_scores = build_model_classifiers(data)
# visualize_multiple_model_classifiers(all_scores)
