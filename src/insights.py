from src.jobs import read


def get_unique_job_types(path):
    file = read(path)
    job_types = set()

    for job in file:
        if job["job_type"] != "":
            job_types.add(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    jobs_filtered_by_type = []

    for job in jobs:
        if job["job_type"] == job_type:
            jobs_filtered_by_type.append(job)

    return jobs_filtered_by_type


def get_unique_industries(path):
    file = read(path)
    unique_industries = set()

    for industry in file:
        if industry["industry"] != "":
            unique_industries.add(industry["industry"])
    return unique_industries


def filter_by_industry(jobs, industry):
    jobs_filtered_by_industry = []

    for job in jobs:
        if job["industry"] == industry:
            jobs_filtered_by_industry.append(job)

    return jobs_filtered_by_industry


def get_max_salary(path):
    file = read(path)
    max_salary = set()

    for salary in file:
        if salary["max_salary"] != "" and salary["max_salary"].isdigit():
            max_salary.add(int(salary["max_salary"]))
    return max(max_salary)


def get_min_salary(path):
    file = read(path)
    min_salary = set()

    for salary in file:
        if salary["min_salary"] != "" and salary["min_salary"].isdigit():
            min_salary.add(int(salary["min_salary"]))

    return min(min_salary)


def matches_salary_range(job, salary):
    if ("min_salary" not in job) or ("max_salary" not in job):
        raise ValueError("There is no 'min_salary' or 'max_salary'")

    elif (
        type(job["min_salary"]) is not int
        or type(job["max_salary"]) is not int
    ):
        raise ValueError("'min_salary' or 'max_salary' is not numeric")

    elif (job["min_salary"]) > job["max_salary"]:
        raise ValueError("'min_salary' cant be higher than 'max_salary'")

    elif type(salary) is not int:
        raise ValueError("salary value is not numeric")

    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary: int):
    list_matches = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                list_matches.append(job)
        except ValueError:
            pass

    return list_matches
