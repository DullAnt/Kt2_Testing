import pandas as pd

def calculatingTheArithmeticMean(dataFrame):
    averageValue = ["test1", "test2", "test3", "test4"]
    dataFrame['Average'] = dataFrame[averageValue].mean(axis=1)

    grade_ranges = {
        'A+': (97, 100),
        'A': (93, 96),
        'A-': (90, 92),
        'B+': (87, 89),
        'B': (83, 86),
        'B-': (80, 82),
        'C+': (77, 79),
        'C': (73, 76),
        'C-': (70, 72),
        'D+': (67, 69),
        'D': (63, 66),
        'D-': (60, 62),
        'F': (0, 59)
    }

    def get_grade(average):
        for grade, (min_val, max_val) in grade_ranges.items():
            if min_val <= average <= max_val:
                return grade
        return 'F'

    dataFrame['CalculatedGrade'] = dataFrame['Average'].apply(get_grade)
    return dataFrame

def test_comparison_of_ratings():
    dataFrame = pd.read_csv(r"C:\python\grades.csv")
    dataFrame = calculatingTheArithmeticMean(dataFrame)
    errors = []

    for index, row in dataFrame.iterrows():
        if row['Grade'] != row['CalculatedGrade']:
            errors.append((index, row['Grade'], row['CalculatedGrade']))

    if errors:
        for error in errors:
            print(f"Error at index {error[0]}: Expected {error[1]}, Got {error[2]}")
        print(f"Total errors: {len(errors)}")
    else:
        print("All grades match!")

test_comparison_of_ratings()