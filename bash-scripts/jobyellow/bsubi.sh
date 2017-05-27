#!/usr/bin/env bash
bsub -Is -W 01:00 -q small -P STDD0004 -R "span[ptile=1]" -n 4 bash
