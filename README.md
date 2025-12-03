# Github-user-base-osint

Script that uses an IDOR on avatars.githubusercontent.com to retrieve user profile pics

# Summary

* How it was easy to retrieve the images directly by using the IDOR

# How it was easy to retrieve the images directly by using the IDOR

Using the  verbose command curl on:
```
https://avatars.githubusercontent.com/u/17337009?v=4
```

I had the following output:
```
curl -vv https://avatars.githubusercontent.com/u/17337009?v=4

...SNIP...
19:05:47.077041 [0-0] < cache-control: max-age=300
19:05:47.077130 [0-0] * [HTTP/2] [1] header: cache-control: max-age=300
19:05:47.077221 [0-0] < content-security-policy: default-src 'none'
19:05:47.077308 [0-0] * [HTTP/2] [1] header: content-security-policy: default-src 'none'
19:05:47.077398 [0-0] < content-type: image/jpeg
19:05:47.077484 [0-0] * [HTTP/2] [1] header: content-type: image/jpeg <-- this is what i want

```

From there using request I would catch that header and enumerating the possible file format.
