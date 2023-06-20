from fastapi.testclient import TestClient
from api_answering import app


client = TestClient(app)


def test_root():
    response_root = client.get("/")
    assert response_root.status_code == 200
    assert response_root.json() == {"message": 'Hello adsfasd'}


def test_nswer():
    response_answer = client.post("/answer/", json={'context': '''Twelve months
    ago Robin Parker left his job at an insurance company. He now runs
    a restaurant which is doing very well since it opened four months ago.
    Opening a restaurant was a big change for Robin. He loves travelling and
    all his favourite television programmes are about cooking. One day, he
    read in a newspaper about a doctor who left her job and moved to Italy
    to start a restaurant. He thought, “I can do that!” His wife wasn’t very
    happy about the idea, and neither was his father. But his brother, a bank
    manager, gave him lots of good ideas. Robin lived in Oxford and had a job
    in London. He thought both places would be difficult to open a restaurant
    in, so he chose Manchester because he knew the city from his years at
    university. He found an empty building in a beautiful old street. It was
    old and needed a lot of repairs, but all the other buildings were
    expensive and he didn’t have much money. Robin loves his new work. It’s
    difficult being the boss, but he has found an excellent chef. He says he
    enjoys talking to customers and some of them have become his good friends.
    He gets up at 6pm and often goes to bed after midnight. It’s a long day
    but he only starts to feel really tired when he takes time off at the
    weekends. Robin’s restaurant is doing so well that he could take a long
    holiday. But he’s busy with his new idea to open a supermarket selling
    food from around the world. He’s already found a building near his
    restaurant.'''.replace('\n', ' ').replace('     ', ' '),
        'question': 'Who helped Robin open his restaurant?'})
    json_data = response_answer.json()

    assert response_answer.status_code == 200
    assert json_data['answer'] == 'his brother, a bank manager'
