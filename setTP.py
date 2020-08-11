from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = 273

y = 144

z=25

    mc.player.setTilePos(x,y,z)
    time.sieep(0.5)
    mc.postToChat("我正在看者你X"+str(x)+"Y:"+str(y)+"Z"+str(z))
    
            