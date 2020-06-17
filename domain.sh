#!/bin/bash
old="ashwinvis.github.io"
new="ashwinvis.github.io"
rg -uu -l $old | xargs sed "s|$old|$new|g" -i
git diff
