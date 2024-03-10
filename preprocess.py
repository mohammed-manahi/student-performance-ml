"""
This script pre-processes the dataset and performs clean up before training
"""
import pandas as pd
from constants import *


def preprocess_raw_data(edu_data_path: str) -> PandasDataFrame:
    """
    Requirements: None
    Description: Rename column names in the dataframe to ensure consistency
    :param edu_data_path:
    :return renamed dataframe:
    """
    data = pd.read_csv(edu_data_path)
    renamed_data = data.rename(columns=consistent_column_names_dict)
    # print("Columns in the dataframe are:", renamed_data.columns)
    return renamed_data


def explore_data(data: PandasDataFrame) -> None:
    """
    Requirements: This function requires renamed columns 'preprocess_raw_data' function
    Description: Print out some stats about the edu data dataset
    :param data:
    :return:
    """
    print("Dataframe description:\n", data.describe())
    print("Dataframe categorical features:\n", data.select_dtypes(include="object").columns.values)
    print("Dataframe numerical features:\n", data.select_dtypes(include=["float64", "int64"]).columns.values)


# data = preprocess_raw_data(dataset_path)
# explore_data(preprocess_raw_data(dataset_path))

def create_numerical_presentation_mapper(data: PandasDataFrame) -> PandasDataFrame:
    """
    Requirements: This function requires renamed columns 'preprocess_raw_data' function
    Description: Create a numerical presentation mapper for non-numerical values in the dataframe
    :param data:
    :return:
    """
    mapped_data = data
    mapped_data.gender = mapped_data.gender.map(gender_dict)
    mapped_data.nationality = mapped_data.nationality.map(nationality_dict)
    mapped_data.place_of_birth = mapped_data.place_of_birth.map(place_of_birth_dict)
    mapped_data.stage_id = mapped_data.stage_id.map(stage_id_dict)
    mapped_data.grade_id = mapped_data.grade_id.map(grade_id_dict)
    mapped_data.section_id = mapped_data.section_id.map(section_id_dict)
    mapped_data.topic = mapped_data.topic.map(topic_dict)
    mapped_data.semester = mapped_data.semester.map(semester_dict)
    mapped_data.relation = mapped_data.relation.map(relation_dict)
    mapped_data.parent_answering_survey = mapped_data.parent_answering_survey.map(parent_answering_survey_dict)
    mapped_data.parent_school_satisfaction = mapped_data.parent_school_satisfaction.map(parent_school_satisfaction_dict)
    mapped_data.student_absence_days = mapped_data.student_absence_days.map(student_absence_days_dict)
    mapped_data.student_class = mapped_data.student_class.map(student_class_dict)
    return mapped_data

# data = create_numerical_presentation_mapper(preprocess_raw_data(dataset_path))
# print(data)

