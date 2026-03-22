import pyxel
WALL_TILES = [(0,1)]
WINDOW_W = 160
WINDOW_H = 120

class Bullet:
    def __init__(self,x,y,a,b):
        self.x = x
        self.y = y
        self.kasol_x = a
        self.kasol_y = b
        self.speed = 5
        self.is_alive = True
        self.life = 60
        self.bullets = []
        pyxel.mouse(True)
    def update(self):
        if self.x <= self.kasol_x:
            self.x += self.speed
        elif self.x >= self.kasol_x:
            self.x -= self.speed
        if self.y <= self.kasol_y:
            self.y += self.speed
        elif self.y >= self.kasol_y:
            self.y -= self.speed
        self.life -= 1
        if self.life <= 0:
            self.is_alive = False
        alive_bullets = []
        for  b in self.bullets:
            if b.is_alive:
                alive_bullets.append(b)
        self.bullets = alive_bullets        
        
    def draw(self):
        pyxel.rect(self.x,self.y,2,2,8)
class enemy:
    def __init__(self,x,y):
        self.x = 100
        self.y = 100
        self.w = 8
        self.h = 8
        self.a = x
        self.b = y
        self.c = 80
        self.is_alive= True
        self.enemys = []
    def update(self,a,b):
        if a >= self.x:
            self.x += 1
        else:
            self.x -= 1
        if b >= self.y:
            self.y += 1
        else:
            self.y -= 1
        if self.a < self.c:
            self.x += 2
            self.c = self.a
        elif self.a > self.c:
            self.x -= 2
            self.c = self.a
        else:
            self.c =self.a
        alive_enemys = []
        for a in self.enemys:
            if a.is_alive:
                alive_enemys.append(a)
        self.bullets = alive_enemys
    def draw(self):
        pyxel.rect(self.x,self.y,self.w,self.h,9)

class App:
    def __init__(self):
        self.d = 50
        self.x=80
        self.y=50
        self.gamenn = 0
        self.u = 0
        self.fream= 0
        pyxel.init(WINDOW_W, WINDOW_H)
        pyxel.image(0).load(0, 0, "assets/pyxel_logo_38x16.png")
        pyxel.image(1).load(0, 0, "assets/cat_16x16.png")
 
        pyxel.load("ground_resource.pyxres")
        # pyxel.mouse(False)
        self.bullet = Bullet(-1000,self.y,0,0)
        self.enemy = []
        pyxel.run(self.update, self.draw)

    def update(self):
        global a,b
        next_x, next_y = self.x+72,self.y
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btn(pyxel.KEY_A):
            next_x -= 2
        if pyxel.btn(pyxel.KEY_D):
            next_x += 2
        if pyxel.btn(pyxel.KEY_W):
            next_y -= 2
        if pyxel.btn(pyxel.KEY_S):
            next_y += 2
        pyxel.mouse(True)
        #self.enemy.update(72,self.y)
        if self.fream % 60 == 0:
            new_enemy = enemy(self.x,self.y)
            self.enemy.append(new_enemy)
        for a in self.enemy:
            a.update(72,self.y)
        
        self.bullet.update()
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            c = pyxel.mouse_x
            d = pyxel.mouse_y 
            new_bullet = Bullet(70,50,c,d)
            self.bullet.bullets.append(new_bullet)
        for b in self.bullet.bullets:
            b.update()

        for b in self.bullet.bullets:
            for c in self.enemy:
                if (self.enemy.x < b.x + 2 and
                    self.enemy.x + self.enemy.w > b.x and
                    self.enemy.y < b.y + 2 and
                    self.enemy.y + self.enemy.h > b.y ):
                    self.enemy.is_alive = False

        next_tile_x,next_tile_y = next_x //  8, next_y // 8
        tile = pyxel.tilemap(0).pget(next_tile_x, next_tile_y)
        tile2 = pyxel.tilemap(0).pget(next_tile_x+1, next_tile_y+1)
        tile3 = pyxel.tilemap(0).pget(next_tile_x+1, next_tile_y)
        tile4 = pyxel.tilemap(0).pget(next_tile_x, next_tile_y+1)
        if tile not in WALL_TILES and tile2 not in WALL_TILES and tile3 not in WALL_TILES and tile4 not in WALL_TILES:
            self.x,self.y = next_x-72,next_y

        

    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0,0,0,self.x,0, 20*8,15*8)

        pyxel.rect(72,self.y,8,8,7)
        self.bullet.draw()
        for b in self.bullet.bullets:
            b.draw()
        
        for a in self.enemy:
            a.draw()

App()