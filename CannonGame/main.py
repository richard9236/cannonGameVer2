
import time
import os
import math
import random
import pygame, sys

pygame.init()
pygame.mixer.init()

class UIButton: # this is what we use to generate a button
    RealPosX, RealPosY = 0, 0
    
    def __init__(self, Window, Text, TextSize, RectColor, TextColor, Hight, Length, PosX, PosY):
        self.Window = Window # init the window and allow all x and y values 
        
        if type(Text) ==type("a"): # this means we do not have a text editor 
            self.TextSize = TextSize
            self.TextColor = TextColor
            smallfont = pygame.font.SysFont('Corbel', TextSize)
            self.Text = smallfont.render(Text, True, TextColor)
            
        self.Rect = RectColor
        self.Hight = Hight
        self.Length = Length
        
        self.PosX, self.PosY = PosX, PosY
        global RealPosX, RealPosY 
        
        RealPosX, RealPosY = Hight, Length
        
    def TestIfWasButton(self, mousePos): # we run this every frame and if our mouse is down and meets the requiremenrts, we run this 
        if self.PosX <= mousePos[0] and self.PosX + self.Length >= mousePos[0] and self.PosY <= mousePos[1] and self.PosY + self.Hight >= mousePos[1]:
            PS(4)

            return True
    def ChangeText(self, newText): # change the text of the button
        smallfont = pygame.font.SysFont('Corbel', self.TextSize)
        self.Text = smallfont.render(newText, True, self.TextColor)
        
    def Draw(self, _int): # how we draw the object and see if it exists
        if _int != 5:
            pygame.draw.rect(self.Window, self.Rect, [self.PosX, self.PosY, self.Length, self.Hight])
            self.Window.blit(self.Text, (self.PosX, self.PosY))
        
    def ShowOrHide(self, action): # how we determine to draw a button or not the draw a button
        if action == True: # show
            self.PosX = RealPosX
            self.PosY = RealPosY
        else: # hide
            hiddenInt = -5555
            self.PosX = hiddenInt
            self.PosY = hiddenInt
FpsLimit = 44
WinHight, WinLength = 1000, 650

Window = pygame.display.set_mode((WinHight, WinLength)) # thie window and hight length of the objects
pygame.display.set_caption("Cannon Shooter .v2")
_Blackout = False
NumOfBulletShot = 0
NumOfBulletHit = 0
NumOfReload = 0
ReloadOnFire = 1
ShotgunUpgrade = 2
    
BackdropsTB = [pygame.image.load(os.path.join("Assets", "Forest0.jpg")),
             
             ] # where we store our backdrops 
MiscTB = [pygame.image.load(os.path.join("Assets", "Cannon.png" )), # where we store our images 
    pygame.image.load(os.path.join("Assets", "CannonBall.png")),
    pygame.image.load(os.path.join("Assets", "Explosion.png")),
    pygame.image.load(os.path.join("Assets", "Bullet_0.png")),
    pygame.image.load(os.path.join("Assets", "Bullet_1.png")),
    pygame.image.load(os.path.join("Assets", "Bullet_2.png")),
    pygame.image.load(os.path.join("Assets", "Bullet_3.png")),
    pygame.image.load(os.path.join("Assets", "Bullet_4.png")),
    pygame.image.load(os.path.join("Assets", "Bullet_5.png")),
    pygame.image.load(os.path.join("Assets", "Health_0.png")),
    pygame.image.load(os.path.join("Assets", "Health_1.png")),
    pygame.image.load(os.path.join("Assets", "Health_2.png")),
    pygame.image.load(os.path.join("Assets", "Health_3.png")),
    pygame.image.load(os.path.join("Assets", "Bat_0.png")),
    pygame.image.load(os.path.join("Assets", "Bat_1.png")),
    pygame.image.load(os.path.join("Assets", "Zombie_0.png")),
    pygame.image.load(os.path.join("Assets", "Zombie_1.png")),
    pygame.image.load(os.path.join("Assets", "Wolf_0.png")),
    pygame.image.load(os.path.join("Assets", "Wolf_1.png")),
    pygame.image.load(os.path.join("Assets", "Tower_3.png")),
    pygame.image.load(os.path.join("Assets", "Tower_2.png")),
    pygame.image.load(os.path.join("Assets", "Tower_0.png")),
    pygame.image.load(os.path.join("Assets", "Tower_1.png")),
    pygame.image.load(os.path.join("Assets", "FireBall.png")),
    pygame.image.load(os.path.join("Assets", "SpitBall.png")),
    pygame.image.load(os.path.join("Assets", "Dragon_0.png")),
    pygame.image.load(os.path.join("Assets", "Dragon_1.png")),
    pygame.image.load(os.path.join("Assets", "BDragon_0.png")),
    pygame.image.load(os.path.join("Assets", "BDragon_1.png"))
    
]
remoteInt = 0
MiscTB[24] = pygame.transform.scale(MiscTB[24], (40, 40)) # spit ball
MiscTB[24] = pygame.transform.rotate(MiscTB[24], 50)

