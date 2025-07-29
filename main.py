# initial scars gc 
friendGroup = {
        "Colson": ["Nasir", "Colin"],
        "Justice": ["Colson", "Preston", "Nasir"],
        "Carlos": ["Luke", "Colson", "Justice", "Kai", "Brennan"],
        "Nasir": ["Preston"],
        "Brennan": ["Colson", "Justice", "Nasir", "Carlos", "Kai"],
        "Luke": ["Colson", "Kai", "Colin"],
        "Kai": ["Carlos", "Colson", "Justice", "Luke"],
        "Colin": ["Colson", "Justice", "Nasir", "Nate"],
        "Nate": ["Preston", "Colson", "Justice"],
        "Preston":["Nasir", "Justice"]
    }

class glazeGraph:
    def __init__(self, graph=None):
        self.graph = graph if graph else {}

    def add(self, name, glazees=None, glazers=None):
        #checking arguments
        if glazees is None:
            glazees = []
        if glazers is None:
            glazers = []
        #adding new friend to graph
        self.graph[name] = glazees
        for glazee in glazees:
            print(f"{glazee} gets glazed by {name}")

        #adjusting relationships
        for glazer in glazers:
            if glazer not in self.graph:
                self.graph[glazer] = []
            if name not in self.graph[glazer]:
                self.graph[glazer].append(name)
            print(f"{glazer} is now a glazer of {name}")

    def deleteGlazee(self, name, glazee):
        if name not in self.graph.keys():
            print(f"{name} not in friend group")
            return
        elif glazee not in self.graph[name]:
            print(f"{name} never glazed {glazee}")
            return
        self.graph[name].remove(glazee)

    def __str__(self):
        return '\n'.join(f"{k} glazes {v}" for k, v in self.graph.items())

def main():
    scars = glazeGraph(friendGroup)
    #scars.add("Kaili", ["Preston", "Nasir", "Colson", "Luke"], ["Nasir", "Brennan", "Kai"])
    #scars.add("Chris", ["Nasir", "Preston", "Justice", "Colin", "Nate"], ["Nasir"])
    scars.deleteGlazee("Preston", "Nasir")
    print(scars)
main()