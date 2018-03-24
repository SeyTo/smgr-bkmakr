#!/bin/zsh
# Creates a tar archive. Files that are listed in 
# .gitignore will also be ignored while making this tar.
#
# ##################################################### #
# TODO
# 1. detect multimedia files and use low compression
#

function make_tar() {
  # $1 = name
  # make tar archive
  tar -cvz -f $1.bkup.tar.gz -X ignore ./*
}


# TODO does not properly detect file from .gitignore
function create_ignore() {
  # collect all ignorer files
  touch ignore
  echo > ignore

  for i in `find -type f -name .gitignore`
  do
    loc=`echo $i | grep -Po ".*\/"`
    while read -r line
    do # append all path into it
      new="$loc$line"
      echo $new
      if [ -f $new ] | [ -d $new ]; then
        echo ok
        echo $loc$line  >> ignore
      fi
    done < $i
  done
  # echo ignore >> ignore
}


# get current directory name
cd $1
NAME=${PWD##*/}

# check if dir is not empty
if find $1 -maxdepth 0 -empty | read v; then
  echo "Empty dir. Nothing to backup";
  exit
fi

create_ignore
# make_tar $NAME
# rm ignore

# todo: remove leading slash for $line
# make a root .gitignore file at the dir root which contain list of all ignored file with full path
# check for existence of .gitignore recursively
