bad_list = ['инженер-конструктор Петр', 'главный бухгалтер Мария',
            'токарь высшего разряда Эдуард', 'директор Елизавета']
for position in bad_list:
    print('Здравствуйте!', position.split()[-1].title())