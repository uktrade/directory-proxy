# directory-proxy

[![code-climate-image]][code-climate]
[![circle-ci-image]][circle-ci]
[![codecov-image]][codecov]

Proxy for rejecting non-whitelisted IP addresses.

---

Proxy sets a [Hawk](https://github.com/hueniverse/hawk) signature header that the upstream service can check, rejecting requests that do not have a valid signature.

## Installation

`pip install directory-proxy`

## Usage

Proxy can be ran as a standalone service or as a WSGI worker running alongside the upstream service.

### WSGI worker

The proxy can be run on the same box as the upstream service. Install proxy on the same box as the upstream service then run the WSGI worker:

```sh
DJANGO_SETTINGS_MODULE=directory_proxy.conf.settings \
gunicorn directory_proxy.conf.wsgi --bind 0.0.0.0:$UPSTREAM_PORT
```

### Standalone service

If you're unable to run the WSGI worker on the same box as the upstream service then the proxy can be ran as a standlone service.


### Configuration

Set the following environment variables to configure the proxy:

| Environment variable                  | Details                                 |
| ------------------------------------- | --------------------------------------- |
| IP_RESTRICTOR_ALLOWED_ADMIN_IPS       | Allow IP addresses. Command delimited   |
| IP_RESTRICTOR_ALLOWED_ADMIN_IP_RANGES | Allow IP ranges. Command delimited      |
| IP_RESTRICTOR_SKIP_CHECK_ENABLED      | Skip IP check. Check cookie instead     |
| IP_RESTRICTOR_SKIP_CHECK_SECRET       | Shared secret for checking cookie       |
| UPSTREAM_DOMAIN                       | Domain of upstream service              |
| UPSTREAM_SIGNATURE_SECRET             | Hawk shared secret for upstream request |
| UPSTREAM_SIGNATURE_SENDER_ID          | Hawk sender ID for upstream request     |


## Local installation

    $ git clone https://github.com/uktrade/directory-proxy
    $ cd directory-proxy

## Debugging

### Setup debug environment

    $ make debug

### Run debug webserver

    $ make debug_webserver

### Run debug tests

    $ make debug_test


[code-climate-image]: https://codeclimate.com/github/uktrade/directory-proxy/badges/issue_count.svg
[code-climate]: https://codeclimate.com/github/uktrade/directory-proxy

[circle-ci-image]: https://circleci.com/gh/uktrade/directory-proxy/tree/master.svg?style=svg
[circle-ci]: https://circleci.com/gh/uktrade/directory-proxy/tree/master

[codecov-image]: https://codecov.io/gh/uktrade/directory-proxy/branch/master/graph/badge.svg
[codecov]: https://codecov.io/gh/uktrade/directory-proxy
