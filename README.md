Fridge
======

*Not yet functional*

Fridge is a ftp bridge over S3, and is controllable via a RestFul api.
It uses [Pure ftd](http://www.pureftpd.org/project/pure-ftpd) as ftp backend and [S3fs](http://code.google.com/p/s3fs/wiki/FuseOverAmazon)
to mount s3 as a filesystem partition.

Before you ask, it's under MIT license.


## Installation

Fridge depends on [fabric](http://docs.fabfile.org/en/latest/) and [fabtools](https://github.com/ronnix/fabtools), a deployment utils lib, and a set of plugins for `fabric`.
In order to install the, ensure you've got [pip](http://pypi.python.org/pypi/pip) installed, and:

```bash
$ pip install -r requirements.txt
```

Then

```bash
$ git clone git@github.com:oleiade/Fridge
```

Now, it's time to deploy it on your hosts. Fridge comes with a suite of fabric rules to make your life easier: at any time, while in Fridge clone repo dir, use `fab -l` to list all possible actions.
So, let's bootstrap fridge on `yourhostname` with:

```bash
$ fab bootstrap --set hosts='yourhostname' --set aws_access_key='myawsaccesskey' --set aws_secret_key='myawssecretkey'
```

It should not take long to install, though I recommend a warm cofee and [This](http://open.spotify.com/track/3zGB8rE7Guy8R1FJ1csX95) to wait in peace.

Hope you enjoy it!

**P.S** : feedback, features request are of course welcome
