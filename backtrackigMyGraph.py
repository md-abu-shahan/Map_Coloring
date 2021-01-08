'''
[[0,0,1,0,0,0,0,0,0,0],[0,0,0,1,1,0,0,0,0,0],[1,0,0,1,0,1,1,0,1,0],[0,1,1,0,0,1,1,1,1,0]
                       ,[0,1,0,0,0,0,1,1,0,0],[0,0,1,1,0,0,1,0,1,0],[0,0,1,1,1,1,0,1,1,1]
                       ,[0,0,0,1,1,0,1,0,0,0],[0,0,1,1,0,1,1,0,0,0],[0,0,0,0,0,0,1,0,0,0]]

colour = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
'''


class Graph():

    colours_name = ['R','G','B','Y','C']
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                              for row in range(vertices)]
 
    def isSafe(self, v, colour, c):
        print("\nisSafe \nv : ",v,"\ncolour : ",colour,"\nc : ",c)
        for i in range(self.V):
            if self.graph[v][i] == 1 and colour[i] == c:
                return False
        return True
     

    def graphColourUtil(self, m, colour, v):
        print("\n\ngraphColourUtil \nm : ",m,"\ncolour : ",colour,"\nv : ",v)
        if v == self.V:
            return True
 
        for c in range(1, m+1):
            if self.isSafe(v, colour, c) == True:
                colour[v] = c
                if self.graphColourUtil(m, colour, v+1) == True:
                    return True
                colour[v] = 0
 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def graphColouring(self, m=None):
        colour = [0] * self.V
        if self.graphColourUtil(m, colour, 0) == False:
            print("graphColouring..................................................................")
            return False
 
        # Print the solution
        x = 0
        for c in colour:
            print('Node-',x,'->',self.colours_name[c-1])
            x = x+1
        return colour
 
def main():
    g  = Graph(10)
    g.graph = [[0,0,1,0,0,0,0,0,0,0],[0,0,0,1,1,0,0,0,0,0],[1,0,0,1,0,1,1,0,1,0],[0,1,1,0,0,1,1,1,1,0]
                       ,[0,1,0,0,0,0,1,1,0,0],[0,0,1,1,0,0,1,0,1,0],[0,0,1,1,1,1,0,1,1,1]
                       ,[0,0,0,1,1,0,1,0,0,0],[0,0,1,1,0,1,1,0,0,0],[0,0,0,0,0,0,1,0,0,0]]
    m=len(g.colours_name)
    print(m)
    c = g.graphColouring(m)
    print("In Bracktracking : ",c)
    return c
    
if __name__ == '__main__':
    main()
    
