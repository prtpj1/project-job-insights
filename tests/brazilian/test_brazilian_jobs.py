from src.brazilian_jobs import read_brazilian_file

PATH = "tests/mocks/brazilians_jobs.csv"
jobs_mock = {"title": "Maquinista", "salary": "2000", "type": "trainee"}


def test_brazilian_jobs():
    jobs = read_brazilian_file(PATH)
    assert jobs_mock in jobs
