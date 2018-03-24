#!/bin/zsh
function test() {
  return 1
}

if find $1 -maxdepth 0 -empty | read v; then 
  echo "Empty dir"; 
else
  echo "Not empty"
fi
