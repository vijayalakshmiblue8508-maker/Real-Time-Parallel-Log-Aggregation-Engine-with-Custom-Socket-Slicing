def sort_file(filename):

    with open(filename,"r") as file:

        data=file.readlines()

    data.sort()

    with open(filename,"w") as file:

        file.writelines(data)