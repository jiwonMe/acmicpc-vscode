import requests
from bs4 import BeautifulSoup as bs
import base64
import json


def login():
    pass


def get_problem(id: int):
    url = "https://www.acmicpc.net/problem/"+str(id)
    s = requests.Session()
    req = s.get(url)
    html = req.text

    soup = bs(html, 'html.parser')
    problem_lang_base64 = soup.find(id='problem-lang-base64').text
    problem_bytes = base64.b64decode(problem_lang_base64)
    problem = problem_bytes.decode('utf-8')

    return json.loads(problem)[0]


if __name__ == "__main__":
    problem = get_problem(3000)

    # print(json.dumps(problem, indent=4))

    print("""
    title: {}
    description: {}
    input: {}
    output: {}
    """.format(problem.get('title'), problem.get('description'), problem.get('input'), problem.get('outputs')))
