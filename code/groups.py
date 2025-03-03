from settings import *

class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.Vector2()

    
    def draw(self, target_pos):
        self.offset.x = -(target_pos[0] - WINDOW_WIDTH / 2)
        self.offset.y = -(target_pos[1] - WINDOW_HEIGHT / 2)

        platform_sprite = [sprite for sprite in self if hasattr(sprite, "main")]
        decor_sprite = [sprite for sprite in self if not hasattr(sprite, "main")]

        for sprite in [platform_sprite, decor_sprite]:
            for sprite in sorted(sprite, key=lambda sprite: sprite.rect.centery):
                self.display_surface.blit(sprite.image, sprite.rect.topleft + self.offset)