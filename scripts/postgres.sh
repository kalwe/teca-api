#!/bin/sh

renew_pgdata() {
  path_dir = "$PWD/docker-compose/postgres/pgdata"

  if -d $path_dir
    rm -rf $path_folder
    exit 0

  mkdir $path_dir
}
