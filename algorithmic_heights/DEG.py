## Finding the degree of the graph
file_name = input('Write the file name here : ')
edges = []
node = ()
with open('docs/' + file_name, 'r') as f:
    for i in f.readlines():
        print(i)
        edges = [ x for x in i]
print(edges)
print(node)