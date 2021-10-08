import json
from pathlib import Path
import pandas as pd


def load_nobel_prizes(filename='prize.json'):
    file = Path('.') / filename
    with open(file) as f:
        return json.load(f)


def nobel_parse(data, **kwargs):
    print(f'********{kwargs}********')

    df = pd.DataFrame(columns=['Winner', 'Motivation'])
    data = data['prizes']
    laureates = []
    for entry in data:
        if all(arg in entry.items() for arg in kwargs.items()):
            if not entry.get('laureates'):
                print(f"{entry['year']}: {entry['overallMotivation']}")
            else:
                laureates += entry['laureates']
    for winner in laureates:
        df = df.append(pd.DataFrame(data=[[f"{winner['firstname']} {winner.get('surname')}",
                                            winner['motivation']]], columns=['Winner', 'Motivation']))
    if not df.empty:
        print(df.to_string() + '\n'*3)
    else:
        print('No winners matching this criteria.')


def main(**kwargs):
    data = load_nobel_prizes()
    nobel_parse(data, **kwargs)


if __name__ == '__main__':
    # main(year='2020')
    # main(category='physics')
    # main(year='1901')
    # main(year='1901', category='economics')
    main()
