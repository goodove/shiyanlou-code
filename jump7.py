import random
WORDS=("python","jumble","easy","difficult","answer","continue","phone","position","game")
print("欢迎参加猜单词游戏,把字母组合成一个正确的单词")
iscontinue="y"
while iscontinue=="y" or iscontinue=="Y":
  word=random.choice(WORDS)
  correct=word
  jumble=""
  while word:
    position=random.randrange(len(word))
    jumble+=word[position]
    word=word[:position]+word[(position+1):]
  print("乱序后单词：",jumble)
  guess=input("\n请你猜:")
  while guess !=correct and guess !="":
    print("对不起不正确")
    guess=input("继续猜：")
  if guess==correct:
    print("真棒，你猜对了!\n")
  iscontinue = input("\n\n是否继续（Y/N）:")
