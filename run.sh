#!/bin/bash
# this can also be called via `make devserver` (!)
pelican content -s pelicanconf.py && pelican --listen
