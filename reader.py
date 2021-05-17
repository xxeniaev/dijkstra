class ReadFromFile:
    def __init__(self, file_name):
        self.file_name = file_name

    def reading(self):
        with open(self.file_name, 'r') as f:
            while True:
                n = f.readline().replace('\\n', '')
                if not n:
                    break
                if len(n.split(" ")) > 1:
                    print("first string should consist one number")
                    quit()
                n = int(n)

                i = 0
                adj_list = []
                while i < n:
                    line = f.readline()
                    adj_list.append(line.replace('\\n', '').split())
                    i += 1

                src = f.readline()
                dest = f.readline()

        print(n, adj_list, src, dest)
        return (n, adj_list, src, dest)