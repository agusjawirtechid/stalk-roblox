import requests

username = input("masukan username roblox: ")
url = f"https://kyyokatsurestapi.my.id/stalk/roblox?username={username}"
data = requests.get(url, headers={"User-Agent": "curl"}).json()

result = data.get("result")
account = result.get("account")
banned = account.get('isBanned')
verivikasi = account.get("hasVerifiedBadge")

print(f'username: {account.get("username")}')
print(f"tampilan nama: {account.get("displayName")}")
print(f"deskripsi: {account.get('description')}")
print(f'dibuat: {account.get('created')}')
if banned == True:
  print('banned: iya')
else:
  print("banned: tidak")
if verivikasi == True:
  print('centang biru: iya')
else:
  print("centang biru: tidak")
