file_name = "wordsList.txt"
sorted_fn = 'wordsListFormated.txt'

def count(x):
    return len(x.decode('utf-8'))

with open(file_name, 'r') as data:
    rows = data.readlines()
    sorted_rows = sorted(rows, key=lambda x: count(x), reverse=False)
    with open(sorted_fn, 'w') as second_file:
        for row in sorted_rows:
            formated_row = "\"{}\", \n".format(row.strip())
            second_file.write(formated_row)
