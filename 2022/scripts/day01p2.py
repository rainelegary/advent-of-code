class Solution:
    def main():
        with open("inputs/day01.txt", "r") as fh:
            contents = fh.readlines()

        stats = Stats()
        cals = 0
        for line in contents:
            if line.strip() == "":
                stats.add_cals(cals)
                cals = 0
            else:
                cals += int(line.strip())

        stats.add_cals(cals)
        print(sum(stats.top_cals))


class Stats:
    def __init__(self):
        self.top_cals = [0, 0, 0]


    def add_cals(self, cals):
        i = len(self.top_cals) - 1
        while i >= 0:
            if cals > self.top_cals[i]:
                self.top_cals[i] = cals
                break
            i -= 1


if __name__ == "__main__":
    Solution.main()