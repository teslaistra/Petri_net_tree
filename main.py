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
        points[int(point)] = int(mark)

    number_of_transition = int(file.readline())
    for i in range(0, number_of_transition):
        transitions.append(int(file.readline()))

    edges_number = int(file.readline())
    for i in range(0, edges_number):
        fr, to = file.readline().split(' ')

        if int(to) in transitions:
            reverse_points_to_transitions[int(to)].append(int(fr))
        if int(to) in points:
            edges_transitions_to_points[int(fr)].append(int(to))


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

# edges to transitions = {5:[1,3]}
# edges to points = {1:[5,5]}
