import collections
import queue

number_of_points = 0
points = dict()

number_of_transition = 0
transitions = []
edges_number = 0
edges_transitions_to_points = collections.defaultdict(list)
reverse_points_to_transitions = collections.defaultdict(list)

root = None


class Node:
    def __init__(self, parent=None, type_node='border', children=None, mark=None):
        if mark is None:
            mark = []
        if children is None:
            children = []
        self.parent = parent
        self.type_node = type_node
        self.children = children
        self.mark = mark


# проверка является ли дублирующей
def check_if_exist(root, Node):
    return False


# проверка является ли терминальной
def check_if_terminates(mark):
    if get_available_transition(mark) is []:
        return True
    return False


# получение переходов, доступных для запуска
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


# считывание входных данных
def parse(file):
    global number_of_points
    global points
    global number_of_transition
    global transitions
    global edges_number
    global edges_transitions_to_points

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


# обработка вершины
def process_mark(node):
    if check_if_exist(root, node.mark):
        Node.type_node = 'duplicate'
        return
    elif check_if_terminates(node.mark):
        node.type_node = 'terminate'
        return
    else:
        calc_children(node)


def run_transition(transition, node):
    expected_marking = node.mark.copy()
    child = Node()

    for i in edges_transitions_to_points[transition]:
        expected_marking[i] += 1

    for i in reverse_points_to_transitions[transition]:
        expected_marking[i] -= 1
    print(expected_marking)
    
    return child

# просчет переходов
def calc_children(node):
    print('calc')
    transitions_to_do = queue.Queue()
    for to_do in get_available_transition(node.mark):
        transitions_to_do.put(to_do)

    children = []
    while transitions_to_do.qsize() > 0:
        to_do = transitions_to_do.get()
        new_node = run_transition(to_do, node)
        children.append(new_node)
    node.children = children


def run():
    global root
    print("Start marking is:", list(points.values()))
    root = Node(mark=list(points.values()))
    active_nodes = queue.Queue()
    active_nodes.put(root)

    while active_nodes.qsize() > 0:
        node = active_nodes.get()
        process_mark(node)
    print(root.type_node)


if __name__ == '__main__':
    parse('vvod.txt')
    print("number_of_points", number_of_points)
    print("points", points)
    print("number_of_transition", number_of_transition)
    print("transitions", transitions)
    print('edges_transitions_to_points', dict(edges_transitions_to_points))
    print('reverse_points_to_transitions', dict(reverse_points_to_transitions))
    print("_______________________________________")
    run()
# edges to transitions = {5:[1,3]}
# edges to points = {1:[5,5]}
