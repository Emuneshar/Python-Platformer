import random, time

fish = {
  "Sea bass": 1,
  "blobfish": 2,
  "trout": 1,
  "hammerhead Shark": 100,
  "goldfish": 2,
  "lion fish": 40,
  "catfish": 10, 
  "megalodon": 4000000000,
  "salmon": 5
}

score = 0

while True:
  print(f"\n Your score is {score} points")
  fishList = list(fish)
  catch = random.choice(fishList)

  input("Press enter to cast your line!\n")
  print("bloop!")

  waitTime = random.uniform(1,5)
  time.sleep(waitTime)

  timeToCatch = 1

  startTime = time.time()
  print("You got a bite!\n Press enter to reel it in!")
  input()
  endTime = time.time()

  reactionTime = 