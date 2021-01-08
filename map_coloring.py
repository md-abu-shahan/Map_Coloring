colors = ['R','G','B','Y','C']

states = ['n0', 'n1', 'n2', 'n3','n4','n5','n6','n7','n8','n9']

neighbors = {'n0':['n2'],
             'n1':['n3','n4'],
             'n2':['n0','n3','n5','n6','n8'],
             'n3':['n1','n2','n5','n6','n7','n8'],
             'n4':['n1','n6','n7'],
             'n5':['n2','n3','n6','n8'],
             'n6':['n2','n3','n4','n5','n7','n8','n9'],
             'n7':['n3','n4','n6'],
             'n8':['n2','n3','n5','n6'],
             'n9':['n6']}

colors_of_states = {}
nodes_colour_of_map = []

def promising(state, color):
    for neighbor in neighbors.get(state): 
        color_of_neighbor = colors_of_states.get(neighbor)
        if color_of_neighbor == color:
            return False

    return True

def get_color_for_state(state):
    for color in colors:
        if promising(state, color):
            return color

def main():
    if(len(colors)<5):
        colors.append("N")
    
    for state in states:
        colors_of_states[state] = get_color_for_state(state)
        
    print(colors_of_states)

    for x in range(len(colors_of_states)):
        temp = 'n'+str(x)
        print(temp,"->",colors_of_states[temp])
        nodes_colour_of_map.append(list(colors_of_states[temp]))
    print(nodes_colour_of_map)

    return nodes_colour_of_map


if __name__ == '__main__':
    main()
