# DrFujiBot

DrFujiBot is a client-side Twitch chat bot that provides a command-based interface to Pokemon data. This repository represents the re-write of the original server-side version of the bot ([OpenFuji](https://github.com/EverOddish/OpenFuji)). The code and data are significantly more readable, extendable, and easier to work on. The intention of the re-write was to eliminate the need for a server to host the bot, and to make rapid updates much easier to implement.

The primary goal of DrFujiBot is to be as easy to install and use as possible. Very little configuration is required out-of-the-box, but customization is possible for advanced users.

# Components

## DrFujiBot Django

The interface and database on which DrFujiBot relies are managed by Django (a Python web framework). Django provides the ability to manage all data and custom commands and settings, and to handle any command requests in a dynamic fashion. The Django instance runs locally on the user's computer, and is never exposed to the wider internet. The user may control the bot settings via their favourite web browser by browsing to the local Django administration web site. The IRC component (described in the next section) will also query the Django instance for command output.

Django itself requires a web server to host its implementation. Apache was chosen as the web server to host the Django instance, as it can run as a Windows service in the background of the host system.

## DrFujiBot IRC

This component is a simple IRC chat bot written in Python. It somewhat resembles a very stripped-down version of the original OpenFuji. The IRC component acts as an intermediary between Twitch chat and the local Django instance. It will do basic command parsing, determine permissions, and forward requests to Django for command output. The component runs as a Windows service in the background of the host system.

## DrFujiBot Installer

This component contains NSIS (Nullsoft Scriptable Install System) scripts that package up Python, Django, Apache, and DrFujiBot itself into a Windows installer. This results in DrFujiBot being installed as a regular Windows program on the user's system, which can later be uninstalled if desired.

## Westwood

DrFujiBot relies on the [Westwood](https://github.com/EverOddish/Westwood) data set. Westwood defines Pokemon data in a human-readable format, then generates database models and data that can be used by projects such as DrFujiBot. See the Westwood project description for more information.

# Contributing

If you would like to contribute, contact @EverOddish on [Twitter](https://twitter.com/EverOddish)

# Disclaimer

All Pokemon data is owned by The Pokemon Company International. This project should not be used for commercial purposes.