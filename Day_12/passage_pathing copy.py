
class Cave:
    def __init__(self, cave):
        """
        Create a cave that is a part of a cave system

        Parameters
        ----------
        cave : str
            Name of the cave
        """
        self.cave = cave
        self.successors = set()
        self.predecessors = set()

    def __add__(self, new_connection):
        """
        Overload + operator to add new_connection to the successors set

        Parameters
        ----------
        new_connection : str
            new_connection to add to Cave
        """
        self.successors.add(new_connection)
    
    def add_predecessor(self, predecessor):
        self.predecessors.add(predecessor)


class CaveSystem:
    def __init__(self, file):
        self.caves = {"start" : Cave("start"), "end" : Cave("end")}
        paths = open(file, 'r').readlines()
        for path in paths:
            first_cave, second_cave = path.strip().split("-")
            # Make sure the caves exist
            self.add_cave(first_cave)
            self.add_cave(second_cave)
            # If the second cave is start, then treat start as root
            if second_cave == "start":
                self.caves["start"] + self.caves[first_cave]
                self.caves[first_cave].add_predecessor(self.caves["start"])
            # If the first node is end, treat end as a leaf
            elif first_cave == "end":
                self.caves["end"].add_predecessor(self.caves[second_cave])
                self.caves[second_cave] + self.caves["end"]
            # Otherwise everything is all good treat first cave as predeccessor to second cave
            else:
                self.caves[first_cave] + second_cave
                self.caves[second_cave].add_predecessor(first_cave)
                if first_cave.isupper:
                    self.caves[second_cave] + first_cave

    
    def add_cave(self, cave):
        """
        First checks if caves exists in cave system,
        if it doesn't add it

        Parameters
        ----------
        cave : str
            Cave to add
        """
        if cave not in self.caves:
            self.caves[cave] = Cave(cave)
    
    def __repr__(self):
        string = ''
        for key in self.caves:
            string = string + '{} :\n\tPredecessors: {}\n\tSuccessors: {}\n'.format(key, self.caves[key].predecessors, self.caves[key].successors)
        return string

    # def go_for_a_walk(self):
    #     paths = [["start"]]
    #     for path in paths:



if __name__ ==  '__main__':
    test_1_caves = CaveSystem('test-1.txt')
    print(test_1_caves)
