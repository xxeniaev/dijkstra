class ReadFromFile:
    def __init__(self, file_name):
        self.file_name = file_name

    def reading(self):
        with open(self.file_name, 'r') as f:
            n = int(f.readline().replace('\\n', ''))

            i = 0
            adj_list = []
            while i < n:
                line = f.readline()
                adj_list.append(line.replace('\\n', '').split())
                i += 1

            src = int(f.readline().replace('\\n', ''))
            dest = int(f.readline().replace('\\n', ''))

        return (n, adj_list, src, dest)