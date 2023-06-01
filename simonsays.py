import sys
commands = sys.stdin.read().splitlines()
commands.pop(0)

for command in commands:
    if 'Simon says' in command:
        print(command.replace('Simon says ', ''))