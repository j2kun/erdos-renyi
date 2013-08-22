import random
import numpy
from numpy import linspace
import matplotlib.pyplot as plt

class Node:
   def __init__(self, index):
      self.index = index
      self.neighbors = []

   def __repr__(self):
      return repr(self.index)

def randomGraph(n,p):
   vertices = [Node(i) for i in range(n)]
   edges = [(i,j) for i in xrange(n) for j in xrange(n) if random.random() < p]

   for (i,j) in edges:
      vertices[i].neighbors.append(vertices[j])
      vertices[j].neighbors.append(vertices[i])

   return vertices


def dfsComponent(node, visited):
   for v in node.neighbors:
      if v not in visited:
         visited.add(v)
         dfsComponent(v, visited)


def connectedComponents(vertices):
   components = []
   cumulativeVisited = set()

   for v in vertices:
      if v not in cumulativeVisited:
        componentVisited = set([v])
        dfsComponent(v, componentVisited)

        components.append(componentVisited)
        cumulativeVisited |= componentVisited

   return components


def sizeOfLargestComponent(vertices):
   return max(len(c) for c in connectedComponents(vertices))


def graphLargestComponentSize(theRange):
   return [(p, sizeOfLargestComponent(randomGraph(n, p))) for p in theRange]


def plot(data):
   xs = [p[0] for p in data]
   ys = [p[1] for p in data]
   plt.plot(xs, ys)
   plt.show()

def movingAverage(a, n=3):
    ret = numpy.cumsum(a, dtype=float)
    return (ret[n - 1:] - ret[:1 - n]) / n


if __name__ == "__main__":
   n = 1000
   #data = graphLargestComponentSize(linspace(0, 0.5, num=1000))
   data = graphLargestComponentSize(linspace(0, 0.005, num=1000))

   #plot(data)

   ys = [p[1] for p in data]
   movingavg = movingAverage(ys, n=50)
   plt.plot(linspace(0,.02, num=len(movingavg)), movingavg, '-')
   plt.show()
