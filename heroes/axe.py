from dota2.base_hero import BaseHero
from dota2.base_skills import BaseSkill


class Axe(BaseHero):
    def __init__(self):
        super().__init__(name="Axe", skills=[BaseSkill(skill_name="Berserker's Call", dmg=3000)])