MiscTB[0] = pygame.transform.scale(MiscTB[0], (200, 200)) # a picture that renders each frame 
MiscTB[1] = pygame.transform.scale(MiscTB[1], (40, 40)) # the noko image
MiscTB[23] = pygame.transform.scale(MiscTB[23], (40, 40)) # kolre the fire ball

MiscTB[2] = pygame.transform.scale(MiscTB[2], (110, 110))

#bullets
for i in range(6):
    i = i +3
    MiscTB[i] = pygame.transform.scale(MiscTB[i], (200, 40))
for i in range(3): # health
    i = i +9
    MiscTB[i] = pygame.transform.scale(MiscTB[i], (110, 40))

# these 2 are the bat
MiscTB[13] = pygame.transform.scale(MiscTB[13], pygame.math.Vector2(100, 100))
MiscTB[14] = pygame.transform.scale(MiscTB[14], pygame.math.Vector2(100, 100))

# these are zombie
MiscTB[15] = pygame.transform.scale(MiscTB[15], pygame.math.Vector2(200, 200))
MiscTB[16] = pygame.transform.scale(MiscTB[16], pygame.math.Vector2(200, 200))

# wolf boy
MiscTB[17] = pygame.transform.scale(MiscTB[17], pygame.math.Vector2(150, 100))
MiscTB[18] = pygame.transform.scale(MiscTB[18], pygame.math.Vector2(150, 100))

# tower boy
MiscTB[19] = pygame.transform.scale(MiscTB[19], pygame.math.Vector2(100, 100))
MiscTB[20] = pygame.transform.scale(MiscTB[20], pygame.math.Vector2(100, 100))

# next tower boy
MiscTB[21] = pygame.transform.scale(MiscTB[21], pygame.math.Vector2(100, 100))
MiscTB[22] = pygame.transform.scale(MiscTB[22], pygame.math.Vector2(100, 100))

# dragon boy
MiscTB[25] = pygame.transform.scale(MiscTB[25], pygame.math.Vector2(150, 100))
MiscTB[26] = pygame.transform.scale(MiscTB[26], pygame.math.Vector2(150, 100))
# blue dragon boy
MiscTB[27] = pygame.transform.scale(MiscTB[27], pygame.math.Vector2(150, 100))
MiscTB[28] = pygame.transform.scale(MiscTB[28], pygame.math.Vector2(150, 100))

# where we store all of our sound 
SoundTB = [pygame.mixer.Sound(os.path.join("Assets", 'Fire.wav')),
           pygame.mixer.Sound(os.path.join("Assets", 'Pop.wav')),
           pygame.mixer.Sound(os.path.join("Assets", 'Pop.wav')),
           pygame.mixer.Sound(os.path.join("Assets", 'Pop.wav')),
           pygame.mixer.Sound(os.path.join("Assets", 'Pop.wav')),
           pygame.mixer.Sound(os.path.join("Assets", 'Pop.wav')),
           pygame.mixer.Sound(os.path.join("Assets", 'Wasted.wav')),
           ]
# this is where we execute our sound 
def PS(i):
    global SoundTB
    pygame.mixer.Sound.play(SoundTB[i])
