from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y,z = mc.player.getPos()

def plantTree(x,y,z):
    mc.setBlocks(x+1,y+5,z+1,x-1,y+3,z-1,18)
    mc.setBlocks(x,y,z,x,y+4,z,17)
for j in range(0,5):
    for i in range(0,5):
        plantTree(x+i,y,z+j)