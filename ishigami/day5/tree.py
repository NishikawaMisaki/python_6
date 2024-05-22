class GreenSoftware:
    def __init__(self):
        self.bug_list = []
        self.plant_list = []
        self.tree_count = 0

    def add_bug(self, bug):
        self.bug_list.append(bug)

    def fix_bug(self, bug):
        if bug in self.bug_list:
            self.bug_list.remove(bug)
            self.plant_tree()
            self.plant_list.append(bug+"の木")
    
    def show_bug(self):
            print(self.bug_list)

    def plant_tree(self):
        self.tree_count += 1
        print(f"バグが修正され、新しい木が植えられました！ 現在の木の数: {self.tree_count}")

    def show_plant(self):
         print(self.plant_list)
         

# 使用例
software = GreenSoftware()
software.add_bug("バグ1")
software.add_bug("バグ2")
software.show_bug()
software.fix_bug("バグ1")  # バグが修正され、新しい木が植えられます！ 現在の木の数: 1
software.show_bug()
software.show_plant()