# these are all of our rendered colors 
ColorTB = [(170,170,170), (100, 100, 100)]
for i in range(len(BackdropsTB)):
    BackdropsTB[i] = pygame.transform.scale(BackdropsTB[i], (WinHight, WinLength))
CurrentBackdrop = 0
 # init the backdrop  
pygame.display.set_icon(BackdropsTB[0])

def wait(f): # a wait statement 
    time.sleep(f)
    a = 1
def Blackout(color): # this function is to blackout the screen 
    # not very effected beacuse we are using a wait directly in an fps clock
    s = pygame.Surface((2000,2000))
    s.set_alpha(0)
    a, remoteInt = 1,0
    if (color == False):
        color = (0,0,0)
    
    while True:
        
        s.set_alpha(remoteInt)
        s.fill(color)
        Window.blit(s, (0,0))
        remoteInt = remoteInt +a
        wait(.02)
        if remoteInt >= 65 or remoteInt <= -5:
            break
        pygame.display.update()
    s.set_alpha(0)
    global _Blackout
    #_Blackout = False
    
    
    
def BuildBackdrop(x):
    # settup the backdrop and begin rendering it 
    Window.blit(BackdropsTB[x], (0, 0))

_BulletImage = 0
_HealthImage = 0
_SpriteOffset = 0
_Gold = 5
TowerUpgrade =2
DoubleCastUpgrade = 2
_HealCost = 0
bulletTB = []
bulletCacheTB = []
bulletHitBoxTB = []
bulletTypeCacheTB = []

MonsterTB = [] # will hold monster type
MonsterCacheTB= [] # will hold monster pos
MonsterCacheTB1 = []# will hold misc image int
MonsterCacheTB2 = [] # will hold monster health
MonsterCacheTB3 = [] # will hold monster speed
bulletCacheTB1 = []

exploTB = []
exploCacheTB = []
exploCacheTB1 = []
for i in range(3):
    bulletCacheTB.append(1) 

CannonLocation = pygame.math.Vector2(0, Window.get_height() - 200)
CannonLocationHead = pygame.math.Vector2(130, Window.get_height() - 140)
def PullFloat(x, min, max): # to assure each integer doesn't exceed another integer 
    if x < min:
        x = min
    elif x > max:
        x = max
    return x

def DrawBullet(): # where we render the bullet 
    global Window
    global bulletTB
    global bulletCacheTB
    global bulletHitBoxTB
    global CannonLocationHead
    global bulletTypeCacheTB
    global CannonLocation
    global bulletCacheTB1
    
    for i in range(len(bulletTB)):
        if bulletTB[i] != True: # loop it to see if the bullet hit anything 
            sheet = bulletCacheTB1[i] + bulletTB[i] * bulletCacheTB[i]
            
            Window.blit(MiscTB[bulletTypeCacheTB[i]], sheet)
            
            pygame.display.update()
            bulletCacheTB[i]= bulletCacheTB[i] +22
            if bulletCacheTB[i] >= 1500: # check the bullet if it exceeds a certain number on the x and y axis 
                bulletTB[i] = True
                bulletCacheTB[i] = 1

def ShowBullets(f): # show our bullets throu an image 
    global _BulletImage
    _BulletImage = f +3
def ShowHealth(f): # show the healt hof an object 
    global _HealthImage
    _HealthImage = f +9

_Health = 3
ShowBullets(5)
ShowHealth(_Health)

def TakeDamage(): # we took some damage  
    global _Health
    _Health = _Health -1
    ShowHealth(PullFloat(_Health, 0, 3))
    
def AddExplosion(vec0): # where we append an explosion to our explosions 
    global exploTB
    global exploImg
    global exploCacheTB
    global exploCacheTB1
    exploTB.append(pygame.math.Vector2(vec0[0] - 30,  vec0[1] - 80))
    exploCacheTB.append(1)
    exploCacheTB1.append(random.randint(0, 5))
exploImg = []
remoteInt = 0
for i in range(6): # loop and generate all possible explosions 
    remoteInt = remoteInt + 5
    exploImg.append(pygame.transform.rotate(MiscTB[2], remoteInt * 10))
    
