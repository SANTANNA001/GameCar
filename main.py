command = ""
started = False
while True:
    command = input('> ').lower()
    if command == 'start':
        if started:
            print('car is already started')
        else:
            started = True
            print('Car Started')
    elif command == 'stop':
        if not started:
            print('Car already stopped')
        else:
            started = False
            print('car Stop')
    elif command == 'help':
        print('''
start - To start Car
stop - stop car
quit - quit game''')
    elif command == 'quit':
        break
    else:
        print("Sorry i don't understand")

