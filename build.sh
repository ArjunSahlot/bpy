#!/bin/bash

download_link=https://github.com/ArjunSahlot/fake_bpy/archive/main.zip
temporary_dir=$(mktemp -d) \
&& curl -LO $download_link \
&& unzip -d $temporary_dir main.zip \
&& rm -rf main.zip \
&& mv $temporary_dir/fake_bpy-main $1/fake_bpy \
&& rm -rf $temporary_dir
echo -e "[0;32mSuccessfully downloaded to $1/fake_bpy[0m"