def DrawExplosion():# coroutine
    global Window
    global MiscTB 
    global exploImg
    global exploTB
    global exploCacheTB
    global exploCacheTB1
    if (len(exploTB) >0): # also make sure that our thing doesn't exceed a certain number 
        for i in range(len(exploTB)):
            if exploTB[i] != 0:
                exploCacheTB[i] = exploCacheTB[i] +1
                
                Window.blit(exploImg
                            [exploCacheTB1[i]], 
                            exploTB[i])
                
                if exploCacheTB[i] >= 66:
                    exploTB[i] = 0

MonsterHealthTB = []
MonsterHealthTB1 = []
        
def SpawnMonster(monsterType, intt): #will be the fast times at ridgmont high
    global MonsterTB
    global MonsterCacheTB
    global MonsterCacheTB1
    global MonsterCacheTB2
    global MonsterCacheTB3
    
    global MonsterHealthTB
    global MonsterHealthTB1
    
    monsterHealth, monsterSpeed, monsterImgInt = 0,0,0
    if monsterType == 1: # a bat
        monsterHealth, monsterSpeed, monsterImgInt = 5, 3, 13
    elif monsterType == 2: # a bear
        monsterHealth, monsterSpeed, monsterImgInt = 25, 1, 15
    elif monsterType == 3: # a wolf
        monsterHealth, monsterSpeed, monsterImgInt = 50, 3.5, 17
    elif monsterType == 4: # a dragon
        monsterHealth, monsterSpeed, monsterImgInt = 50, 2, 25
    elif monsterType == 5: # a blue dragon
        monsterHealth, monsterSpeed, monsterImgInt = 50, 5, 27        
    
    monsterXAxis = random.randint(0, 5) + 10 # monster x axis 
    monsterXAxis = monsterXAxis * 100 
    
    MonsterCacheTB.append(pygame.math.Vector2(monsterXAxis, intt)) # y spawn point
    MonsterCacheTB1.append(monsterImgInt) # misc img
    MonsterCacheTB2.append(monsterHealth) # health
    MonsterCacheTB3.append(monsterSpeed) # speed
    
    MonsterTB.append(monsterType) # monster type

def SpawnBat(i): # init a bat and append it 
    if i >= 1 :
        for _i in range(i):
            SpawnMonster(1, random.randint(30, 250))
def SpawnZombie(i): # init 
    if i >= 1 :
        for _i in range(i):
            SpawnMonster(2, random.randint(400, 500))
def SpawnWolf(i): # inti 
    if i >= 1 :
        for _i in range(i):
            SpawnMonster(3, random.randint(400, 500))
def SpawnDragon(i): # init 
    if i >= 1 :
        for _i in range(i): # spawn time is random
            SpawnMonster(4, random.randint(30, 250))
def SpawnBossDragon(i): # int 
    if i >= 1 :
        for _i in range(i): # the range of the objecct 
            SpawnMonster(5, random.randint(30, 250))
    
def DrawTime(i): # double check that the draw time doesn't exceed a 1313
    smallfont = pygame.font.SysFont('Corbel', 35)
    Text = smallfont.render("Time: "+ str(i / 2), True, (0,0,0))
    Window.blit(Text, (0, 0))
    
def DrawGold(i): # show the gold value thu a text 
    smallfont = pygame.font.SysFont('Corbel', 35)
    Text = smallfont.render("Money: "+ str(i ), True, (0,0,0))
    Window.blit(Text, (200, 0))
def ClearCache(): # reset cache
    global MonsterTB
    global MonsterCacheTB
    global MonsterCacheTB1
    global MonsterCacheTB2
    global MonsterCacheTB3
    global exploCacheTB
    global exploCacheTB1
    global exploTB 
    
    global bulletTB 
    global bulletTypeCacheTB 
    global bulletCacheTB
    global bulletCacheTB1
    global bulletHitBoxTB
    
    MonsterTB = []
    bulletTypeCacheTB =[]
    exploCacheTB = []
    bulletCacheTB1 = []
    MonsterCacheTB = []
    MonsterCacheTB1= []
    MonsterCacheTB2= []
    MonsterCacheTB3= []
    exploCacheTB1 = []
    exploTB = []
    
    bulletTB = []
    bulletCacheTB = []
    bulletHitBoxTB= []
    
