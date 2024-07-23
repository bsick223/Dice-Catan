class Player:
    def __init__(self, name):
        self.name = name
        self.resources = {'gold': 0, 'wood': 0, 'brick': 0, 'grain': 0, 'ore': 0, 'sheep': 0}
        self.settlements = 0
        self.cities = 0
        self.roads = 0
        self.victory_points = 0
        self.knights = 0
        self.has_longest_road = False
        self.has_largest_army = False

    def reset_resources(self):
        self.resources = {'gold': 0, 'wood': 0, 'brick': 0, 'grain': 0, 'ore': 0, 'sheep': 0}

    def build_knight(self):
        if self.resources['ore'] >= 1 and self.resources['sheep'] >= 1 and self.resources['grain']:
            self.resources['ore'] -= 1
            self.resources['grain'] -= 1
            self.resources['sheep'] -= 1
            self.knights += 1
            return True
        return False

    def build_settlement(self):
        if self.resources['wood'] >= 1 and self.resources['brick'] >= 1 and self.resources['grain'] >= 1 and self.resources['sheep'] >= 1:
            self.resources['wood'] -= 1
            self.resources['brick'] -= 1
            self.resources['grain'] -= 1
            self.resources['sheep'] -= 1
            self.settlements += 1
            self.victory_points += 1
            return True
        return False

    def build_city(self):
        if self.resources['ore'] >= 3 and self.resources['grain'] >= 2:
            self.resources['ore'] -= 3
            self.resources['grain'] -= 2
            self.cities += 1
            self.victory_points += 2
            return True
        return False

    def build_road(self):
        if self.resources['wood'] >= 1 and self.resources['brick'] >= 1:
            self.resources['wood'] -= 1
            self.resources['brick'] -= 1
            self.roads += 1
            return True
        return False

    def __str__(self):
        achievements = []
        if self.has_longest_road:
            achievements.append("Longest Road")
        if self.has_largest_army:
            achievements.append("Largets Army")
        achievements_str = ', '.join(achievements) if achievements else 'None'
        return (f"Player {self.name}: Settlements: {self.settlements}, Cities: {self.cities}, "
                f"Roads: {self.roads}, Knights: {self.knights}, Victory Points: {self.victory_points}, "
                f"Achievements: {achievements_str}")
