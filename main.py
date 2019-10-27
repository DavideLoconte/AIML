import sys
import importlib.util

from os import listdir
from os.path import isfile, join



def print_avaliable_examples(examples):
    print("Input example number:")
    for index, example in enumerate(examples):
        print("[{}] {}".format(index, example))
    print("Default: exit")


def get_selection():
    try:
        return int(input())
    except:
        return -1



def start(examples, selection):
    for index, example in enumerate(examples):
        if index == selection:
            spec = importlib.util.spec_from_file_location("example", join("examples", example))
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module.main()
    return 0



def main():
    examples = [f for f in listdir("examples") if isfile(join("examples", f))]
    print_avaliable_examples(examples)
    return start(examples, get_selection())


if __name__ == "__main__":
    sys.exit(main())
