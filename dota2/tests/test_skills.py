from unittest import TestCase

from dota2.base_skills import BaseSkill


class TestSkill(TestCase):

    def setUp(self) -> None:
        self.skill = BaseSkill()

    def test_base_skill(self):
        self.skill.damage_range = [10, 20, 30, 40]
        self.assertEqual(self.skill.damage, 10)

    def test_base_skill_cast(self):
        self.skill.damage_range = [10, 20, 30, 40]
        self.skill.level_up()
        self.assertEqual(self.skill.damage, 20)
