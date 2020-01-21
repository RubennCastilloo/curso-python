
def run():
    counter = 0
    with open('aleph.txt') as f:
        # with open('texto.txt', 'r', encoding='utf8') asf: Para manejar errores con tildes
        # print(f.readlines())
        for line in f:
            counter += line.count('Beatriz')

        if counter == '1':
            print('Beatriz se encuentra {} vez en el texto'.format(counter))
        else:
            print('Beatriz se encuentra {} veces en el texto'.format(counter))



if __name__ == '__main__':
    run()