# sip-digest

Create a responde for SIP Digest access authentication, applying a MD5 cryptographic hashing with usage of nonce values. Useful to check the password we are expecting is the encrypted value matches the trace captures.

How to run:

```console
felix@bandonga:~$ python sip_digest.py
  # username: marcelofpfelix
  # nonce: Xck7cV3JOkWQIcDRg6dcUj0R7LjCB77A
  # realm: phone.plivo.com
  # password: password

  # HA1 String: marcelofpfelix:phone.plivo.com:password
  # HA1 Encrypted: 6a8718c9afa458401b91f606376abd52
  # HA2 String: REGISTER:sip:phone.plivo.com
  # HA2 Encrypted: 8022a1d8cb9d611365e28323f3184f4c
  # Response String: 6a8718c9afa458401b91f606376abd52:Xck7cV3JOkWQIcDRg6dcUj0R7LjCB77A:8022a1d8cb9d611365e28323f3184f4c

Response Encrypted: 4339495f0502e3dceed0357db619afec
```

you should compare the `Response Encrypted` with the `response` in the Authorization Header, from the SIP REGISTER message.

```
Authorization:  Digest realm="phone.plivo.com", nonce="Xck7cV3JOkWQIcDRg6dcUj0R7LjCB77A", username="marcelofpfelix",  uri="sip:phone.plivo.com", response="4339495f0502e3dceed0357db619afec"  
```

* follwing the article https://nickvsnetworking.com/reverse-md5-on-sip-auth/
