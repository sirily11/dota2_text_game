class BaseSkill:
    def __init__(self, skill_name, dmg):
        self.skill_name = skill_name
        self.dmg = dmg

    def get_dmg(self):
        return self.dmg
