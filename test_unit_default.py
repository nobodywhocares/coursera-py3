import unittest

from ClassesInheritance import *


class TestGrassPokemon(unittest.TestCase):
    def test_leveling_attack_value(self):
        """
        Test that the attack value is not updated until reaching level 10 or above via training
        """
        attack_init = 15
        g_poke = Grass_Pokemon('Badass')
        for i in range(9 - g_poke.level):
            g_poke.train()
            self.assertEqual(g_poke.attack, attack_init)
        g_poke.train()
        self.assertEqual(g_poke.attack, attack_init+g_poke.getAttackBoost())
        g_poke.train()
        self.assertEqual(g_poke.attack, attack_init+(g_poke.getAttackBoost()*2))

if __name__ == '__main__':
    unittest.main()
