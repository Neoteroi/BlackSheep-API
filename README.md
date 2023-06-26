# BlackSheep-API Cookiecutter template
This repository contains a [Cookiecutter](https://github.com/cookiecutter/cookiecutter)
template to boostrap a new BlackSheep application to build a Web API.

## Using the BlackSheep CLI

```bash
pip install blacksheep-cli
```

```bash
blacksheep create api

🚀 Project name example
🤖 Use controllers? Yes
📜 Use OpenAPI Documentation? Yes
🔧 App settings format (Use arrow keys)
 » YAML
   TOML
   JSON
   INI
   None
```

## Using Cookiecutter

```bash
pip install cookiecutter

cookiecutter https://github.com/Neoteroi/BlackSheep-API
```


## Documentation
The documentation of the [framework can be read here](https://www.neoteroi.dev/blacksheep/).

## Getting started

```bash
pip install -r requirements

uvicorn main:app --port 44777 --reload --log-level info
```

Navigate to [http://localhost:44777](http://localhost:44777).

## Features

- Basic folder structure
- Strategy to read configuration from YAML, TOML, JSON, INI files, and environmental
  variables; using [`essentials-configuration`](https://github.com/Neoteroi/essentials-configuration)
- Handling of [dependency injection](https://www.neoteroi.dev/blacksheep/dependency-injection/), using [`rodi`](https://github.com/RobertoPrevato/rodi)
- Configuration of exceptions handlers
- Handling of [application start and stop events](https://www.neoteroi.dev/blacksheep/application/)
- Strategy to handle [authentication](https://www.neoteroi.dev/blacksheep/authentication/) and [authorization](https://www.neoteroi.dev/blacksheep/authorization/), using [`guardpost`](https://github.com/RobertoPrevato/GuardPost)

## For more information on rodi

For more information and documentation about `rodi`, see:

- [dependency injection in BlackSheep](https://www.neoteroi.dev/blacksheep/dependency-injection/)
- [rodi](https://github.com/RobertoPrevato/rodi)
- [rodi wiki](https://github.com/RobertoPrevato/rodi/wiki)
- [rodi wiki examples](https://github.com/RobertoPrevato/rodi/wiki/Examples)
