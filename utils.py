def print_bold(*args):
    print('\033[1m' + "".join(args) + '\033[0m')


def usage_message(__description__):
    print(__description__)
    print_bold("\nUSAGE")
    print("  taco <command> <options>")
    print_bold("\nCORE COMMANDS")
    #     [  <-------     <--------------------
    print("  add:         Add a new task with specified parameters")