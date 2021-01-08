class Arc():
    nodes_connect_list = [['n2'],['n3','n4'],['n0','n3','n5','n6','n8'],['n1','n2','n5','n6','n7','n8']
                       ,['n1','n6','n7'],['n2','n3','n6','n8'],['n2','n3','n4','n5','n7','n8','n9']
                       ,['n3','n4','n6'],['n2','n3','n5','n6'],['n6']]


    '''nodes_domain_list = [['R','G','B','C','Y'],['R','B','C'],['R','G','B','C','Y']
                      ,['R','G','B','C','Y'],['R','G','B','C','Y'],['R','G','B','C']
                      ,['R','G','B','C','Y'],['R','C'],['R','G','B','C','Y']
                      ,['R','G','B','C','Y']]'''
    queue_list = []
    print("In")
    nodes_domain_list = []

    def __init__(self,domain):
        self.nodes_domain_list = domain

        
    def queueMaking(self):
        print("In2")
        for x in range(len(self.nodes_connect_list)):
            for y in range(len(self.nodes_connect_list[x])):
                temp1 = ["n"+str(x)+","+(self.nodes_connect_list[x][y])]
                (self.queue_list).append(temp1)
                temp2 = [(self.nodes_connect_list[x][y])+","+"n"+str(x)]
                (self.queue_list).append(temp2)

        print(self.queue_list,"\n\n")
        if(self.deletingFromQueue()==True):
            print("\n\nDomain Value is Consistent...")
            return True
        else:
            print("Domain Value is not Consistent...")
            return False
        
    def deletingFromQueue(self):
        x = 0
        
        while(x<len(self.queue_list)):
            
            if(self.isConsistent(self.queue_list[0])==True):
                self.queue_list.pop(0)
            else:
                print(self.isConsistent(self.queue_list[0]))
                print("\n\nFailed....")
                return False
                break
        return True

    def isConsistent(self,element):
        print("In Consistent : ",element)
        first_node_number = int(element[0][1:2])
        second_node_number = int(element[0][4:])
        print("First Node Domain : ",self.nodes_domain_list[first_node_number])
        print("Second Node Domain : ",self.nodes_domain_list[second_node_number])
        if((len(self.nodes_domain_list[first_node_number]) == 0) or (len(self.nodes_domain_list[second_node_number]) == 0)):
            print("Null")
            return False

        for x in range(len(self.nodes_domain_list[first_node_number])):
            first_node_color = self.nodes_domain_list[first_node_number][x]
            second_node_length = len(self.nodes_domain_list[second_node_number])
            if(second_node_length>1):
                return True
            elif((second_node_length==1) and (first_node_color not in self.nodes_domain_list[second_node_number])):
                return True
            
            else:
                c = self.nodes_domain_list[first_node_number].remove(self.nodes_domain_list[first_node_number][x])
                if(self.nodes_domain_list[first_node_number] is not ""):
                    self.addInQueue(first_node_number)
                    return True
                
                else:
                    return False

    def addInQueue(self,node_number):
        for x in range(len(self.nodes_connect_list[node_number])):
                temp = ["n"+str(node_number)+","+(self.nodes_connect_list[node_number][x])]
                (self.queue_list).append(temp)
                return
        
            


def main(domain):
    print(domain)
    obj = Arc(domain)
    obj1 = obj.queueMaking()
    print(obj1)
    return obj1

if __name__ == '__main__':
    main()


            
