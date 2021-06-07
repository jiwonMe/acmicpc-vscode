import requests
from bs4 import BeautifulSoup as bs
import base64
import json


def login():
    pass


def get_problem(id: int) -> (dict):
    """
    get_problem
    """

    url = "https://www.acmicpc.net/problem/"+str(id)
    s = requests.Session()
    req = s.get(url)
    html = req.text
    soup = bs(html, 'html.parser')

    problem = {
        "problem_id": str(id),
    }

    try:
        """
        base64로 인코딩된 문제 정보 json을 제공하는 경우
        """
        problem_lang_base64 = soup.find(id='problem-lang-base64').text
        problem_bytes = base64.b64decode(problem_lang_base64)
        problem = problem_bytes.decode('utf-8')

        problem = json.loads(problem)[0]

    except:
        """
        없는 경우
        """
        problem['title'] = soup.find(id='problem_title')
        problem['description'] = soup.find(id='description')
        problem['input'] = soup.find(id='input')
        problem['outputs'] = soup.find(id='output')

    problem['sampleinput'] = []

    _ = 1
    while(True):
        ele = soup.find(id='sample-input-{}'.format(_))

        _ += 1
        if(ele == None):
            break

        problem['sampleinput'].append(ele)

    problem['sampleoutput'] = []

    _ = 1
    while(True):
        ele = soup.find(id='sample-output-{}'.format(_))
        _ += 1
        if(ele == None):
            break

        problem['sampleoutput'].append(ele)

    return problem


if __name__ == "__main__":
    problem = get_problem(21871)

    # print(json.dumps(problem, indent=4))

    print("""
    problem_id: {}
    title: {}
    description:
    {}
    input:
    {}
    output:
    {}
    sample:
        input:
        {}
        output:
        {}
    """.format(
        problem.get('problem_id'),
        problem.get('title'),
        problem.get('description'),
        problem.get('input'),
        problem.get('outputs'),
        problem.get('sampleinput'),
        problem.get('sampleoutput')
    ))
