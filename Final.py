import networkx as nx
import matplotlib.pyplot as plt

def read_input(file_path):
    preferences = {}
    course_loads = {}

    with open(file_path, 'r') as file:
        lines = file.readlines()

        
        course_load_line = lines[0].strip().split(',')
        for entry in course_load_line:
            professor, load = entry.split(':')
            course_loads[professor] = float(load)

        
        priority_line = lines[1].strip().split(',')
        
        compulsory_courses = []
        if 'compulsory:' in priority_line[0]:
            compulsory_courses = priority_line[0].split('compulsory:')[1].split('|')

        elective_courses = []
        if 'elective:' in priority_line[1]:
            elective_courses = priority_line[1].split('elective:')[1].split('|')
            
        priority_order = compulsory_courses + elective_courses

    
        for line in lines[2:]:
            parts = line.strip().split(',')
            professor = parts[0]
            courses = parts[1:]
            preferences[professor] = {'courses': courses}

    return preferences, course_loads, priority_order

def solve_assignment_problem_graph(preferences, course_loads, priority_order):
    G = nx.DiGraph()
    G.add_nodes_from(["source", "sink"] + list(preferences.keys()) + priority_order)

   
    for faculty, load in course_loads.items():
        G.add_edge("source", faculty, capacity=load)

    
    for course in priority_order[:len(priority_order)//2]:  
        G.add_edge(course, "sink", capacity=1)

    
    for course in priority_order[len(priority_order)//2:]:
        G.add_edge(course, "sink", capacity=1)  

    
    for faculty, courses in preferences.items():
        for course in courses['courses']:
            G.add_edge(faculty, course, capacity=float('inf'))

   
    flow_value, flow_dict = nx.maximum_flow(G, "source", "sink")

    
    print("Assignment:")
    total_assigned_courses = 0
    for faculty in preferences:
        for course in preferences[faculty]['courses']:
            if flow_dict[faculty][course] > 0:
                print(f"{faculty} is assigned to {course}")
                total_assigned_courses += 1

    print(f"Total assigned courses: {total_assigned_courses}")

    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='lightblue', font_color='black')
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['capacity'] for u, v, d in G.edges(data=True)})
    plt.show()


input_file_path = 'testcase.txt'
preferences, course_loads, priority_order = read_input(input_file_path)
solve_assignment_problem_graph(preferences, course_loads, priority_order)
