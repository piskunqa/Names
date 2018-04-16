from main_parser import Parser


class Init(Parser):
    def __init__(self):
        for name in self.parse_file():
            self.get_result(name)


if __name__ == '__main__':
    Init()