class Node(object):

    def __init__(self, simbol, frequency):
        self.simbol = simbol
        self.frequency = frequency
        self.left = None
        self.right = None
        self.path = ""
        
    def build_map(self, map):
        if self.left == None and self.right == None:
            map[self.simbol] = self.path
        else:
            self.left.path = self.path + '0'
            self.left.build_map(map)
            
            self.right.path = self.path + '1'
            self.right.build_map(map)
            
def getKey(node):
    return node.frequency

class Huffman(object):

    def encode(self, text):
        stats = {}
        
        simbols = list(text)
        for simbol in simbols:
            if simbol in stats:
                frequency = stats[simbol]
                stats[simbol] = frequency + 1
            else:
                stats[simbol] = 1
        
        print(stats)
        
        nodes = []
        for simbol, frequency in stats.items():
            nodes.append(Node(simbol, frequency))

        while len(nodes) > 1:
            nodes = sorted(nodes, key=getKey, reverse=False)
            
            node1 = nodes.pop(0)
            node2 = nodes.pop(0)
            
            print(node1.simbol, node2.simbol)
            
            node = Node("<" + node1.simbol + '|' + node2.simbol + ">", node1.frequency + node2.frequency)
            node.left = node1
            node.right = node2
            nodes.append(node)    

        map = {}
        nodes[0].build_map(map)
        for node in nodes:
            print(node.simbol, node.frequency)
            
        print(map)
        
        result = ''
        for simbol in simbols:
            code = map[simbol]
            result = result + code
            
        return result 

if __name__ == '__main__':
    encoder = Huffman()
    result = encoder.encode("abracadabra")
    print(result)
