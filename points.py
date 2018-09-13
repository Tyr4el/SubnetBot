import json

data = {}


def load():
    with open('points.json', 'r') as file:
        json.load(file)
    print('Opened points.json file')


def save():
    with open('points.json', 'w') as file:
        json.dump(data, file)
    print('Saved points to file points.json.')


def get_points(user_id):
    if user_id not in data:
        return 0
    else:
        return data[user_id]


def set_points(user_id, points):
    data[user_id] = points
    if data[user_id] == 0:
        data[user_id] = 0


def get_leaderboard():
    for key, value in data.items():
        return key, value