Fridge
======

Ftp bridge over S3, controllable via RestFul api
It's under MIT license.

*Not yet functional*


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
Enjoy!