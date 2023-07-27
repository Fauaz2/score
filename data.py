import csv
import statistics

def read_student_data(file_path):
    """
    Read student data from a CSV file and return a list of dictionaries.
    Each dictionary represents a student with keys 'name', 'age', and 'score'.
    """
    student_data = []
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            student_data.append({
                'name': row['Name'],
                'age': int(row['Age']),
                'score': float(row['Score'])
            })
    return student_data

def calculate_average_score(student_data):
    """
    Calculate the average score of all students.
    """
    scores = [student['score'] for student in student_data]
    return sum(scores) / len(scores)

def calculate_highest_score(student_data):
    """
    Find the highest score among all students.
    """
    scores = [student['score'] for student in student_data]
    return max(scores)

def calculate_lowest_score(student_data):
    """
    Find the lowest score among all students.
    """
    scores = [student['score'] for student in student_data]
    return min(scores)

def calculate_standard_deviation(student_data):
    """
    Calculate the standard deviation of student scores.
    """
    scores = [student['score'] for student in student_data]
    return statistics.stdev(scores)

def find_top_performers(student_data, n=5):
    """
    Find the top-performing students based on their scores.
    Returns a list of dictionaries containing their 'name', 'age', and 'score'.
    """
    sorted_students = sorted(student_data, key=lambda x: x['score'], reverse=True)
    return sorted_students[:n]

def main():
    file_path = 'student_scores.csv'
    student_data = read_student_data(file_path)

    average_score = calculate_average_score(student_data)
    highest_score = calculate_highest_score(student_data)
    lowest_score = calculate_lowest_score(student_data)
    standard_deviation = calculate_standard_deviation(student_data)
    top_performers = find_top_performers(student_data, n=5)

    print(f"Average Score: {average_score}")
    print(f"Highest Score: {highest_score}")
    print(f"Lowest Score: {lowest_score}")
    print(f"Standard Deviation: {standard_deviation}")

    print("Top Performers:")
    for student in top_performers:
        print(f"Name: {student['name']}, Age: {student['age']}, Score: {student['score']}")

if __name__ == "__main__":
    main()
