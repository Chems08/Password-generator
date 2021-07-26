import random
a = int(input("Saisissez le nombre de caracteres dans le mot de passe : "))
klog = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@&!-#"
print("Le mot de passe est : ")
print("".join(random.sample(klog, a)))