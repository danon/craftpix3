from hex.core.Color import DARK_GRAY
from hex.core.Obstacle import Obstacle
from hex.core.Point import Point
from hex.core.port import ForReadingSpriteFiles, ForRenderingView, ForRunningGame
from hex.core.SpriteLoader import SpriteLoader
from test.core.test_Collectible import Collectible

class SpritePreview(ForRunningGame):
    def __init__(self, window: ForRenderingView, fs: ForReadingSpriteFiles):
        self.__window = window
        self.__loader = SpriteLoader(fs)
        self.__ticks = 0
        self.__obstacles = [
            Obstacle(self.__loader.sprite('obstacle/lightning')),
            Obstacle(self.__loader.sprite('obstacle/asid_drop/tube')),
            Obstacle(self.__loader.sprite('obstacle/asid_drop/drop')),
            Obstacle(self.__loader.sprite('obstacle/asid_drop/blob')),
            Obstacle(self.__loader.sprite('obstacle/axe')),
            Obstacle(self.__loader.sprite('obstacle/bomb')),
            Obstacle(self.__loader.sprite('obstacle/chest')),
            Obstacle(self.__loader.sprite('obstacle/fire_skull/skull')),
            Obstacle(self.__loader.sprite('obstacle/fire_skull/fire1')),
            Obstacle(self.__loader.sprite('obstacle/fire_skull/fire2')),
            Obstacle(self.__loader.sprite('obstacle/fire_skull/fire3')),
            Obstacle(self.__loader.sprite('obstacle/fire_skull/fire4')),
            Obstacle(self.__loader.sprite('obstacle/ghost_bottle')),
            Obstacle(self.__loader.sprite('obstacle/guillotine')),
            Obstacle(self.__loader.sprite('obstacle/ram')),
            Obstacle(self.__loader.sprite('obstacle/stone1')),
            Obstacle(self.__loader.sprite('obstacle/stone2')),
            Obstacle(self.__loader.sprite('obstacle/stone3')),
            Obstacle(self.__loader.sprite('obstacle/stone4')),
            Obstacle(self.__loader.sprite('obstacle/trap')),
            Obstacle(self.__loader.sprite('obstacle/web')),
        ]
        self.__obstacle_index = 0
        self.__magic_effects_index = 0
        self.__boss_index = 0
        self.__hero_index = 0
        self.__monster_index = 0
        collect_families = ['castle', 'dungeon', 'forrest', 'mountain']
        collect_items = ['arrow', 'coin', 'crystal', 'heart', 'hit_point', 'star']
        self.__collectibles = [
            [Collectible(
                self.__loader.sprite(f'collect/{family}/{item}'),
                idle=32) for item in collect_items]
            for family in collect_families
        ]
        self.__magic_effects = [
            # Area of effect
            Collectible(self.__loader.sprite(f'magic-effect/ball_shield/animation_ball')),
            Collectible(self.__loader.sprite(f'magic-effect/ball_shield/ball')),
            Collectible(self.__loader.sprite(f'magic-effect/ball_shield/animation')),

            Collectible(self.__loader.sprite(f'magic-effect/spiral_dark')),
            Collectible(self.__loader.sprite(f'magic-effect/death_skull')),

            Collectible(self.__loader.sprite(f'magic-effect/explosion_fire')),
            Collectible(self.__loader.sprite(f'magic-effect/star')),
            Collectible(self.__loader.sprite(f'magic-effect/lightning_horizontal')),
            Collectible(self.__loader.sprite(f'magic-effect/drops_yellow')),
            Collectible(self.__loader.sprite(f'magic-effect/static_purple/start')),
            Collectible(self.__loader.sprite(f'magic-effect/static_purple/cycle')),
            Collectible(self.__loader.sprite(f'magic-effect/static_purple/end')),

            Collectible(self.__loader.sprite(f'magic-effect/spikes_up')),
            Collectible(self.__loader.sprite(f'magic-effect/spikes_forward')),
            Collectible(self.__loader.sprite(f'magic-effect/explosion_star')),

            # Projectile
            Collectible(self.__loader.sprite(f'magic-effect/fireball_purple/start')),
            Collectible(self.__loader.sprite(f'magic-effect/fireball_purple/cycle')),
            Collectible(self.__loader.sprite(f'magic-effect/fireball_purple/end')),

            Collectible(self.__loader.sprite(f'magic-effect/fireball/start')),
            Collectible(self.__loader.sprite(f'magic-effect/fireball/cycle')),
            Collectible(self.__loader.sprite(f'magic-effect/fireball/end')),
            Collectible(self.__loader.sprite(f'magic-effect/fireball_big/start')),
            Collectible(self.__loader.sprite(f'magic-effect/fireball_big/cycle')),
            Collectible(self.__loader.sprite(f'magic-effect/fireball_big/end')),

            Collectible(self.__loader.sprite(f'magic-effect/spiral_green/start')),
            Collectible(self.__loader.sprite(f'magic-effect/spiral_green/cycle')),
            Collectible(self.__loader.sprite(f'magic-effect/spiral_green/end')),
            Collectible(self.__loader.sprite(f'magic-effect/ice_ball/start')),
            Collectible(self.__loader.sprite(f'magic-effect/ice_ball/cycle')),
            Collectible(self.__loader.sprite(f'magic-effect/ice_ball/end')),

            Collectible(self.__loader.sprite(f'magic-effect/lightning_vertical/start')),
            Collectible(self.__loader.sprite(f'magic-effect/lightning_vertical/cycle')),
            Collectible(self.__loader.sprite(f'magic-effect/lightning_vertical/end')),

            Collectible(self.__loader.sprite(f'magic-effect/tornado/start')),
            Collectible(self.__loader.sprite(f'magic-effect/tornado/cycle')),
            Collectible(self.__loader.sprite(f'magic-effect/tornado/end')),
            Collectible(self.__loader.sprite(f'magic-effect/water_ball/start')),
            Collectible(self.__loader.sprite(f'magic-effect/water_ball/cycle')),
            Collectible(self.__loader.sprite(f'magic-effect/water_ball/end')),
        ]
        boss_families = ['king', 'skull', 'wizard']
        boss_stances = ['anger', 'attack', 'death', 'hurt', 'idle',
                        'walk', 'run',
                        'magic_blade', 'magic_fire', 'magic_lightning']
        self.__bosses = [
            [Collectible(self.__loader.sprite(f'boss/{family}/{stance}')) for stance in boss_stances]
            for family in boss_families
        ]
        self.__boss_common = [
            Collectible(self.__loader.sprite('boss/common_blade')),
            Collectible(self.__loader.sprite('boss/common_fire')),
            Collectible(self.__loader.sprite('boss/common_lightning')),
        ]
        hero_families = ['knight1', 'knight2', 'knight3',
                         'mage1', 'mage2', 'mage3',
                         'rogue1', 'rogue2', 'rogue3']
        hero_stances = ['attack1', 'attack2', 'climb', 'death', 'hurt',
                        'idle', 'jump', 'jumphigh', 'push', 'run', 'run_attack',
                        'walk', 'walk_attack']
        self.__heroes = [
            [Collectible(self.__loader.sprite(f'hero/{family}/{stance}')) for stance in hero_stances]
            for family in hero_families
        ]
        hero_projectile_families = ['mage1', 'mage2', 'mage3']
        hero_projectile_stances = ['projectilefire1', 'projectilefire2']
        self.__hero_mage_projectiles = [
            [Collectible(self.__loader.sprite(f'hero/mage_projectile/{family}/{stance}')) for stance in hero_projectile_stances]
            for family in hero_projectile_families
        ]
        monster_families = [
            'melee/lizard_yellow',
            'ranged/lizard_red',
            'ranged/lizard_purple',
            'melee/animal_bear',
            'ranged/animal_spider',
            'melee/minion_wraith',
            'ranged/minion_eye',
            'ranged/warrior_jinn',
            'melee/goblin_snow',
            'melee/goblin_green',
            'melee/minion_person2',
            'ranged/warrior_vampire',
            'melee/warrior_skeleton',
            'melee/creature_ent',
            'melee/creature_troll',
            'ranged/minion_skull_fire',
            'ranged/goblin_fire',
            'melee/goblin_yellow',
            'melee/goblin_dark',
            'melee/minion_person1',
            'melee/warrior_bident',
            'melee/warrior_axe_fire',
            'melee/warrior_axe',
            'melee/dragon_skeleton',
            'melee/dragon_orange',
            'ranged/dragon_purple',
            'melee/animal_snake',
        ]
        monster_stance = ['attack', 'death', 'hurt', 'idle', 'walk']
        self.__monsters = [
            [Collectible(self.__loader.sprite(f'monster/{family}/{stance}')) for stance in monster_stance]
            for family in monster_families
        ]

    def tick(self):
        for obstacle in self.__obstacles:
            obstacle.tick()
        for family in self.__collectibles:
            for collectible in family:
                collectible.tick()
        for family in self.__bosses:
            for boss in family:
                boss.tick()
        for family in self.__heroes:
            for hero in family:
                hero.tick()
        for family in self.__monsters:
            for monster in family:
                monster.tick()
        for family in self.__hero_mage_projectiles:
            for projectile in family:
                projectile.tick()
        for effect in self.__magic_effects:
            effect.tick()
        for common in self.__boss_common:
            common.tick()
        self.__window.fill_background(DARK_GRAY)
        self.__window.draw_frame(self.__loader.abs_path(self.__current_obstacle().frame()), Point(0, 128))
        self.__window.draw_frame(self.__loader.abs_path(self.__current_magic_effect().frame()), Point(0, 512 - 128))
        self.__window.draw_frame(self.__loader.abs_path(self.__current_boss_stance(0).frame()), Point(0, -64 + 512))
        self.__window.draw_frame(self.__loader.abs_path(self.__current_boss_stance(1).frame()), Point(0, 128 + 512 - 32))
        self.__window.draw_frame(self.__loader.abs_path(self.__current_boss_stance(2).frame()), Point(0, 256 + 64 + 512 - 64))
        self.__window.draw_frame(self.__loader.abs_path(self.__boss_common[0].frame()), Point(128, -64 + 512))
        self.__window.draw_frame(self.__loader.abs_path(self.__boss_common[1].frame()), Point(128, 128 + 512))
        self.__window.draw_frame(self.__loader.abs_path(self.__boss_common[2].frame()), Point(128, 256 + 64 + 512))

        cut_point = 13
        for index, monster in enumerate(self.__monsters):
            col = index % 2
            row = index // 2
            if index < cut_point:
                x = 512 + 256 + (128 * col)
                y = row * 128
            else:
                new_index = index - cut_point
                col = new_index % 4
                row = new_index // 4
                x = 512 + 512 + (256 * col)
                y = row * 256

            self.__window.draw_frame(
                self.__loader.abs_path(self.__current_monster_stance(index).frame()), Point(x, y))

        for index, hero in enumerate(self.__heroes):
            self.__window.draw_frame(
                self.__loader.abs_path(hero[self.__hero_index].frame()),
                Point(512 - 128, index * (64 + 32)))

        for fam_index, family in enumerate(self.__hero_mage_projectiles):
            for index, collectible in enumerate(family):
                self.__window.draw_frame(
                    self.__loader.abs_path(collectible.frame()),
                    Point(index * 48 + 512, fam_index * 64 + 256))

        for fam_index, family in enumerate(self.__collectibles):
            for index, collectible in enumerate(family):
                self.__window.draw_frame(
                    self.__loader.abs_path(collectible.frame()),
                    Point(index * 32, fam_index * 32))
        self.__window.render_finish()
        self.__ticks += 1

    def __current_obstacle(self) -> Obstacle:
        return self.__obstacles[self.__obstacle_index]

    def __current_magic_effect(self) -> Collectible:
        return self.__magic_effects[self.__magic_effects_index]

    def __current_boss_stance(self, i: int) -> Collectible:
        return self.__bosses[i][self.__boss_index]

    def __current_monster_stance(self, i: int) -> Collectible:
        return self.__monsters[i][self.__monster_index]

    def click(self):
        for element in self.__obstacles:
            element.initiate()

    def left(self, active: bool):
        self.__obstacle_index -= 1
        self.__magic_effects_index -= 1
        self.__boss_index -= 1
        self.__hero_index -= 1
        self.__monster_index -= 1

    def right(self, active: bool):
        self.__obstacle_index = (self.__obstacle_index + 1) % len(self.__obstacles)
        self.__magic_effects_index = (self.__magic_effects_index + 1) % len(self.__magic_effects)
        self.__boss_index = (self.__boss_index + 1) % len(self.__bosses[0])
        self.__hero_index = (self.__hero_index + 1) % len(self.__heroes[0])
        self.__monster_index = (self.__monster_index + 1) % len(self.__monsters[0])
