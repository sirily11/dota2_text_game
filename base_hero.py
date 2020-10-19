from .base_skills import BaseSkill
from typing import List


class BaseHero:
    name: str
    base_hp = 300
    base_dmg = 40
    hp = 300
    strength = 20
    agility = 20
    intelligence = 20
    skills: List[BaseSkill] = []

    def __init__(self, name, skills: List[BaseSkill]):
        self.name = name
        self.skills = skills

    def get_hp(self):
        return self.strength * 20 + self.base_hp

    def get_dmg(self):
        return self.strength * 3 + self.base_dmg

    def attack(self, target):
        target.been_attacked(self)
        print(f"{target.name}: {target.hp}")

    def attack_by_skill(self, target, skill: BaseSkill):
        if skill not in self.skills:
            print("Skill is not avaliable")
        else:
            target.been_attacked(from_skill=skill)

    def defense(self):
        pass

    def been_attacked(self, from_hero=None, from_skill: BaseSkill = None):
        if from_hero:
            self.hp -= from_hero.get_dmg()
        if from_skill:
            self.hp -= from_skill.get_dmg()
        if self.hp < 0:
            print(f"{self.name} die")
