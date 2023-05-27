## build image
docker image build -t mlops-lab3:0.1 .

## run container
docker run -p 127.0.0.1:8000:8000/tcp mlops-lab3:0.1

## test functionality

http://127.0.0.1:8000/

http://127.0.0.1:8000/docs

http://127.0.0.1:8000/docs#/default/predict_predict__post

{
  "context": "Twelve months ago Robin Parker left his job at an insurance company. He now runs a restaurant which is doing very well since it opened four months ago. Opening a restaurant was a big change for Robin. He loves travelling and all his favourite television programmes are about cooking. One day, he read in a newspaper about a doctor who left her job and moved to Italy to start a restaurant. He thought, “I can do that!” His wife wasn’t very happy about the idea, and neither was his father. But his brother, a bank manager, gave him lots of good ideas. Robin lived in Oxford and had a job in London. He thought both places would be difficult to open a restaurant in, so he chose Manchester because he knew the city from his years at university. He found an empty building in a beautiful old street. It was old and needed a lot of repairs, but all the other buildings were expensive and he didn’t have much money. Robin loves his new work. It’s difficult being the boss, but he has found an excellent chef. He says he enjoys talking to customers and some of them have become his good friends. He gets up at 6pm and often goes to bed after midnight. It’s a long day but he only starts to feel really tired when he takes time off at the weekends. Robin’s restaurant is doing so well that he could take a long holiday. But he’s busy with his new idea to open a supermarket selling food from around the world. He’s already found a building near his restaurant.",
  "question": "Who helped Robin open his restaurant?"
}
