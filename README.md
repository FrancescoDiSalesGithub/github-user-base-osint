# Github-user-base-osint

Script that uses an IDOR on avatars.githubusercontent.com to retrieve user profile pics

# Summary

* Introduction
* How to run
* How to run using range script

# Introduction

This script uses an idor to download all the user pics from github. If you want to know the making of of this program check:

* making-of/binary
* making-of/network

The first branch is about an old implementation by downloading the files without extensions and guessing it reading the file header.
The second instead is more simple by extracting the header Content-Type from the response,

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
