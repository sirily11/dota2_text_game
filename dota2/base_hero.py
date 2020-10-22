from typing import List, TYPE_CHECKING
from enum import Enum
from random import random
from math import ceil

if TYPE_CHECKING:
    from dota2.base_skills import BaseSkill


class Status(Enum):
    NORMAL = 0
    STUN = 1
    # Received magic damage increase
    MAGIC_DAMAGE_INCREASE = 2
    # Received physical damage increase
    PHYSICAL_DAMAGE_INCREASE = 3
    SLEEP = 4
    VOID = 5


class BaseHero:
    name: str
    __base_hp__ = 300
    __base_dmg__ = 40
    strength = 20
    agility = 20
    intelligence = 20
    skills: List['BaseSkill'] = []
    # Current hero's status
    current_status: Status = Status.NORMAL
    current_exp: int = 0
    current_level = 1
    is_dead = False
    respawn_remaining_time = 0

    def __init__(self, name, skills: List['BaseSkill']):
        self.name = name
        self.skills = skills
        self.current_hp = self.__calculate_hp__()
        self.current_mp = self.__calculate_mp__()

    def __calculate_hp__(self) -> float:
        """
        Get current hp
        :return:
        """
        return self.strength * 20 + self.__base_hp__

    def __calculate_mp__(self) -> float:
        return self.intelligence * 20

    @property
    def agility_grow(self) -> float:
        """
        Agility growing rate.
        :return:
        """
        raise NotImplementedError

    @property
    def intelligence_grow(self) -> float:
        """
        Agility growing rate.
        :return:
        """
        return 20

    @property
    def strength_grow(self) -> float:
        """
        Agility growing rate.
        :return:
        """
        raise NotImplementedError

    @property
    def damage(self) -> float:
        """
        Get current damage
        :return:
        """
        return self.strength * 3 + self.__base_dmg__

    @property
    def respawn_time(self) -> float:
        """
        Get respawn time. Hero will respawn after this time
        :return: respawn time
        """
        return min(ceil(self.current_level * 0.2), 5)

    @property
    def evasion_rate(self):
        return min(self.agility * 0.1, 0.95)

    def level_up(self) -> bool:
        """
        Level up.
        :return:
        """
        level = self.current_exp / (self.current_level ** 2)
        if level >= self.current_level:
            self.agility += self.agility_grow
            self.strength += self.strength_grow
            self.intelligence += self.intelligence_grow
            self.current_hp = self.__calculate_hp__()
            self.current_mp = self.__calculate_mp__()
            self.current_level = level
            return True
        return False

    def attack(self, target: 'BaseHero'):
        """
        Base attack
        """
        success = target.been_attacked(self)
        if success:
            pass

        print(f"{target.name}: {target.current_hp}")

    def cast_skill_on(self, target, skill: 'BaseSkill'):
        """
        Cast skill on hero
        :param target: Hero
        :param skill: Skill
        :return:
        """
        pass

    def been_attacked(self, by_hero: 'BaseHero') -> bool:
        """
        Been attacked by hero.
        Physical damage.
        :param by_hero: hero
        :return: return True, if success, else False
        """
        value = random()
        if value > self.evasion_rate:
            damage = by_hero.damage
            self.current_hp = max(self.current_hp - damage, 0)
            if self.current_hp == 0:
                self.is_dead = True
                self.respawn_remaining_time = self.respawn_time
            return True
        else:
            return False

    def attacked_by_skill(self, by_hero, by_skill: 'BaseSkill'):
        """
        Been attacked by skill
        Magic or physical damage
        :param by_hero:
        :param by_skill:
        :return:
        """
        pass
