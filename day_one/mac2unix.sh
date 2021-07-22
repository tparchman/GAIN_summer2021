#!/usr/bin/bash

cat $1 | tr '\r' '\n' > u_$1
