# Github-user-base-osint

Script that uses an IDOR on avatars.githubusercontent.com to retrieve user profile pics

# Summary

* Introduction
* How to run
* How to run using range script

# How to run
Just run the download script as the following:

```
python3 download.py '/download/directory' 500
```

With this statement, the script will download the first 500 users on github.

# How to run using range script

```
 python3 download-range.py '/download/directory' 1000 2000
```

The instruction will download all the users between range 1000 and 2000