def DrawMonsters(): # this is also a coroutine 
    global MiscTB
    global _SpriteOffset
    global CannonLocationHead
    
    global MonsterTB
    global MonsterCacheTB
    global MonsterCacheTB1
    global MonsterCacheTB2
    global MonsterCacheTB3
    
    # these are to check if you actually hit the monster
    global bulletTB # direction vector 2
    global bulletCacheTB # magnitude
    global bulletHitBoxTB
    
    global MonsterHealthTB
    global MonsterHealthTB1
    global bulletCacheTB1
    
    global NumOfBulletShot
    global NumOfBulletHit
    global NumOfReload
    global _Gold
    
    for i in range(len(MonsterTB)): # the lnenght to actualyly manage the speed accordingly to and async number as speed 
        if MonsterTB[i] != 0:
            takeSomeDamage = False
            MonsterCacheTB[i] = MonsterCacheTB[i] + pygame.math.Vector2(-1, 0) * MonsterCacheTB3[i]
            for ii in range(len(bulletTB)):
                if bulletTB[ii] != True:
                    vec0 = pygame.math.Vector2(MonsterCacheTB[i][0] + 50, MonsterCacheTB[i][1] + 50)
                    vec1 =(bulletCacheTB1[ii] + bulletCacheTB[ii] * bulletTB[ii])
                    #pygame.draw.rect(Window, (0, 0, 0), [vec0[0], vec0[1], 22, 22])
                    
                    if int((vec0 - vec1).magnitude()) <= 66:
                        PS(MonsterTB[i])
                        
                        bulletTB[ii] = True
                        MonsterTB[i] = 0
                        NumOfBulletHit = NumOfBulletHit +1
                        _Gold = _Gold +1
                        AddExplosion(vec0)
                        
            # determine what image to use in a deterministic list 
            determinedImage = MiscTB[MonsterCacheTB1[i]+ _SpriteOffset]
            
            Window.blit(determinedImage, MonsterCacheTB[i])
            
            if MonsterCacheTB2[i] <= 0:
                MonsterTB[i] = 0 # died
            elif MonsterCacheTB[i][0] <= 0: # the x axis
                MonsterTB[i] = 0
                TakeDamage()
                AddExplosion(MonsterCacheTB[i]) # the monster crached into us and died.
                # we also took some damage 
                
            
def SecondsPast(intt, x): # our time real time that passed 
    if intt == 1:#2.0 seconds
        SpawnZombie(1 +x)
        SpawnBossDragon(x - 2)
    elif intt == 4:
        SpawnBat(2+ x)
        SpawnZombie(2 +x)
    elif intt == 15: # 10 seconds
        SpawnBat(2 +x)
        SpawnZombie(1 +x )
    elif intt == 44:
        SpawnBat(2 +x)
        SpawnWolf(1 +x)
    elif intt== 55:
        SpawnBat(3 +x)
        SpawnZombie(2 +x)
    elif intt == 66: 
        if random.randint(1, 2) == 1:
            SpawnDragon(x)
        SpawnBat(2 +x)
        SpawnZombie(x)
        SpawnWolf(2 +x)
    elif intt > 77 and x <= 2:
        return True
    elif intt > 100 and x >=3:
        ClearCache()
        return True
    return False

