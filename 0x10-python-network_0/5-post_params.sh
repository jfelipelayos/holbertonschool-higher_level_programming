#!/bin/bash
# takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -sd "$1" -X POST "email=hr@holbertonschool.com&subject=I will always be here for PLD"
