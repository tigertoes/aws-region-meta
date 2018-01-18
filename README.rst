AWS Meta
========
This repo aims to provide feeds of commonly needed data to define, and interact
with various AWS services. Too much of AWS's infrastructure details are only
defined as various tables in documentation and this project exists to collate
these sources, amongst others sources to expose values that inevitably end up
being used in code that defines various pieces of infrastructure.

You can either clone or run this locally, or access the feeds from Github
itself.

Building and using it locally
-----------------------------
Installation:: 

    pip install git+ssh://git@github.com/tigertoes/aws-region-meta

Update the data::

    make version

Serve it locally::

    cd api && python -m SimpleHTTPServer

API
---
This is a read-only API so when served via HTTP, everything will be GET calls,
however your HTTP server of choice should also implement HEAD. Cache lifetimes
for all except `/versions.json` and `latest/` may be indefinite with
immutability.

/versions.json
~~~~~~~~~~~~~~
List all available API versions. Different versions of the feed may have
differing data structure as well as data content.

/$version/regions.json
~~~~~~~~~~~~~~~~~~~~~~
Contains regional meta-data. All keys in the parent are region names. 

/$version/regions.schema.json
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
JSON Schema (automatically generated) for the regional data.

Example Usage
-------------
Get the ELB hosted zone for a given region::
    curl -s https://tigertoes.github.io/aws-region-meta/api/latest/regions.json | jq '.["ap-southeast-1"]["elb"]["elb_hosted_zone_id"]'

Get total count of availability zones for `eu-west-1`::
    curl -s https://tigertoes.github.io/aws-region-meta/api/latest/regions.json | jq '.["eu-west-1"]["availability_zones"] | length'

Licence
-------
Apache 2. Please see the LICENSE file included with the source code.

Data Sources
------------
- `AWS Global Infrastructure  <https://aws.amazon.com/about-aws/global-infrastructure/>`_
- `AWS Regions and Endpoints <https://docs.aws.amazon.com/general/latest/gr/rande.html>`_
- `Enable Access Logs for Your Classic Load Balancer <https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-access-logs.html>`_
