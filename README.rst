
This repo aims to provide feeds of commonly needed data to define, and interact
with various AWS services. Too much of AWS's infrastructure details are only
defined as various tables in documentation and this project exists to collate
these sources, amongst others sources to expose values that inevitably end up
being used in code that defines various pieces of infrastructure.

You can either clone or run this locally, or access the feeds from Github
itself.

Building and using it locally
-----------------------------
:: 
    pip install git+ssh://git@github.com/tigertoes/aws-region-meta

Licence
-------
Apache 2. Please see the LICENSE file included with the source code.

Data Sources
------------
- `AWS Global Infrastructure  <https://aws.amazon.com/about-aws/global-infrastructure/>`_
- `AWS Regions and Endpoints <https://docs.aws.amazon.com/general/latest/gr/rande.html>`_
- `Enable Access Logs for Your Classic Load Balancer <https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-access-logs.html>`_
