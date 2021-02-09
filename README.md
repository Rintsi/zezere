# Zezere

[Zezere](https://en.wikipedia.org/wiki/Z%C3%AAzere_River) is a provisioning server for Fedora IoT.
It can be used for deploying Fedora IoT to devices without needing a physical console.

It is still under development.

## Getting Started

### Running with Docker

The easiest way to run Zezere is to run the official container and authenticate
with OpenID Connect:

```
$ docker run --detach --rm --name zezere \
    -e OIDC_RP_CLIENT_ID=<client id> \
    -e OIDC_RP_CLIENT_SECRET=<client secret> \
    -e OIDC_OP_AUTHORIZATION_ENDPOINT=<authorization endpoint> \
    -e OIDC_OP_TOKEN_ENDPOINT=<token endpoint> \
    -e OIDC_OP_USER_ENDPOINT=<userinfo endpoint> \
    -e OIDC_OP_JWKS_ENDPOINT=<jwks endpoint> \
    -e AUTH_METHOD=oidc \
    -e SECRET_KEY=localtest \
    -e ALLOWED_HOSTS=localhost \
    -p 8080:8080 \
    -t quay.io/fedora-iot/zezere:latest
```

The default signing algorithm is `RS256` but it can also be controlled with the
environment variable `OIDC_OP_SIGN_ALGO`

### Running with Python

If you're using any Python virtual environment you might want to setup that
first. With conda it would look something like this:

```
$ conda create --name zezere && conda activate zezere
```

We also want to run Python 3 (at the time of writing it was 3.9.1):

```
$ conda install python=3
```

Before you can install the python requirements you need to have Apache httpd
installed. Please follow instructions from
[mod-wsgi project documentation](https://pypi.org/project/mod-wsgi/)

After the prequisites have been met we can install required packages:

```
$ pip install .
```

Before using the `zezere-manage` tool, database and models needs to be migrated
and a configuration needs to be created.

Synchronize the database state with the current set of models and migrations:

```
$ python manage.py migrate
```

Default configuration can be used as a base:

```
$ cp zezere/default.conf ./zezere.conf
```

Authentication method and secret key needs to be set in order to satisfy the
tool. Also, make sure that the allowed_hosts is what you want.

```
allowed_hosts = localhost
secret_key = very-secret
auth_method = local
```

Now we can create a superuser:

```
$ zezere-manage createsuperuser --username admin --email user@domain.tld
```

After a password has been set, we are ready to run Zezere:

```
./app.sh
```

Use the admin credentials we created to login to localhost:8080

## Ignition

[Setting up a Device with Zezere :: Fedora Docs](https://docs.fedoraproject.org/en-US/iot/ignition/)

When you want to provision a device against your local Zezere like in the
documentation the easiest way is to use the kernel command line. Before a better
documentation is written, please refer to this
[commit](https://github.com/fedora-iot/zezere/commit/f66c0b6bcbf99c1fb57f96ed0413faf3147aaab1)

The easiest way to test this with a Fedora IoT device you might have in the same
network is to
[make a temporary change to the GRUB 2 menu](https://docs.fedoraproject.org/en-US/fedora/rawhide/system-administrators-guide/kernel-module-driver-configuration/Working_with_the_GRUB_2_Boot_Loader/#sec-Making_Temporary_Changes_to_a_GRUB_2_Menu)

## Contributing

In order to start contributing to the project, please visit
[Contribute to Fedora IoT Edition :: Fedora Docs](https://docs.fedoraproject.org/en-US/iot/contributing/)
