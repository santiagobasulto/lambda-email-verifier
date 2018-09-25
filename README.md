## Fake Email Checker

This code creates a simple [AWS Lambda](https://aws.amazon.com/lambda/) function (using [Zappa](https://github.com/Miserlou/Zappa)) which exposes a one-endpoint API to check for fake (throwaway) email addresses.

Throwaway emails have domains like `"mailinator.com"`, `"mvrht.net"`, etc.

The list of all the domains included is in this [gist](https://gist.github.com/santiagobasulto/61768c38dd6a64aa9c449592738cdedb) (originally forked from [this repo](https://github.com/MattKetmo/EmailChecker/blob/master/res/throwaway_domains.txt)).

## Usage:

**Basic Usage**

```bash
curl -X POST -d '{"email": "santiago@rmotr.com"}' -H "Content-Type: application/json" <URL>
```

**Validate the Email Address**<br>
_(Email validation is turned off by default)_
```bash
curl -X POST -d '{"email": "santiago@rmotr.com", "validate_email": true}' -H "Content-Type: application/json" <URL>
```

**Send a list of extra invalid domains**
```bash
curl -X POST -d '{"email": "santiago@rmotr.com", "extra_invalid_domains": ["rmotr.com"]}' -H "Content-Type: application/json" <URL>
```

## Install instructions

To deploy this lambda in your own AWS account you need to use Zappa.

**0. AWS Access and Secret keys (prerequisite)**

Before you start installing this, please make sure that you have the correct [configuration](boto3.readthedocs.io/en/latest/guide/configuration.html) for boto3 (that includes AWS Access and Secret keys).

**1. Create a virtual environment and install dependencies**

```bash
$ mkvirtualenv my-super-virtualenv -p $(which python3)
$ pip install -r requirements.txt
```

**2. Review Zappa settings**

I've included the minimum configuration for Zappa (in `zappa_settings.json`). You can check the [official Zappa documentation](https://github.com/Miserlou/Zappa) for more info.
You can also chose to name your env in a different way (I've left `dev` as default).

**3. Deploy your app**

```bash
$ zappa deploy dev
```

## Updating the domains list

This script turns the original .txt file in a big Python [set](https://docs.python.org/3/library/stdtypes.html#set) (an efficient O(1) collection) which is then imported as a regular python module. If you need to update the static list of domains, you can use the script in `code_utils.py` which reads a text file line by line and creates a valid Python module with only one variable (by default `INVALID_DOMAIN_SETS`) containing a set with all the domain names.

```bash
$ wget https://raw.githubusercontent.com/MattKetmo/EmailChecker/master/res/throwaway_domains.txt
$ python code_utils.py
```
