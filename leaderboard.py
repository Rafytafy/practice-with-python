import csv

class Leaderboard:
    def __init__(self):
        self.users = []
        self.index = -1

    def _get_users(self):
        with open("hangman.csv", "r") as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                self.users.append(row)

    def _find_user(self, name):
        for i in range(len(self.users)):
            if name in self.users[i]:
                self.index = i
                break
    
    def _write_to_file(self):
        with open("hangman.csv", "w", newline='') as file:
            writer = csv.writer(file, delimiter=',')

            for row in self.users:
                writer.writerow(row)

    def update_leaderboard(self, name, win):
        self._get_users()
        self._find_user(name)

        print(self.index)
        if win and self.index != -1:
            self.users[self.index][1] = int(self.users[self.index][1]) + 1
        elif not win and self.index != -1:
            self.users[self.index][2] = int(self.users[self.index][2]) + 1
        elif win and self.index == -1:
            self.users.append([name, 1, 0])
        elif not win and self.index == -1:
            self.users.append([name, 0, 1])

        self._write_to_file()

l1 = Leaderboard()
l1.update_leaderboard("Rj", False)