def Main():
    clock = pygame.time.Clock()
    run = True
    
    global MiscTB
    global bulletTB
    global bulletCacheTB
    global _SpriteOffset 
    
    global exploTB
    global exploCacheTB
    
    global _Blackout
    global _BulletImage
    global bulletTypeCacheTB 
    global _HealthImage
    global _Health
    global CannonLocationHead
    global CannonLocation
    
    global NumOfBulletShot
    global bulletCacheTB1
    global NumOfBulletHit
    global NumOfReload
    global _Gold
    global _HealCost
    global DoubleCastUpgrade 
    global TowerUpgrade 
    TowerPower = -2
    global ReloadOnFire
    global ShotgunUpgrade 
    _TowerPrice = 50
    
    CannonBulletLimit = 5
    CannonBullets = CannonBulletLimit 
    eCHEATCODES = True;
    # Button(Window, "text", textSize,   (color), size y, size x, pos x, pos y)
    # where we load each button accordingly 
    ReloadB = UIButton(Window, "Reload!", 22, (177, 177, 177),(0, 0, 0), 40 * 1.7, 77 ,    0,   200)
    Upgrade0B = UIButton(Window, "Doublecast - 150 gold", 22, (232, 239, 33), (0,0,0), 40 , 190 ,    400,0)
    Upgrade2B = UIButton(Window, "Shotgun - 200 gold", 22, (232, 239, 33), (0,0,0), 40 , 190 ,    400,0)
    Upgrade3B = UIButton(Window, "RELOAD_ON_FIRE - 666", 18, (0, 0, 0), (255,255,255), 40 , 190 ,    400,0)
    
    Upgrade1B = UIButton(Window, "Turret - 50 gold", 22, (232, 239, 33), (0,0,0), 40 , 190 ,    600,0)
    
    CannonLocationRotateAxis = pygame.math.Vector2(150, Window.get_height() - 100)
    TowerMuzzleLocation = pygame.math.Vector2(650, 530)
    
    TimeCache = len(MiscTB)
    RealHalfSeconds, FakeHalfSeconds, Difficulty = 0, 0, 0
    
    # this starts the entire game
    while run:
        TimeCache = TimeCache + 1;
        
        BuildBackdrop(CurrentBackdrop)
        clock.tick(44)
        if TimeCache >= 20: # to check our time and make sure it is accurate 
            if (_SpriteOffset == 0):
                _SpriteOffset = 1
            else:
                _SpriteOffset = 0
                
            n = SecondsPast(FakeHalfSeconds, Difficulty)
            if (n == True):
                FakeHalfSeconds = 1
                Difficulty = Difficulty +1
            TimeCache = 0
            # the fake half seconds 
            FakeHalfSeconds = FakeHalfSeconds +1
            RealHalfSeconds = RealHalfSeconds +1
        
        
        for event in pygame.event.get(): # our event in the game 
            
            if event.type == pygame.QUIT: # okay we quit the game 
                run = False
                pygame.quit()
                break
            elif event.type == pygame.MOUSEBUTTONDOWN: # a second mouse button 
                mousePos = pygame.mouse.get_pos()
                
                wutt0 = ReloadB.TestIfWasButton(mousePos)
                wutt1 = False
                if (DoubleCastUpgrade != 5): # we bought an upgrade
                    wutt1 = Upgrade0B.TestIfWasButton(mousePos)
                wutt2 = Upgrade1B.TestIfWasButton(mousePos)
                wutt3 = Upgrade2B.TestIfWasButton(mousePos)
                wutt4 = False
                if (ReloadOnFire == 1): # we bought another upgrade 
                    wutt4 = Upgrade3B.TestIfWasButton(mousePos)
                
                if (wutt0 != True and wutt1 != True and wutt2 != True and wutt3 != True and wutt4 != True and CannonBullets >= 1): # didn't click a button, and we have some ammo. Lets shoot
                    CannonBullets = CannonBullets - ReloadOnFire # unique instance 
                    NumOfBulletShot = NumOfBulletShot +1
                    
                    ShowBullets(CannonBullets)
                    
                    AddExplosion(CannonLocationHead) # we append an explosion at the head of the cannon to make it look realistic 
                    PS(0)
                    mouseVector = pygame.math.Vector2(int(mousePos[0]), int(mousePos[1]) )
                    
                    bulletCacheTB1.append(CannonLocationHead)# the cache of the bullet to append 
                    # we do not have a unique function for this action 
                    magnitudeScale = mouseVector - CannonLocationHead 
                    fireDirection = (magnitudeScale).normalize()
                    
                    bulletTB.append(fireDirection)
                    bulletCacheTB.append(2)
                    bulletTypeCacheTB.append(1)
                    
                    if (ShotgunUpgrade == 5): # this is where the bullet spread is added 
                        magnitudeScale = 77* ((magnitudeScale).magnitude() / 1000)
                        NumOfBulletShot = NumOfBulletShot +2 
                        
                        bulletTB.append(((mouseVector + pygame.math.Vector2(0, magnitudeScale))- CannonLocationHead).normalize())
                        bulletTypeCacheTB.append(1)
                        bulletCacheTB1.append(CannonLocationHead)
                        bulletCacheTB.append(-1)
                        bulletTB.append(((mouseVector + pygame.math.Vector2(0, -magnitudeScale))- CannonLocationHead).normalize())
                        bulletTypeCacheTB.append(1)
                        bulletCacheTB1.append(CannonLocationHead)
                        bulletCacheTB.append(-1)
                        # an extra play sound of the explosion, more realistic 
                          
                    elif (DoubleCastUpgrade == 5): # we bought double cast and shoots 2 bullets at once 
                        bulletTB.append(fireDirection)
                        bulletTypeCacheTB.append(1)
                        bulletCacheTB1.append(CannonLocationHead)
                        bulletCacheTB.append(-50)
                        PS(0)
                        NumOfBulletShot = NumOfBulletShot +1
                        
                        
                    if TowerPower ==0: # we bought a tower.
                        bulletCacheTB1.append(TowerMuzzleLocation)
                        fireDirection = (mouseVector - TowerMuzzleLocation).normalize()
                        
                        bulletTB.append(fireDirection)
                        bulletTypeCacheTB.append(23)
                        bulletCacheTB.append(2)
                        
                        NumOfBulletShot = NumOfBulletShot +1
                    elif TowerPower ==2: # a tower increase din levle 
                        fireDirection = (mouseVector - TowerMuzzleLocation).normalize()
                        bulletCacheTB1.append(TowerMuzzleLocation)
                        
                        bulletTB.append(fireDirection)
                        bulletTypeCacheTB.append(24 )
                        bulletCacheTB.append(2)
                        
                        NumOfBulletShot = NumOfBulletShot +1
                        
                elif wutt0 == True and (CannonBullets < CannonBulletLimit):# clicked the button
                    CannonBullets = CannonBulletLimit #CannonBullets +1
                    ShowBullets(CannonBullets)  # just show the bullet s
                    NumOfReload = NumOfReload +1
                elif wutt1 == True: # how many exists 
                    if _Gold >= 150:
                        _Gold = _Gold -150
                        DoubleCastUpgrade = 5
                elif wutt2 == True:
                    if _Gold >= _TowerPrice:
                        _Gold = _Gold - _TowerPrice
                        TowerPower = TowerPower +2
                        if TowerPower == 0:
                            _TowerPrice = 75
                            UIButton.ChangeText(Upgrade1B, "NOKO - 75")
                        else:
                            TowerUpgrade = 5
                elif wutt3 == True and ShotgunUpgrade != 5:
                    if _Gold >= 200:
                        _Gold = _Gold -200
                        ShotgunUpgrade = 5
                elif wutt4 == True:
                    if _Gold >= 666:
                        _Gold = _Gold -666
                        ReloadOnFire = 0
                        
                        CannonBullets = CannonBulletLimit 
                        ShowBullets(CannonBullets)
                elif (CannonBullets <= 0): # the cannon does not have enough ammunition 
                    print("Must reload!")
            if event.type == pygame.KEYDOWN and eCHEATCODES == True: # the cheat codes of the game may exists 
                if event.key== pygame.K_9:
                    _Gold = _Gold +1000
                elif event.key == pygame.K_r:
                    if CannonBullets < CannonBulletLimit:
                        CannonBullets = CannonBullets +1
                        ShowBullets(CannonBullets)
                        NumOfReload = NumOfReload +1
                    
                _Blackout = True # we are going 
                # Blackout(False)
        if _Health <= 0: # we died 
            run = False
            # died
            PS(6) # play the death soudn 
            Blackout(False)
            return RealHalfSeconds

        UIButton.Draw(Upgrade3B, ReloadOnFire + 5)    
        UIButton.Draw(Upgrade2B, ShotgunUpgrade)
        UIButton.Draw(ReloadB, CannonBullets)
        UIButton.Draw(Upgrade0B, DoubleCastUpgrade)
        UIButton.Draw(Upgrade1B, TowerUpgrade)
        if TowerPower >= 0: # we do have the tower 
            Window.blit(MiscTB[19 + _SpriteOffset + TowerPower], (600 ,530))
        
        Window.blit(MiscTB[0], CannonLocation)
        
        Window.blit(MiscTB[_HealthImage], (0, 300))
        Window.blit(MiscTB[_BulletImage], (0, 360))
        
        DrawTime((RealHalfSeconds))
        DrawGold(_Gold)
        
        DrawMonsters()
        DrawBullet()
        DrawExplosion()
        
        pygame.display.update()
