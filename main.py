import collections

number_of_points = 0
points = dict()

number_of_transition = 0
transitions = []
edges_number = 0
edges_transitions_to_points = collections.defaultdict(list)
reverse_points_to_transitions = collections.defaultdict(list)

global_id = 0
markers = []


class Node:
    def __init__(self):
        self.parent = None
        self.type_node = 'border'
        self.children = []
        self.mark = []


root = Node()


# проверка является ли дублирующей
def check_if_exist(root, Node):
    return False


# проверка является ли терминальной
def check_if_terminates(root, Node):
    return False


def get_available_transition(marking):
    available = []
    for transition in reverse_points_to_transitions:
        points_from = reverse_points_to_transitions[transition]
        is_available = True
        for point in points_from:
            if not marking[point]:
                is_available = False
        if is_available:
            available.append(transition)

    return available


def parse(file):
    global number_of_points
    global points
    global number_of_transition
    global transitions
    global edges_number
    global edges_transitions_to_points
    global edges_points_to_transitions

    file = open(file)
    number_of_points = int(file.readline())
    for i in range(0, number_of_points):
        point, mark = file.readline().split(' ')
        points[int(point) - 1] = int(mark)

    number_of_transition = int(file.readline())
    for i in range(0, number_of_transition):
        transitions.append(int(file.readline()) - 1)

    edges_number = int(file.readline())
    for i in range(0, edges_number):
        fr, to = file.readline().split(' ')

        if int(to) - 1 in transitions:
            reverse_points_to_transitions[int(to) - 1].append(int(fr) - 1)
        if int(to) - 1 in points:
            edges_transitions_to_points[int(fr) - 1].append(int(to) - 1)


def run():
    print("Start marking is:", list(points.values()))
    root = Node


if __name__ == '__main__':
    parse('vvod.txt')
    print("number_of_points", number_of_points)
    print("points", points)
    print("number_of_transition", number_of_transition)
    print("transitions", transitions)
    print('edges_transitions_to_points', dict(edges_transitions_to_points))
    print('reverse_points_to_transitions', dict(reverse_points_to_transitions))
    run()
    print(get_available_transition(list(points.values())))
# edges to transitions = {5:[1,3]}
# edges to points = {1:[5,5]}
