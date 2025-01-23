from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero
class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land=Mapmanager()
        self.land.loadLand("land.txt")
        x,y=self.land.loadLand("land.txt")
        self.hero=Hero((x // 2, y // 2,2), self.land)

        model=self.loader.loadModel("model/sky_sphere")
        model.reparentTo(self.render)
        base_texture=loader.loadTexture("model/img.png")
        model.setTexture(base_texture)
        # model.setColor((1,0,0,1))
        model.setPos(0,0,0)
        model.setScale(50,50,50)
        model.setHpr(90,0,0)

        model=self.loader.loadModel("model/Boeing")
        model.reparentTo(self.render)
        base_texture=loader.loadTexture("model/BoeingTexture.tif")
        model.setTexture(base_texture)
        # model.setColor((1,0,0,1))
        model.setPos(13,13,13)
        model.setScale(0.2,0.2,0.2)
        model.setHpr(90,0,0)


        model=self.loader.loadModel("model/planet_sphere")
        model.reparentTo(self.render)
        base_texture=loader.loadTexture("model/earth_1k_tex.jpg")
        model.setTexture(base_texture)
        # model.setColor((1,0,0,1))
        model.setPos(-10,-18,20)
        model.setScale(7,7,7)
        model.setHpr(10,50,50)



        base.camLens.setFov(90)
game = Game()
game.run()
planet_sphere.egg.pz