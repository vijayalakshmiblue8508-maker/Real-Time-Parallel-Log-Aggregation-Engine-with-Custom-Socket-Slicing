def split_data(lines, parts):

    chunk = len(lines) // parts

    result = []

    start = 0

    for i in range(parts):

        end = start + chunk

        if i == parts - 1:
            end = len(lines)

        result.append(lines[start:end])

        start = end

    return result