# backups

make backup:

1) pack:
$ cd && mkdir backup
$ tar cvf backup/<NAME>.tar <NAME>
dirs: books razn math foto + <private> (with gpg -c)
2) upload to cloud

roll backup:
1) download from cloud
2) unpack (with gpg -d)
