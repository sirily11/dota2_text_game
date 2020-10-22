from dota2.base_hero import BaseHero


class BaseSkill:
    skill_name = "skill"
    damage_range = [30, 40, 50, 60]
    mp_costs = [30, 40, 50, 60]
    current_level = 0

    @property
    def mp_cost(self):
        """
        Get mp cost for skill at current level
        :return:
        """
        return self.mp_costs[self.current_level]

    @property
    def damage(self):
        return self.damage_range[self.current_level]

    def level_up(self) -> bool:
        """
        Level up the skill
        :return:
        """
        if self.current_level == len(self.damage_range) - 1:
            return False

        self.current_level += 1
        return True

    def cast_skill(self, from_hero, to_hero):
        raise NotImplementedError

    def get_physical_damage(self, from_hero: BaseHero, to_hero: BaseHero) -> float:
        raise NotImplementedError

    def get_magical_damage(self, from_hero: BaseHero, to_hero: BaseHero) -> float:
        raise NotImplementedError


class BaseMagicSkill(BaseSkill):
    skill_name = "magic skill"

    def cast_skill(self, from_hero, to_hero):
        pass

    def get_physical_damage(self, from_hero: BaseHero, to_hero: BaseHero) -> float:
        pass

    def get_magical_damage(self, from_hero: BaseHero, to_hero: BaseHero) -> float:
        pass
