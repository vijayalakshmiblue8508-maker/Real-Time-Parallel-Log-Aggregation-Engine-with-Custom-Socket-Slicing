def mapper(lines):

    mapped = []

    for line in lines:

        words = line.strip().split()

        for word in words:

            mapped.append((word.lower(),1))

    return mapped