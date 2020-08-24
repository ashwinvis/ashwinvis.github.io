#!/bin/env bash
set -e
nb=$1
name=${1%.*}
filetype=rst
filestatus=published

jupyter-nbconvert --to $filetype --output-dir=converted $nb

if [[ $filetype == "markdown" ]]; then
  conv=converted/${name}.md
  sed -i '1,10{s/^-\ //}' $conv
  sed -i '/^Title/i ---' $conv
  sed -i "/^Date/a Status:\ ${filestatus}" $conv
  sed -i '/^Summary/a ---' $conv
  head $conv
else
  conv=converted/${name}.rst
  sed -i '1,10{s/^-\ */:/}' $conv
  sed -i "/^:Date/a :Status:\ ${filestatus}" $conv
  # image path
  sed -i "/^..\ image/ s/${name}_files/images/" $conv
  # title level inconsistent: ^^^^
  sed -i '/^\^*/ s/\^/\~/g' $conv
  if [[ -d converted/${name}_files ]]; then
    mv -f converted/${name}_files/* images/
    rmdir converted/${name}_files/
  fi
  head $conv
  grep '^..\ image' $conv
fi
