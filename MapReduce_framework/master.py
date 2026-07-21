import os

from multiprocessing import Process

from splitter import split_data
from mapper import mapper
from partitioner import partition
from sorter import sort_file
from reducer import reducer

REDUCERS = 4

with open("input/input.txt","r") as file:

    lines=file.readlines()

chunks = split_data(lines,REDUCERS)

mapped=[]

for chunk in chunks:

    mapped.extend(mapper(chunk))

partition(mapped,REDUCERS)

processes=[]

for i in range(REDUCERS):

    filename=f"partitions/part-{i}.txt"

    p=Process(target=sort_file,args=(filename,))

    p.start()

    processes.append(p)

for p in processes:

    p.join()

final={}

for i in range(REDUCERS):

    filename=f"partitions/part-{i}.txt"

    output=reducer(filename)

    for key,value in output.items():

        final[key]=final.get(key,0)+value

os.makedirs("output",exist_ok=True)

with open("output/result.txt","w") as file:

    file.write("Word,Count\n")

    for key in sorted(final):

        file.write(f"{key},{final[key]}\n")

print("========== MapReduce Completed ==========")

for key in sorted(final):

    print(key,":",final[key])

print("\nOutput saved in output/result.txt")