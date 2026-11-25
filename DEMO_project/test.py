#update 2 แก้ไข ให้ shell อ่านง่ายขึ้นทำให้เล่นเกมมได้ง่ายขึ้น
import random

print("START GAME!!!")

def player():
	critical_dmg = 1
	score = 0
	attack = 10
	ply_data = {'name':input("your name :") , 'attack':attack , 'hp':100, 'critical':critical_dmg,'score':score}
	return ply_data
	print(ply_data)


def monster():
	name = ['oogba' , 'royal' , 'oahit']
	ran_name_mons = random.choice(name)
	mons_data = {'name':ran_name_mons,'attack':10 ,'hp':100 }
	print(mons_data)
	return mons_data

plystatus = player()
while True:
	plystatus["hp"] = 100
	print("your opponent")
	mons_rt = monster()
	print("_______________________")
	print("START TURN!!!")
	
	mons_rt["hp"] = 100
	while plystatus["hp"] >0 and mons_rt["hp"] >0:
	
		
		print("attack Press : 1")
		try:
			attack = int(input("number?"))
		except:
			print("try agian")
			continue
		#ATTACK
		if attack == 1:
			mons_rt["hp"] -= plystatus["attack"]
			plystatus["hp"] -= mons_rt["attack"]
		if attack ==1:
			percen = random.randint(1,3)
			if percen == 3:
				mons_rt["hp"] -= plystatus["critical"]
				print("you hit critical damage :", plystatus["critical"])
			print("___________________")
			print("player status:","player HP :",plystatus["hp"],"damage",plystatus["attack"])
			print("monster status","monster HP :",mons_rt["hp"],"monster Damage",mons_rt["attack"])
			print("___________________")
			#check $DRAW win loss
		if plystatus["hp"] <=0 and mons_rt["hp"] <=0:
			print("DRAW")
		elif mons_rt["hp"] <=0:
			print("your win")
			plystatus["score"] += 1
			print(plystatus)
		elif plystatus["hp"] <=0:
			print("your LOss")
			print(plystatus)
		
	print("try agian")
	try:
		chossen1 = int(input("1 to re try"))
	except:
		print("write agian")
		continue
	if chossen1 != 1:
		break
	
