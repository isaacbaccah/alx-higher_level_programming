#!/bin/bash
# Displays the size of the body response
curl -s "$1" | wc -c
