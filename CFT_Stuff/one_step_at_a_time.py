def create_sub_maze(start, end, maze):
    sub_maze = []
    found_sub_maze = False
    
    # For each line in the maze, we locate the portion that contains our start and end
    for line in maze:
        if start in line:
            found_sub_maze = True
        if found_sub_maze:
            sub_maze.append(line)
        if end in line and found_sub_maze:
            found_sub_maze = False

    # In the portion we just generated, we shrink the maze to our needs (length of start & end)
    index = sub_maze[0].index(start)
    i = 0
    for line in sub_maze:
        sub_maze[i] = line[index:index+len(start)]
        i += 1

    # We return the submaze
    return sub_maze

def find_character(start, end, line, column, maze):
    sub_maze = create_sub_maze(start, end, maze)

    # We return the correct character
    return sub_maze[int(line)][int(column)]


def main():
    # We load both file in a list
    maze = [l.strip() for l in open("maze.txt")]
    mapp = [l.strip() for l in open("map.txt") if l.strip()]

    flag = ""
    i = 0
    # For each map we get the output character and add it to flag
    while i < len(mapp):
        flag += find_character(mapp[i], mapp[i+4], mapp[i+1], mapp[i+2], maze)
        i += 5

    # Print the flah
    print(flag)

if __name__ == "__main__":
    main()