def BleckOut(): # second bleck
    s = pygame.Surface((2000,2000))
    s.set_alpha(256)
    a, remoteInt = 1,0
    color = (0,0,0)
    s.fill(color)
    Window.blit(s, (0,0))

# Button(Window, "text", textSize,   (color), size y, size x, pos x, pos y)
PlayAgainB = UIButton(Window, "Play Again", 44, (177, 177, 177), (0,0,0), 100, 200 ,    300, 400)
            
if __name__ == "__main__": # the name of the thing 
    BleckOut()
    
    goalText = "WelCome plaYer. YoU're goAl Is to live as long as possible so GooD Luck.".lower()
    currentText = ""
    smallfont = pygame.font.SysFont('Corbel', 30)
    
    pygame.display.update()
    remoteInt = 0
    while len(currentText) < len(goalText):
        BleckOut()
        currentText = currentText + goalText[remoteInt]
        wait(0.09) # just inne
        
        Text0 = smallfont.render(currentText, True, (255,255,255))
        Window.blit(Text0, (0, 0))
        pygame.display.update()
        
        remoteInt = remoteInt +1
        
    BuildBackdrop(0) # the second backdrop 
    
    if (True):
        wait(2);
        
        while (True):
            n = (Main()) / 2
            smallfont = pygame.font.SysFont('Corbel', 100)
            Text0 = smallfont.render("YOU DIED", True, (255,255,255))
            
            smallfont = pygame.font.SysFont('Corbel', 35)
            Text1 = smallfont.render("Seconds lasted: " + str(n), True, (255,255,255))
            
            smallfont = pygame.font.SysFont('Corbel', 35)
            Text2 = smallfont.render("Bullets Fired: " + str(NumOfBulletShot), True, (255,255,255))
            
            smallfont = pygame.font.SysFont('Corbel', 35)
            Text3 = smallfont.render("Bullets Landed: " + str(NumOfBulletHit), True, (255,255,255))
            
            smallfont = pygame.font.SysFont('Corbel', 35)
            huh = 0
            if NumOfBulletHit >= 1: # our house 
                huh = math.floor((NumOfBulletHit / NumOfBulletShot) * 100)
            NumOfBulletShot, NumOfBulletHit,NumOfReload = 0, 0, 0
            Text4 = smallfont.render("Accuracy: " + str(huh) +"%", True, (255,255,255))
            
            smallfont = pygame.font.SysFont('Corbel', 35)
            Text5 = smallfont.render("Gold Earned: " + str(_Gold) +"", True, (255,255,255))
            
            Window.blit(Text0, (0, 0))
            Window.blit(Text1, (0, 100))
            
            Window.blit(Text4, (0, 135))
            Window.blit(Text3, (0, 135 + 35))
            Window.blit(Text2, (0, 135 + 35 +35))
            Window.blit(Text5, (0, 135 + 35 +70))
            
            pygame.display.update() # reset the data 
            ClearCache()
            _Gold =5
            DoubleCastUpgrade, TowerUpgrade, ShotgunUpgrade = 2, 2, 2
            ReloadOnFire = 1 # reload on fire of the bullet 
            _Health = 3
            ShowBullets(5)
            ShowHealth(_Health)
            wait(1) # the wait statement doesn't do anything 
            run = True
            clock = pygame.time.Clock()
            
            UIButton.Draw(PlayAgainB, 2)
            pygame.display.update()
            while run:
                clock.tick(22) # a tick to make sure we eventually click the button 
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mousePos = pygame.mouse.get_pos()
                        n = PlayAgainB.TestIfWasButton(mousePos)
                        if n == True:
                            run = False
                    elif event.type == pygame.QUIT:
                        run = False;
                        pygame.quit()

