#!/usr/bin/bash

echo "Create directories..."
mkdir -p data
echo "Download the compressed files..."
cd data
curl https://s3.amazonaws.com/fast-ai-imageclas/imagenette2-160.tgz -O ../data/imagenette2-160.tgz
echo "Uncompress the raw data..."
tar -xzf imagenette2-160.tgz
mv imagenette2-160 raw
touch raw/.datalock 
echo "Cleaning up..."
rm -f imagenette2-160.tgz
echo "Done"
