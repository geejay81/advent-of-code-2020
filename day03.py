
def get_data(filename) :
    data = []
    file_contents = open(filename, 'r')
    lines = file_contents.readlines()
    for line in lines :
        data.append(list(line.strip()))
    return data

def slide(data, right_slide, down_slide) :
    current_column = 0
    tree_count = 0
    row_skip = down_slide
    tree_marker = '#'
    
    for row_number in range(len(data)) :

        if (row_number % down_slide) == 0 :

            if data[row_number][current_column] == tree_marker :
                tree_count += 1

            current_column += right_slide

            if current_column > (len(data[row_number]) - 1) :
                current_column = (current_column - len(data[row_number]))
    
    return tree_count

def main() :
    data = get_data('day03.txt')

    result1 = slide(data, 3, 1)

    print('Result 1: {}'.format(result1))

    result2 = slide(data, 1, 1) * slide(data, 3, 1) * slide(data, 5, 1) * slide(data, 7, 1) * slide(data, 1, 2)

    print('Result 2: {}'.format(result2))

main()