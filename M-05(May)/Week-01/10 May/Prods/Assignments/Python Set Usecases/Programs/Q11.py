def find_unique_skills_across_departments(department_employee_skills):
    unique_skills = set()
    for department_skills in department_employee_skills.values():
        unique_skills.update(department_skills)
    return unique_skills


if __name__ == '__main__':
    department_employee_skills = {
        "Java": {"prankur", "aayush", "ishaan"},
        "Python": {"ishaan", "aaditya", "aayush"},
        "Cloud": {"aayush", "aaditya", "prankur"},
    }
    unique_skills_across_departments = find_unique_skills_across_departments(department_employee_skills)
    print(unique_skills_across_departments)
