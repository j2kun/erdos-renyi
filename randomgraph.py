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
   edges = [(i,j) for i in xrange(n) for j in xrange(i) if random.random() < p]

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

   assert sum(len(c) for c in components) == len(vertices)
   return components


def sizeOfLargestComponent(vertices):
   return max(len(c) for c in connectedComponents(vertices))


def graphLargestComponentSize(n, theRange):
   return [(p, sizeOfLargestComponent(randomGraph(n, p))) for p in theRange]


def movingAverage(a, n=3):
    window = numpy.ones(n) / float(n)
    return numpy.convolve(a, window, 'same')


def plot(numVertices, xstart, xend, xpts, filename, windowSize=5):
   plt.clf() # clear figure

   xs = linspace(xstart, xend, num=xpts)
   data = graphLargestComponentSize(numVertices, xs)

   ys = [p[1] for p in data]
   movingavg = movingAverage(ys, windowSize)
   newxs = linspace(xstart, xend, num=len(movingavg))

   plt.plot(xs, ys, 'b-', newxs, movingavg, 'r-', lw=2)
   plt.xlabel("p")
   plt.ylabel("Size of largest component")
   plt.ylim(ymax=numVertices)
   plt.xlim((xs[0], xs[-1]))
   plt.title("Phase Transition for Connectivity of a Random Graph")
   plt.savefig(filename)


if __name__ == "__main__":
   plot(50, xstart=0, xend=0.5, xpts=1000, filename="zoomedout-50-1000.png", windowSize=20)
   plot(50, xstart=0, xend=0.15, xpts=1000, filename="zoomedin-50-1000.png", windowSize=20)
   plot(100, xstart=0, xend=0.15, xpts=1000, filename="zoomedin-100-1000.png", windowSize=20)
   plot(500, xstart=0, xend=0.01, xpts=1000, filename="zoomedin-500-1000.png", windowSize=20)

   for i,n in enumerate(range(20, 500, 20), start=1):
      plot(n, xstart=1.0/n, xend=5.0/n, xpts=500, filename="animation/%02d.png" % i, windowSize=20)



