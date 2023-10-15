import settings
from settings import *
from camera import Camera
import objects_3d as obj_3d


class Game:
    def __init__(self):
        self.running = True
        self.clock = settings.clock
        self.FPS = settings.FPS
        self.display = settings.DISPLAY
        self.display_size = vec2(settings.D_W, settings.D_H)

        self.camera = Camera(self.display_size, pos=vec3(10, 10, 10), normal=vec3(1, 0, 0))
        self.cube = obj_3d.Cube()

        self.font = pg.font.Font(None, 40)

    def run(self):
        while self.running:
            events = pg.event.get()
            dt = self.clock.tick(self.FPS)/1000

            self.process_events(events)

            self.update(dt)

            self.draw(dt)

    def process_events(self, events):
        for event in events:
            if event.type == pg.QUIT:
                self.running = False

        keys_pressed = pg.key.get_pressed()
        self.camera.process_events(keys_pressed)

    def draw(self, dt):
        self.display.fill((255, 255, 255))

        self.display.blit(self.camera.frame, (0, 0))

        self.draw_debug_screen()

        pg.display.update()

    def update(self, dt):
        self.camera.reset_frame()
        self.camera.render_object(self.cube)

    def draw_debug_screen(self):
        self.display.blit(self.font.render(f"normal  x: {round(self.camera.normal.x, 2)}, "
                                           f"y: {round(self.camera.normal.y, 2)}, "
                                           f"z: {round(self.camera.normal.z, 2)}",
                                           True, (15, 128, 25)), (10, 10))
        self.display.blit(self.font.render("normal magnitude  " + str(round(self.camera.normal.magnitude(), 5)), True, (15, 128, 25)), (10, 50))
        self.display.blit(self.font.render(f"rotation  x: {round(self.camera.rotation.x/pi, 2)}π, "
                                           f"y: {round(self.camera.rotation.y/pi, 2)}π, "
                                           f"z: {round(self.camera.rotation.z/pi, 2)}π",
                                           True, (15, 128, 25)), (10, 90))

        self.display.blit(self.font.render(f"actual radius  {round(self.camera.actual_circle_radius, 2)}", True, (15, 128, 25)), (10, 130))


DuTresis = Game()
DuTresis.run()
