#!/bin/bash
old="ashwinvis.github.io"
new="fluid.quest"
rg -uu -l $old | xargs sed "s|$old|$new|g" -i
git diff
