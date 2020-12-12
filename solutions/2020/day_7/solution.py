# prompt: https://adventofcode.com/2020/day/7

from ...base import BaseSolution, InputTypes
# from typing import Tuple
import networkx as nx

class Solution(BaseSolution):
    year = 2020
    number = 7
    input_type = InputTypes.STRSPLIT

    def part_1(self) -> int:
        pass

    def part_2(self) -> int:
        pass

    def solve(self) -> tuple((int, int)):
        G = nx.DiGraph()
        for line in self.input:
            if ' contain no other bags.' in line:
                pos = line.find(' bags contain no other bags.')
                root = line[:pos]
                G.add_node(root)
            else:
                container = line.split(' contain ')[0]
                adj, color, _ = container.split(' ')
                root = adj + ' ' + color
                G.add_node(root)

                content = line.split(' contain ')[1].split(', ')
                for bag in content:
                    weight, adj, color, _ = bag.split(' ')
                    leave = adj + ' ' + color
                    G.add_edges_from([(root, leave, {'weight':int(weight)})])
        
        predecessors = [node for node in G.nodes if 'shiny gold' in nx.single_source_dijkstra_path(G, node)]

        predecessors.remove('shiny gold')
        # leaf nodes which have shiny gold as predecessor

        result = 0
        while True:
            if 'shiny gold' in G.nodes:
                leafNodes = [node for node in nx.single_source_dijkstra_path(G, 'shiny gold') if G.out_degree(node)==0]
            else:
                print('shiny gold not in G')
                break
            if len(leafNodes) == 0: break
            # paths from a leaf to shiny gold: eg ['shiny gold', 'dark olive', 'faded blue']
            for leaf in leafNodes:
                leafPaths = [p for p in nx.all_simple_paths(G, 'shiny gold', leaf)]
                for leafPath in leafPaths:
                    iteration = 1
                    for i in range(len(leafPath)-1):
                        iteration *= G[leafPath[i]][leafPath[i+1]]['weight']
                    print(iteration, leafPath)
                    result += iteration
            G.remove_nodes_from(leafNodes)
            
        return len(predecessors), result
