from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = 10
y = 11
z = 12
gift = mc.getBlock(x, y, z)
diamond = 57
sapling = 6

if diamond == 1:
    mc.postToChat("thanks")
elif sapling == 1:
    mc.postToChat("thanks")

else:
    mc.postToChat("bring a gift to" + str(x) + "," + str(y) + "," + str(z))
    
