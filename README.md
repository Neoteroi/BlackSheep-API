# BlackSheep empty project template
Basic project template for BlackSheep web framework.

## Getting started
1. Clone the repository

```bash
$ git clone https://github.com/RobertoPrevato/BlackSheepEmptyProject.git yourproject
```

2. Navigate to its folder

3. Create a Python virtual environment and install requirements.txt

4. Run the application
```bash
$ uvicorn server:app --port 44777 --reload --log-level info
```

## Features
* Basic folder structure
* Strategy to read configuration from YAML, JSON, INI files, and environmental variables; using [`roconfiguration`](https://github.com/RobertoPrevato/roconfiguration)
* Handling of dependency injection, using [`rodi`](https://github.com/RobertoPrevato/rodi)
* Configuration of exceptions handlers
* Handling of application start and stop events
* Strategy to handle authentication and authorization, using [`guardpost`](https://github.com/RobertoPrevato/GuardPost)

## For more information on rodi
For more information and documentation about `rodi`, see its Wiki and examples:

* [rodi](https://github.com/RobertoPrevato/rodi)
* [rodi wiki](https://github.com/RobertoPrevato/rodi/wiki)
* [rodi wiki examples](https://github.com/RobertoPrevato/rodi/wiki/Examples)

## Note about ASGI servers
This project template includes references to [`uvicorn`](uvicorn.org). However, it is possible to use other implementations of ASGI HTTP Servers.

For example, to use the same application with [`Hypercorn`](https://pypi.org/project/Hypercorn/):

```bash
$ pip install Hypercorn

$ hypercorn server:app
```
