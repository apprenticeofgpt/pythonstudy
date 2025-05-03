members = ['김', '고', '장', '백']
costs = {person: 0 for person in members}

restaurant_participant = [p.strip() for p in input('restaurant: ').split()]
bar_participant = [p.strip() for p in input('bar: ').split()]
cafe_participant = [p.strip() for p in input('caffe: ').split()]

restaurant_cost = int(input('restaurant cost: '))
bar_cost = int(input('bar cost: '))
cafe_cost = int(input('caffe cost: '))

for participant in restaurant_participant:
    costs[participant] += restaurant_cost / len(restaurant_participant)
for participant in bar_participant:
    costs[participant] += bar_cost / len(bar_participant)
for participant in cafe_participant:
    costs[participant] += cafe_cost / len(cafe_participant)

for participant in members:
    print(f'{participant}: {costs[participant]:.0f}원')
