"""
This script sets up constants used in the model
"""
from typing import TypeVar

dataset_path = "data/xAPI-Edu-Data.csv"
plots_path = "plots/"

# Define custom type annotation for pandas dataframe
PandasDataFrame = TypeVar("PandasDataFrame")

# Rename column names to consistent names
consistent_column_names_dict = {
    "NationalITy": "nationality",
    "PlaceofBirth": "place_of_birth",
    "StageID": "stage_id",
    "GradeID": "grade_id",
    "SectionID": "section_id",
    "Topic": "topic",
    "Semester": "semester",
    "Relation": "relation",
    "raisedhands": "raised_hands",
    "VisITedResources": "visited_resources",
    "AnnouncementsView": "announcement_views",
    "Discussion": "discussion",
    "ParentAnsweringSurvey": "parent_answering_survey",
    "ParentschoolSatisfaction": "parent_school_satisfaction",
    "StudentAbsenceDays": "student_absence_days",
    "Class": "student_class"
}

# Numerical presentation for gender column
gender_dict = {
    "M": 1,
    "F": 2
}

# Numerical presentation for nationality column
nationality_dict = {
    "Iran": 1,
    "SaudiArabia": 2,
    "USA": 3,
    "Egypt": 4,
    "Lybia": 5,
    "lebanon": 6,
    "Morocco": 7,
    "Jordan": 8,
    "Palestine": 9,
    "Syria": 10,
    "Tunis": 11,
    "KW": 12,
    "KuwaIT": 12,
    "Iraq": 13,
    "venzuela": 14
}

# Numerical presentation for place of birth column
place_of_birth_dict = {
    "Iran": 1,
    "SaudiArabia": 2,
    "USA": 3,
    "Egypt": 4,
    "Lybia": 5,
    "lebanon": 6,
    "Morocco": 7,
    "Jordan": 8,
    "Palestine": 9,
    "Syria": 10,
    "Tunis": 11,
    "KW": 12,
    "KuwaIT": 12,
    "Iraq": 13,
    "venzuela": 14
}

# Numerical presentation for stage id column
stage_id_dict = {
    "HighSchool": 1,
    "lowerlevel": 2,
    "MiddleSchool": 3
}

# Numerical presentation for grade id column
grade_id_dict = {
    "G-02": 2,
    "G-08": 8,
    "G-09": 9,
    "G-04": 4,
    "G-05": 5,
    "G-06": 6,
    "G-07": 7,
    "G-12": 12,
    "G-11": 11,
    "G-10": 10
}

# Numerical presentation for section id column
section_id_dict = {
    "A": 1,
    "C": 2,
    "B": 3
}

# Numerical presentation for topic column
topic_dict = {
    "Biology": 1,
    "Geology": 2,
    "Quran": 3,
    "Science": 4,
    "Spanish": 5,
    "IT": 6,
    "French": 7,
    "English": 8,
    "Arabic": 9,
    "Chemistry": 10,
    "Math": 11,
    "History": 12
}

# Numerical presentation for semester column
semester_dict = {
    "S": 1,
    "F": 2
}

# Numerical presentation for relation column
relation_dict = {
    "Father": 1,
    "Mum": 2
}

# Numerical presentation for parent answering survey column
parent_answering_survey_dict = {
    "Yes": 1,
    "No": 0
}

# Numerical presentation for parent school satisfaction column
parent_school_satisfaction_dict = {
    "Bad": 0,
    "Good": 1
}

# Numerical presentation for parent school satisfaction column
student_absence_days_dict = {
    "Under-7": 0,
    "Above-7": 1
}

# Numerical presentation for student class column
student_class_dict = {
    "H": 10,
    "M": 5,
    "L": 2
}

# Define dummy test data
test_data = [
    {
        "gender": "M",
        "nationality": "SaudiArabia",
        "place_of_birth": "SaudiArabia",
        "stage_id": "MiddleSchool",
        "grade_id": "G-09",
        "section_id": "B",
        "topic": "Arabic",
        "semester": "F",
        "relation": "Mum",
        "raised_hands": 35,
        "visited_resources": 45,
        "announcement_views": 15,
        "discussion": 28,
        "parent_answering_survey": "Yes",
        "student_absence_days": "Above-7",
        "student_class": "M",
        "parent_school_satisfaction": ""
    },
]
