#!/bin/bash

miner_stop() {
  if [ "$(whoami)" != "root" ]; then
    echo "Script must be run as root"
    exit 1
  fi

  # Stop the HiveOS miner
  /hive/bin/miner stop
}

miner_stop