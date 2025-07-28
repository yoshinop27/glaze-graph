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
    }

class glazeTree:
    def __init__(self, graph=None):
        self.graph = graph if graph else {}

    def add(self, name, glazees=[], glazers=[]):
        self.graph[name] = glazees
        for glazer in glazers:
            self.graph[glazer].append(name)
            print("{glazer} is now a glazer of {name}".format(glazer, name))

