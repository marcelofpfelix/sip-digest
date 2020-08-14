import hashlib

nonce = 'Xck7cV3JOkWQIcDRg6dcUj0R7LjCB77A'
realm = 'phone.plivo.com'
password = 'password'
username    =   str("marcelofpfelix")
requesturi  =   str("sip:phone.plivo.com")

# Digest realm="phone.plivo.com", nonce="Xck7cV3JOkWQIcDRg6dcUj0R7LjCB77A", username="marcelofpfelix",
# uri="sip:phone.plivo.com", response="4339495f0502e3dceed0357db619afec"

print("  # username: " + username)
print("  # nonce: " + nonce)
print("  # realm: " + realm)
print("  # password: " + password + "\n")

HA1str = username + ":" + realm + ":" + password
HA1enc = (hashlib.md5(HA1str.encode()).hexdigest())
print ("  # HA1 String: " + HA1str)
print ("  # HA1 Encrypted: " + HA1enc)
HA2str = "REGISTER:" + requesturi
HA2enc = (hashlib.md5(HA2str.encode()).hexdigest())

print ("  # HA2 String: " + HA2str)
print ("  # HA2 Encrypted: " + HA2enc)

responsestr = HA1enc + ":" + nonce + ":" + HA2enc
print("  # Response String: " + responsestr)
responseenc = str((hashlib.md5(responsestr.encode()).hexdigest()))
print("\nResponse Encrypted: " + responseenc + "\n")
