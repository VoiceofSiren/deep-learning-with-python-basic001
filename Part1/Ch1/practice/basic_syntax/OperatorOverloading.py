class SquareNumbers:
    def __init__(self, my_list):
        self.my_list = my_list

    def __getitem__(self, idx):
        return self.my_list[idx] + 10

    def __len__(self):
        return len(self.my_list)

squares = SquareNumbers([0, 1, 2, 3, 4])

for i in range(len(squares)):
    print(squares[i], end=" ")